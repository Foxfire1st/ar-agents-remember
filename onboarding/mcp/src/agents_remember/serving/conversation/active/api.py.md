# mcp/src/agents_remember/serving/conversation/active/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The two registered production routes of the active conversation surface (260718-CHATS-L1): the
authorized native-hydrated page and the resumable SSE event stream. Every wire resolves the
caller through the L0 authorization dependency, compares `expectedBridgeEpoch` against the live
submission authority, and maps every typed refusal to the serving status idiom — pre-stream as
typed HTTP errors, established-stream failures as one typed `gap` plus close. Raw 500s are
never a routine refusal path (L0 reviewer obligation O4).

## Code Commentary

### Logic

`conversation_page` (L121-L150, `GET /api/terminal/{ar_session_id}/conversation`) invokes the
two L0 dependency functions directly inside the handler (dependency-raised refusals would
otherwise become untyped 500s before the handler runs — worker round-2 issue 1), decodes the
optional `before` page cursor, and returns the atomically assembled page.
`conversation_events` (L153-L186, `GET …/conversation/events`) runs every pre-stream check —
authorization, epoch, dual-resume agreement (`after` query + `Last-Event-ID` header must name
the same event cursor, `_resume_cursor` L106-L118), generation, retention floor — BEFORE the
`StreamingResponse` exists, so all routine failures are typed HTTP responses.
`_map_typed_error` (L72-L94) maps each typed refusal to one precise status: 409
`bridge-epoch-mismatch` (with expected/actual), 403 `authorization-failed`, 503
`composition-unavailable`/`control-unavailable`, the cursor family (400
`cursor-invalid`/`cursor-conflict`, 403 `cursor-authorization`, 409
`cursor-reset-required`), and the session-resolution family (404 `unknown-session`, 409
`unsupported`). `_event_stream` (L189-L204) yields `resume-replay`-marked replay envelopes,
then live envelopes until the close sentinel or a gap mutation (returning after the gap frame).
`_sse_frame` (L207-L216) emits explicit wire frames (`event`/`data`/`retry`/`id`) rather than
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
- The router still owns only these two GET routes; library/control shells are untouched.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this route module; the strict wire contract
and the production-route suite are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The active service these routes invoke for page assembly and subscription validation. | L83-L135 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |
| The cursor error family mapped to exact statuses here. | L39-L82 | [cursor.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/cursor.py) |
| The L0 request dependencies invoked directly in-handler for typed mapping. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The production-route suite driving these routes over a real socket. | L362-L781 | [test_conversation_active_api.py](agents-remember/mcp/tests/test_conversation_active_api.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this route module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

The active API now keeps cursor and generation behavior coherent for fresh page/event handoff, including the bootstrap event path that lets a newly connected client establish a live stream without treating a valid fresh page as a cursor fault.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: rewrote the sidecar from the L9 route-shell
  card to the implemented two production routes — typed pre-stream error ladder, dual-cursor
  agreement, explicit SSE frames, close/gap termination; governing overview re-pointed to the
  new active route overview. Verification hash stays pinned at the last commit that touched the
  source until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the active route-shell sidecar.
  Verification is blank until closeout commits and stamps the new source.
