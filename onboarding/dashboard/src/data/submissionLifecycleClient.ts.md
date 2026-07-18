# dashboard/src/data/submissionLifecycleClient.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submissionLifecycleClient.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Projects the server's raw-free submission authority into the cockpit and implements the authoritative
Alt+Up withdrawal/recovery contract. It is the single browser seam for status polling, lifecycle
settlement, exact withdrawal, and revision-safe draft recovery.

## Code Commentary

### Logic

The client strictly parses authority/status/withdraw responses, caches the bridge epoch per session,
and polls visible sessions every 750ms, hidden sessions every 2.5s, with 1/2/5-second failure
backoff. Status requests are batched to at most 64 ids. Every poll and response enters the central
`submitMachine` fold, preserving the captured observation version so reordered responses remain
monotonic. Alt+Up records an exact pending withdrawal transaction (`requestId`, original text,
epoch, and draft revision), survives concurrent polls and response loss, and converges through
status. A successful queued withdrawal restores only when the current draft revision still matches;
otherwise it creates one explicit recovery slot with replace/keep-current actions. Dismissal is
exact-request plus exact-revision local state and never causes network I/O.

### Invariants And Boundaries

- Only the newest authoritative queued prompt is eligible for pop-back; dispatching/delivered,
  generation-lost, and not-found states never infer safe restoration.
- Withdrawal is server-linearized. The browser never removes a queue row first and hopes the server
  agrees.
- Response loss cannot create a second withdrawal or a resend; polling the same id converges truth.
- Auto-restore uses revision CAS. User edits win, with displaced text retained in exactly one
  recovery slot until explicit replace, keep-current, or exact dismissal.
- Raw vendor evidence and prompt text from unrelated submissions are never requested or exposed.

### Todos

None for FEUI-L5. New lifecycle sources must use the same settlement/fold seam.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Withdrawal, central settlement, poll cadence, response-loss convergence, and recovery. | L403-L1018 | [submissionLifecycleClient.ts](submissionLifecycleClient.ts) |
| The pure evidence fold defines admissible lifecycle progression. | — | [submitMachine.ts](submitMachine.ts) |
| The cockpit store owns pending-withdrawal and recovery-slot projections. | — | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The composer binds Alt+Up and renders the queue/recovery affordances. | — | [../panels/SessionComposer.tsx](../panels/SessionComposer.tsx) |
| Tests exercise withdrawal races, lost responses, CAS recovery, exact dismissal, and poll order. | — | [submissionLifecycleClient.test.ts](submissionLifecycleClient.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The lifecycle client is internal to the dashboard/daemon protocol. | — | — |

## FEUI-L8 Reviewed Candidate Delta

All cached authority reads, pollers, and authoritative withdrawals now carry a dev-scenario generation. Reset clears timers/maps and every post-await mutation validates ownership, including convergence retry and in-flight-map cleanup, so old same-id work cannot corrupt a successor.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; documented authoritative status polling,
  the central fold, exact epoch/request withdrawal, response-loss convergence, revision-CAS draft
  restoration, and the explicit recovery-slot decisions required by pop-back. Verification metadata
  remains pinned to the leaf base until closeout.
