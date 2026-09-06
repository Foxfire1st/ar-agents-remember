# mcp/tests/test_task_document_master.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_master.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks master task authoring without creating a lifecycle, numbered subtask insertion/update, exact leaf readiness at completion, and refusal to erase or change unresolved row identity/multiplicity. Completed rows are revalidated against their leaf; removal deletes a ready leaf and row but leaves all bytes untouched on unresolved refusal.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Create master writes task json without lifecycle | `test_create_master_writes_task_json_without_lifecycle` | mcp/tests/test_task_document_master.py:55-59 |
| Set subtask inserts then updates by number | `test_set_subtask_inserts_then_updates_by_number` | mcp/tests/test_task_document_master.py:61-73 |
| Set subtask completed refuses unready or missing exact leaf | `test_set_subtask_completed_refuses_unready_or_missing_exact_leaf` | mcp/tests/test_task_document_master.py:75-88 |
| Replace cannot erase or change unresolved row identity or multiplicity | `test_replace_cannot_erase_or_change_unresolved_row_identity_or_multiplicity` | mcp/tests/test_task_document_master.py:90-141 |
| Master completion revalidates pending leaf behind completed row | `test_master_completion_revalidates_pending_leaf_behind_completed_row` | mcp/tests/test_task_document_master.py:143-168 |
| Remove subtask deletes leaf doc and row | `test_remove_subtask_deletes_leaf_doc_and_row` | mcp/tests/test_task_document_master.py:189-201 |
| Remove subtask refuses unresolved row without touching any file | `test_remove_subtask_refuses_unresolved_row_without_touching_any_file` | mcp/tests/test_task_document_master.py:203-219 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints the public tool response registry to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: task-doc imports moved under
  `application/task_docs/`; `MasterApplicationTests` gained the sprint-get regression proving
  `task_doc.get` on a sprint carries declared `linkageFacts` in the identity payload. Verified at
  code commit e5cb139f.
- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-16T04:24+02:00 — No content impact: removed the now-unused `write_contract` import after the lifecycle-id fixture moved to the real document builder; assertions and production route are unchanged.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: lifecycle-id altitude is tested through the document builder with a master contract, avoiding an impossible persisted leaf topology while preserving the non-leaf assertion.
- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: partial leaf-artifact removal remains
  idempotent, deleting and reporting only the JSON or Markdown sibling that still exists.
- 2026-08-15T12:53+02:00 — No content impact: corrected one synthetic leaf row's repository id to
  the canonical `agents-remember` fixture scope required by queue-aware topology publication; the
  master application assertion is unchanged.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
