# dashboard/src/data/catalogPoll.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **shared terminal-catalog poll driver** (260715-FEUI-L2 S1/R1), hoisted verbatim out of
`panels/Chats.tsx` so the session feed stays alive with ANY view — or none — in front. Catalog rows
have NO push channel by design: this 2500 ms poll is the authoritative reconciler (the seat events
in `seatEvents.ts` only pre-apply what the next beat confirms). Refcounted: Cockpit starts it
unconditionally, Chats and SessionsView consume the same interval — never a second timer. The
**L8 Chats-cutover decision explicitly depends on this hoist having landed** (module comment):
Chats now consumes this driver unchanged instead of owning the interval.

## Code Commentary

### Logic

- `CATALOG_REFRESH_INTERVAL_MS = 2500` (L14) — the one poll cadence, exported for tests.
- `readLastActiveSessionId`/`writeLastActiveSessionId` (L18-L33) — the
  `ar-dashboard:last-active-chat-session` localStorage preference, moved with the hydrate (a UI
  preference only; failures swallowed for private contexts).
- `hydrateTerminalSessionsFromCatalog(allowEmpty, excludeSessionIds)` (L40-L51) — ONE catalog
  fetch → session-store hydrate, moved verbatim from Chats. Every read ALSO records a poll-health
  beat (`sessionCockpitStore.recordPollBeat(list !== null)`, R15/F3): a `null` (network/HTTP
  failure) counts as a missed beat so a dead poll surfaces as the rail's stale banner instead of
  freezing rows silently. Guards preserved byte-for-byte from Chats: an empty list applies only
  when `allowEmpty`; `excludeSessionIds` filters just-terminated ids so a stale snapshot cannot
  resurrect them; the hydrate keeps the last-active preference.
- `startCatalogPollDriver()` (L60-L77) — the refcounted subscription: the FIRST subscriber starts
  the `window.setInterval`, the LAST release clears it; each returned release is idempotent (a
  `released` latch), so React StrictMode double-mount (start/release/start) and double-release are
  safe. Consumers never see each other.

### Invariants And Boundaries

- The poll is AUTHORITATIVE for session rows; push (seatEvents) is a pre-apply layer only. Nothing
  here may be replaced by an event channel without a design ruling.
- One interval regardless of subscriber count; zero subscribers ⇒ no timer (no leak).
- Every catalog read — driver tick or manual hydrate (Chats mount, post-bulk-end refresh) —
  records a beat; `hydrateTerminalSessionsFromCatalog` is the ONLY sanctioned read path.
- Consumers: `cockpit/Cockpit.tsx` (unconditional), `panels/Chats.tsx`, and
  `panels/session-cockpit/SessionsView.tsx` — all via `useEffect(() => startCatalogPollDriver(), [])`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The refcount driver, hydrate helper, beat recording, and localStorage preference. | L14-L77 | [catalogPoll.ts](catalogPoll.ts) |
| The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). | — | [terminal.ts](terminal.ts) |
| The session-store hydrate + row conversion the helper feeds. | — | [sessions.ts](sessions.ts) |
| The poll-health state the beats update (`recordPollBeat`, 3 misses ⇒ stale). | L83-L84, L162-L172 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The former owner, now a consumer (interval effect replaced 1:1 by the driver). | L306-L333 | [../panels/Chats.tsx](../panels/Chats.tsx) |
| The unconditional shell subscription keeping the feed alive with no view in front. | L352-L354 | [../cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. | L29-L100 | [catalogPoll.test.ts](catalogPoll.test.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S1 (R1, poll-driver hoist): the shared
  refcounted 2500 ms catalog poll driver + `hydrateTerminalSessionsFromCatalog` moved verbatim
  from Chats, extended only by poll-health beat recording on every read (R15/F3; review finding 6
  routed Chats' initial mount hydrate through the same helper). Verification metadata pinned to
  the leaf base until closeout stamps the L2 code commit.
