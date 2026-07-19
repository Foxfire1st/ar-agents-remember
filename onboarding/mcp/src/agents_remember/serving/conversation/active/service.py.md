# mcp/src/agents_remember/serving/conversation/active/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
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
neither gap nor duplicate an envelope (L126-L135). `_projector_for` (L143-L182) resolves the
catalog entry, verifies the expected bridge epoch against the live submission authority, builds
the proven identity, and returns the matching live projector or closes/replaces a stale one;
projectors are bounded at 32 per app with LRU eviction (L54, L184-L197) — an evicted projector
rehydrates from native authority and establishes a new cursor generation, so stale event cursors
reset loudly instead of mixing sequences. Every blocking sync IPC read is offloaded with
`asyncio.to_thread` (L150-L156) so the daemon event loop stays responsive. One service per
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

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the active serving
  authority — per-app service, epoch verification per wire, atomic page+cursor assembly,
  pre-stream cursor checks, bounded projector LRU. Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
