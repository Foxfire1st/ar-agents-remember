# mcp/tests/test_atomic_master_review_public.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_master_review_public.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T23:05:00+00:00 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2`|
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No relevant external documentation was configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this test module. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registered stdio client and the readable/structured wire-payload agreement assertion. | `_call_registered`; `_call`; `_assert_wire_payload` | mcp/tests/test_atomic_master_review_public.py:49-90 |
| Review-free fixture setup: the leaf review record is cleared. | `_remove_leaf_review` | mcp/tests/test_atomic_master_review_public.py:93-97 |
| The real closeout journal for the atomic child is written and finalized for the landing proof. | `_prepare_atomic_leaf_landing` | mcp/tests/test_atomic_master_review_public.py:130-167 |
| Production leaf landing runs under the started integration operation and moves the protected branch. | `_integrate_exact_leaf` | mcp/tests/test_atomic_master_review_public.py:100-127 |
| The route-review gate is absent at both altitudes while the exact landing still completes. | `test_closeout_never_gates_on_a_route_review_record_at_either_altitude` | mcp/tests/test_atomic_master_review_public.py:170-258 |

## Cross-Repo References

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

## Update History
- 2026-09-11T23:05:00+00:00: Curator content reconciliation: the cited 1,129-line composition is gone because its named test set was deleted deliberately — `b06b3a27` removed the master route-review gate and its tests, `6982c6a7` cut the door-operation-journal plane, and `2ec5d244` deleted what the remaining failures exposed as dead (all provable with `git log -S '<symbol>'`). The module is now the 258-line closeout route-review gate-removal proof, so the R26/V3/V6/CQ06/CQ07/R27/L41 review-state and ledger-identity claims were replaced by the helpers and the single test that actually exist, the superseded byte-identity bindings were compressed into one source-binding note, and the removal provenance was recorded as durable negative knowledge. The retained route-boundary contract is unchanged: the review gate stays absent at both altitudes.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_call`; `_assert_wire_payload` repointed to mcp/tests/test_atomic_master_review_public.py:72-77; mcp/tests/test_atomic_master_review_public.py:80-90. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `00ebadf8ddd33be0ecba0fefb64d6d5a415bc64a8ecde50a5361e3682d7fab9f`, `44173` bytes, `1131` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T23:09:11+02:00 — CCR-R27/R28 bounded memory citation correction: repaired current report-listed table-safe anchors, source ranges, and implementation-only provenance against the paired frozen source; verification metadata and historical bindings remain unchanged.
- 2026-09-08T22:56:00+02:00 — CCR-R27/R28 bounded memory curation: corrected 2 report-listed citation anchor/range entries against the paired frozen source; existing verification metadata and historical bindings remain unchanged.
- 2026-09-08T22:32:00+02:00 — CCR-R28 L41 memory curation: preserved the historical V3/V6/R27
  bindings and recorded the exact frozen L41 public default-state fields without changing the
  route-boundary, ledger, or integration claims; no test, review, or acceptance claim was added.
- 2026-09-08T22:13:45+02:00 — CCR-R27 L40 API memory preparation: rebound the public atomic-master card to the 1,129-line source, recorded the review-state caller assertions, and retained V6 as historical composition evidence; no code commit, review, or acceptance claim.
- 2026-09-08T20:37:13+02:00 — CCR-CQ07 V6 successor curation: rebased the public-test fixture
  citations to the 1,047-line source, recorded the 10,000-character identity bound and truncation
  assertion, and replaced the active V5 binding with the exact V6 file bytes; no test, source,
  shared-overview, or landed-commit claim was added.
- 2026-09-08T20:26:49+02:00 — CCR-CQ07 V5 successor curation: rebased public-test citations to the
  composed 1,032-line source, recorded the full/abbreviated/missing/non-commit/ambiguous ledger
  identity fixture and its protected-state assertions, and bound the card to the exact V5 file
  bytes; no test pass, source edit, shared overview edit, or verification pin was claimed.
- 2026-09-08T20:12:08+02:00 — CCR-L24 v4 citation repair: re-read the direct-door and CQ06 claims against the current 871-line successor, expanded every pooled source segment to a full path, and anchored formatter/narrowing evidence to unique literals; CQ07 successor preparation remains pending and no verification pin or code/shared overview was changed.
- 2026-09-08T19:14:44+02:00 — CCR-CQ06 successor-preparation curation: rebased public-test anchors to the 871-line corrected file, recorded the two explicit optional-door assertions and formatter-only shifts, replaced the active v3 whole-tree binding with the exact successor file SHA, and preserved v3 as historical evidence; no code or shared overview was edited.
- 2026-09-08T19:06:02+02:00 — CCR-CQ03/R25 source-ground memory repair: expanded the card to the five current public operation proofs, corrected all source ranges to frozen v3, and updated the candidate binding; no code or shared overview was edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: re-read the renamed admission-evidence test, corrected its source range, and updated the active candidate tree to frozen v2; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card for public
  route-boundary checks from the frozen source. Commit-owned verification metadata remains blank.
