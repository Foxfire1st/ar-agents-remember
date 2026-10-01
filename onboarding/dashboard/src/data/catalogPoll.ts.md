# dashboard/src/data/catalogPoll.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The refcount driver, reconciler, hydrate helper, beat recording, and localStorage preference. [1]
- The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). [2]
- The session-store hydrate + row conversion the helper feeds. [3]
- The poll-health state the beats update: three misses mark the catalog stale. [4]
- The shell owns the shared timer and eager/cross-tab reconciler for every view lifetime. [5]
- The sole shell subscriptions keep both the poll driver and reconciler alive with no view in front. [6]
- Current manual hydration after bulk termination. [7]
- Current manual hydration after launch confirmation or failed-launch recovery. [8]
- The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. [9]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Historical FEUI-L8 Reviewed Candidate Delta

Adds a generation-scoped dev authority, separates live action preference from cockpit inspection focus, and owns one refcounted eager/cross-tab reconciler beside the timer. Terminated ids are removed before and excluded from confirmation so stale catalog echoes cannot resurrect them.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.
