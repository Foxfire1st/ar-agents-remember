# dashboard/src/data/submissionLifecycleClient.ts

## Governing Overview

[data overview](overview.md)

## 260731-EFA-L8 Change

The withdrawal helpers moved to `data/submissionWithdrawal.ts` (authoritative
queued-withdrawal target resolution, result application, and recovery/dismiss), and
the `wireFixtureGuard` cast was replaced with a validated narrow so the client
rejects unvalidated submission lifecycle states. Behavior is otherwise unchanged.

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

### 2026-07-24 Curator Delta

Lifecycle reads are abort-bounded and continue after a dispatching or unknown projection until the
authority supplies a terminal word. The watch shares the reconciliation budget; expiry enters the
existing honest endgame rather than polling or displaying delivering forever.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- Withdrawal, central settlement, poll cadence, response-loss convergence, and recovery. [1]
- The pure evidence fold defines admissible lifecycle progression. [2]
- The cockpit store owns pending-withdrawal and recovery-slot projections. [3]
- The composer binds Alt+Up and renders the queue/recovery affordances. [4]
- Tests exercise withdrawal races, lost responses, CAS recovery, exact dismissal, and poll order. [5]

### Cross-Repo References

No meaningful cross-repo references found.

The lifecycle client is internal to the dashboard/daemon protocol.

## FEUI-L8 Reviewed Candidate Delta

All cached authority reads, pollers, and authoritative withdrawals now carry a dev-scenario generation. Reset clears timers/maps and every post-await mutation validates ownership, including convergence retry and in-flight-map cleanup, so old same-id work cannot corrupt a successor.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
