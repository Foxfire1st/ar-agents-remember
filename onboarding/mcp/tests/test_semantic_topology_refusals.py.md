# mcp/tests/test_semantic_topology_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_semantic_topology_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash |  `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate |  2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces exact typed failures for missing, ambiguous and malformed semantic-topology facts, plus duplicate-node refusal during whole-graph admission. Status and detail assertions matter: no permissive fallback or invented authority substitutes for the missing structural input.

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
| Semantic topology refuses exact missing ambiguous and malformed facts | `test_semantic_topology_refuses_exact_missing_ambiguous_and_malformed_facts` | mcp/tests/test_semantic_topology_refusals.py:91-149 |
| Semantic topology refuses duplicate node during whole graph admission | `test_semantic_topology_refuses_duplicate_node_during_whole_graph_admission` | mcp/tests/test_semantic_topology_refusals.py:152-162 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read both new refusal cohorts against their
  exact working-tree ranges; commit verification remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the semantic-topology refusal card.
  Verification remains closeout-owned.
