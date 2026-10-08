# mcp/tests/test_knowledge_store.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Read behavior and schema integrity of derived knowledge index files.

## Code Commentary

### Logic

Test-only rows supply the branching fixture. Production readers preserve divergent same-label revisions, reopen exact identities/digests and reject writable or absent-file opens. [1] [2] [13]

Cases protect database immutability triggers, read-time payload seals, declared schema structure and its pin. Missing tables/triggers or another version refuse open and name conversion. Canonical insert/duplicate/lineage write rules and their old cases are removed. [6] [7] [8]

### Invariants And Boundaries

- Production opens are read-only; fixture row insertion is test-only.
- Schema drift refuses rather than repairing or re-pinning.

## Evidence

### Repo-Internal References


- Both successors remain separately readable. [1]


- Identity/schema preserved on reopen. [2]


- Stored revisions reject mutation. [6]


- Decode verifies seal beyond statement. [7]


- Schema drift and unsupported files refuse. [8]


- Read-only production store and test-only builder. [13]


### Cross-Repo References

No cross-repository contract is established by this file.
