# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Protect exact integration-ref ownership, two-output CAS races, and real object/ancestry checks independently of cached ledger data.

## Code Commentary

### Logic

The class exercises protected branch aliases/nested checkouts/memory names, a code CAS followed by a competing memory CAS, and successful publication with missing or damaged cache data. The torn-pair case preserves the raced memory ref and reports accepted/intended code and actual memory commits. Cache-damage cases verify the accepted refs land without increasing reachable memory history.

Two minimal real-repository cases exercise the surviving proof directly: accepted memory outside the exact source ancestry refuses, and an absent accepted code object refuses even when memory is current. Historical table-row/header tests and their cache-commit fixture machinery are retired; arbitrary cached rows are no longer a publication predicate.

### Conventions

The broader cases use the shared configured authority fixture; the object/ancestry cases use a minimal contract so the Git predicate is the subject. These assertions do not certify a live installation.

### Invariants And Boundaries

- A torn pair never permits clobbering concurrent memory work.
- Cache damage cannot change accepted output identity or block ref movement.
- The accepted code object and memory source ancestry remain mandatory.
- Fixture setup and historical coverage notes do not imply additional retained scenarios.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Protected branch aliases and nested/foreign workbench identities refuse. [1]
- A competing memory CAS is preserved after code has landed. [2]
- Cache absence/corruption cannot affect the accepted pair or create another memory commit. [3]
- Real accepted-object and source-ancestry failures remain enforced. [4]
- Production ref preparation and publication proof. [5]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
