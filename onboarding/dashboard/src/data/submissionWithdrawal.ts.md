# dashboard/src/data/submissionWithdrawal.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/data/submissionWithdrawal.ts`                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The withdrawal entry points. | `withdrawLastQueuedSubmission`; `applyWithdrawalResult`; `restoreWithdrawnRecovery` | dashboard/src/data/submissionWithdrawal.ts:138-188; dashboard/src/data/submissionWithdrawal.ts:352-377; dashboard/src/data/submissionWithdrawal.ts:405-417 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  submission-withdrawal module extracted from `submissionLifecycleClient.ts`.
  Verification pinned to the leaf base until closeout stamps the code commit.
