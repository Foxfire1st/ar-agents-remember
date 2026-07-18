# dashboard/src/data/catalogPoll.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
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
| The refcount driver, hydrate helper, beat recording, and localStorage preference. | L14-L77 | [catalogPoll.ts](catalogPoll.ts) |
| The catalog fetch this wraps (`fetchTerminalSessionsOrNull`, null on failure). | — | [terminal.ts](terminal.ts) |
| The session-store hydrate + row conversion the helper feeds. | — | [sessions.ts](sessions.ts) |
| The poll-health state the beats update (`recordPollBeat`, 3 misses ⇒ stale). | L83-L84, L162-L172 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The shell owns the shared timer and eager/cross-tab reconciler for every view lifetime. | — | [Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The unconditional shell subscription keeping the feed alive with no view in front. | L352-L354 | [../cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The unit suite: hydrate/beat recording, guards, exclusion set, refcount single-interval. | L29-L100 | [catalogPoll.test.ts](catalogPoll.test.ts) |

## FEUI-L8 Reviewed Candidate Delta

Adds a generation-scoped dev authority, separates live action preference from cockpit inspection focus, and owns one refcounted eager/cross-tab reconciler beside the timer. Terminated ids are removed before and excluded from confirmation so stale catalog echoes cannot resurrect them.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S1 (R1, poll-driver hoist): the shared
  refcounted 2500 ms catalog poll driver + `hydrateTerminalSessionsFromCatalog` moved verbatim
  from Chats, extended only by poll-health beat recording on every read (R15/F3; review finding 6
  routed Chats' initial mount hydrate through the same helper). Verification metadata pinned to
  the leaf base until closeout stamps the L2 code commit.
