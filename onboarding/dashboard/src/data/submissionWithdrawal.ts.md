# dashboard/src/data/submissionWithdrawal.ts

## Governing Overview

[dashboard/src/data overview](overview.md)

## Purpose

The authoritative submission-withdrawal helpers extracted from
`submissionLifecycleClient.ts` by the 260731-EFA-L8 split. Owns withdrawal target
resolution, result application, convergence catches, and the recovery/dismiss
handlers for the queued-withdrawal surface.

## Code Commentary

### Logic

`withdrawLastQueuedSubmission` resolves the queued target from the per-session
cockpit state; `applyWithdrawalResult` folds the result back; `restoreWithdrawnRecovery`
and `dismissWithdrawnRecovery` drive the recovery UI; `convergenceCatch` keeps the
withdrawal state honest across races.

### Conventions

Withdrawal is authoritative: pop-back never falls back to shared paste.

### Invariants And Boundaries

The module must not submit anything itself; it only withdraws and reconciles.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The withdrawal entry points. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
