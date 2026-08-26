# mcp/tests/test_closeout_queue_projection.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_closeout_queue_projection.py`          |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Covers closeout projection reconstruction from current task, review, priority, waiting-door, and
source-pair activation truth. The suite proves old rows are never rebuild input, source evidence
drift is fingerprinted, unsafe filesystem authorities fail closed, completed sprints become valid
terminal-empty projections, and multiple live atomic series remain independently observable.

## Code Commentary

### Logic

The fixture publishes canonical tasks and waiting doors, then calls the production rebuild path.
Focused cases mutate one source at a time: task/review/grade evidence, nonregular series or door
entries, a symlinked door ancestor, sprint completion, activation reselection, and malformed
activation. The two-series case selects master A then master B and checks that readiness and
`atomic-series-paused-by` waiting reverse without deleting either series.

### Conventions

Filesystem hazards use real paths; projection membership is asserted through public model fields.
Selector corruption is injected directly only to prove strict observation and scoped invalidation.

### Invariants And Boundaries

- Rebuild inputs are current canonical sources, never old projection rows.
- Multiple live series are valid; selection supplies readiness, not existence or retirement.
- Malformed/nonregular evidence becomes explicit invalid-empty projection evidence, never absence.
- Projection failure does not mutate task truth, selector state, or operation lifecycle evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rebuild discards old rows and derives membership only from current waiting doors. | `test_rebuild_uses_only_current_waiting_doors_not_old_rows` | mcp/tests/test_closeout_queue_projection.py:41-63 |
| Multiple live series project selected/paused waiting independently. | `test_multiple_live_atomic_series_are_valid_active_paused_waiting_candidates` | mcp/tests/test_closeout_queue_projection.py:196-253 |
| Malformed activation invalidates only the disposable projection and names selection repair. | `test_malformed_activation_invalidates_only_projection_and_names_selection_repair` | mcp/tests/test_closeout_queue_projection.py:255-275 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned projection suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces source-census purity, deterministic fingerprints, drift fencing, malformed-neighbor refusal,
waiting-only membership, valid terminal-empty projections, and independent atomic-series activation.
Two simultaneous live series are valid: the selected master can be ready while the other reports
`atomic-series-paused-by`, and switching selection reverses the candidate-local waits. With no
selection, both wait as `atomic-series-not-selected`. Malformed selector evidence invalidates only
the disposable projection and names selecting-dispatch repair; it does not mutate tasks or lifecycle
evidence.

### Current Invariants

- Old queue rows are never rebuild input.
- Source mismatch or unreadable authority is non-admitting and never treated as absence.
- Multiple live series contracts are normal; activation state, not contract census order, supplies
  selection waiting.
- Corrupt activation produces invalid-empty projection and explicit repair rather than stale rows
  or a task-authoring lock.

## Update History

- 2026-08-26T08:45+02:00 — Replaced obsolete queue-artifact references with the frozen
  door-derived, multi-series activation cases and restored canonical Docs/Cross-Repo sections.

- 2026-08-26T03:37+02:00 — Added real two-live-series activation switching and malformed-selector
  projection-isolation forcing. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue projection test suite.
  Verification metadata pinned until closeout stamps the L8 commit.
