# mcp/tests/test_task_documents_graph_projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_documents_graph_projection.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `dca949f3c1652d76edf277eef86c6399c4ab8404` |
| lastVerifiedCommitDate | 2026-09-14T10:26:38+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks rendered graph projection joins actual master documents to segment titles, wave/predecessor facts and frontier state. Duplicate local leaf numbers keep master-qualified titles rather than colliding in a flat lookup. An `abandoned` master reads `abandoned` and stops gating the segment that waited on it. Projection is display data, not independent execution authority.

Since 260913-LCA-L10 it also pins the projection's **index reachability** contract: a master's sub-task
row must resolve to a projected document whatever build wrote the leaf's durable JSON, while a genuinely
broken document is still withheld. `SubTaskIndexReachabilityTests` drives that through the reader the
dashboard's own index rule uses, so a read edge that deletes unparseable documents fails here instead of
appearing in the UI as a row of dead text.

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
| Segmented master scenario projects titles and predecessors | `_segmented_scenario`; `test_segmented_master_scenario_projects_titles_and_predecessors` | mcp/tests/test_task_documents_graph_projection.py:64-128; mcp/tests/test_task_documents_graph_projection.py:130-151 |
| An abandoned master reads `abandoned` and no longer gates its successor, whose frontier becomes ready | `test_abandoned_master_reads_abandoned_and_stops_gating_its_successor` | mcp/tests/test_task_documents_graph_projection.py:153-168 |
| Duplicate local leaf numbers keep master qualified titles | `test_duplicate_local_leaf_numbers_keep_master_qualified_titles` | mcp/tests/test_task_documents_graph_projection.py:170-221 |
| The dashboard's own index rule, reproduced: a row drills in only when the pool holds a document in the master's own directory whose file stem is the row's `file`. | `_index_doc` | mcp/tests/test_task_documents_graph_projection.py:224-240 |
| The reachability contract: a completed leaf written by a newer build stays reachable, an unstarted one stays reachable, and a broken document is still withheld. | `SubTaskIndexReachabilityTests`; `test_completed_leaf_written_by_another_build_stays_reachable_from_the_index` | mcp/tests/test_task_documents_graph_projection.py:243-343; mcp/tests/test_task_documents_graph_projection.py:307-343 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## 260913-LCA-L10 Sub-Task Index Reachability

The module gained `_index_doc` (224-240) and `SubTaskIndexReachabilityTests` (243-343) with one case,
`test_completed_leaf_written_by_another_build_stays_reachable_from_the_index` (307-343). `_index_doc`
reproduces the dashboard's own index rule (`sliceForRef`): a master's sub-task row drills in only when
the projected pool holds a document in the master's own directory whose file stem is the row's `file`.
The case therefore asserts the exact property the projection owes every authored row, through
`read_task_documents`, rather than a proxy for it.

The fixture writes three rows over one temporary task root: `D-L1` completed, `D-L2` unstarted, and
`D-L3` whose master row points at a genuinely broken document. It then republishes the completed leaf's
durable JSON with one unknown field added at the step level — the skew the live incident carried — and
writes the broken document by **deleting a required field**. The assertions split by outcome:
`D-L1` (written by a newer build) resolves with `("01_DONE", "Completed", 1, 1)`, `D-L2` resolves as
before, and `D-L3` is `None`, i.e. still withheld. That third assertion is the fail-closed half: an
unknown key must not become "project anything".

Two mechanics a future reader must not "fix": the skewed payload is written with `Path.write_text`
rather than `write_task_doc`, because `write_task_doc` takes a validated `TaskDocument` and **must**
refuse a document carrying the unknown key — the direct write is what models another build's durable
output, not a workaround; and the unknown field is spelled `checkpoint` on the step, mirroring where the
live skew landed (`step.note`, `tasks/document.py:121`) without depending on a field this reader may
later learn.

The case is the module's only protection for the tolerant read edge: reverting the single
`extra_forbidden` condition fails exactly this case and nothing else.

## Update History

- 2026-09-14T10:16+02:00 — 260913-LCA-L10 (curator, uncommitted change set on `ar/260913-lca-l10-ar`,
  base `4214d7a1`): registered the new `_index_doc` helper and `SubTaskIndexReachabilityTests` with its
  single reachability case — a completed leaf written by a newer build stays reachable from the master's
  sub-task index while a broken document is still withheld — and recorded the two mechanics that must
  not be "fixed" later (the direct `Path.write_text` because `write_task_doc` must refuse the skewed
  document, and the `checkpoint` field on a step mirroring where the live skew landed). **Re-pointed the
  three pre-existing rows**, which the new imports shifted by two lines (`_segmented_scenario` 62 → 64,
  the segmented case 128 → 130, the abandonment case 151 → 153, the duplicate-leaf-numbers case
  168 → 170). For the record, the dead-text element this case keeps a row out of is exactly
  `dashboard/src/panels/detail-panel/taskReader.tsx:434`; this card never carried a range for it, and no
  dashboard file is in this change set. Metadata stamps remain
  closeout-owned; no verification stamp advanced and no execution or acceptance claim is made here.
- 2026-09-11T23:05:00+00:00: Master abandonment curation: the segmented-scenario body was extracted into the `_segmented_scenario(atomic_status=...)` helper and `test_abandoned_master_reads_abandoned_and_stops_gating_its_successor` was added, proving an abandoned master reads `abandoned` and stops gating its successor. Rebound all three rows to their current extents and added the new test's row. Content change, not a range repoint.
- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: added the public-reader proof that duplicate local
  leaf numbers retain their owning master's qualified title through the served projection.
  Verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the task-documents projection

wiring suite — render-ready graph view on sprint docs, segmented-master scenario, and the

master-join-table builder. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the task-documents projection
  wiring suite — render-ready graph view on sprint docs, segmented-master scenario, and the
  master-join-table builder. Verified at code commit b7f2c8e2.
