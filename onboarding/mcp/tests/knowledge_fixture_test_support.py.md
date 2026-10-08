# mcp/tests/knowledge_fixture_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Shared read-side rows for divergent revisions, overlapping families and realization claims.

## Code Commentary

### Logic

One dataset holds the base revision and two different same-label successors. The graph half adds invariants, overlapping families, family successors and three realizations including an absent source path. BranchingKnowledgeFixture retains their identities and reopens persisted rows. [1] [2]

Construction uses the test-only RowStore, which computes production seals and inserts index-shaped rows without retired write-admission guards. [5]

### Invariants And Boundaries

- Friendly display labels are not revision identity.
- An unavailable source does not erase a fixture claim.
- This fixture is not production write authority.

## Evidence

### Repo-Internal References


- Fixture identities and both scenario halves. [1]


- One builder constructs both halves. [2]


- The test-only builder supplies rows without canonical write rules. [5]


- Both same-label successors remain readable. [7]


### Cross-Repo References

No cross-repository contract is established by this file.
