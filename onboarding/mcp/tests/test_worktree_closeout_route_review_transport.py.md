# mcp/tests/test_worktree_closeout_route_review_transport.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Route-review refusal payload shaping at the certification-admission seam, after the closeout
transport gate was removed.

## Code Commentary

### Logic

The registered preview and apply cases were deleted with the closeout route-review gate, and
the gate's removal is pinned at both altitudes by
`test_closeout_never_gates_on_a_route_review_record_at_either_altitude`. What remains is the
payload shaping for a refusal some other caller raises: the case raises a certification
admission refusal carrying a `route-review-required` finding and proves the structured
response keeps the observed status and detail, promotes the concrete status, and names
`record_route_review` as the next operation without inventing `nextTool`. This fixture does not
publish a review, commit code, or certify closeout.

### Conventions

This file is integration evidence for public transport serialization and application-boundary
projection. The review payload remains caller-supplied; `nextRequiredArgs` names it without
inventing `nextArgs`.

### Invariants And Boundaries

- A route-review refusal leaves task documents, contracts, and code `HEAD` unchanged.
- The response keeps exact observed status/detail and task-bound recovery identity.
- Temporary transport evidence does not establish terminal rail, Dagger, aggregate review, or
  acceptance behavior.

## Evidence

### Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture.

No external domain evidence applies.

### Repo-Internal References

- Registered preview transport case was deleted with the closeout route-review gate; the removal is pinned at both altitudes by the atomic-master public closeout test. [1]
- Certification projection preserves the route finding while promoting status. [2]
- Registered apply transport case was deleted: the module docstring records that the gate was removed, so only the certification-admission refusal payload shaping remains as this module's route-review evidence. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

The fixture does not establish a live external integration.
