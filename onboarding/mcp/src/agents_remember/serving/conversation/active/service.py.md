# mcp/src/agents_remember/serving/conversation/active/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The app-scoped active conversation serving authority (leaf R1/R4): one service per installed
`ConversationRuntime`, holding the cursor secret and the bounded set of live session projectors.
It resolves the exact session, verifies the expected bridge epoch against the live authority on
every wire, assembles atomic page+eventCursor responses, and performs every pre-stream cursor
check before an SSE response exists.

## Code Commentary

### Logic

`ActiveConversationService` (L65-L227) mints its own 32-byte random cursor secret (L71 — per
app, never persisted; a daemon restart invalidates old cursor generations loudly). `page`
(L83-L104) resolves the projector, decodes the optional `before` page cursor against the
authorized identity, bounds the limit (≤500), and assembles the `ConversationPage` (identity,
window, fresh page cursor, event cursor, hydration id, canonical status, capabilities) in
`_assemble_page` (L199-L227). `subscribe` (L106-L135) decodes the event cursor, enforces
same-generation and the retention floor (`cursor-reset-required` with `generation-changed` /
`retention-overflow` reasons), then attaches the subscriber queue and snapshots the replay
window with no await between them — the poll task cannot interleave, so replay and live delivery
neither gap nor duplicate an envelope (L126-L135). `release_session` (L143-L156) de-registers and closes one
session's projector when the session ends: it pops the projector from `_projectors`, drops it from
the LRU order, and awaits `projector.close()`, releasing the whole per-session projection
(ProjectionStore items, the L5 live-turn/request id-sets, retained SSE envelopes) immediately
instead of leaving it registered until the tombstone self-idles and then falls to 32-LRU eviction
(260718-CHATS-L5F R5). `_projector_for` (L157-L196) resolves the
catalog entry, verifies the expected bridge epoch against the live submission authority, builds
the proven identity, and returns the matching live projector or closes/replaces a stale one;
projectors are bounded at 32 per app with LRU eviction (L54, L198-L203) — an evicted projector
rehydrates from native authority and establishes a new cursor generation, so stale event cursors
reset loudly instead of mixing sequences. Every blocking sync IPC read is offloaded with
`asyncio.to_thread` (L165-L172) so the daemon event loop stays responsive. One service per
runtime is kept through a weak-key registry (L248-L260).

### Conventions

Projectors are reconstructable projections, never authorities: eviction/loss costs nothing but a
rehydration, and the generation change is the honest signal. The service holds the only cursor
secret; minting/decoding never happens in routes or projectors without it.

### Invariants And Boundaries

- Every wire verifies `expectedBridgeEpoch` against the LIVE authority per request; ambient
  server context is never a substitute (409 `bridge-epoch-mismatch` with expected/actual).
- Page + eventCursor are atomic: the projector captures them under its apply lock after the
  latest poll.
- All cursor checks complete before a `StreamingResponse` exists; established-stream failures
  are gap events, never HTTP resets.
- Sync IPC reads never run on the event loop (worker round-2 issue 3 — a production
  responsiveness rule, not a test workaround).
- `release_session` (explicit session-end projection release) is implemented and unit-tested but,
  as of this leaf, has NO production caller — the terminate/retire endpoints do not invoke it
  (reviewer F1, accepted-bounding disposition). The tombstone-projector leak is closed by
  bounded-by-construction (the 32-projector LRU) plus the projector's own idle-self-release
  (`_release_dormant_state` at the dormant idle-break, ~30-60s after the last subscriber departs),
  NOT by an explicit end-hook. R5's "released or bounded" is met; the "removed on session end"
  sub-clause is met only via idle release. Recorded wiring locus for the follow-on: expose the
  app-scoped `ConversationRuntime` (minted once in
  `harness_control_api.register_harness_control_routes`) and call `release_session` after
  `catalog.mark_terminated` in the terminate and retire handlers, scheduling the async release onto
  the loop (`run_coroutine_threadsafe`) from the sync endpoint.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The composition and wire contracts
are repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this service. | — | — |

## Repo-Internal References

The L0 runtime authority is the composition this service keys on; the cursor authority does the
signing/binding; the projector engine does hydration/polling; the routes call only this service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The immutable app-scoped `ConversationRuntime` is the authority one service instance binds. | L47-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| Cursor mint/decode/generation checks run through the cursor authority with this service's secret. | L197-L272 | [cursor.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/cursor.py) |
| The projector captures the atomic page + event cursor under its apply lock. | L213-L234 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The two routes invoke this service and map its typed refusals to the serving status idiom. | L121-L186 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |

## Cross-Repo References

No cross-repository implementation participates in this service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260727-CHATS-IM-L2 Selected-Child Service Delta

`hydrate_agent_history` resolves the same exact authorized session/projector and bridge epoch as
page/SSE, then delegates only the requested child id to `refresh_agent_native` (L138-L153). The
service does not widen parent paging, invent child eligibility, or translate the local hydration
outcome; those contracts remain projector-owned.

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented the exact-session selected-child
  service seam and its parent-page/projector ownership boundaries. Verification metadata remains
  pinned while uncommitted.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded R5 — added `release_session`, which
  de-registers and closes one session's projector on session end (pop from `_projectors`, drop from
  the LRU, await `projector.close()`), freeing the whole per-session projection immediately instead
  of waiting for the tombstone to self-idle and fall to 32-LRU eviction. Recorded the honest F1
  disposition: `release_session` has no production caller this leaf (terminate/retire do not invoke
  it), so the leak is closed by bounded-by-construction plus the projector's idle-self-release, not
  by an explicit end-hook; captured the recorded wiring locus for the follow-on. Refreshed stale
  line refs shifted by the new method. Verification metadata stays pinned until L5F closeout stamps
  the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the active serving
  authority — per-app service, epoch verification per wire, atomic page+cursor assembly,
  pre-stream cursor checks, bounded projector LRU. Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
