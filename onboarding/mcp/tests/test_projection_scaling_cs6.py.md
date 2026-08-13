# mcp/tests/test_projection_scaling_cs6.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_projection_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |                                                `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[mcp/tests overview](overview.md) — the route-local `mcp/tests/overview.md` established on 2026-07-12 (260712-TRH-L4) now governs this test sidecar.

## Purpose

`test_projection_scaling_cs6.py` pins the projection tick fixes from HFX2-L12 fix round 2. It focuses on the 1-second projection path surfaces that previously double-folded gate logs, double-walked task JSON, re-ran git status per leaf, re-parsed unchanged lifecycle logs, and allowed task-document body payload growth; the current suite now pins bounded, body-free summaries plus on-demand full bodies.

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

`GateReadFoldTests` counts `GateStore.read()` calls and proves `read_gates()` folds each gate log once per tick. `TaskDocSharedCacheTests` proves task and series readers share the same parsed task-json cache. `GitStatusCacheTests` proves `_safe_status_payload()` is TTL-cached. `LifecycleLogCacheTests` proves unchanged lifecycle logs are not re-read at two event-log sizes. `TaskDocumentsPayloadBudgetTests` runs two corpus sizes and pins a bounded summary window, `bodyRevision` on every emitted summary, zero broadcast body bytes, body-free series summaries, on-demand full content, and the rate-limited over-budget warning backstop. `ContractSnapshotSharedPassTests` (PTS-L2) counts `contract_snapshot.load_contract` calls (the builder's only parse site) and `iter_leaf_enclosure_contracts` walks, seeds real contracts via `default_contract`/`write_contract` (since 260731-EFA-L2 called as `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...))`, with the leaf's `lifecycle_id` now a `LeafIdentity` field and the disabled-memory cases simply omitting the optional `memory=` plan), forces stat-identity changes with `_bump_mtime`, and steps past the kernel's coarse-clock granule (`_step_past_ctime_granule`, 50ms) before chmod/rewrite cases because ctime cannot be set explicitly; the chmod case is skipped for root (root ignores file modes).

### Conventions

The tests patch module-level seams only inside `try/finally` blocks, clear the relevant caches before assertions, and use deterministic counters instead of wall-clock where possible.

### Invariants And Boundaries

F6 payload windowing is implemented and load-bearing: always-on task and series summaries remain bounded and body-free, while full content is retrieved only through the on-demand reader. The warning remains a write-path backstop, not the primary bound.

### Todos

None recorded.

## Docs References

No external documentation governs these repo-local projection scaling regressions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The test file covers gate one-read folds, shared task-doc cache, git status TTL, lifecycle-log cache, and bounded/body-free task-document summaries with on-demand full bodies. | `GateReadFoldTests`; `TaskDocSharedCacheTests`; `GitStatusCacheTests`; `LifecycleLogCacheTests`; `TaskDocumentsPayloadBudgetTests` | mcp/tests/test_projection_scaling_cs6.py:67-99; mcp/tests/test_projection_scaling_cs6.py:102-148; mcp/tests/test_projection_scaling_cs6.py:151-189; mcp/tests/test_projection_scaling_cs6.py:323-418; mcp/tests/test_projection_scaling_cs6.py:421-587 |
| `LandingProjectionHotPathTests`: the invalid-landing containment case and the heartbeat landing-tail regression. | `LandingProjectionHotPathTests` | mcp/tests/test_projection_scaling_cs6.py:192-320 |
| `ContractSnapshotSharedPassTests`: parse counting, one-enumeration-per-tick, output parity, live-set retention, chmod-000 and utime-pinned-rewrite ctime hardening, and malformed-retry regressions. | `ContractSnapshotSharedPassTests` | mcp/tests/test_projection_scaling_cs6.py:590-858 |
| The shared per-tick contract snapshot + stat-identity parse cache under test. | `ContractSnapshotCache` | mcp/src/agents_remember/serving/projections/contract_snapshot.py:60-126 |
| The single per-tick build in `project_and_write` the full-tick regression instruments: one shared `ContractSnapshotCache`, then exactly one `state.read(...)` pass per tick. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275 |
| Projection store implements lifecycle-log caching and over-budget task-document payload warnings. | `project_and_write`; `_warn_if_task_documents_payload_over_budget` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275; mcp/src/agents_remember/serving/projections/projection_store.py:278-304 |
| Snapshot readers implement the shared task-document cache (`_task_doc_cache` + `_iter_task_document_payloads`), the single-read gate fold (`read_gates`), and the git-status TTL cache (`STATUS_PAYLOAD_TTL_SECONDS` / `_cached_local_status`). | "_task_doc_cache = TaskDocumentPayloadCache()"; "def read_gates(coordination_root: Path"; "STATUS_PAYLOAD_TTL_SECONDS = 8.0"; "def _cached_local_status(  # pragma: no cover" | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:26-26; mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:32-32; mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:105-105; mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:382-382 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## 260727-CHATS-IM-L2 Current Delta

`LandingProjectionHotPathTests` now proves a heartbeat replaces only landing rows from published
landing authority while contract, guidance, and other status facts retain identity and value.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: replaced the obsolete unbounded-payload characterization and todo with the source-proven bounded/body-free summary and on-demand-body contract.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:31+02:00 — 260731-EFA-L4 curator: repaired the `observer/snapshots.py` citation,
  which named three symbols and pointed at none of them. `L485-L516` and `L601-L663` sat in an
  unrelated docstring and in `read_agent_pickups`; the row is now L132-L144 (the two module-level
  caches declared together: `_task_doc_cache = TaskDocumentPayloadCache()` at L137 and
  `STATUS_PAYLOAD_TTL_SECONDS`/`_status_payload_cache` at L143-L144), L155-L173
  (`_iter_task_document_payloads`, which routes through the cache when `now` is not None),
  L520-L549 (`read_gates`, the one-scan/one-read-per-log fold with the
  `GATE_COMPACT_TTL_SECONDS`-gated physical prune) and L744-L797 (`_safe_status_payload` plus
  `_cached_local_status`, the TTL lookup). Each range re-read at its new position. That drift
  pre-dates this leaf: `snapshots.py` changed here only at L675-L680 and L787-L792 (two
  `dict(...)` widenings at the now-TypedDict `lifecycle_guidance` / `projected_status_payload`
  boundaries), both below every cited range, and the claim itself is unchanged. In the test file
  the only change was two `LandingProjectionHotPathTests` fixtures moving `workflow_kind="light"`
  to `"light-task"`, one-for-one, so all six own-file ranges plus the `contract_snapshot.py` (whole
  file, 145 lines) and `projection_store.py` rows were re-verified and still land — no counter,
  cache assertion, budget threshold or ctime-hardening case changed.

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
