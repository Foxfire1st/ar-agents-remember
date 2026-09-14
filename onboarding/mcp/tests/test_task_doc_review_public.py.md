# mcp/tests/test_task_doc_review_public.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_review_public.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T07:05+02:00 |
| lastVerifiedCommitHash | `4214d7a103dcc120481c6fe0059b322396ec9be6`|
| lastVerifiedCommitDate | 2026-09-14T07:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Focused public task-document API coverage for CCR-R27's bounded review-state transitions and
CCR-R28's ordinary cap/direct recorded-permission behavior. The module exercises the registered
application seam in an isolated task fixture and records the machine-readable `reviewState`
contract; it does not perform an independent review or certify a candidate.

## Code Commentary

### Logic

`_create` authors a minimal sub-task through `task_doc_tool`, and `_call` invokes the same public
target for `begin_review`, `record_review`, or replacement operations. Since 260913-LCA-L5 `_create`
first writes the task root's **master document** through `write_task_doc`, because the review API is
exercised on a leaf and the authoring plane now refuses a leaf document whose series has no master
document at all — nothing would ever bind the leaf's derived `seriesContractPath`/`enclosures[]` (see
the `application/task_docs/task_doc_tools.py` card). The master write is the fixture prerequisite for the
allowed planning flow, not a weakening of the refusal; no case in this module exercises the refusal.
The main sequence proves
that an absent persisted review state is projected as round zero, `begin_review` starts round one,
and a repeated begin resumes the pending round without incrementing it. The first `record_review`
seals findings A and B; later rounds can only shrink the remaining set through B and then an empty
passing set.

The boundary cases prove that recording without a prior begin starts the baseline and still
needs a verdict, replacement re-projects `reviewState` to round zero, and a successor cannot
introduce a new finding after the baseline has been sealed. The cap case proves that the public
route refuses the fourth ordinary round with
the current count and limit, accepts a nonblank direct `developerApproval` plus positive
`additionalRounds` only at exhaustion, carries the permission and cumulative allowance through
rounds four and five, and leaves a pending replay unchanged. The source preserves the public error
dialect and does not authenticate the purported developer.

### Conventions

Each test creates its own temporary runtime configuration and task document. Assertions inspect the
returned dictionary and typed `TaskDocError` messages from the real application function. Focused
source assertions are preparation evidence; they do not replace the combined master integration
run or issue an acceptance verdict.

### Invariants And Boundaries

- Missing persisted state is an explicit zero projection with no pending round or findings.
- Recording without a prior begin starts the baseline; a repeated begin is idempotent while pending.
- The first finding list is sealed; successors may shrink remaining IDs but cannot add, duplicate,
  reintroduce, or leave unresolved findings while passing.
- The ordinary public cap is three rounds; an exhaustion-only direct permission carries a positive
  cumulative allowance without resetting the round or sealed findings.
- `create` authors no review state; `replace` can reset the projected state to round zero, and
  the explicit review operations own the recorded transition.
- The test owns only disposable task fixtures and makes no source, task, or control-plane edits.

### Todos

The combined public API and master integration exercise remains parent-owned.

## Docs References

No relevant external documentation was configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this test module. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Isolated public target, creation helper, and operation caller. | `_target`; `_create`; `_call` | mcp/tests/test_task_doc_review_public.py:18-19; mcp/tests/test_task_doc_review_public.py:22-55; mcp/tests/test_task_doc_review_public.py:58-70 |
| Absent-state projection, begin replay, sealed baseline, shrink-only successors, and final pass. | `test_public_review_operations_seal_then_shrink_findings` | mcp/tests/test_task_doc_review_public.py:73-120 |
| Recording without a prior begin starts the baseline, and replacement can reset the projected state. | `test_public_review_api_records_without_begin_and_replace_can_set_state` | mcp/tests/test_task_doc_review_public.py:123-150 |
| New successor finding refusal after the baseline is sealed. | `test_successor_cannot_add_a_new_finding` | mcp/tests/test_task_doc_review_public.py:153-172 |
| Public cap, exhaustion-only direct permission, cumulative rounds four/five, and pending replay. | `test_public_review_api_enforces_cap_and_carries_explicit_extra_rounds` | mcp/tests/test_task_doc_review_public.py:175-236 |
| The master document the fixture now writes first, without which the leaf the review API is exercised on could not be authored at all. | `_create` | mcp/tests/test_task_doc_review_public.py:22-55 |

## Cross-Repo References

No meaningful cross-repository implementation reference is required for this preparation test card.

## Current R27 API Candidate Binding

The source checkout is based at code commit `8133b6a9de2f787cb6c4527621a70123357aff31`; the frozen
R27 API composition of this file is 4,532 bytes and 150 lines with SHA-256
`3778b3fcfbe9aa9adae77949b5a802706023dbde7c1115b982b05194c5f3b1d2`. The source includes the
worker's public review-state checks and helper typing correction. No focused test pass, landed
commit identity, independent review, or acceptance is asserted here; verification metadata remains
blank until governed closeout stamps a genuine code commit.

## Current R28 L41 Candidate Binding

The frozen L41 source tree is `2d2e1ae39b2046b5663aca2cf82f27779dafe0c2`. This public-test source is
6,775 bytes and 214 lines with SHA-256
`ec40e92a4b8b66cea3b73d71c00e641e7ffe45d6cef25c55beb0375567ee5308`. It extends the R27 public
operation proof with exhaustion-only direct permission and cumulative round-four/round-five
behavior. No focused pass, landed commit identity, independent review, or acceptance is asserted;
verification metadata remains blank until governed closeout stamps a genuine code commit.

## Update History
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): recorded the fixture prerequisite the authoring refusal forced — `_create` now writes the
  task root's master document first, because this module exercises the review API on a leaf and a leaf
  whose series has no master document at all is now refused (nothing would ever bind its derived
  `seriesContractPath`/`enclosures[]`). Re-derived all four cited ranges and `_target`/`_call` against the
  current source with AST (`_target` 17-18 → 18-19, `_create` 21-37 → 22-55, `_call` 40-52 → 58-70, the
  four tests 55-102/105-132/135-154/157-218 → 73-120/123-150/153-172/175-236). **The `Current R27 API
  Candidate Binding` and `Current R28 L41 Candidate Binding` sections above are left exactly as written:
  they are frozen bindings to earlier candidate bytes, not claims about the current file, and the file has
  since grown past them.** Verification metadata remains closeout-owned; no execution or acceptance claim.
- 2026-09-11T23:05:00+00:00: The row cited the deleted `test_public_review_api_requires_begin_and_rejects_generic_state_reset`, which asserted the opposite of the current contract. `test_public_review_api_records_without_begin_and_replace_can_set_state` now pins that recording without a prior begin starts the baseline, and that replacement resets the projected state to round zero; the Logic and Invariants prose were corrected to match.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `ec40e92a4b8b66cea3b73d71c00e641e7ffe45d6cef25c55beb0375567ee5308`, `6775` bytes, `214` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.


- 2026-09-08T22:32:00+02:00 — CCR-R28 L41 memory curation: preserved the R27 binding and added the
  exact frozen L41 public cap/permission proof, including round-four/round-five state and pending
  replay semantics; no test, review, or acceptance claim was added.

- 2026-09-08T22:13:45+02:00 — CCR-R27 L40 API memory preparation: created the one-to-one onboarding card for the newly frozen public task-document review API test and bound all claims to its exact source bytes; no code commit, review, or acceptance claim.
