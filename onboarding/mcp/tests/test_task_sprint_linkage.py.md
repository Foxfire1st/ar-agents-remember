# mcp/tests/test_task_sprint_linkage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_sprint_linkage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Provides a shared temporary task-linkage fixture and canonical attach/detach/report helpers; no test methods remain. It writes typed master/sprint documents and snapshots their bytes for consuming structural-publication tests. The historical attach/render/registration acceptance inventory in its docstring is not the current executed population.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The test-shaped filename is retained for imports by other suites. Helper availability is not
a passing test, and the module has no collected test definitions of its own.

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
| Shared helper _judgment_register | `_judgment_register` | mcp/tests/test_task_sprint_linkage.py:53-54 |
| Shared helper _judgment_row | `_judgment_row` | mcp/tests/test_task_sprint_linkage.py:57-61 |
| Shared helper _register_section | `_register_section` | mcp/tests/test_task_sprint_linkage.py:64-69 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: added explicit sprint-seat
  schema forcing for the polymorphic reviewer. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — Rebuilt topology fixtures after each task publication so linkage assertions always consume the current generation.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added test_report_does_not_flag_a_sprint_as_uncommanded_master and test_attach_wraps_a_serving_build_preflight_refusal; updated test_report_seat_row_edge_shapes to the F8 fact vocabulary (seat-doc-row-unresolved). Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created (sidecar was missing since the file's L14
  creation) and recorded the L16 signature-compat update (`call=TaskDocCall(dry_run=...)`);
  suite purpose unchanged. Verified at code commit a9d50e08.
