# dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate |  2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Keeps authoritative landed-cleanup outcomes and unavailable-result recovery visible at the Chats
root, independent of the collapsible rail or the command surface that launched cleanup.

## Code Commentary

An unavailable result renders the exact intended `{label,id}` snapshot, retry against the same
targets, and explicit dismissal. A returned result renders closed/skipped truth and reasons. Retrying
cannot be double-triggered and successful authority replaces the failure notice.

## Invariants And Boundaries

No response is not success and not failure: it is unknown authority. Never drop targets, fabricate a
closed count, or hide recovery inside a pane that can collapse.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Cross-Repo References

The notice consumes the repository-local lifecycle authority client/store; no cross-repository implementation governs it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Notice store and detailed cleanup. | `lifecycleNoticeStore`; `endLandedDetailed` | dashboard/src/data/sessionLifecycle.ts:68-121; dashboard/src/data/sessionLifecycle.ts:230-251 |
| Root host. | `SessionsView` | dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx:23-23 |

## Update History

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 2 citation claims
  (Repo-Internal reference rows); scoped result 0 findings.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 landed-cleanup authority honesty; verification
  metadata remains blank until commit.
