# mcp/tests/test_sequential_default_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sequential_default_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force graph-less atomic execution nature while keeping durable master work independent from
source-pair activation. Multiple non-terminal series contracts may coexist; one strict selector
decides which master may expose implementation for a protected code/external-memory pair.

## Code Commentary

### Logic

`SchedulingModeTests` proves mode resolution (graph ⇒ dag, no graph ⇒ atomic-sequential, non-sprint
refused), the effective-nature matrix, and that activation remains a separate authority even under
an authored DAG. `AtomicSeriesSelectionTests` proves a second bootstrap selects the new master and
logically pauses the first without retiring its branches/contract; a pre-publication bootstrap
failure preserves the former selection; a post-publication sync refusal keeps the requested master
`reconciling`; retry resumes it to `active`; terminal stale artifacts remain replaceable; standalone
selection binds the repository-default pair; leaf construction selects its parent first; and
manager dispatch selects the requested master before spawning.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- Contract presence never proves selection. Assertions read the strict source-pair activation
  snapshot and preserve both masters' durable work.
- Failure timing is explicit: before contract publication leaves selection unchanged; after
  selection publication leaves durable `reconciling` evidence for exact retry/cancel.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode/effective-nature and activation-independence forcing. | `SchedulingModeTests` | mcp/tests/test_sequential_default_mode.py:122-190 |
| Selection switch, pause, failure timing, retry, standalone, leaf, and dispatch forcing. | `AtomicSeriesSelectionTests` | mcp/tests/test_sequential_default_mode.py:184-348 |
| Scheduling mode deliberately owns no series-contract lane reader. | `resolve_scheduling_mode`; `effective_execution_nature` | mcp/src/agents_remember/worktrees/scheduling_mode.py:45-72; mcp/src/agents_remember/worktrees/scheduling_mode.py:93-116 |
| Series bootstrap selects and reconciles through the activation transaction. | `ensure_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:216-286 |
| Structural implementation admission selects before spawn. | `_implementation_series_admission_refusal` | mcp/src/agents_remember/application/structural/agent_tools.py:521-603 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned scheduling suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for this changed
  graph-less scheduling suite card.

- 2026-08-26T08:25+02:00 — Rebound the atomic-series selection class to its frozen source range;
  pause/reselection semantics are unchanged.

- 2026-08-26T03:37+02:00 — Replaced global sequential-lane forcing with independent source-pair
  selection, logical pause, reconciling retry, multiple-live-series preservation, and
  reconciliation-before-leaf/dispatch exposure. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired the `_manager_series_bootstrap_refusal` citation range (agent_tools.py:419-484 → 518-582) surfaced by the leaf-scoped quality check; no content impact on the documented test contract. Verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the atomic-sequential default and series
  lane forcing suite. Verification remains closeout-owned.
