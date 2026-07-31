# mcp/tests/test_projection_scaling_cs6.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_projection_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |                                                `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[mcp/tests overview](overview.md) — the route-local `mcp/tests/overview.md` established on 2026-07-12 (260712-TRH-L4) now governs this test sidecar.

## Purpose

`test_projection_scaling_cs6.py` pins the projection tick fixes from HFX2-L12 fix round 2. It focuses on the 1-second projection path surfaces that previously double-folded gate logs, double-walked task JSON, re-ran git status per leaf, re-parsed unchanged lifecycle logs, and silently allowed task-document body payload growth.

### 260712-TRH-L7 invalid landing containment

The scaling suite adds a raising landing snapshot reader case. It proves local status survives with a warning and the projection tick does not lose unrelated contracts.

### 260712-PTS-L2 shared contract snapshot

`ContractSnapshotSharedPassTests` pins the one-shared-contract-pass-per-tick change: N parses on a
cold build, zero on an unchanged build, exactly the changed file afterwards (R7/R2); one enumeration
per full `project_and_write` tick with zero re-parses on the next tick (R1); reader-output parity for
enclosures, engine facts, and prune keys with and without the injected snapshot, malformed contract
skipped-never-fatal (R4); cache retention bounded to the live path set (R3); the two ctime-hardening
adversarial cases — a `chmod 000` invalidates instead of serving the stale good parse forever, and an
`os.utime`-pinned same-size rewrite is still detected; and parse failures retried every build, never
cached.

## Code Commentary

### 260707-HFX2-L13 F6/F7 Two-Size And Cache Proof

`LifecycleLogCacheTests` instruments the real `EventStore.read_log` parse boundary. A cold pass must
parse once; a later heartbeat-sidecar change must update the merged event view without another log
parse, closing round-1 B2. Task-document scaling cases at two corpus sizes assert the broadcast is
windowed, every summary has a `bodyRevision`, and reader-body byte cost is zero. Separate cases prove
series summaries are body-free and the on-demand reader returns full content.

### Logic

`GateReadFoldTests` counts `GateStore.read()` calls and proves `read_gates()` folds each gate log once per tick. `TaskDocSharedCacheTests` proves task and series readers share the same parsed task-json cache. `GitStatusCacheTests` proves `_safe_status_payload()` is TTL-cached. `LifecycleLogCacheTests` proves unchanged lifecycle logs are not re-read at two event-log sizes. `TaskDocumentsPayloadBudgetTests` characterizes the still-unbounded task-doc body payload and proves the write-path guardrail logs only when over budget and is rate-limited. `ContractSnapshotSharedPassTests` (PTS-L2) counts `contract_snapshot.load_contract` calls (the builder's only parse site) and `iter_leaf_enclosure_contracts` walks, seeds real contracts via `default_contract`/`write_contract` (since 260731-EFA-L2 called as `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...))`, with the leaf's `lifecycle_id` now a `LeafIdentity` field and the disabled-memory cases simply omitting the optional `memory=` plan), forces stat-identity changes with `_bump_mtime`, and steps past the kernel's coarse-clock granule (`_step_past_ctime_granule`, 50ms) before chmod/rewrite cases because ctime cannot be set explicitly; the chmod case is skipped for root (root ignores file modes).

### Conventions

The tests patch module-level seams only inside `try/finally` blocks, clear the relevant caches before assertions, and use deterministic counters instead of wall-clock where possible.

### Invariants And Boundaries

F6 payload windowing is not implemented here; the test deliberately characterizes the unbounded body cost and pins the guardrail that HFX2-L13 will turn into a bounded broadcast contract.

### Todos

Replace the F6 characterization with a bounded assertion when HFX2-L13 moves full task bodies out of the always-on projection.

## Docs References

No external documentation governs these repo-local projection scaling regressions.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test file covers gate one-read folds, shared task-doc cache, git status TTL, lifecycle-log cache, and task-doc payload guardrail. | L67-L99; L102-L148; L151-L189; L323-L418; L421-L587 | [mcp/tests/test_projection_scaling_cs6.py](agents-remember/mcp/tests/test_projection_scaling_cs6.py) |
| `LandingProjectionHotPathTests`: the invalid-landing containment case and the heartbeat landing-tail regression. | L192-L320 | [mcp/tests/test_projection_scaling_cs6.py](agents-remember/mcp/tests/test_projection_scaling_cs6.py) |
| `ContractSnapshotSharedPassTests`: parse counting, one-enumeration-per-tick, output parity, live-set retention, chmod-000 and utime-pinned-rewrite ctime hardening, and malformed-retry regressions. | L590-L862 | [mcp/tests/test_projection_scaling_cs6.py](agents-remember/mcp/tests/test_projection_scaling_cs6.py) |
| The shared per-tick contract snapshot + stat-identity parse cache under test. | L1-L145 | [mcp/src/agents_remember/observer/contract_snapshot.py](agents-remember/mcp/src/agents_remember/observer/contract_snapshot.py) |
| The single per-tick build in `project_and_write` the full-tick regression instruments: one shared `ContractSnapshotCache`, then exactly one `state.read(...)` pass per tick. | L96-L102; L214-L237 | [mcp/src/agents_remember/observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Projection store implements lifecycle-log caching and over-budget task-document payload warnings. | L89-L109; L112-L154; L275; L280-L306 | [mcp/src/agents_remember/observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Snapshot readers implement the shared task-document cache, single-read gate fold, and git-status TTL cache. | L113-L155; L485-L516; L601-L663 | [mcp/src/agents_remember/observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## 260727-CHATS-IM-L2 Current Delta

`LandingProjectionHotPathTests` now proves a heartbeat replaces only landing rows from published
landing authority while contract, guidance, and other status facts retain identity and value.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired both `observer/projection_store.py`
  citations (4 ranges), all read back in the 365-line file. The per-tick-build row is now
  L96-L102 (the comment + `_contract_snapshot_cache = ContractSnapshotCache()`, the one
  enumeration/parse pass per tick) and L214-L237 (`project_and_write` through its single
  `state.read(...)` call); the old `L211-L230` opened inside `ProjectionTickState` and cut off
  before the read. The caching/warning row is now L89-L109 (`_LifecycleLogCacheEntry` and the
  `_lifecycle_log_cache` dict with its rationale comment), L112-L154 (`read_lifecycle_logs`, the
  `(mtime_ns, size)` reuse and the prune-to-live-set at L152-L153), L275 (the call site) and
  L280-L306 (`_warn_if_task_documents_payload_over_budget`, rate-limited by
  `TASK_DOCUMENTS_PAYLOAD_WARN_INTERVAL_SECONDS`); the old `L248-L274` now lands mid-`project_and_write`.
  Both claims unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass rewrote the three
  `default_contract` seedings in this suite, so the card names the new shape and its own-file
  citations were re-derived. Contracts are now built as
  `default_contract(ContractTask(name, repo_name, coordination_root, workflow_kind, memory_mode),
  leaf=LeafIdentity(...), code=RepoBranchPlan(...))`; the former `worktree_name=` and
  `lifecycle_id=` keywords are `LeafIdentity` fields, the four `code_*` keywords are a
  `RepoBranchPlan`, and the disabled-memory cases omit the now-optional `memory=` plan instead of
  passing four empty strings. Those expansions plus the three added imports and the `ruff format`
  reflow of several collapsed literals moved every class in the file, so both own-file rows in the
  references table were recomputed from the current source and re-read at their new positions
  (`GateReadFoldTests` L67-L99, `TaskDocSharedCacheTests` L102-L148, `GitStatusCacheTests`
  L151-L189, `LifecycleLogCacheTests` L323-L418, `TaskDocumentsPayloadBudgetTests` L421-L587, and
  `ContractSnapshotSharedPassTests` L590-L862). Most of that correction is older drift this leaf
  merely exposed: the cited ranges were already tens of lines off at the L2 base commit, and
  `LandingProjectionHotPathTests` had no row at all, so one was added for it. No counter, cache
  assertion, budget threshold or ctime-hardening case changed — the seeded contracts carry the same
  values, so every scaling claim in this card still holds. Verification metadata stays pinned until
  closeout stamps the code commit.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: added the heartbeat landing-tail
  regression proving a refresh replaces only landing rows while retaining contract, guidance, and
  non-landing status facts. Verification metadata remains pinned until closeout.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2: added `ContractSnapshotSharedPassTests` — parse-count
  N/zero/changed-only across builds, one contract enumeration per full projection tick, reader-output
  parity with/without the injected snapshot, live-set cache retention, the chmod-000 and
  utime-pinned-rewrite ctime-hardening cases, and failure-retried-every-build. Also repointed
  `governingOverview` to the now-existing route-local `mcp/tests/overview.md`. Verification metadata
  pinned until closeout stamps the PTS-L2 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: scaling regressions prove invalid landing snapshots sacrifice only one contract's landing detail and do not block the projection tick.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6/F7/B2: revived the lifecycle-log cache instrument,
  proved sidecar merge without reparse, and added body-free/windowed broadcast plus on-demand body
  regressions. Verification metadata remains pinned until closeout stamps the eventual L13 code
  commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the projection CS-6 scaling regressions added in fix round 2. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
