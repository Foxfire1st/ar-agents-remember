# dashboard/src/data/submitMachine.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitMachine.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Defines the FEUI-L5 reliable-submit state machine and the one evidence fold used by every frontend
ingress. It turns immediate receipts, status polls, reconciliation, withdrawal results, and
availability loss into a monotonic per-request lifecycle without interpreting silence as success or
re-sending an ambiguous prompt.

## Code Commentary

### Logic

`SubmitReceipt` normalizes `immediate | queued | rejected | unknown | unsupported`; reconciliation
normalizes `accepted | rejected | unresolved | unsupported`. `SubmitPhase` preserves the operator-
visible lifecycle from `sending` through accepted/queued/delivering/withdrawn and the explicit
rejected, unsupported, ambiguous, reconciling, endgame, released, generation-lost, not-found, and
route-error outcomes. `foldSubmitEvidence` orders evidence classes as queued, availability loss,
dispatching, unknown, then definitive. A dispatching observation joined with authority loss becomes
unknown; definitive evidence always wins; observations within a class use their captured authority
version. Retry scheduling uses real wall-clock elapsed time, a 120-second window, and 1/2/5-second
backoff while preserving the immutable request id.

### Invariants And Boundaries

- One request id denotes one immutable text/source submission; retries and reconciliation never mint
  a replacement id or send the prompt again.
- `not-found` and `generation-lost` are availability evidence, not proof that the prompt was not
  delivered. They therefore cannot restore a draft or dominate later definitive evidence.
- Release means stop waiting and retain truthful ambiguity; it is not cancellation or retry.
- All response and polling paths must use this fold so arrival order cannot regress settled truth.

### Todos

None for FEUI-L5. Any new lifecycle ingress must extend the central evidence algebra rather than add
component-local precedence.

### 2026-07-24 Curator Delta

A bare queued receipt is acceptance evidence, not proof that a request remains pre-dispatch and
withdrawable. Only the lifecycle authority's own queued word earns that claim; dispatching and unknown
states start one bounded terminal-word watch shared with reconciliation.

## Docs References

No Domain Documentation source is configured for this repository; the implemented state algebra and
its tests are the authority for this internal protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle client feeds status, withdrawal, and response observations through this fold. | "possible-send-join" | dashboard/src/data/submissionLifecycleClient.ts:526-526 |
| The transport driver preserves the same request id through submit and reconciliation. | `executeReliableSubmit`, `continueReliableReconcile` | dashboard/src/data/submitClient.ts:411-491; dashboard/src/data/submitClient.ts:493-499 |
| The unit suite locks the partial order, availability-loss join, monotonicity, and deadlines. | "joins stale dispatching with newer authority loss as possible-send unknown", "finds only truly resolving submissions as active", "backs off 1s → 2s → 5s and stops before crossing the ~2 minute window" | dashboard/src/data/submitMachine.test.ts:102-120; dashboard/src/data/submitMachine.test.ts:136-151; dashboard/src/data/submitMachine.test.ts:192-211 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This state machine is repository-local. | — | — |

## Update History

- 2026-08-02T20:48:04+02:00 — 260731-EFA-L6 curator W2-B10: repaired 6 citation findings (3 reference rows); scoped recheck clean.

- 2026-07-24T13:17:50Z — Corrected queued-receipt semantics and documented the bounded lifecycle
  watch. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5 after canonical review PASS; documented the
  central evidence fold, real-time retry window, immutable request correlation, and the boundary
  between availability loss and delivery truth. Verification metadata remains pinned to the leaf
  base until closeout stamps the code commit.
