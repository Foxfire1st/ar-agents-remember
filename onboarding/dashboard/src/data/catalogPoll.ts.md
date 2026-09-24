# dashboard/src/data/catalogPoll.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T16:02+02:00                           |
| lastVerifiedCommitHash | `2e11db883f77bb1bf2827ae537b5d1d564e020b3`       |
| lastVerifiedCommitDate | 2026-09-24T22:33:57+02:00|
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
| The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). | `fetchTerminalSessionsOrNull` | dashboard/src/data/terminal.ts:413-432 |
| The session-store hydrate + row conversion the helper feeds. | `sessionStore`; `fromTerminalSessionInfo` | dashboard/src/data/sessions.ts:543-557; dashboard/src/data/sessions.ts:668-676 |
| The poll-health state the beats update: three misses mark the catalog stale. | `recordPollBeat`; `POLL_STALE_MISSED_BEATS` | dashboard/src/data/sessionCockpitStore.ts:186-186; dashboard/src/data/sessionCockpitStore.ts:228-228 |
| The shell owns the shared timer and eager/cross-tab reconciler for every view lifetime. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:886-940 |
| The sole shell subscriptions keep both the poll driver and reconciler alive with no view in front. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:886-940 |
| Current manual hydration after bulk termination. | `endLandedDetailed` | dashboard/src/data/sessionLifecycle.ts:230-251 |
| Current manual hydration after launch confirmation or failed-launch recovery. | "import { useState } from \"react\";"; "import type { LaunchPrefill } from "; `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:1-1; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:9-9; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:69-143; dashboard/src/panels/session-cockpit/LaunchFlow.tsx:353-413 |
| The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. | "describe(\"hydrateTerminalSessionsFromCatalog\""; "describe(\"startCatalogPollDriver (refcounted)\""; "describe(\"startCatalogReconciler (eager + cross-tab)\"" | dashboard/src/data/catalogPoll.test.ts:58-58; dashboard/src/data/catalogPoll.test.ts:205-205; dashboard/src/data/catalogPoll.test.ts:264-264; dashboard/src/data/catalogPoll.test.ts:1-1; dashboard/src/data/catalogPoll.test.ts:3-3; dashboard/src/data/catalogPoll.test.ts:9-9; dashboard/src/data/catalogPoll.test.ts:10-10; dashboard/src/data/catalogPoll.test.ts:11-11; dashboard/src/data/catalogPoll.test.ts:12-12; dashboard/src/data/catalogPoll.test.ts:18-18; dashboard/src/data/catalogPoll.test.ts:21-21; dashboard/src/data/catalogPoll.test.ts:22-22; dashboard/src/data/catalogPoll.test.ts:23-23; dashboard/src/data/catalogPoll.test.ts:26-26; dashboard/src/data/catalogPoll.test.ts:32-32; dashboard/src/data/catalogPoll.test.ts:37-37; dashboard/src/data/catalogPoll.test.ts:42-42; dashboard/src/data/catalogPoll.test.ts:47-47; dashboard/src/data/catalogPoll.test.ts:49-49; dashboard/src/data/catalogPoll.test.ts:50-50; dashboard/src/data/catalogPoll.test.ts:53-53; dashboard/src/data/catalogPoll.test.ts:54-54; dashboard/src/data/catalogPoll.test.ts:55-55; dashboard/src/data/catalogPoll.test.ts:56-56; dashboard/src/data/catalogPoll.test.ts:60-60; dashboard/src/data/catalogPoll.test.ts:61-61; dashboard/src/data/catalogPoll.test.ts:62-62; dashboard/src/data/catalogPoll.test.ts:63-63; dashboard/src/data/catalogPoll.test.ts:64-64; dashboard/src/data/catalogPoll.test.ts:67-67; dashboard/src/data/catalogPoll.test.ts:68-68; dashboard/src/data/catalogPoll.test.ts:69-69; dashboard/src/data/catalogPoll.test.ts:70-70; dashboard/src/data/catalogPoll.test.ts:71-71; dashboard/src/data/catalogPoll.test.ts:72-72; dashboard/src/data/catalogPoll.test.ts:74-74; dashboard/src/data/catalogPoll.test.ts:75-75; dashboard/src/data/catalogPoll.test.ts:76-76; dashboard/src/data/catalogPoll.test.ts:77-77; dashboard/src/data/catalogPoll.test.ts:80-80; dashboard/src/data/catalogPoll.test.ts:82-82; dashboard/src/data/catalogPoll.test.ts:83-83; dashboard/src/data/catalogPoll.test.ts:84-84; dashboard/src/data/catalogPoll.test.ts:85-85; dashboard/src/data/catalogPoll.test.ts:87-87; dashboard/src/data/catalogPoll.test.ts:88-88; dashboard/src/data/catalogPoll.test.ts:89-89; dashboard/src/data/catalogPoll.test.ts:90-90; dashboard/src/data/catalogPoll.test.ts:92-92; dashboard/src/data/catalogPoll.test.ts:96-96; dashboard/src/data/catalogPoll.test.ts:97-97; dashboard/src/data/catalogPoll.test.ts:99-99; dashboard/src/data/catalogPoll.test.ts:100-100; dashboard/src/data/catalogPoll.test.ts:110-110; dashboard/src/data/catalogPoll.test.ts:113-113; dashboard/src/data/catalogPoll.test.ts:114-114; dashboard/src/data/catalogPoll.test.ts:116-116; dashboard/src/data/catalogPoll.test.ts:117-117; dashboard/src/data/catalogPoll.test.ts:118-118; dashboard/src/data/catalogPoll.test.ts:120-120; dashboard/src/data/catalogPoll.test.ts:124-124; dashboard/src/data/catalogPoll.test.ts:125-125; dashboard/src/data/catalogPoll.test.ts:126-126; dashboard/src/data/catalogPoll.test.ts:127-127; dashboard/src/data/catalogPoll.test.ts:129-129; dashboard/src/data/catalogPoll.test.ts:131-131; dashboard/src/data/catalogPoll.test.ts:134-134; dashboard/src/data/catalogPoll.test.ts:135-135; dashboard/src/data/catalogPoll.test.ts:136-136; dashboard/src/data/catalogPoll.test.ts:137-137; dashboard/src/data/catalogPoll.test.ts:138-138; dashboard/src/data/catalogPoll.test.ts:139-139; dashboard/src/data/catalogPoll.test.ts:140-140; dashboard/src/data/catalogPoll.test.ts:146-146; dashboard/src/data/catalogPoll.test.ts:147-147; dashboard/src/data/catalogPoll.test.ts:148-148; dashboard/src/data/catalogPoll.test.ts:149-149; dashboard/src/data/catalogPoll.test.ts:152-152; dashboard/src/data/catalogPoll.test.ts:154-154; dashboard/src/data/catalogPoll.test.ts:155-155; dashboard/src/data/catalogPoll.test.ts:156-156; dashboard/src/data/catalogPoll.test.ts:157-157; dashboard/src/data/catalogPoll.test.ts:159-159; dashboard/src/data/catalogPoll.test.ts:161-161; dashboard/src/data/catalogPoll.test.ts:162-162; dashboard/src/data/catalogPoll.test.ts:165-165; dashboard/src/data/catalogPoll.test.ts:166-166; dashboard/src/data/catalogPoll.test.ts:168-168; dashboard/src/data/catalogPoll.test.ts:169-169; dashboard/src/data/catalogPoll.test.ts:170-170; dashboard/src/data/catalogPoll.test.ts:173-173; dashboard/src/data/catalogPoll.test.ts:177-177; dashboard/src/data/catalogPoll.test.ts:178-178; dashboard/src/data/catalogPoll.test.ts:179-179; dashboard/src/data/catalogPoll.test.ts:180-180; dashboard/src/data/catalogPoll.test.ts:181-181; dashboard/src/data/catalogPoll.test.ts:185-185; dashboard/src/data/catalogPoll.test.ts:186-186; dashboard/src/data/catalogPoll.test.ts:187-187; dashboard/src/data/catalogPoll.test.ts:188-188; dashboard/src/data/catalogPoll.test.ts:192-192; dashboard/src/data/catalogPoll.test.ts:193-193; dashboard/src/data/catalogPoll.test.ts:194-194; dashboard/src/data/catalogPoll.test.ts:195-195; dashboard/src/data/catalogPoll.test.ts:196-196; dashboard/src/data/catalogPoll.test.ts:197-197; dashboard/src/data/catalogPoll.test.ts:198-198; dashboard/src/data/catalogPoll.test.ts:200-200; dashboard/src/data/catalogPoll.test.ts:202-202; dashboard/src/data/catalogPoll.test.ts:203-203; dashboard/src/data/catalogPoll.test.ts:207-207; dashboard/src/data/catalogPoll.test.ts:208-208; dashboard/src/data/catalogPoll.test.ts:209-209; dashboard/src/data/catalogPoll.test.ts:211-211; dashboard/src/data/catalogPoll.test.ts:212-212; dashboard/src/data/catalogPoll.test.ts:213-213; dashboard/src/data/catalogPoll.test.ts:214-214; dashboard/src/data/catalogPoll.test.ts:216-216; dashboard/src/data/catalogPoll.test.ts:217-217; dashboard/src/data/catalogPoll.test.ts:218-218; dashboard/src/data/catalogPoll.test.ts:219-219; dashboard/src/data/catalogPoll.test.ts:221-221; dashboard/src/data/catalogPoll.test.ts:222-222; dashboard/src/data/catalogPoll.test.ts:223-223; dashboard/src/data/catalogPoll.test.ts:224-224; dashboard/src/data/catalogPoll.test.ts:227-227; dashboard/src/data/catalogPoll.test.ts:235-235; dashboard/src/data/catalogPoll.test.ts:238-238; dashboard/src/data/catalogPoll.test.ts:239-239; dashboard/src/data/catalogPoll.test.ts:241-241; dashboard/src/data/catalogPoll.test.ts:243-243; dashboard/src/data/catalogPoll.test.ts:244-244; dashboard/src/data/catalogPoll.test.ts:245-245; dashboard/src/data/catalogPoll.test.ts:246-246; dashboard/src/data/catalogPoll.test.ts:247-247; dashboard/src/data/catalogPoll.test.ts:251-251; dashboard/src/data/catalogPoll.test.ts:252-252; dashboard/src/data/catalogPoll.test.ts:254-254; dashboard/src/data/catalogPoll.test.ts:255-255; dashboard/src/data/catalogPoll.test.ts:256-256; dashboard/src/data/catalogPoll.test.ts:257-257; dashboard/src/data/catalogPoll.test.ts:259-259; dashboard/src/data/catalogPoll.test.ts:261-261; dashboard/src/data/catalogPoll.test.ts:262-262; dashboard/src/data/catalogPoll.test.ts:266-266; dashboard/src/data/catalogPoll.test.ts:267-267; dashboard/src/data/catalogPoll.test.ts:268-268; dashboard/src/data/catalogPoll.test.ts:269-269; dashboard/src/data/catalogPoll.test.ts:271-271; dashboard/src/data/catalogPoll.test.ts:272-272; dashboard/src/data/catalogPoll.test.ts:276-276; dashboard/src/data/catalogPoll.test.ts:277-277; dashboard/src/data/catalogPoll.test.ts:278-278; dashboard/src/data/catalogPoll.test.ts:280-280; dashboard/src/data/catalogPoll.test.ts:282-282; dashboard/src/data/catalogPoll.test.ts:283-283; dashboard/src/data/catalogPoll.test.ts:284-284; dashboard/src/data/catalogPoll.test.ts:285-285; dashboard/src/data/catalogPoll.test.ts:291-291; dashboard/src/data/catalogPoll.test.ts:292-292; dashboard/src/data/catalogPoll.test.ts:293-293; dashboard/src/data/catalogPoll.test.ts:296-296; dashboard/src/data/catalogPoll.test.ts:302-302; dashboard/src/data/catalogPoll.test.ts:303-303; dashboard/src/data/catalogPoll.test.ts:304-304; dashboard/src/data/catalogPoll.test.ts:306-306; dashboard/src/data/catalogPoll.test.ts:307-307; dashboard/src/data/catalogPoll.test.ts:312-312; dashboard/src/data/catalogPoll.test.ts:313-313; dashboard/src/data/catalogPoll.test.ts:314-314; dashboard/src/data/catalogPoll.test.ts:316-316; dashboard/src/data/catalogPoll.test.ts:317-317; dashboard/src/data/catalogPoll.test.ts:319-319; dashboard/src/data/catalogPoll.test.ts:320-320 |

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
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `fromTerminalSessionInfo`, `sessionStore` repointed to dashboard/src/data/sessions.ts:543-557, dashboard/src/data/sessions.ts:668-676. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

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
