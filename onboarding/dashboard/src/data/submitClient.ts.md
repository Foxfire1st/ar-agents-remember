# dashboard/src/data/submitClient.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitClient.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Implements the browser transport and driver for reliable, epoch-bound whole-message submission.
It is the only frontend layer that decides whether a failed request is certified safe to retry,
ambiguous and therefore reconcile-only, or a definitive receipt.

## Code Commentary

### Logic

Every submit carries the exact `{requestId, text, expectedBridgeEpoch}` tuple. Only the server's
exact 503 certificate `{pre-dispatch-failed, retrySafe:true, stage:control-ipc}` permits a same-id,
same-text transport retry; browser/network loss is ambiguous because bytes may have crossed the
boundary. The driver races requests against a real wall-clock deadline, preserves first-byte
evidence, and reconciles the same id without native resend. Store integration records source
provenance (`composer`, `leaf-context`, `highlight`, or `background`), applies revision-CAS draft
clearing only for accepted composer sends, queues/restores only composer drafts, and leaves
non-composer text ownership unchanged. `waitForSubmissionReady` supports create-then-control-ready
flows without treating draft editability as transport readiness.

### Invariants And Boundaries

- A request id never changes text, source, epoch, or draft provenance.
- Timeout or connection loss after a possible write is ambiguous; it never becomes blind resend.
- Only the exact server-issued pre-dispatch certificate is retry-safe.
- Drafts remain editable before control readiness, but send is gated until the exact session bridge
  is ready.
- The lifecycle client's central fold remains evidence authority; this module owns transport and
  store-driving only.

### Todos

None for FEUI-L5.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Transport parsing, deadline, reconciliation, submit driver, and store integration. | L35-L734 | [submitClient.ts](submitClient.ts) |
| The evidence state machine supplies receipt/reconcile transitions and retry scheduling. | — | [submitMachine.ts](submitMachine.ts) |
| The browser authority client owns polling, withdrawal, and recovery after initial delivery. | — | [submissionLifecycleClient.ts](submissionLifecycleClient.ts) |
| Tests cover safe certificates, ambiguous loss, no-resend reconciliation, readiness, and provenance. | — | [submitClient.test.ts](submitClient.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The transport is internal to agents-remember's dashboard/API boundary. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5 after review round 6 PASS; documented
  exact-epoch submission, the sole safe-retry certificate, ambiguous first-byte loss, same-id
  reconciliation, source provenance, revision-CAS composer clearing, and create-ready gating.
  Verification metadata remains pinned to the leaf base until closeout.
