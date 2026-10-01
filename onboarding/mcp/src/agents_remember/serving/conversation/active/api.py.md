# mcp/src/agents_remember/serving/conversation/active/api.py

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The three registered production routes of the active conversation surface: the authorized
native-hydrated page, selected-child history hydration, and the resumable SSE event stream. Every
wire resolves the
caller through the L0 authorization dependency, compares `expectedBridgeEpoch` against the live
submission authority, and maps every typed refusal to the serving status idiom — pre-stream as
typed HTTP errors, established-stream failures as one typed `gap` plus close. Raw 500s are
never a routine refusal path (L0 reviewer obligation O4).

## Code Commentary

### 260731-EFA-L4 Current Delta — The Three Routes Declare Their Contract

- `GET ""` (cit:(["response_model=ConversationPage"], mcp/src/agents_remember/serving/conversation/active/api.py:130-130)) declares `response_model=ConversationPage`.
- `POST /agents/{agent_id}/history` (cit:(["response_model=AgentHistoryHydrated"], mcp/src/agents_remember/serving/conversation/active/api.py:166-166)) declares `response_model=AgentHistoryHydrated` —
  the first model this assembled body has ever had. The comment above it states the rule this
  card already documented: **a typed child failure is a SUCCESSFUL local outcome**, so the
  failure vocabulary lives inside the 200 body's `status`/`code` and only parent-bridge refusals
  reach `responses`.
- `GET /events` (cit:(["response_model=ConversationEventEnvelope"], mcp/src/agents_remember/serving/conversation/active/api.py:210-210)) declares `response_model=ConversationEventEnvelope` — one envelope
  per SSE frame's `data` — plus an explicit `200: {"content": {"text/event-stream": {}}}` entry.
  The declaration is coherent here precisely because every failure on this route is typed
  PRE-stream, which is why the handler returns an explicit `StreamingResponse` rather than being
  a generator route.

All three share `responses=CONVERSATION_RESPONSES` (from
`serving/conversation/response_contract.py`), which is `CONTROL_RESPONSES` with the cursor
refusals layered on: 400 and 409 carry `CursorRefusal`, the only refusals on this surface that
may carry a machine-readable `reason`. That table is `_map_typed_error`'s ladder transcribed, so
adding a status there without adding it to the table leaves this route emitting an undeclared
shape.

Nothing validates at runtime — the two JSON handlers return `JSONResponse` and the stream
returns `StreamingResponse`, and FastAPI applies `response_model` only to values it serializes
itself. The former route-conformance suite was retired; declarations alone do not prove
current route conformance.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

`conversation_page` (L126-L155, `GET /api/terminal/{ar_session_id}/conversation`) invokes the
two L0 dependency functions directly inside the handler (dependency-raised refusals would
otherwise become untyped 500s before the handler runs — worker round-2 issue 1), decodes the
optional `before` page cursor, and returns the atomically assembled page.
`conversation_events` (L204-L247, `GET …/conversation/events`) runs every pre-stream check —
authorization, epoch, dual-resume agreement (`after` query + `Last-Event-ID` header must name
the same event cursor, `_resume_cursor` L111-L123), generation, retention floor — BEFORE the
`StreamingResponse` exists, so all routine failures are typed HTTP responses.
cit:([`_map_typed_error`], mcp/src/agents_remember/serving/conversation/active/api.py:77-99) maps each typed refusal to one precise status: 409
`bridge-epoch-mismatch` (with expected/actual), 403 `authorization-failed`, 503
`composition-unavailable`/`control-unavailable`, the cursor family (400
`cursor-invalid`/`cursor-conflict`, 403 `cursor-authorization`, 409
`cursor-reset-required`), and the session-resolution family (404 `unknown-session`, 409
`unsupported`). cit:([`_event_stream`], mcp/src/agents_remember/serving/conversation/active/api.py:250-271) primes the stream with one `: connected` SSE comment
(the first body chunk makes GZipMiddleware flush the response start, so a caught-up subscriber's
headers arrive at connect; it carries no cursor and no event field), then yields
`resume-replay`-marked replay envelopes, then live envelopes until the close sentinel or a gap
mutation (returning after the gap frame), detaching the subscription in `finally`.
cit:([`_sse_frame`], mcp/src/agents_remember/serving/conversation/active/api.py:274-282) emits explicit wire frames (`event`/`data`/`retry`/`id`) rather than
the generator-route idiom: this FastAPI version only encodes `ServerSentEvent` objects after
the stream starts, which would make pre-stream typed errors impossible (declared deviation,
review-ruled legitimate).

### Conventions

The routes hold no state and no cursor secret; all authority lives in the active service. The
error ladder maps subclass-before-base so cursor/session errors keep their exact statuses.

### Invariants And Boundaries

- All validation completes before any SSE header is committed; established-stream failures are
  gap events, never HTTP resets.
- Dual resume inputs must agree; a missing resume cursor is `400 cursor-invalid`.
- No raw 500 on any routine refusal path (O4).
- The router owns two GET routes plus the selected-child POST; library/control routes are untouched.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this route module; the strict wire contract
and the production-route suite are the direct evidence.

No configured domain documentation was available.

### Repo-Internal References

- The active service these routes invoke for page assembly and subscription validation. [1]
- The cursor error family mapped to exact statuses here. [2]
- The L0 request dependencies invoked directly in-handler for typed mapping. [3]

| The `CONVERSATION_RESPONSES` table these routes declare and the `AgentHistoryHydrated` model the child-history body finally has. | `CONVERSATION_RESPONSES`; `AgentHistoryHydrated` | mcp/src/agents_remember/serving/conversation/response_contract.py:81-87; mcp/src/agents_remember/serving/conversation/response_contract.py:113-120 |


### Cross-Repo References

No meaningful cross-repo boundary exists for this route module.

No meaningful cross-repo references found.

## 260718-CHATS-L5I Current Delta

The active API now keeps cursor and generation behavior coherent for fresh page/event handoff, including the bootstrap event path that lets a newly connected client establish a live stream without treating a valid fresh page as a cursor fault.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Selected-Child Route Delta

`POST /agents/{agent_id}/history` resolves the same authorization and exact bridge epoch as the
page/event wires, then asks the active service to hydrate only that child
(cit:([`hydrate_agent_history`], mcp/src/agents_remember/serving/conversation/active/api.py:160-198)). Typed
child-local unavailable/not-eligible outcomes are successful response bodies with status, exact
agent id, and optional detail/code; authority, epoch, composition, cursor, control, and session
failures retain the existing typed HTTP mapping. The route never replaces the parent page or SSE
stream.
