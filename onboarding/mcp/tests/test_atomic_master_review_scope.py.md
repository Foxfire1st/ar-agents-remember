# mcp/tests/test_atomic_master_review_scope.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Checks route-review altitude and ownership: atomic child deferral, a missing canonical master,
a parented leaf without its parent contract, and the existing organizational leaf review boundary.
Aggregate master currentness, membership and dependency checks belong to the identity tests.

## Code Commentary

### Logic

The tests construct canonical contracts and exercise the four retained ownership/altitude cases.
Explicit worktree-services composition enables converted-memory fixture setup without adding
aggregate-master assertions. The shared fixture requires a parent contract before loading it,
so a parented leaf cannot silently become a standalone case. Typed ownership refusals and the
organizational leaf's current review boundary remain distinct.

### Conventions

These tests cover pure scope composition and refusal classification. They do not run the full
integration quality gate or make any protected-ref publication.

### Invariants And Boundaries

- Atomic child review is deferred and never accepted as a local gate.
- The atomic fixture must retain a parent contract before the series contract is loaded.
- Missing or invalid parent/master ownership keeps its typed refusal.
- Organizational leaves retain their own current review; aggregate membership and dependency checks are elsewhere.

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
