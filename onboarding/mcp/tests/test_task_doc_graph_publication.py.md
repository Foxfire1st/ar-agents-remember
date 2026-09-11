# mcp/tests/test_task_doc_graph_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_graph_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash |  `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate |  2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that task publication accepts zero or one graph-bearing document in a batch. Two graph documents refuse before either document bytes, the supplied publisher, or projection publication can change. Exact snapshot comparisons make the no-partial-write boundary observable.

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
| Plain or single graph document is the supported batch shape | `test_plain_or_single_graph_document_is_the_supported_batch_shape` | mcp/tests/test_task_doc_graph_publication.py:101-110 |
| Two graph documents refuse before task or projection publication | `test_two_graph_documents_refuse_before_task_or_projection_publication` | mcp/tests/test_task_doc_graph_publication.py:112-140 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-24T13:43+02:00 — Created for DAGQC L1: focused zero/one/two graph-publication
  cardinality and no-effect forcing. Verification remains closeout-owned because the test source
  is uncommitted.
