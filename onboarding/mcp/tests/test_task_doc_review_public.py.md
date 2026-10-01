# mcp/tests/test_task_doc_review_public.py

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

## Evidence

### Docs References

No relevant external documentation was configured.

No external documentation source was configured for this test module.

### Repo-Internal References

- Isolated public target, creation helper, and operation caller. [1]
- Absent-state projection, begin replay, sealed baseline, shrink-only successors, and final pass. [2]
- Recording without a prior begin starts the baseline, and replacement can reset the projected state. [3]
- New successor finding refusal after the baseline is sealed. [4]
- Public cap, exhaustion-only direct permission, cumulative rounds four/five, and pending replay. [5]
- The master document the fixture now writes first, without which the leaf the review API is exercised on could not be authored at all. [6]

### Cross-Repo References

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
