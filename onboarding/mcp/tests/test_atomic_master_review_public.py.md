# mcp/tests/test_atomic_master_review_public.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

The registered stdio calls preview closeout for an atomic child and an organizational leaf and separately dry-run ff-only integration for the atomic child. The fixture prepares code and memory and calls the production closeout application and integration handlers directly. The test checks the child code commit on the protected master code branch and verifies that both the child and master task documents still omit route review.

## Code Commentary

### Logic

`_call_registered` drives the real MCP stdio server with the fixture settings file and returns the
raw `CallToolResult`; `_call` runs it synchronously. `_assert_wire_payload` requires the readable
text block and `structuredContent` to agree, so a route that renders one shape and returns another
cannot pass.

`_remove_leaf_review` clears the leaf's `routeReview` record. `_prepare_atomic_leaf_landing`
publishes the activation, commits the fixture code and memory, declares the fixture and calls the production
`worktree_closeout_apply_tool` application handler, and reloads the completed contract.
`_integrate_exact_leaf` calls `integrate_result` directly and checks the integrated result
and candidate code commit on the protected master source branch.

The single test, `test_closeout_never_gates_on_a_route_review_record_at_either_altitude`, first
previews closeout for an atomic child with its review removed. It checks that the response omits `route_review` and that the child task document, contract bytes and code HEAD are unchanged. After direct closeout and a check of both task documents, the registered integration dry run reports `would-integrate` while the protected code branch still differs from the child commit. The direct integration then moves that branch to the child commit and both documents still omit route review. The organizational leaf also gets a successful review-free preview. The removal it pins is deliberate: quality is
checked focused within the leaves and the adversarial review that precedes integration is a process
step owned by the reviewer role, not a code gate at closeout.

### Conventions

Public route tests compare the readable and structured response payloads, task-document state,
contract bytes, and protected ref movement inside disposable fixtures. They observe the review
boundary; they do not authorize a verdict or substitute for the combined master integration run.

### Invariants And Boundaries

- Both registered closeout previews succeed without a leaf route-review record and omit route-review output.
- The route-review *record* survives as task shape through `task_doc.record_route_review`; only the
  closeout gate is gone. Pinning the removal here keeps the gate from returning unnoticed.
- The atomic child’s preview leaves its task document, contract bytes and code HEAD unchanged.
- The real atomic leaf-to-master integration moves the protected master source branch while
  both task documents remain review-free.
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


- The atomic fixture invokes the production closeout application handler and checks the resulting completed contract and candidate commit. [3]




- The direct atomic integration operation moves the protected master source branch to the candidate code commit. [4]



- The registered stdio calls preview closeout for an atomic child and an organizational leaf and separately dry-run ff-only integration for the atomic child. The fixture prepares code and memory and calls the production closeout application and integration handlers directly. The test checks the child code commit on the protected master code branch and verifies that both the child and master task documents still omit route review. [5]



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
