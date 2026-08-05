# mcp/src/agents_remember/serving/conversation/active/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

cit:([`ActiveConversationService`], mcp/src/agents_remember/serving/conversation/active/service.py:57-259) mints the
per-app cursor secret and owns page, subscription, and projector lifecycle. cit:([`page`, `_assemble_page`],
mcp/src/agents_remember/serving/conversation/active/service.py:78-99; mcp/src/agents_remember/serving/conversation/active/service.py:233-259)
resolves the authorized projector, decodes the optional `before` cursor, bounds the limit, and assembles the
`ConversationPage`. cit:([`subscribe`], mcp/src/agents_remember/serving/conversation/active/service.py:101-127)
cit:([`generation`], mcp/src/agents_remember/serving/conversation/active/cursor.py:256-256) checks cursor generation and
retention before attaching the subscriber queue and replay snapshot without an interleaving await.

cit:([`release_session`], mcp/src/agents_remember/serving/conversation/active/service.py:152-158)
cit:([`close`], mcp/src/agents_remember/serving/conversation/active/projector/facade.py:162-168) removes the projector
from the registry and LRU order and awaits its close. This is registry/projector release evidence; it does not
prove immediate deletion of every store item, live-turn/request id-set, or retained envelope.

cit:([`_projector_for`], mcp/src/agents_remember/serving/conversation/active/service.py:160-176) resolves and validates the
catalog entry, closes or replaces stale projectors, and bounds the registry. cit:(["asyncio.to_thread"],
mcp/src/agents_remember/serving/conversation/active/service.py:178-216) keeps blocking sync reads off the event loop;
the weak-key registry is maintained by the service's runtime lookup.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this service. | — | — |

## Repo-Internal References

The L0 runtime authority is the composition this service keys on; the cursor authority does the
signing/binding; the projector engine does hydration/polling; the routes call only this service.

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable app-scoped `ConversationRuntime` is the authority one service instance binds. | `ConversationRuntime` | mcp/src/agents_remember/serving/conversation/runtime.py:55-78 |
| The cursor authority's `decode_event_cursor` validates event-cursor generation. | `decode_event_cursor` | mcp/src/agents_remember/serving/conversation/active/cursor.py:248-262 |
| The rebuild coordinator captures the atomic page + event cursor under its apply lock. | `page` | mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:103-127 |
| The page route invokes this service and maps typed refusals to the serving status idiom. | `ConversationPage` | mcp/src/agents_remember/serving/conversation/active/api.py:126-155 |
| The SSE route invokes this service and maps typed refusals to the serving status idiom. | `StreamingResponse` | mcp/src/agents_remember/serving/conversation/active/api.py:215-247 |

## Cross-Repo References

No cross-repository implementation participates in this service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260727-CHATS-IM-L2 Selected-Child Service Delta

`hydrate_agent_history` resolves the same exact authorized session/projector and bridge epoch as
page/SSE, then delegates only the requested child id to cit:([`refresh_agent_native`], mcp/src/agents_remember/serving/conversation/active/service.py:138-153). The
service does not widen parent paging, invent child eligibility, or translate the local hydration
outcome; those contracts remain projector-owned.

## 260731-EFA-L2 Current Delta

The service now constructs one `ProjectedSession(identity=…, authorization=…, entry=…, mapper=…,
secret=self._secret)` and hands it to the projector facade, instead of passing the five as separate
keywords. The concept is WHICH conversation is being projected plus the authority to mint
references for it — see [projector/facade.py](projector/facade.py.md). No behaviour change here.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected cursor-generation and route citations,
  split projector release from broader cleanup claims, and bound lifecycle evidence to its source owners.

- 2026-07-31T18:05+02:00 — 260731-EFA-L2 curator: re-derived 4 stale self-citations (plus the three
  sub-citations riding the same sentences). The class head moved up 8 lines while
  `hydrate_agent_history` pushed the tail down: `ActiveConversationService` L65-L227→L57-L259,
  the cursor-secret line L71→L63, `page` L84-L105→L78-L99, `_assemble_page` L199-L227→L233-L259,
  `subscribe` L107-L136→L101-L127 with the no-await queue+replay capture L127-L136→L121-L127, and
  the two offloaded sync IPC reads (`current_bridge_epoch`, `live_snapshot`) L166-L173→L188-L191.
  No claim text changed; every range was read back.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `active/projector.py`
  no longer exists — it is now the `active/projector/` package, and the atomic page + event-cursor capture
  under the apply lock is `RebuildCoordinator.page` at `projector/rebuild_coordinator.py` L103-L127 (was
  `projector.py` L213-L234); both the link path and the range were repointed and read back.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ProjectedSession` call shape into the projector facade.
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
