# mcp/src/agents_remember/providers/metrics.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/metrics.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T19:45+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`metrics.py` is the central provider containment metrics module (containment
R4, task 260707-HFX-L1, developer ruling 2026-07-07): the MCP observes
per-stack uptime, reliability, and resource pressure so degradation is a
detectable state instead of a post-mortem. One store under the observer root
holds the samples; the serving daemon's sampling loop writes them,
`provider_status` reads them now, and the degradation protocol (260707-HFX-L7)
and the dashboard statistics board (260703_statistics-component) consume the
same rows later.

## Code Commentary

### 260731-EFA-L5 This Log Is On `ar-durable-store/1.0`

The leaf's first pass put six `controlplane/` stores on the contract and left this one behind **on
the strength of nothing but its directory**. It has the identical shape — append-only JSONL plus a
reclaim pass that rewrites the file whole — so it had the identical defect, and this one is a
genuine two-process pairing: the MCP process appends index-lifecycle rows from its provider-setup
thread (`providers/provider_setup.py::_record_index_state`, reached from `worktree_start` /
`runtime_install`) while the dashboard's `_metrics_loop` (`serving/app.py`) runs `record` and then
`compact` — a tail rewrite.

**On the loss numbers: record the direction, not a rate.** Several base-commit percentages for this
store are in circulation and they do not agree, because each run used a different pacing and none of
them recorded it. `metrics.py`'s own docstring states 35.88% / 40.00% / 36.75% at 2 appenders and
800 records, and `tests/test_provider_store_durability.py` re-measured against a `git archive` of
the base commit after fixing the harness's scratch directory and got 1.50-3.50% at the shipped
profile and 5.25-5.50% at the same 2×800 shape. That test file says so itself and instructs the
reader to treat the figures as evidence of direction only. **This card asserts no rate.** What is
stable and worth carrying: *this store lost records at the base commit and loses none now.* The
zero is the part a reader can check in one step, and it is an assertion rather than prose —
`ProviderStoreDurabilityTests` pins `lost == 0`, `torn_lines == 0` and `stragglers == []` over
`attempted == 200` (the shipped `STRESS_PROFILE`: 4 appenders × 50) for both provider stores, plus
`lost == 0` over the forced single-record window. The leaf also reports zero loss at the
2-appender/800-record shape — four times the volume — but that one is narrative, not an assertion.
The rate was never the finding; the direction was.

**Ownership: `PROVIDER_METRICS_OWNERSHIP`**, declared beside the store rather than in
`durable_store.py`'s register (that register is titled for the six control-plane logs and is the
contract, not a directory of every store in the tree; the contract itself is imported, never
re-implemented). `writers=("mcp", "dashboard")`, `compaction_owner="dashboard"`. It did **not** earn
the operator-inbox's `compaction_owner=None` exception, and the reason is worth keeping: that store
earned `None` because *both* processes must physically remove rows and neither removal can travel to
the other process without the decision it implements. Nothing in the MCP process removes a metrics
row at all — so a single owner was **available** here, and the contract requires one wherever it is
available. The owner is enforced structurally rather than by a runtime predicate: `compact()` has
exactly one caller and it is inside the dashboard's loop.

**Every write now holds `metrics.jsonl`'s lock.**

- `record()` appends and republishes `metrics-current.json` under **one** hold of the log's lock, so
  the current-state file always names a row that is really in the log. It is the only place two of
  these locks are held at once, and the **lock order is stated**: the log's lock first, the
  current-state file's inside it, never the other way round.
- `record_index_state()` is the MCP process's write — the one that made the two-process pairing
  real — and takes the same lock.
- `compact()` holds the lock across the byte-budget `stat`, the `_tail_lines` read **and** the
  rewrite. Holding it only around the rewrite would leave the tail a stale choice: every row
  appended after it was read is not in the temp file and is gone at the replace — the lost update
  wearing a lock. The old docstring called that acceptable ("a sample racing the atomic replace is
  acceptable"); it was not a tolerance, it was the defect. The cost of the fix is one uncontended
  `flock` on the sampler's 30s tick.
- `rewrite_lines` supplies the pid-scoped temp name, the fsynced file and directory, and a refusal
  if the caller is not holding the lock. The unscoped `metrics.jsonl.compact.tmp` and
  `metrics-current.json.tmp` names are **gone** — two rewriters sharing one temp path meant one
  `os.replace`d it away and the other took a `FileNotFoundError` out of a store call that had
  reported nothing wrong.

**Reads stay lock-free and per-row tolerant, argued structurally.** `_parse_row(text)` returns
`None` for a blank, torn, non-object or unknown-major row; `read_recent`, `read_recent_index_states`
and `read_current` all go through it. The leaf's rule is that a store may read tolerantly only if it
carries no authority, because a tolerant read that feeds a rewrite drops the unreadable row
permanently — and `_parse_row`'s docstring argues both halves rather than pleading "it is only
telemetry":

1. **Nothing is decided on the presence of a metrics row.** The distinguishing property of an
   authority log is that the *absence* of a row reads as "the thing it records never happened",
   which then permits what the row existed to refuse — a dropped `applied` gate marker re-opens a
   replay window. This log has no such marker. Its one consumer that mutates anything, the
   degradation detector's critical failsafe, re-derives the whole state machine from a rolling
   window of live samples every 30s and consumes nothing, so a row lost to a torn line costs at most
   one tick's accuracy and the next sample corrects it.
2. **Nothing a read returns is ever written back.** `compact` reclaims from a **raw** byte tail
   (`_tail_lines`) and drops rows **by age alone**, so a row `_parse_row` skipped is skipped for one
   call and stays on disk. The permanent-drop cost the strict rule exists to prevent cannot arise.

**There is an escalation clause, and it is part of the contract, not a comment.** `_parse_row` states
that if either of those ever stops being true — a decision keyed to a specific row, or a rewrite that
filters by parsing — this read **must become strict in the same change**.

Reads take no lock on purpose: a reader that took the log's lock would queue the dashboard's status
route behind a compaction, and the worst a concurrent append can cost a read is the torn last line
`_parse_row` skips.

**`schemaVersion` is stamped by the store, not by a caller.** `_stamped(payload)` adds
`SCHEMA_VERSION` to every appended row. Per `ar-durable-store/1.0` it is MAJOR.MINOR, an unknown
major is refused, an unknown minor is accepted, and an **absent** field means `1.0` — which is what
makes this additive rather than a migration: every row already on disk was written by this same
build under the same meaning, so `_parse_row` reads an existing `metrics.jsonl` unchanged and the
field only appears on rows written from now on.

### 260707-HFX2-L12 CS-6 Update

`ProviderMetricsStore` now reads recent samples from a bounded EOF tail instead of materializing the whole `metrics.jsonl`, and `compact()` rewrites oversized logs to newest retained rows behind an O(1) byte-budget check.

### Logic

Two frozen dataclasses model a sample. `ContainerSample` is one provider
container's state at sample time (`name`, the `provider`/`instance` ownership
labels, `running`, `restarts`, and optional `mem_bytes`/`mem_limit_bytes`/
`cpu_percent`). `MetricsSnapshot` is one sampling pass over every labeled
provider container on the host (`schema` = `PROVIDER_METRICS_SCHEMA`,
`ar-provider-metrics-sample/v1`; `sampledAt`; `containers`; an optional
`error`), with a `running_count` property and `to_payload()` that adds
`runningCount` to the `asdict` dump.

`ProviderMetricsStore(coordination_root)` is the append-log + rolling-current
store under `<coordinationRoot>/logs/observer/providers/`: `metrics.jsonl`
accretes samples for trend/statistics consumers, and `metrics-current.json` is
the cheap always-fresh read for status packets and the projection. `record()`
appends one JSON line to the log and republishes the current snapshot — **since
260731-EFA-L5 both under one hold of the log's lock, through `durable_store.append_line` and
`rewrite_lines`, not the old hand-rolled tmp file + `os.replace`** (see the L5 section above for
the lock order and why the unscoped temp names had to go).
`read_current()` returns the parsed current snapshot or `None` on a
missing/unreadable file; `read_recent(limit=120)` returns the newest samples
oldest-first and skips unreadable rows per row via `_parse_row`, so a torn append (the crash class
this master exists for) costs one sample row, never the store.

`record_index_state(payload)` (260707-HFX-L2) appends one index-lifecycle row
— seed catch-up, index staleness — to the SAME `metrics.jsonl`: the row is
stamped `schema = PROVIDER_INDEX_STATE_SCHEMA` (`ar-provider-index-state/v1`,
beside the container-sample schema) so consumers such as the degradation
detector and the statistics board tell the row kinds apart, and a `sampledAt`
default is filled in when the payload carries none. The rolling
`metrics-current.json` stays container-only; index rows ride the append log
only. `read_recent_index_states(limit=20)` is the read side: the newest
index-lifecycle rows oldest-first, schema-filtered out of the shared log (it
scans the last 500 rows through `read_recent`) — `provider_status` attaches
the last 10 as the packet's `indexState`.

`sample_provider_containers(cwd=..., timeout=DOCKER_SAMPLE_TIMEOUT_SECONDS)`
is one read-only sampling pass. Discovery is label-based: every provider
container carries the ownership labels from `identity.provider_ownership_labels`
(`OWNERSHIP_LABEL_KEY` = `agents-remember.provider`, `INSTANCE_LABEL_KEY` =
`agents-remember.instance-id`), so the sampler needs no settings at all — a
leftover stack from a dead session is exactly what must stay observable. The
pass runs `docker ps --all --filter label=<ownership> --format {{json .}}`
and, when RUNNING rows exist, one `docker stats --no-stream` pass fed ONLY the
running names (`State == running`): a stopped name fed to `docker stats` can
fail the whole command and blind every pressure number (review follow-up), so
stopped containers appear in the snapshot without stats instead. Dockerless
hosts (a `ContextProviderError` from `docker_command`) and a
failed `docker ps` yield an error-annotated empty snapshot, never a crash or a
launch — status must stay legal while providers are disabled. Since
260718-CHATS-L5F R6, a `docker ps` that TIMES OUT (a slow or hung docker daemon)
is bounded the same way: the call passes `allow_timeout=True` cit:([`allow_timeout`], mcp/src/agents_remember/providers/metrics.py:392-392) and the
`timedOut` branch cit:([`sample_provider_containers`], mcp/src/agents_remember/providers/metrics.py:363-420) returns an error-annotated empty `MetricsSnapshot`
("docker ps timed out after {timeout}s") instead of letting a
`subprocess.TimeoutExpired` escape and dump a full traceback into the daemon's
30s `metrics_loop` every sampling interval (the developer's image1 log noise). A
failed `docker stats` costs only the mem/cpu numbers, never the sample (its
timeout is not yet bounded — reviewer F5, a small recorded follow-on).

The parsers absorb docker's text formats: `_json_rows` keys a
`--format {{json .}}` line stream and skips bad lines; `_parse_labels` splits
the comma/`=` label string; `_parse_mem_usage`/`_parse_bytes` convert the
`used / limit` string via the `_UNIT_FACTORS` table (b/kb/kib/mb/mib/gb/gib);
`_parse_percent` strips the `%`. `_parse_restarts` flags `Restarting` status
strings as 1 (otherwise 0) — docker's durable restart count needs `inspect`,
which is too heavy per tick, so the degradation detector treats restart-loop
detection as state-change based. `DEFAULT_SAMPLE_INTERVAL_SECONDS` (30.0) is
the daemon's sampling cadence; `DOCKER_SAMPLE_TIMEOUT_SECONDS` (20) bounds
each docker call.

### Invariants And Boundaries

- Sampling is read-only and dockerless-safe: it never launches anything and
  never raises on a missing docker binary or stopped daemon — an
  error-annotated empty sample keeps the sampling loop and status packet legal
  while providers are disabled.
- Discovery is label-based, never settings-based: leftover stacks from dead
  sessions must remain visible without any lifecycle settings file.
- **Every append and every rewrite of `metrics.jsonl` holds its lock (`ar-durable-store/1.0`).**
  Two processes write here — the dashboard's `_metrics_loop` and the MCP's provider-setup thread —
  and the reclaim is a whole-file replace, so an unlocked append landing inside a compaction is a
  lost update. Take the lock only around the rewrite and the loss returns, because the tail was
  already stale when it was read.
- **When `record()` holds two locks the order is fixed:** the log's lock first, `metrics-current.json`'s
  inside it. Never the other way round.
- **The reads are lock-free and per-row tolerant, and both are conditional.** Tolerance is licensed
  by two structural facts — nothing is decided on a row's presence, and the reclaim drops rows by
  age from a raw byte tail so nothing a read returns is written back. `_parse_row` carries the
  escalation clause: if either stops holding, the read becomes strict **in the same change**.
- **The store stamps `schemaVersion`; a caller cannot override it.** Absent means `1.0`, which is
  what makes existing rows readable unchanged.
- `metrics.jsonl` carries BOTH row kinds — container samples and index-state
  rows — distinguished by the `schema` field; the rolling current-state file
  stays container-only (260707-HFX-L2).
- One `docker ps` plus at most one `docker stats` pass per sample; stats is
  fed only running names so a stopped container can never fail it, and a stats
  failure degrades the numbers, not the snapshot.
- A `docker ps` timeout is bounded (`allow_timeout=True`): a slow/hung daemon
  returns an error-annotated empty snapshot, never a `TimeoutExpired` traceback
  in the daemon's per-interval metrics loop. The sibling `docker stats` timeout
  is not yet bounded (reviewer F5); the sampler still catches its non-timeout
  failures.
- The store lives under the observer root (`logs/observer/providers/`); the
  sampling cadence belongs to the serving daemon, not this module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ownership labels every provider container carries (`provider_ownership_labels`). | `provider_ownership_labels` | mcp/src/agents_remember/kernel/primitives/identity.py:123-135 |
| `run_command` / `docker_command` seams the sampler runs through. | `timeout_command_result` | mcp/src/agents_remember/providers/lifecycle/command_runner.py:58-74 |
| The serving daemon's lifespan runs the 30s sampling loop into this store. | "async def _metrics_loop(config: McpRuntimeConfig" | mcp/src/agents_remember/serving/_app_lifespan.py:73-73 |
| `provider_status_packet` attaches `read_current()` to the status packet. | `provider_status_packet` | mcp/src/agents_remember/providers/status.py:53-87 |
| Containment tests pin the parsers, the sampler paths (incl. dockerless), and the store's torn-line tolerance. | `MetricsTests` | mcp/tests/test_provider_containment.py:318-450 |
| The seed catch-up stage records index-state rows through `_record_index_state`. | `_record_index_state` | mcp/src/agents_remember/providers/provider_setup.py:434-453 |
| Index-lifecycle tests pin the `record_index_state` row landing in the log with its schema. | `record_index_state` | mcp/src/agents_remember/providers/metrics.py:269-283 |
| `ar-durable-store/1.0` itself: `exclusive_access`, `append_line`, `rewrite_lines`, `SCHEMA_VERSION`, `schema_version_supported` and the `StoreOwnership` record `PROVIDER_METRICS_OWNERSHIP` instantiates. Cited by symbol: this file grew ~100 lines mid-leaf and earlier line ranges into it are invalid. | `DURABLE_STORE_CONTRACT` | mcp/src/agents_remember/controlplane/durable_store.py:43-43 |
| The MCP-side appender that makes this a two-process store (`_record_index_state`). | `_record_index_state` | mcp/src/agents_remember/providers/provider_setup.py:434-453 |
| The durability suite for this store and its sibling: R10 no-record-lost under real processes, R14 the harness proven able to fail against a `git archive` of the base commit, R8 the tolerant-read policy, R2 the ownership decisions as assertions. Its docstring is also where the base-commit figures are explicitly disclaimed as unreproducible. | `ProviderStoreDurabilityTests`, `ProviderReadPolicyTests`, `ProviderOwnershipTests`, `ProviderReclaimShapeTests` | mcp/tests/test_provider_store_durability.py:280-351; mcp/tests/test_provider_store_durability.py:391-571; mcp/tests/test_provider_store_durability.py:630-723; mcp/tests/test_provider_store_durability.py:726-801 |

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 13 citation findings (5 rows and 2 prose pointers); scoped recheck clean.

- 2026-08-01T19:45+02:00 — 260731-EFA-L5 (durable store integrity). This store was brought onto
  `ar-durable-store/1.0`, and the card described the pre-contract shape throughout. Recorded: the
  two-process pairing that makes it a real defect (dashboard `_metrics_loop` `record` + `compact`
  against the MCP's `_record_index_state`); `PROVIDER_METRICS_OWNERSHIP` with
  `compaction_owner="dashboard"`, and **why it did not earn the operator-inbox's `None` exception**
  — nothing in the MCP process removes a provider row, so a single owner was available and the
  contract requires one where it is; that the owner is enforced structurally, `compact()` having one
  caller inside the dashboard's loop. Corrected the "replace-atomic tmp + `os.replace`" description
  of `record()` to the contract's `append_line`/`rewrite_lines` under one lock, and recorded the
  stated **lock order** (log first, current-state file inside). Recorded that `compact` holds the
  lock across the stat, the tail read and the rewrite, and why locking only the rewrite is the lost
  update wearing a lock. Recorded the tolerant `_parse_row` **argued structurally** — nothing is
  decided on a row's presence, and the reclaim drops rows by age from a raw tail so nothing read is
  written back — together with its **escalation clause** (strict in the same change if either stops
  holding), and that reads stay lock-free so a status route is never queued behind a compaction.
  Recorded `_stamped`/`schemaVersion` with absent-means-1.0 as what keeps it additive, and that both
  unscoped temp names are gone. **On the numbers: no rate is asserted.** Several disagree
  (35.88-40.00% in this module's docstring, 1.50-3.50% and 5.25-5.50% re-measured in
  `test_provider_store_durability.py`) because the pacing was not recorded; the card carries the
  direction, and carries the zero as what it actually is — an assertion (`lost == 0`,
  `torn_lines == 0`, `stragglers == []` over `attempted == 200` on the shipped `STRESS_PROFILE`,
  plus the forced single-record window), with the 800-record zero marked as reported rather than
  asserted. Replaced one invariant with five and added four reference rows.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/metrics.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 7 line(s), touching only redundant grouping
  parentheses. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R6 — `sample_provider_containers` now passes
  `allow_timeout=True` for `docker ps` and returns an error-annotated empty `MetricsSnapshot` on the
  `timedOut` branch, so a slow/hung docker daemon no longer lets a `subprocess.TimeoutExpired` escape
  and dump a full traceback into the daemon's 30s metrics loop every interval. Recorded the sibling
  `docker stats` timeout as still-unbounded (reviewer F5, small follow-on). Change uncommitted;
  closeout re-stamps verification.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review follow-up: added `read_recent_index_states`
  (newest index-lifecycle rows oldest-first, schema-filtered from the shared log) — the read
  seam `provider_status`'s new `indexState` packet field consumes. Verification metadata pinned
  until closeout stamps the HFX-L2 commit.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 (index lifecycle): added `PROVIDER_INDEX_STATE_SCHEMA`
  (`ar-provider-index-state/v1`) and `ProviderMetricsStore.record_index_state` — index-lifecycle
  rows (seed catch-up, staleness) ride the same `metrics.jsonl` distinguished by the `schema`
  field; the rolling current-state file stays container-only. Verification metadata pinned until
  closeout stamps the HFX-L2 commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix: `sample_provider_containers` now feeds
  `docker stats` ONLY running container names (`State == running`), because a stopped name can
  fail the whole stats command and blind every pressure number; stopped containers ride the
  snapshot without stats. Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — Created for 260707-HFX-L1 (provider containment R4): the central
  containment metrics module — `ContainerSample`/`MetricsSnapshot`, the
  `ProviderMetricsStore` (append log + replace-atomic rolling current snapshot under
  `logs/observer/providers/`), the label-discovering single-pass `docker ps` + `docker stats`
  sampler (dockerless-safe error snapshot), and the mem/cpu/label parsers. Verification metadata
  pinned to the branch base until closeout stamps the HFX-L1 commit.
