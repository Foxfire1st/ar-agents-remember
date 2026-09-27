# mcp/tests/test_curator_family_retention.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_family_retention.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T00:42:04Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c`|
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Exercises the public curator CLI path for a family successor that retains exact stored sibling revisions and adds a genuine new obligation. Fixtures use separate leaf scopes and candidates, so successful retention cannot be explained by replaying another leaf’s allocation.

## Code Commentary

### Logic

The baseline and successor are authored through the existing CLI with an ordinary enclosure and the declared published memory location. The 2- and 11-sibling cases check projected preview without writes, published exact rosters, one genuinely new invariant/revision, unchanged old rows across seven protected tables, and deterministic retry after reordering references.

Invalid-reference cases cover malformed IDs, absent memberships, wrong-family and undeclared-predecessor references, repeated IDs and a membership read from a separately published foreign namespace. Both preview and commit refuse without changing published bytes or the existing candidate identity.

Separate tests reject two historical memberships that collapse to one successor endpoint, retaining and retiring the same source membership in the same or separate entries, and changing an allocated retention set or basis. Two further public preview/publication cases isolate already-refused effects: a refused retirement cannot block a valid retaining successor, and a refused declaration’s retention cannot block eligible retirement or independent authoring. Both preserve the original declaration refusal and verify actual published rosters and old records. These cases measure the existing public writer and readback; fixture-authored guarantees are test data rather than project knowledge.

### Conventions

Reuse the existing ordinary-publication and curator-family fixtures. Read-only SQLite snapshots compare complete old row values; they are verification observations and never a write path. The module is registered in the unit-regression evidence lane.

### Invariants And Boundaries

- Unchanged siblings keep exact revision IDs; only the new obligation adds an invariant revision.
- Old family revisions, memberships, scope and provenance remain stored.
- Failed and projected authoring cannot be reported as published knowledge.
- Tests do not certify the real L38 family update or replace curator-authored input.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| Preview, cross-leaf publication, old-row preservation and exact retry. | `test_public_successor_retains_exact_siblings_and_publishes_across_leaf_scopes` | mcp/tests/test_curator_family_retention.py:147-199 |
| Invalid and foreign references refuse without changing current knowledge. | `test_invalid_retention_refuses_without_changing_existing_knowledge` | mcp/tests/test_curator_family_retention.py:202-268 |
| Different old edges cannot duplicate one new endpoint. | `test_distinct_old_memberships_cannot_duplicate_one_successor_endpoint` | mcp/tests/test_curator_family_retention.py:271-303 |
| Retain/retire conflict refuses in the same or different entries. | `test_retaining_and_retiring_the_same_source_membership_refuses_without_history_change` | mcp/tests/test_curator_family_retention.py:306-326 |
| Changing the retained set or a basis conflicts with its allocated declaration. | `test_changed_retention_cannot_reuse_an_allocated_family_declaration` | mcp/tests/test_curator_family_retention.py:430-448 |

| Refused-entry effects stay outside conflict admission; preview and publication preserve the eligible outcome and original refusal. | `test_refused_retirement_does_not_block_an_eligible_retaining_successor` | mcp/tests/test_curator_family_retention.py:329-372 |
| Refused-entry effects stay outside conflict admission; preview and publication preserve the eligible outcome and original refusal. | `test_refused_retention_does_not_block_eligible_retirement_or_independent_entry` | mcp/tests/test_curator_family_retention.py:375-427 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-27T00:42:04Z — L39: corrected this new file’s verification header. The file does not exist at the old base commit, so its verification hash/date remain blank until normal closeout stamps the real source commit. Working-candidate provenance is retained in task artifacts, not substituted into the verification fields. Prior history remains unchanged.

- 2026-09-27T00:23:24+00:00: Generated citation repair: `test_changed_retention_cannot_reuse_an_allocated_family_declaration` repointed to mcp/tests/test_curator_family_retention.py:430-448. No content impact: mechanical anchor-range projection bound to citation source snapshot b3d8afb8f498929bc7654ed009a5dcd2751720da84f958f62808fd0ab2890e00; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T00:16:25Z — L39 W2: Added the two public refusal-isolation regressions while preserving the valid-conflict, immutable-retention and retry account. Source-candidate tests remain distinct from installed or actual L38 publication.


- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

