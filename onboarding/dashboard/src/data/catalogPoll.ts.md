# dashboard/src/data/catalogPoll.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T16:02+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

The shell-wide terminal-catalog authority boundary. It owns the single refcounted 2500 ms poll
driver, eager initial hydration, and cross-tab invalidation reconciler used by the canonical Chats
cockpit. Every read records poll health; remote termination is removed locally and excluded from the
confirming read so a stale echo cannot resurrect it. The persisted active id is restricted to live
action routing while cockpit focus may continue inspecting landed rows. Dev-bench generation guards
prevent retired scenario reads from mutating successor rows or poll health.

## Code Commentary

### Logic

- `CATALOG_REFRESH_INTERVAL_MS = 2500` cit:([`CATALOG_REFRESH_INTERVAL_MS`], dashboard/src/data/catalogPoll.ts:15-15) — the one poll cadence, exported for tests.
- `readLastActiveSessionId`/cit:([`readLastActiveSessionId`, `writeLastActiveSessionId`], dashboard/src/data/catalogPoll.ts:104-110; dashboard/src/data/catalogPoll.ts:112-119) — the
  `ar-dashboard:last-active-chat-session` localStorage preference, moved with the hydrate (a UI
  preference only; failures swallowed for private contexts).
- cit:([`hydrateTerminalSessionsFromCatalog`], dashboard/src/data/catalogPoll.ts:139-157) — ONE
  catalog fetch → session-store hydrate. Its extraction from the retired `Chats` component is
  historical provenance; current behavior also carries a generation-scoped dev authority so a
  superseded scenario cannot mutate successor rows or poll health. Every accepted read records a
  poll-health beat; an empty list applies only when `allowEmpty`; `excludeSessionIds` filters
  just-terminated ids so a stale snapshot cannot resurrect them; hydration keeps the last-active
  preference.
- cit:([`scheduleCatalogPoll`, `startCatalogPollDriver`], dashboard/src/data/catalogPoll.ts:163-173; dashboard/src/data/catalogPoll.ts:179-192) — the refcounted subscription: the FIRST subscriber arms
  one `window.setTimeout` for `CATALOG_REFRESH_INTERVAL_MS`; it does not hydrate eagerly. After that
  delayed tick's bounded hydration settles, the scheduler arms the next delay. The LAST release clears a pending timeout; each returned release is idempotent (a
  `released` latch), so React StrictMode double-mount (start/release/start) and double-release are
  safe. Consumers never see each other.
- cit:([`startCatalogReconciler`], dashboard/src/data/catalogPoll.ts:206-231) — the refcounted immediate eager hydrate plus cross-tab invalidation
  owner. Remote termination is removed before and excluded from its confirming read; create/leaf
  invalidations rehydrate with `allowEmpty`.

### Invariants And Boundaries

- The poll is AUTHORITATIVE for session rows; push (seatEvents) is a pre-apply layer only. Nothing
  here may be replaced by an event channel without a design ruling.
- One serialized timeout chain regardless of subscriber count; zero subscribers ⇒ no timer (no leak).
- Every catalog read — driver tick, eager/cross-tab reconciliation, post-bulk-end confirmation, or
  launch/failure refresh — records a beat through `hydrateTerminalSessionsFromCatalog`, the only
  sanctioned read path.
- `CockpitShell` is the sole production owner of `startCatalogPollDriver` and
  `startCatalogReconciler`. Current manual-hydrate callers are `sessionLifecycle.ts`,
  `session-cockpit/LaunchFlow.tsx`, and `session-cockpit/FailedLaunchBanner.tsx`; `SessionsView`
  consumes the shared store and starts no catalog timer.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The refcount driver, reconciler, hydrate helper, beat recording, and localStorage preference. | "export function startCatalogPollDriver(): () => void {"; "export function startCatalogReconciler(): () => void {"; "export async function hydrateTerminalSessionsFromCatalog("; "recordPollBeat: (ok) =>"; "export function writeLastActiveSessionId(" | dashboard/src/data/catalogPoll.ts:68-68; dashboard/src/data/catalogPoll.ts:112-119; dashboard/src/data/catalogPoll.ts:139-157; dashboard/src/data/catalogPoll.ts:179-192; dashboard/src/data/catalogPoll.ts:206-231; dashboard/src/data/sessionCockpitStore.ts:294-304 |
| The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). | `fetchTerminalSessionsOrNull` | dashboard/src/data/terminal.ts:414-433 |
| The session-store hydrate + row conversion the helper feeds. | `sessionStore`; `fromTerminalSessionInfo` | dashboard/src/data/sessions.ts:494-508; dashboard/src/data/sessions.ts:615-623 |
| The poll-health state the beats update: three misses mark the catalog stale. | `recordPollBeat`; `POLL_STALE_MISSED_BEATS` | dashboard/src/data/sessionCockpitStore.ts:186-186; dashboard/src/data/sessionCockpitStore.ts:228-228 |
| The shell owns the shared timer and eager/cross-tab reconciler for every view lifetime. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| The sole shell subscriptions keep both the poll driver and reconciler alive with no view in front. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| Current manual hydration after bulk termination. | `endLandedDetailed` | dashboard/src/data/sessionLifecycle.ts:230-251 |
| Current manual hydration after launch confirmation or failed-launch recovery. | "import { useState } from \"react\";"; "import type { LaunchPrefill } from "; `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:10-10; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:70-144; dashboard/src/panels/session-cockpit/LaunchFlow.tsx:362-423; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:1-1 |
| The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. | `hydrateTerminalSessionsFromCatalog`; `startCatalogPollDriver`; `startCatalogReconciler` | dashboard/src/data/catalogPoll.test.ts:58-272 |

## Historical FEUI-L8 Reviewed Candidate Delta

Adds a generation-scoped dev authority, separates live action preference from cockpit inspection focus, and owns one refcounted eager/cross-tab reconciler beside the timer. Terminated ids are removed before and excluded from confirmation so stale catalog echoes cannot resurrect them.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: generated the final ranges for the two
  S18-T3 `:1-1` prose citations (`scheduleCatalogPoll`/`startCatalogPollDriver` → 163-173 and
  179-192, `startCatalogReconciler` → 206-231) and kept the reviewed `recordPollBeat` implementation
  binding (sessionCockpitStore.ts 294-303) after the fixer retargeted the declaration line. Zero
  findings remain.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: replaced the obsolete interval account with
  the current serialized timeout chain: a tick waits for bounded hydration to settle before it
  schedules the next, and the final subscriber release clears the pending timeout. Citation
  mechanics are handed to the exact-document curator through explicit `:1-1` fixer input.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: normalized 19 mechanical citation findings across the self-file prose and repo-internal reference rows. Max-reviewer subject-binding addendum retargeted `recordPollBeat` to its implementation and `POLL_STALE_MISSED_BEATS` threshold. Preserved one Tier-3 claim-truth finding: the prose still says the driver uses `window.setInterval`, while the frozen source schedules serialized `window.setTimeout` polls; no source was fabricated for that disputed claim.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. The
  `readLastActiveSessionId`/`writeLastActiveSessionId` pair cited L18-L33, which is now
  `CatalogAuthority` + `captureCatalogAuthority`/`catalogAuthorityIsCurrent`; the two localStorage
  helpers moved below the dev-bench authority block and now sit at L44-L50 and L52-L59, so the
  citation is L44-L59.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: labeled the old `Chats` extraction as historical,
  recorded `CockpitShell` as the sole driver/reconciler owner, and replaced the deleted consumer
  list with the current manual-hydrate callers; labeled the former uncommitted-candidate note as
  historical after landing. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S1 (R1, poll-driver hoist): the shared
  refcounted 2500 ms catalog poll driver + `hydrateTerminalSessionsFromCatalog` moved verbatim
  from Chats, extended only by poll-health beat recording on every read (R15/F3; review finding 6
  routed Chats' initial mount hydrate through the same helper). Verification metadata pinned to
  the leaf base until closeout stamps the L2 code commit.
