# mcp/tests/test_author_execution_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_author_execution_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Incremental execution-graph authoring through the public task-document operation.

## Code Commentary

### Logic

The retained successful batch replaces a master node with two segments and adds a provenance-bearing edge. Dry run preserves the entire document snapshot; apply persists typed nodes, derived waves and rendered navigation. A duplicate-node batch refuses atomically without changing any document.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Disposable coordination roots isolate publication. Do not attribute the removed graph-bootstrap, role-validation or edge-error matrix to these two cases.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Dry run previews and writes nothing then apply publishes. | `test_dry_run_previews_and_writes_nothing_then_apply_publishes` | mcp/tests/test_author_execution_graph.py:130-191 |
| Batch atomicity leaves everything untouched on failure. | `test_batch_atomicity_leaves_everything_untouched_on_failure` | mcp/tests/test_author_execution_graph.py:193-215 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: judgment-provenance forcing now asserts the typed task-execution-graph-judgment-required refusal for a judgmentless add_edge (F5) instead of the old raw pydantic wrap. Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the unmigrated-sprint refusal became the graph-less
  bootstrap forcing (first `add_node` batch creates the graph with `bootstrapped: true`; final
  validation requires exact membership and explicit natures). Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created for the incremental graph-authoring forcing
  suite (split from `test_task_execution_topology.py`). Verification remains closeout-owned.
