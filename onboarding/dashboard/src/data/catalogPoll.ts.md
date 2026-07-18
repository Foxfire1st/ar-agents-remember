# dashboard/src/data/catalogPoll.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T16:02+02:00                           |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee`       |
| lastVerifiedCommitDate | 2026-07-18T15:41:39+02:00|
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

- `CATALOG_REFRESH_INTERVAL_MS = 2500` (L14) — the one poll cadence, exported for tests.
- `readLastActiveSessionId`/`writeLastActiveSessionId` (L18-L33) — the
  `ar-dashboard:last-active-chat-session` localStorage preference, moved with the hydrate (a UI
  preference only; failures swallowed for private contexts).
- `hydrateTerminalSessionsFromCatalog(allowEmpty, excludeSessionIds, authority)` (L79-L96) — ONE
  catalog fetch → session-store hydrate. Its extraction from the retired `Chats` component is
  historical provenance; current behavior also carries a generation-scoped dev authority so a
  superseded scenario cannot mutate successor rows or poll health. Every accepted read records a
  poll-health beat; an empty list applies only when `allowEmpty`; `excludeSessionIds` filters
  just-terminated ids so a stale snapshot cannot resurrect them; hydration keeps the last-active
  preference.
- `startCatalogPollDriver()` (L105-L122) — the refcounted subscription: the FIRST subscriber starts
  the `window.setInterval`, the LAST release clears it; each returned release is idempotent (a
  `released` latch), so React StrictMode double-mount (start/release/start) and double-release are
  safe. Consumers never see each other.
- `startCatalogReconciler()` (L136-L160) — the refcounted eager hydrate plus cross-tab invalidation
  owner. Remote termination is removed before and excluded from its confirming read; create/leaf
  invalidations rehydrate with `allowEmpty`.

### Invariants And Boundaries

- The poll is AUTHORITATIVE for session rows; push (seatEvents) is a pre-apply layer only. Nothing
  here may be replaced by an event channel without a design ruling.
- One interval regardless of subscriber count; zero subscribers ⇒ no timer (no leak).
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The refcount driver, reconciler, hydrate helper, beat recording, and localStorage preference. | L15-L160 | [catalogPoll.ts](catalogPoll.ts) |
| The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). | — | [terminal.ts](terminal.ts) |
| The session-store hydrate + row conversion the helper feeds. | — | [sessions.ts](sessions.ts) |
| The poll-health state the beats update (`recordPollBeat`, 3 misses ⇒ stale). | L83-L84, L162-L172 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The shell owns the shared timer and eager/cross-tab reconciler for every view lifetime. | — | [Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The sole shell subscriptions keep both the poll driver and reconciler alive with no view in front. | L366-L370 | [../cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| Current manual hydration after bulk termination. | L239-L244 | [sessionLifecycle.ts](sessionLifecycle.ts) |
| Current manual hydration after launch confirmation or failed-launch recovery. | L300-L316; L88-L98 | [LaunchFlow.tsx](../panels/session-cockpit/LaunchFlow.tsx); [FailedLaunchBanner.tsx](../panels/session-cockpit/FailedLaunchBanner.tsx) |
| The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. | L29-L100 | [catalogPoll.test.ts](catalogPoll.test.ts) |

## Historical FEUI-L8 Reviewed Candidate Delta

Adds a generation-scoped dev authority, separates live action preference from cockpit inspection focus, and owns one refcounted eager/cross-tab reconciler beside the timer. Terminated ids are removed before and excluded from confirmation so stale catalog echoes cannot resurrect them.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
