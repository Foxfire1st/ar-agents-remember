# dashboard/src/data/conversation/client.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The HTTP client for the landed active + control conversation routes. It follows the house data-client
idiom (`setClient.ts`/`terminal.ts`): a same-origin `base` param, `encodeURIComponent` template paths,
an injectable `fetch` for tests, "or-null" reads, and **typed evidence for control operations — a
refusal is never guessed into success**. Route shapes are the exact landed wire (`active/api.py`,
`control/api.py`), and every epoch-guarded route sends the camelCase `expectedBridgeEpoch` query param.

## Code Commentary

### Logic

- `activeBase` builds `${base}/api/terminal/{sessionId}/conversation`; `epochQuery` appends
  `expectedBridgeEpoch`.
- `fetchConversationPage` returns a typed `PageResult` — `{ok:true, page}`, OR `{ok:false, error:
  ConversationRouteError}` when the server refuses (the typed reason `{status, detail, httpStatus}` is
  threaded to the banner — §14.5, F15), OR `{ok:false, error:null}` on a transport drop. A read failure
  NEVER fabricates a page (§9.1). `asRouteError` extracts the server's `{status, detail}` and falls back
  to a `transport` marker.
- `fetchConversationTelemetry` GETs evidence-bound telemetry; absent metrics are omitted server-side and
  a failure returns `null` (unavailable, never zero — A2). This is the previously-orphaned function
  `AmbientTelemetry.tsx` now consumes (F3).
- `requestInterrupt` / `interruptStatus` / `interruptReconcile` POST `{turnId, requestId}` to the three
  interrupt routes through `postInterrupt`; `parseInterrupt` discriminates on the operation's own
  `acknowledgement` discriminator so a typed refusal (e.g. a 422 capability refusal or version mismatch)
  is returned as `{ok:false, error}` and NEVER rendered as an accepted interrupt. A transport failure is
  a typed `transport`/httpStatus 0 error, not a guess.
- `conversationEventsUrl` builds the resumable SSE URL with `after=<cursor>` only (never a
  `Last-Event-ID` header — the cursor-conflict avoidance owned by `stream.ts`).

### Invariants And Boundaries

- **A refusal is evidence, never success.** `parseInterrupt` keys on the payload discriminator; only a
  body carrying `acknowledgement` is an operation.
- **Typed reasons survive.** A page/interrupt failure preserves the server's exact `{status, detail}`
  so the banner/control can show the real reason (F15) instead of a generic message.
- **Caller-stable requestId.** The interrupt id is supplied by the caller and reconciled under the SAME
  id (invariant 27); for pi that id is the active AR operation id, not a native turn id (L4-facing
  ruling 3) — the client is agnostic and posts whatever the caller supplies.
- **Injectable + or-null.** All reads accept a `FetchLike`; a network error is a typed transport result,
  never a thrown exception to the caller.

### 2026-07-24 Curator Delta

Page, telemetry, and interrupt requests now share a 15-second abort bound. A half-open transport
therefore enters the client's established error and recovery paths instead of freezing a conversation
operation forever.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The page/telemetry/interrupt/error wire shapes this client returns. [1]
- The store that threads `PageResult` errors to `errorBySession`/the banner. [2]
- The SSE controller that consumes `conversationEventsUrl`. [3]
- The interrupt hook that discriminates `ControlResult` into ack/settlement/refusal. [4]
- The landed active + control routes this client calls. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260727-CHATS-IM-L2 Selected-Child Client Delta

`requestAgentHistory` posts to the exact active-session child route with the expected bridge epoch
and encoded agent id cit:(["export async function requestAgentHistory"], dashboard/src/data/conversation/client.ts:191-191). Its discriminated result preserves the four successful
child-local statuses and converts non-2xx, invalid successful payloads, network failure, and
timeout into typed route errors cit:(["function asRouteError"], dashboard/src/data/conversation/client.ts:37-37). These errors are returned to the child store; they do
not fail the parent stream.
