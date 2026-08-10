# mcp/src/agents_remember/controlplane/agent_notifier_signals.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/controlplane/agent_notifier_signals.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-01T20:15+02:00 |
| lastVerifiedCommitHash |                                                                `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |                                                                2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persisted cooldown memory for agent-notifier-owned pane/seat-liveness signals. It prevents the
deterministic agent-notifier sweep from minting a new owner-addressed inbox row every sweep for the same
target owner, leaf, finding kind, and detail.

### 260713-TES-L1 Rename

Module renamed from `supervisor_signals.py`; Python identifiers are `AgentNotifierSignalRecord`,
`AgentNotifierSignalTarget`, `AgentNotifierSignalKey`, `AgentNotifierSignalCooldownStore`, and the
ownership constant `AGENT_NOTIFIER_SIGNAL_OWNERSHIP`. Retained byte-identical during the
compatibility window (durable/on-disk surfaces): the schema string `ar-supervisor-signal/v1`
(`AGENT_NOTIFIER_SIGNAL_SCHEMA`), the log filename `supervisor-signals.jsonl` (`log_path()`),
and the ownership label `store="supervisor-signals"`. Removal rides the schema migration that owns
the cooldown log.

## Code Commentary

### 260731-EFA-L5 Durable Store Contract

The `durable_store.py` module docstring records this log losing **10.50 percent** of appended
records at the base commit, the second-highest of the six, and that figure is quoted here on its
authority: it appears at that one site and nowhere else in the tree, unlike the 31.45 percent
figure below, which is carried at several independent sites. The loss is of whole rows — the
durability harness (`mcp/tests/_store_durability.py`, driven by
`test_controlplane_store_durability.py`) is what produces a loss rate at all, and no recorded
base-commit run of it is in the tree. What matters structurally is checkable without the number:
like attention-dismissals, this happened to a store with a **single writer** — the dashboard's
agent-notifier sweep is the only thing that appends a signal and the only thing that compacts the
cooldown log.

The lesson the leaf drew from that pair is recorded in the code and belongs on this card: "only one
process writes this file" is a **deployment fact, not a structural one**. An earlier draft of this
leaf left the two single-writer stores unlocked on exactly that reasoning, and the proof run
measured 31.45 percent loss on this store's twin, attention-dismissals, whose single-writer claim
was just as true. `StoreOwnership` therefore has no `serialized` field: locking is not a setting a
store may opt out of.

All file I/O now routes through `controlplane/durable_store.py` under
`AGENT_NOTIFIER_SIGNAL_OWNERSHIP`, which names the dashboard both sole writer and compaction owner:

- `append` calls `check_declared_writer()` — which is what makes the single-writer claim *checkable*
  inside the two daemons rather than merely asserted — and then holds `exclusive_access` around
  `append_line`, which fsyncs before the handle closes.
- `compact` opens `exclusive_access` and delegates to the new `_compact_locked`, so the read, the
  retention filter and the rewrite happen under one hold. The returned `kept` list is still the
  sweep's cooldown snapshot.
- `_replace` no longer unlinks an emptied log and no longer builds its own temp path; it delegates
  to `durable_store.rewrite_lines`, which refuses unless the calling thread holds the lock.
- `AgentNotifierSignalRecord` now inherits `DurableRecord`, picking up `extra="forbid"` (previously
  declared locally) plus a validated `schemaVersion`: unknown major rejected, unknown minor
  accepted, and this store's tolerant reader skips a rejected row.

**Read policy: tolerant, and it stays tolerant.** A torn, legacy or version-skewed line is a
durability event, not a reason to freeze the agent-notifier sweep that folds this non-authoritative
cooldown log. The consequence is worth stating: `_compact_locked` reclaims from that tolerant read,
so an unparseable cooldown row is dropped permanently by a compaction. The failure mode is
fail-open — a signal that could have been suppressed is sent again — which is why it is acceptable
here and would not be in an authority-bearing log.

### 260707-HFX2-L17 Pair-Scoped Cooldown Identity

Signal records and cooldown lookups add `seatRole`, so two roles with the same leaf, finding kind,
and detail retain independent cooldown slots. Existing bounded snapshot/compaction behavior is
unchanged.

### 260707-HFX2-L13 CS-6 Update

`AgentNotifierSignalCooldownStore` is no longer an unbounded per-finding full-file fold: reads skip malformed rows, `in_cooldown(records=...)` consumes a sweep snapshot, and `compact()` atomically retains only records inside the cooldown window.

### Logic

`AgentNotifierSignalRecord` is the strict JSONL record shape for one posted agent-notifier signal. Its
dedupe key is the tuple `_signal_emit` supplies: `targetAgentId`, `targetLifecycleId`,
`targetRole`, `leafKey`, `findingKind`, and `detail`, plus the stored `deliveryState` returned by
the hosted inbox delivery attempt.

`AgentNotifierSignalCooldownStore(observer_root)` writes `workspace/supervisor-signals.jsonl`.
`append(record)` creates the workspace directory and appends one alias-rendered JSON row. `read()`
parses the current full file into `AgentNotifierSignalRecord` rows.

Two frozen parameter objects (260731-EFA-L2) make the dedupe key a value rather than a keyword
list:

- **`AgentNotifierSignalTarget(agent_id=None, lifecycle_id=None, role=None, leaf_key=None,
  seat_role=None)`** — the owner inbox a signal is addressed to. Derived as one routing decision by
  `derive_signal_owner` and stamped verbatim onto every `AgentNotifierSignalRecord`.
- **`AgentNotifierSignalKey(target, finding_kind, detail)`** — what makes two signals "the same
  signal" for cooldown purposes: the same target told the same thing. **Every field is compared,
  all of them or none** — a partial match is a different signal and must not suppress delivery.

`last_sent(signal, *, records=None)` filters the full
record set to rows matching that key and returns the newest timestamp.
`in_cooldown(signal, *, now, cooldown_seconds, records=None)`
validates `cooldown_seconds` through `inbox_backoff.require_redelivery_floor_seconds`, then compares
the latest matching record's timestamp to `now`; malformed timestamps fail open for that row so the
next valid signal can be posted and persisted.

### Conventions

The store mirrors the control-plane JSONL-store style but is intentionally small: no MCP surface, no
catalog read, and no delivery itself. `serving/agent_notifier.py` is the production caller that
decides the routed owner, checks this store, posts the inbox row, and appends the cooldown record.

### Invariants And Boundaries

- The cooldown floor is shared with inbox redelivery and cannot be below 900 seconds.
- The key is owner/leaf/kind/detail scoped; different owner addresses or different finding details
  are allowed to post independently.
- This store records agent-notifier signal cooldown only. It does not consume inbox rows, ack
  expectations, deliver hosted messages, or decide the escalation ladder.
- **Locked unconditionally, single writer notwithstanding.** `append` and `compact` both take
  `exclusive_access`. The single-writer claim is a deployment fact and is enforced only as far as
  `check_declared_writer` reaches — inside the two daemons; the lock is what makes the file correct
  everywhere else, including CLI and test processes that declare nothing.
- **The lock is held across the read and the rewrite.** `compact` wraps `_compact_locked`;
  `rewrite_lines` raises `DurableStoreError` on a caller that skipped it.
- **`_replace` never unlinks.** An empty kept set is an empty file, so a concurrent appender cannot
  write into an unlinked inode.

### Todos

Tracked HFX2-L11 gap from the HFX2-L9 reviewer verdict, now partly closed. The unbounded-log half
is **resolved**: `compact(now=, retain_seconds=)` reclaims records outside the cooldown window and
returns the sweep's snapshot (added at HFX2-L13; made lock-safe at 260731-EFA-L5). What remains is
the hot-path half — `in_cooldown()` still reaches `read()` through `last_sent()` once per
pane/seat-liveness finding when the caller passes no `records` snapshot, which is a CS-6/L7-class
cost on the agent-notifier path. `serving/agent_notifier.py` does pass the snapshot, so the production path
is bounded. Non-blocking while `orchestration.agent-notifier.enabled` remains disabled.

## Docs References

No external/domain documentation is configured for this repo memory layer. The behavior is internal
supervisor control-plane state.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `AgentNotifierSignalRecord` defines the persisted signal-cooldown key fields and delivery state. | `AgentNotifierSignalRecord` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:30-46 |
| The store resolves `workspace/supervisor-signals.jsonl` (retained name), reads it tolerantly, and appends under the log's lock after the declared-writer check. | `AgentNotifierSignalCooldownStore` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:71-135 |
| `last_sent` matches on the whole `AgentNotifierSignalKey` (target plus kind plus detail) and `in_cooldown` enforces the shared redelivery floor before comparing elapsed time. | "def in_cooldown(" | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:136-173 |
| `compact` holds one `exclusive_access` across the `_compact_locked` read-filter-rewrite half, and `_replace` delegates to `rewrite_lines` without unlinking. | `AgentNotifierSignalCooldownStore` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:71-220 |
| `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` names the dashboard sole writer and compaction owner (retained label `store="supervisor-signals"`), and states why the log is locked all the same. | `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:212-221 |
| `_signal_emit` checks this cooldown before posting and appends a record after the inbox signal delivery attempt. | "def _signal_emit(" | mcp/src/agents_remember/serving/_agent_notifier_actions.py:289-289 |
| The serving app imports `AgentNotifierSignalCooldownStore` and wires "signal_cooldown_seconds = (" into each agent-notifier context. | "signal_cooldown_store=AgentNotifierSignalCooldownStore(root),",  | mcp/src/agents_remember/serving/_app_lifespan.py:101-101 |
| The 900-second floor constant and the shared validator that refuses anything below it. | `MIN_REDELIVERY_INTERVAL_SECONDS`, `require_redelivery_floor_seconds` | mcp/src/agents_remember/kernel/primitives/inbox_backoff.py:49-49; mcp/src/agents_remember/kernel/primitives/inbox_backoff.py:66-76 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository supervisor state only. | N/A | N/A |
## Update History
- 2026-08-10T09:45+02:00 — 260731-EFA-L9 curator repair: refreshed the renamed signal-store card and L9 primitive path.


- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the `AgentNotifierSignal*` identifiers and the retained durable names (`ar-supervisor-signal/v1`, `supervisor-signals.jsonl`, `store="supervisor-signals"`) with their migration removal point. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-03T02:46:27+02:00 — W3-B05 curator: anchored 5 Tier-2 table citations and 1 Tier-2 prose citation with exact source paths; fixer generated all ranges.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **One stale citation and one
  unsourced number.** The `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` row cited `durable_store.py`
  **L327-L336**; the constant is at **L398** — the file grew 598 → 699 lines mid-pass, so every
  range written earlier is off. Replaced with a symbol-name citation and no range. Re-read the three
  citations into this module's own source and left them: `AgentNotifierSignalRecord` (cit:([`AgentNotifierSignalRecord`], mcp/src/agents_remember/controlplane/agent_notifier_signals.py:30-46)), the path/read/append row L83-L107 (`log_path` L83, `read` L86, `append` L103), `last_sent` /
  `in_cooldown` L109-L155 (L109, L131), and `compact` L157-L213 (L157, `_compact_locked` L178,
  `_replace` L206). The **10.50 percent** figure is now attributed rather than asserted: it appears
  only in the `durable_store.py` docstring, which is also the only place 10.20, 9.20 and 0.00 appear
  — unlike the 31.45 percent this card also quotes, which four independent files carry. Removed the
  "never torn" assertion about the base commit: `torn_lines == 0` is asserted by
  `test_controlplane_store_durability.py` against the **current** tree, not the base commit, and no
  recorded base-commit run is stored anywhere in the tree. This card's read-policy statements were
  already correct — it says plainly that `_compact_locked` reclaims from the tolerant read and that
  compaction therefore drops an unparseable cooldown row — and were left unchanged.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded the 10.50 percent
  measured loss and the routing of all file I/O through `durable_store.py` under
  `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` (dashboard as sole writer and compaction owner): `append` checks
  the declared writer and locks, `compact` holds one lock across the new `_compact_locked`
  read-filter-rewrite half, `_replace` delegates to `rewrite_lines` and no longer unlinks an
  emptied log, and `AgentNotifierSignalRecord` now inherits `DurableRecord` for `extra="forbid"` plus
  a validated `schemaVersion`. Recorded why a single-writer store is still locked unconditionally
  and that its twin measured 31.45 percent when a draft trusted the single-writer claim. Stated
  that the tolerant read drives this store's rewrite, so compaction drops an unparseable cooldown
  row, and that the failure mode is fail-open. Corrected the Todos section, which still described
  this store as an unbounded log with no compactor after HFX2-L13 added `compact` — a contradiction
  with this card's own HFX2-L13 section. Repaired six citations: three intra-file ranges the leaf
  moved, one row that carried only two cells in a three-column table, and two pre-existing
  cross-file ranges that pointed at unrelated code (`_signal_emit` is at
  `serving/supervisor.py` L850, not L701-L747; the `AgentNotifierSignalCooldownStore` import is at
  `serving/app.py` L81, not L70). Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `AgentNotifierSignalTarget` and `AgentNotifierSignalKey`, and re-signed
  `last_sent(signal, *, records=None)` and `in_cooldown(signal, *, now, cooldown_seconds,
  records=None)` onto the key. `in_cooldown` now forwards the whole key to `last_sent` in one
  argument, so the two can no longer compare on different field sets — the L17 seat-role identity
  is part of the key by construction rather than by both call sites remembering to pass it.
  Matching semantics are unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: extended persisted cooldown identity with seat role so
  different seats on one leaf do not suppress one another.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: created for the new persisted supervisor signal
  cooldown store, including the known unbounded-log/no-compactor limitation tracked for HFX2-L11.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.


