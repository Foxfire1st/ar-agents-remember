# mcp/tests/test_atomic_master_review_scope.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Checks the pure route-review scope resolver: atomic child deferral, master ownership, currentness,
evidence and dependency freshness, ordered membership, and exclusion of status-only bookkeeping.

## Code Commentary

### Logic

The tests construct canonical contract and candidate inputs, then exercise scope ownership errors,
master-review requirements, currentness changes, stale evidence, membership changes, and status-only
updates. The shared fixture asserts that a parent contract exists before loading the series contract,
so a parented leaf cannot silently become a standalone case. They keep the resolver's typed refusal
surface explicit so integration callers can act on the exact stale edge.

### Conventions

These tests cover pure scope composition and refusal classification. They do not run the full
integration quality gate or make any protected-ref publication.

### Invariants And Boundaries

- Atomic child review is deferred and never accepted as a local gate.
- The atomic fixture must retain a parent contract before the series contract is loaded.
- Master scope membership/order and evidence/dependency digests are currentness inputs.
- Status-only bookkeeping cannot manufacture a current review.

### Todos

Final combined master integration execution remains parent-owned.

## Evidence

### Docs References

No relevant external documentation was configured.

No external documentation source was configured for this test module.

### Repo-Internal References

- Fixture parent-contract invariant. [1]
- Deferred atomic child and ownership behavior. [2]
- Master review requirement and stale-evidence behavior. The requirement is gone from this module and from integration; aggregate currentness now lives in the atomic-master identity tests. [3]
- Membership and status-only invariants moved to the identity tests; this module retains the organizational leaf boundary. [4]
- Canonical resolver under test; the master-only require_current_master_route_review was folded away into the altitude-dispatching resolver. [5]

### Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.
