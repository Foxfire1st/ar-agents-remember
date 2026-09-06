# mcp/tests/test_lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_lifecycle_finalize.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Lifecycle finalization of a leaf and immediate parent row.

## Code Commentary

### Logic

Finalization marks the leaf Completed and its parent subtask row Completed, records the finalization decision and leaves the master inProgress. Failure while publishing the second document rolls back the leaf, parent and their rendered files to exact previous bytes.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Child completion does not automatically complete the master. Document publication is atomic across the affected pair and is not a replacement for lifecycle acceptance.

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
| Finalized updates leaf and immediate parent row. | `test_finalized_updates_leaf_and_immediate_parent_row` | mcp/tests/test_lifecycle_finalize.py:125-146 |
| Second document publish failure rolls back leaf and parent. | `test_second_document_publish_failure_rolls_back_leaf_and_parent` | mcp/tests/test_lifecycle_finalize.py:148-176 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: widened the
  WorktreeSupportTests citation to the class range it actually occupies (979-1054).
- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read and bounded the unchanged
  `TaskDocument` fixture dependency to the current source. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T04:54+02:00 — 260815-DAG-L14 curator: re-read the `TaskDocument` claim — the persisted
  model gained sprint `seats` and typed `masterRef` rows; wording retained, citation regenerated to
  the current class lines, stamp advanced to code commit 2f494982.


- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: a queue-governed task-document
  reconciliation refusal now returns the exact `task-queue-blocked` result without mutating task
  facts after worktree cleanup.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the finalize-response import move and confirmed the
  regression contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — No content impact: the parameterized finalization subtest reports a
  serializable label under xdist; finalization setup, operation, and assertions are unchanged.
  Verification metadata remains pinned until closeout.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-07-31T16:50+02:00 — No content impact: the fixture's `default_contract` call now passes the
  `ContractTask` / `LeafIdentity` / `RepoBranchPlan` parameter objects added for PLR0913 instead of
  ten loose keyword arguments, and `ruff format` rewrapped the `patch(...)` context manager in the
  cleanup-blocked test. The temporary Git repos, the disabled-memory contract, the `write_task_doc`
  fixture path, and every covered behavior enumerated above are unchanged.
- 2026-06-23T22:50+02:00 — Created focused lifecycle finalizer regression coverage. Verification metadata is pending until closeout stamps the source commit.
