# dashboard/src/data/submitClient.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitClient.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

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

### 2026-07-24 Curator Delta

The submission gate lets an actively streaming projection outrank a lagging disconnected sweep state.
Composer drafts clear once authority has committed the request through queued, delivering, or accepted;
withdrawability remains reserved for a server-confirmed queued lifecycle state.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Transport parsing, deadline, reconciliation, submit driver, and store integration. | `createFetchSubmitTransport`; `executeReliableSubmit`; `continueReliableReconcile`; `submitSessionText` | dashboard/src/data/submitClient.ts:197-254; dashboard/src/data/submitClient.ts:411-491; dashboard/src/data/submitClient.ts:493-499; dashboard/src/data/submitClient.ts:627-681 |
| The evidence state machine supplies receipt/reconcile transitions and retry scheduling. | `reduceReceipt`; `reduceReconciliation`; `reconcileDelay` | dashboard/src/data/submitMachine.ts:215-263; dashboard/src/data/submitMachine.ts:330-358; dashboard/src/data/submitMachine.ts:360-362 |
| The browser authority client owns polling, withdrawal, and recovery after initial delivery. | `ensureSubmissionLifecyclePolling`; `restoreWithdrawnRecovery`; `withdrawLastQueuedSubmission` | dashboard/src/data/submissionLifecycleClient.ts:787-799; dashboard/src/data/submissionLifecycleClient.ts:1043-1068; dashboard/src/data/submissionLifecycleClient.ts:1096-1108 |
| Tests cover safe certificates, ambiguous loss, no-resend reconciliation, readiness, and provenance. | "retries only an explicitly proven pre-dispatch loss, using the same id and immutable text"; "treats a browser rejection as ambiguous and reconciles without resending"; "never resends an unclassified post-dispatch loss; it reconciles the same id at 1s → 2s"; "allows composing before ready but submits only a ready controlled session"; "records a background queue receipt without clearing or joining composer pop-back state" | dashboard/src/data/submitClient.test.ts:103-128; dashboard/src/data/submitClient.test.ts:210-227; dashboard/src/data/submitClient.test.ts:297-325; dashboard/src/data/submitClient.test.ts:432-446; dashboard/src/data/submitClient.test.ts:638-664 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The transport is internal to agents-remember's dashboard/API boundary. | — | — |

## FEUI-L8 Reviewed Candidate Delta

`submissionReceiptAnnouncement` centralizes accepted/queued/rejected/unsupported copy. Settlement announces politely only when the exact submitted session is currently focused; evidence storage remains authoritative for every seat.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 4 citation rows with exact anchors (transport/machine/lifecycle-client definitions, quoted test names) and ledger-verified source ranges; scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-24T13:17:50Z — Documented live-turn gate precedence, draft clearing, and queued-receipt
  honesty. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5 after review round 6 PASS; documented
  exact-epoch submission, the sole safe-retry certificate, ambiguous first-byte loss, same-id
  reconciliation, source provenance, revision-CAS composer clearing, and create-ready gating.
  Verification metadata remains pinned to the leaf base until closeout.
