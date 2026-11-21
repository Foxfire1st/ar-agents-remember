# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Protect exact integration-ref ownership, two-output CAS races, and real object/ancestry checks independently of cached ledger data.

## Code Commentary

### Logic

The class exercises protected branch aliases/nested checkouts/memory names, a code CAS followed by a competing memory CAS, and successful publication with missing or damaged cache data. The torn-pair case preserves the raced memory ref and reports accepted/intended code and actual memory commits. Cache-damage cases verify the accepted refs land without increasing reachable memory history.

Two minimal real-repository cases exercise the surviving proof directly: accepted memory outside the exact source ancestry refuses, and an absent accepted code object refuses even when memory is current. Arbitrary cached rows are not a publication predicate.

`test_a_code_side_that_lands_nothing_is_not_checked_again` supplies a deliberately failing hook and asserts that it never runs when the protected code reference already equals the candidate; this test prepares the landing without publishing refs.

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

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Protected branch aliases and nested/foreign workbench identities refuse. [1]

- A competing memory CAS is preserved after code has landed. [2]

- Cache absence/corruption cannot affect the accepted pair or create another memory commit. [3]
- Real accepted-object and source-ancestry failures remain enforced. [4]



- Production ref preparation and publication proof. Anchor: `prepare_integration_ref_move` [5]




### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
