# dashboard/src/data/conversation/stream.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/stream.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
- On `error` it closes, fires `onDisconnect`, and schedules the established-connection
  `reconnectDelayMs` (default 2000) backoff. Before the first successful open, the boot window uses
  `bootReconnectDelayMs` instead; both are configured in the transport's defaults and applied by the
  open/error lifecycle. cit:([`bootReconnectDelayMs`, `reconnectDelayMs`], dashboard/src/data/conversation/stream.ts:55-55; dashboard/src/data/conversation/stream.ts:63-63)
  cit:([`open`], dashboard/src/data/conversation/stream.ts:137-203)
  A stale generation guard (`source !== next`) ignores callbacks from a superseded source.
- cit:([`reconnect`, `stop`], dashboard/src/data/conversation/stream.ts:82-83) exposes controller
  operations for reopening or stopping the transport. The store's recovery path owns stopping and
  recreating the stream through `startStream`, rather than claiming that it calls controller
  `reconnect()`. cit:([`startStream`], dashboard/src/data/conversation/store.ts:382-425)

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The event-URL builder (`after=` only) this controller opens. | `conversationEventsUrl` | dashboard/src/data/conversation/client.ts:294-303 |
| The envelope type this controller parses and forwards. | `eventCursor` | dashboard/src/data/conversation/types.ts:286-315 |
| The store recovery path that stops and recreates the stream. | `startStream` | dashboard/src/data/conversation/store.ts:382-425 |
| The active-conversation cursor authority names the `cursor-conflict` refusal. | "cursor-conflict" | mcp/src/agents_remember/serving/conversation/active/cursor.py:82-82 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04: split boot versus established reconnect delays,
  corrected store/controller ownership, and converted transport references to source-backed citations.

- 2026-07-24T13:17:50Z — Recorded boot-aware reconnect, open-deadline, and half-open watchdog
  behavior. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the resumable SSE
  controller — the manual fresh-EventSource reconnect from `after=<cursor>` (no `Last-Event-ID`) that
  avoids the landed cursor-conflict preflight (L4.3), the malformed-frame swallow, and the
  transport-only boundary. Verification is pinned to the leaf base (`0be0099`) because the new source
  file is uncommitted; closeout owns its first source stamp.
