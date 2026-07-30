# dashboard/src/data/conversation/client.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/client.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-27T14:20+02:00                           |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`       |
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
| governingOverview      | `overview.md`                                    |

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
| The page/telemetry/interrupt/error wire shapes this client returns. | L8-L15 | [types.ts](types.ts.md) |
| The store that threads `PageResult` errors to `errorBySession`/the banner. | L96-L104 | [store.ts](store.ts.md) |
| The SSE controller that consumes `conversationEventsUrl`. | L9-L10 | [stream.ts](stream.ts.md) |
| The interrupt hook that discriminates `ControlResult` into ack/settlement/refusal. | L115-L132 | [../../panels/session-cockpit/conversation/useConversationControls.ts](../../panels/session-cockpit/conversation/useConversationControls.ts.md) |
| The landed active + control routes this client calls. | — | [active/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) · [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## 260727-CHATS-IM-L2 Selected-Child Client Delta

`requestAgentHistory` posts to the exact active-session child route with the expected bridge epoch
and encoded agent id (L179-L198). Its discriminated result preserves the four successful
child-local statuses and converts non-2xx, invalid successful payloads, network failure, and
timeout into typed route errors (L110-L177). These errors are returned to the child store; they do
not fail the parent stream.

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented the selected-child POST,
  discriminated outcomes, strict response validation, and visible transport/error mapping.
  Verification metadata remains pinned while uncommitted.

- 2026-07-24T13:17:50Z — Added the conversation HTTP timeout boundary. Verification hash/date remain
  pinned to the pre-commit source stamp.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the active/control HTTP
  client — the typed `PageResult` threading the server's `ConversationRouteError` to the banner (F15),
  the telemetry read now consumed by AmbientTelemetry (F3), and the caller-stable interrupt trio whose
  refusal is discriminated as evidence, never guessed into success. Verification is pinned to the leaf
  base (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
