# mcp/tests/test_task_doc_review_public.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_review_public.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:10+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
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
target for `begin_review`, `record_review`, or replacement operations. The main sequence proves
that an absent persisted review state is projected as round zero, `begin_review` starts round one,
and a repeated begin resumes the pending round without incrementing it. The first `record_review`
seals findings A and B; later rounds can only shrink the remaining set through B and then an empty
passing set.

The refusal cases prove that recording without a pending begin is rejected, replacement cannot
author or rewrite `reviewState`, and a successor cannot introduce a new finding after the baseline
has been sealed. The cap case proves that the public route refuses the fourth ordinary round with
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
- A review round must begin before recording; a repeated begin is idempotent while pending.
- The first finding list is sealed; successors may shrink remaining IDs but cannot add, duplicate,
  reintroduce, or leave unresolved findings while passing.
- The ordinary public cap is three rounds; an exhaustion-only direct permission carries a positive
  cumulative allowance without resetting the round or sealed findings.
- `create` and `replace` cannot author or directly modify the review state; explicit review
  operations own that transition.
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
| Isolated public target, creation helper, and operation caller. | `_target`; `_create`; `_call` | mcp/tests/test_task_doc_review_public.py:17-52 |
| Absent-state projection, begin replay, sealed baseline, shrink-only successors, and final pass. | `test_public_review_operations_seal_then_shrink_findings` | mcp/tests/test_task_doc_review_public.py:55-103 |
| Begin-before-record requirement and replacement refusal. | `test_public_review_api_requires_begin_and_rejects_generic_state_reset` | mcp/tests/test_task_doc_review_public.py:105-128 |
| New successor finding refusal after the baseline is sealed. | `test_successor_cannot_add_a_new_finding` | mcp/tests/test_task_doc_review_public.py:131-150 |
| Public cap, exhaustion-only direct permission, cumulative rounds four/five, and pending replay. | `test_public_review_api_enforces_cap_and_carries_explicit_extra_rounds` | mcp/tests/test_task_doc_review_public.py:153-214 |

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

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `ec40e92a4b8b66cea3b73d71c00e641e7ffe45d6cef25c55beb0375567ee5308`, `6775` bytes, `214` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.


- 2026-09-08T22:32:00+02:00 — CCR-R28 L41 memory curation: preserved the R27 binding and added the
  exact frozen L41 public cap/permission proof, including round-four/round-five state and pending
  replay semantics; no test, review, or acceptance claim was added.

- 2026-09-08T22:13:45+02:00 — CCR-R27 L40 API memory preparation: created the one-to-one onboarding card for the newly frozen public task-document review API test and bound all claims to its exact source bytes; no code commit, review, or acceptance claim.
