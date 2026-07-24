# dashboard/src/data/conversation/stream.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/stream.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The **resumable SSE transport** for active-conversation events (§9.2, §14.5). It deliberately does NOT
use EventSource's native auto-reconnect: native reconnect keeps the original `after=` query AND adds a
`Last-Event-ID` header from the latest received id, which the server rejects as `cursor-conflict` when
the two disagree (`active/api.py` preflight). Instead any transport error closes, backs off, and opens a
FRESH EventSource whose only resume input is `after=<latest cursor>` — a brand-new instance has no
`lastEventId`, so no header is sent (L4.3). Gap/reset recovery is owned by the reducer + store; this
controller only delivers ordered envelopes and reports connect/disconnect.

## Code Commentary

### Logic

- `openConversationStream(options)` takes `sessionId`/`epoch`/`base`, a `getResumeCursor()` closure
  (reads the store's `projection.eventCursor` at each (re)connect), the `onEnvelope`/`onOpen`/
  `onDisconnect` handlers, an injectable `EventSourceCtor`, and test-overridable backoff/timers.
- `open()` closes any prior source and constructs a new `EventSource` from `conversationEventsUrl(…,
  getResumeCursor())`. It listens for `open` (→ `onOpen`), the named `conversation` message event
  (JSON-parses the envelope; a malformed frame is IGNORED so the reducer only ever sees well-formed
  envelopes), and `error`.
- On `error` it closes, fires `onDisconnect`, and schedules a `reconnectDelayMs` (default 2000)
  backoff that reopens from the latest cursor. A stale generation guard (`source !== next`) ignores
  callbacks from a superseded source.
- The returned controller exposes `reconnect()` (reopen from the current cursor — used by the store
  after a re-page) and `stop()` (mark stopped, clear the timer, close the source).

### Invariants And Boundaries

- **No native auto-reconnect.** Every resume is a fresh EventSource with no `lastEventId`, so only
  `after=` carries the cursor — the deliberate avoidance of the landed `cursor-conflict` preflight (L4.3).
- **Transport, not interpretation.** This module owns browser wiring only; ordering, dedupe, gap
  handling, and recovery all live in the reducer/store.
- **A malformed frame is swallowed**, never forwarded — the reducer's contract is well-formed envelopes.
- **Superseded sources are inert** (the `source !== next` guard), so a slow close cannot demote a fresh
  connection.

### 2026-07-24 Curator Delta

Before its first successful open, the stream retries the bridge boot window quickly; established
drops retain the normal backoff. An open deadline and shared liveness watchdog distinguish an
unopened or half-open channel from an honestly live one, while a quiet resume remains visually quiet.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The event-URL builder (`after=` only) this controller opens. | L182-L192 | [client.ts](client.ts) |
| The envelope type this controller parses and forwards. | L9-L10 | [types.ts](types.ts) |
| The store that owns connect/recovery and calls `reconnect()`/`stop()`. | L170-L223 | [store.ts](store.ts) |
| The server preflight that rejects a conflicting `after=`/`Last-Event-ID`. | — | [active/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-24T13:17:50Z — Recorded boot-aware reconnect, open-deadline, and half-open watchdog
  behavior. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the resumable SSE
  controller — the manual fresh-EventSource reconnect from `after=<cursor>` (no `Last-Event-ID`) that
  avoids the landed cursor-conflict preflight (L4.3), the malformed-frame swallow, and the
  transport-only boundary. Verification is pinned to the leaf base (`0be0099`) because the new source
  file is uncommitted; closeout owns its first source stamp.
