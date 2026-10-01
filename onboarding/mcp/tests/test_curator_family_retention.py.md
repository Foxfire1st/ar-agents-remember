# mcp/tests/test_curator_family_retention.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- Preview, cross-leaf publication, old-row preservation and exact retry. [1]
- Invalid and foreign references refuse without changing current knowledge. [2]
- Different old edges cannot duplicate one new endpoint. [3]
- Retain/retire conflict refuses in the same or different entries. [4]
- Changing the retained set or a basis conflicts with its allocated declaration. [5]

| Refused-entry effects stay outside conflict admission; preview and publication preserve the eligible outcome and original refusal. | `test_refused_retirement_does_not_block_an_eligible_retaining_successor` | mcp/tests/test_curator_family_retention.py:329-372 |
| Refused-entry effects stay outside conflict admission; preview and publication preserve the eligible outcome and original refusal. | `test_refused_retention_does_not_block_eligible_retirement_or_independent_entry` | mcp/tests/test_curator_family_retention.py:375-427 |

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
