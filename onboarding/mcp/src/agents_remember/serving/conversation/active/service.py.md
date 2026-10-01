# mcp/src/agents_remember/serving/conversation/active/service.py

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

cit:([`ActiveConversationService`], mcp/src/agents_remember/serving/conversation/active/service.py:57-259) mints the
per-app cursor secret and owns page, subscription, and projector lifecycle. cit:([`page`, `_assemble_page`],
mcp/src/agents_remember/serving/conversation/active/service.py:78-99; mcp/src/agents_remember/serving/conversation/active/service.py:233-259)
resolves the authorized projector, decodes the optional `before` cursor, bounds the limit, and assembles the
`ConversationPage`. cit:([`subscribe`], mcp/src/agents_remember/serving/conversation/active/service.py:101-127)
cit:(["generation = payload.get(\"generation\")"], mcp/src/agents_remember/serving/conversation/active/cursor.py:258-258) checks cursor generation and
retention before attaching the subscriber queue and replay snapshot without an interleaving await.

cit:([`release_session`], mcp/src/agents_remember/serving/conversation/active/service.py:163-169)
cit:([`close`], mcp/src/agents_remember/serving/conversation/active/projector/facade.py:162-168) removes the projector
from the registry and LRU order and awaits its close. This is registry/projector release evidence; it does not
prove immediate deletion of every store item, live-turn/request id-set, or retained envelope.

cit:([`_projector_for`], mcp/src/agents_remember/serving/conversation/active/service.py:160-176) resolves and validates the
catalog entry, closes or replaces stale projectors, and bounds the registry. cit:([`_projector_for_locked`],
mcp/src/agents_remember/serving/conversation/active/service.py:178-216) keeps blocking sync reads off the event loop —
since 260731-EFA-L16 the catalog resolution too: `_projector_for_locked` offloads
`resolve_running_entry` via `asyncio.to_thread` alongside the epoch/snapshot reads (a catalog
RLock wait on the loop thread was the event-loop seat of the 2026-08-05 deadlock). The weak-key
registry is maintained by the service's runtime lookup.

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

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The composition and wire contracts
are repository-owned and cited below.

No configured domain documentation was available for this service.

### Repo-Internal References

The L0 runtime authority is the composition this service keys on; the cursor authority does the
signing/binding; the projector engine does hydration/polling; the routes call only this service.

- The immutable app-scoped `ConversationRuntime` is the authority one service instance binds. [1]
- The cursor authority's `decode_event_cursor` validates event-cursor generation. [2]
- The rebuild coordinator captures the atomic page + event cursor under its apply lock. [3]
- The page route invokes this service and maps typed refusals to the serving status idiom. [4]
- The SSE route invokes this service and maps typed refusals to the serving status idiom. [5]

### Cross-Repo References

No cross-repository implementation participates in this service.

No meaningful cross-repo references found.

## 260727-CHATS-IM-L2 Selected-Child Service Delta

`hydrate_agent_history` resolves the same exact authorized session/projector and bridge epoch as
page/SSE, then delegates only the requested child id to cit:([`refresh_agent_native`], mcp/src/agents_remember/serving/conversation/active/service.py:155-155). The
service does not widen parent paging, invent child eligibility, or translate the local hydration
outcome; those contracts remain projector-owned.

## 260731-EFA-L2 Current Delta

The service now constructs one `ProjectedSession(identity=…, authorization=…, entry=…, mapper=…,
secret=self._secret)` and hands it to the projector facade, instead of passing the five as separate
keywords. The concept is WHICH conversation is being projected plus the authority to mint
references for it — see [projector/facade.py](projector/facade.py.md). No behaviour change here.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
