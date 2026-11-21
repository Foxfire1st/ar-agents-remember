# mcp/tests/test_worktree_closeout_route_review_transport.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Route-review refusal payload shaping at the certification-admission seam, after the closeout
transport gate was removed.

## Code Commentary

### Logic

The registered preview and apply cases were deleted with the closeout route-review gate, and
the sibling module checks the gate’s removal on an atomic child and organizational leaf in
`test_closeout_never_gates_on_a_route_review_record_at_either_altitude`. What remains is the
payload shaping for an existing refusal: the case constructs a certification admission error carrying a `route-review-required` finding and proves the structured
response keeps the observed status and detail, promotes the concrete status, and names
`record_route_review` as the next operation without inventing `nextTool`. This fixture does not
publish a review, commit code, or certify closeout.

### Conventions

The remaining test supplies a finding to the application refusal-payload helper. The registered stdio calls preview closeout for an atomic child and an organizational leaf and separately dry-run ff-only integration for the atomic child. The fixture prepares code and memory and calls the production closeout application and integration handlers directly. The test checks the child code commit on the protected master code branch and verifies that both the child and master task documents still omit route review.

### Invariants And Boundaries

- The pure fixture asserts the exact status and detail, `record_route_review` as the next action and operation, and absence of `nextTool`.
- The fixture constructs no task document, contract, Git state or MCP transport.

## Evidence

### Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture.

No external domain evidence applies.

### Repo-Internal References




- The registered stdio calls preview closeout for an atomic child and an organizational leaf and separately dry-run ff-only integration for the atomic child. The fixture prepares code and memory and calls the production closeout application and integration handlers directly. The test checks the child code commit on the protected master code branch and verifies that both the child and master task documents still omit route review. [1]



- Certification projection preserves the route finding while promoting status. [2]
- Registered apply transport case was deleted: the module docstring records that the gate was removed, so only the certification-admission refusal payload shaping remains as this module's route-review evidence. [3]

### Cross-Repo References

The fixture is local to the pure application response adapter.
