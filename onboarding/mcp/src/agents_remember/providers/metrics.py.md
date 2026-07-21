# mcp/src/agents_remember/providers/metrics.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/metrics.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383` |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
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
appends one JSON line to the log and rewrites the current snapshot
replace-atomically (tmp file + `os.replace`, like the sibling observer
stores). `read_current()` returns the parsed current snapshot or `None` on a
missing/invalid file; `read_recent(limit=120)` returns the newest samples
oldest-first and skips invalid lines, so a torn append (the crash class this
master exists for) costs one sample row, never the store.

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
is bounded the same way: the call passes `allow_timeout=True` (L252) and the
`timedOut` branch (L254-L259) returns an error-annotated empty `MetricsSnapshot`
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
- `metrics-current.json` writes are replace-atomic; readers of `metrics.jsonl`
  must skip invalid lines, so a torn append line costs one sample row, never
  the store.
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

| Finding | Source Path |
| --- | --- |
| The ownership labels every provider container carries (`provider_ownership_labels`). | [identity.py](agents-remember/mcp/src/agents_remember/providers/identity.py) |
| `run_command` / `docker_command` seams the sampler runs through. | [command_runner.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/command_runner.py); [docker_runtime.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py) |
| The serving daemon's lifespan runs the 30s sampling loop into this store. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| `provider_status_packet` attaches `read_current()` to the status packet. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Containment tests pin the parsers, the sampler paths (incl. dockerless), and the store's torn-line tolerance. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |
| The seed catch-up stage records index-state rows through `_record_index_state`. | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |
| Index-lifecycle tests pin the `record_index_state` row landing in the log with its schema. | [test_provider_index_lifecycle.py](agents-remember/mcp/tests/test_provider_index_lifecycle.py) |

## Update History

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
