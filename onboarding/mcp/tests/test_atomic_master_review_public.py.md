# mcp/tests/test_atomic_master_review_public.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins the removal of the closeout route-review gate at both altitudes through the registered public
tools. It proves that closeout consults no route-review record -- an atomic child is not deferred
into one and an organizational leaf is not refused for the lack of one -- and that the real atomic
leaf-to-master landing still completes while both task documents remain review-free.

## Code Commentary

### Logic

`_call_registered` drives the real MCP stdio server with the fixture settings file and returns the
raw `CallToolResult`; `_call` runs it synchronously. `_assert_wire_payload` requires the readable
text block and `structuredContent` to agree, so a route that renders one shape and returns another
cannot pass.

`_remove_leaf_review` clears the leaf's `routeReview` record, which is how the test creates
review-free documents. `_prepare_atomic_leaf_landing` activates the atomic master, commits the child
candidate, declares the waiting door, starts the real closeout operation and journal, finalizes the
contract record, and returns the reloaded contract plus the exact candidate commit.
`_integrate_exact_leaf` starts the production integration operation and then runs
`integrate_result` with the running operation key and generation, asserting an `integrated` state and
that the master's protected source branch now holds the candidate commit.

The single test, `test_closeout_never_gates_on_a_route_review_record_at_either_altitude`, first
previews closeout for an atomic child with its review removed and asserts the payload carries no
`route_review` field and that neither the task document nor the contract changed; it then performs
the real leaf-to-master landing and re-asserts both documents stay review-free. It repeats the
review-free preview for an organizational leaf. The removal it pins is deliberate: quality is
checked focused within the leaves and the adversarial review that precedes integration is a process
step owned by the reviewer role, not a code gate at closeout.

### Conventions

Public route tests compare the readable and structured response payloads, task-document state,
contract bytes, and protected ref movement inside disposable fixtures. They observe the review
boundary; they do not authorize a verdict or substitute for the combined master integration run.

### Invariants And Boundaries

- Closeout consults no route-review record at either altitude: an atomic child is not deferred into
  one and an organizational leaf is not refused for the lack of one.
- The route-review *record* survives as task shape through `task_doc.record_route_review`; only the
  closeout gate is gone. Pinning the removal here keeps the gate from returning unnoticed.
- A review-free closeout preview mutates neither the task document nor the contract and moves no
  ref.
- The real atomic leaf-to-master landing still integrates: the lifecycle operation is started and
  `integrate_result` moves the master's protected source branch while both task documents remain
  review-free.
- The test owns no mutation outside its isolated fixtures.

### Todos

The final combined public integration exercise remains parent-owned.

## Evidence

### Docs References

No relevant external documentation was configured.

No external documentation source was configured for this test module.

### Repo-Internal References

- Registered stdio client and the readable/structured wire-payload agreement assertion. [1]
- Review-free fixture setup: the leaf review record is cleared. [2]
- The real closeout journal for the atomic child is written and finalized for the landing proof. [3]
- Production leaf landing runs under the started integration operation and moves the protected branch. [4]
- The route-review gate is absent at both altitudes while the exact landing still completes. [5]

### Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.

## Source Binding

The card was created for the CCR-R26 public route-boundary composition and later carried the V3, V6,
CQ06, CQ07, R27 and L41 candidate bindings, whose exact byte identities are superseded historical
composition evidence and are not re-asserted here. The 1,129-line composition is gone because its
whole named test set was removed deliberately, and each removal is provable: `b06b3a27` (2026-09-10,
"Remove the master route-review gate that integration never consulted") deleted
`test_atomic_master_public_integration_refuses_without_review_before_ref_move`,
`test_public_master_review_stamps_branch_candidate_and_allows_exact_protected_landing` and
`test_public_master_integration_refuses_after_admission_evidence_changes` under an explicit developer
ruling that quality is checked focused within the leaves; `6982c6a7` (2026-09-10, the
door-operation-journal cut) deleted `test_registered_direct_organizational_door_keeps_leaf_review_gate`;
and `2ec5d244` (2026-09-11) deleted what the remaining failures exposed as dead, including
`test_atomic_leaf_public_closeout_defers_review_and_organizational_leaf_keeps_gate`,
`_ambiguous_memory_commit_prefix`, `_external_atomic_ledger_door_case` and `_exercise_blocked_direct_review`.
`master_route_review_refusal` was deleted by the same `b06b3a27` ruling; its role now lives in
`mcp/src/agents_remember/worktrees/route_review.py` as `route_review_refusal_projection` and
`route_review_refusal_fields`. The current source reduces the module to the closeout-gate-removal
proof described above; no focused test pass, landed commit identity, independent review, or
acceptance is asserted, and commit-owned verification metadata remains closeout-owned.
