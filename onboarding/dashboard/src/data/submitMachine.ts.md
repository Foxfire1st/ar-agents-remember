# dashboard/src/data/submitMachine.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitMachine.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Docs References

No Domain Documentation source is configured for this repository; the implemented state algebra and
its tests are the authority for this internal protocol.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The lifecycle client feeds status, withdrawal, and response observations through this fold. | — | [submissionLifecycleClient.ts](submissionLifecycleClient.ts) |
| The transport driver preserves the same request id through submit and reconciliation. | — | [submitClient.ts](submitClient.ts) |
| The unit suite locks the partial order, availability-loss join, monotonicity, and deadlines. | — | [submitMachine.test.ts](submitMachine.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This state machine is repository-local. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5 after canonical review PASS; documented the
  central evidence fold, real-time retry window, immutable request correlation, and the boundary
  between availability loss and delivery truth. Verification metadata remains pinned to the leaf
  base until closeout stamps the code commit.
