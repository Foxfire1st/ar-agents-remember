# mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks contract recovery for unknown vocabulary: the reader degrades without stranding the task, a rewrite heals the file, the writer refuses unsupported values the reader tolerated, and a live contract projects into the strict wire model. Tolerant reads are an explicit recovery boundary, not permission for writers to emit arbitrary values.

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
| Every vocabulary cell degrades rather than stranding the task | `test_every_vocabulary_cell_degrades_rather_than_stranding_the_task` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:119-129 |
| A rewrite heals the file and that is the recovery path | `test_a_rewrite_heals_the_file_and_that_is_the_recovery_path` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:131-139 |
| The writer refuses what the reader tolerated | `test_the_writer_refuses_what_the_reader_tolerated` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:141-156 |
| A live contract projects onto the wire model | `test_a_live_contract_projects_onto_the_wire_model` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:159-171 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-11T19:58+02:00 — Reconciled `test_wire_vocabulary_exhaustiveness_boundary.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
