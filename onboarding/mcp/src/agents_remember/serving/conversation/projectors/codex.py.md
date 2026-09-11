# mcp/src/agents_remember/serving/conversation/projectors/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Codex active projector: maps app-server thread items (native `thread/read` pages) and live
notification frames into normalized items, blocks, deltas, and turn outcomes with stable native
identity — and preserves every unrecognized shape as `unknown-vendor` evidence instead of
guessing. Codex's documented historical tool loss stays visible through capabilities, never
hidden by a completeness claim. The notification's native METHOD is
carried on `frame.native_method` (previously stripped before the projector), so the codex 0.144.5
fresh-open lifecycle/status burst is recognized and dropped by method instead of flooding one
`unknown-vendor` row per MCP server, and a truly-unknown method is named rather than anonymous.
The projector is also sub-agent aware: the app-server auto-attaches
sub-agent thread listeners to the seat's connection, so one multiplexed evidence stream carries
many threads demuxed by `threadId`. Parent-thread `collabAgentToolCall` / `subAgentActivity`
items and non-parent lifecycle notifications (`thread/started`, `thread/status/changed`,
`turn/started`, `turn/completed`) map to a per-agent roster item (`codex-agent-<threadId>`)
upserted through the collab lifecycle, while an agent turn's completion mints an agent-bound
turn-result item but NEVER a `MappedTurnOutcome` — the canonical status service stays
parent-scoped.

## Code Commentary

### Logic

cit:([`map_native_frame`], mcp/src/agents_remember/serving/conversation/projectors/codex.py:129-142) parses one `thread/read` item frame and delegates to
`_map_thread_item`; turn parenting comes from the frame's `nativeParentId`. `map_evidence_frame`
discriminates live evidence by adapter event kind, then — for `codex-notification`
frames — by the native METHOD the adapter preserves on cit:([`native_method`], mcp/src/agents_remember/serving/conversation/projectors/codex.py:210-210) (the method
used to be dropped before the projector, so shapeless startup notices
flooded as one `unknown-vendor` row per configured MCP server). It also accepts the multiplexed
demux context cit:(["def __init__(self"], mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py:52-52), consulted only where parent-vs-agent
cannot be told from the frame alone (`thread/started`) — without it those frames keep the
pre-multiplexing silent behavior rather than guess. cit:([`_SILENT_NOTIFICATION_METHODS`], mcp/src/agents_remember/serving/conversation/projectors/codex.py:105-122) drops the
codex 0.144.5 session lifecycle/status/telemetry burst — one `mcpServer/startupStatus/updated`
per configured MCP server, `remoteControl/status/changed`, the `warning`/`configWarning`
advisory family, plus `account/rateLimits/updated` and `thread/tokenUsage/updated` — by method,
recognized and never re-guessed, so a stock codex open mints ZERO `unknown-vendor` rows
(`configWarning` was the recovery seat's live-observed addition, firing at open on setups with a
config note). Sub-agent multiplexing changed this set at both ends: `thread/settings/updated` was ADDED
(the parent occurrence rides the `state` kind; the agent-thread one crosses as a
`codex-notification` and is equally timeline-less), and `thread/started` was REMOVED — it is no
longer blanket-silent but mapped by `_map_thread_started`. Frames without a known drop method
fall through the schema-disjoint params-shape branches: `completed` frames map `turn/completed`
to a `turn-result` item plus `MappedTurnOutcome` (via `_map_turn_completed` (mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:557-598));
`transcript` frames carry full `item/completed` items; `state` frames feed canonical status only
and mint no items; item-bearing `startedAtMs` frames resolve item started/completed, indexed
deltas (`summaryIndex`/`contentIndex`) to their named blocks, bare deltas (agentMessage/plan/
commandExecution output share one shape) to an empty block id the engine resolves through the
item kind, `patchUpdated` change lists to diff-block tool items, and token-usage/rate-limit
frames to nothing (telemetry evidence, never token-theater rows). A method that matches no
drop and no shape becomes cit:(["class MappedUnknownVendor:"], mcp/src/agents_remember/serving/conversation/projectors/common.py:84-84) but NAMES the method
(`codex:notification:<method>` / `unrecognized codex notification <method>`), so a genuinely
novel notification stays visible AND identifiable rather than anonymous.

Sub-agent roster mapping cit:(["codex app-server thread/started (sub-agent registration)"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:413-413). The four agent-thread lifecycle methods are no longer four
branches inside `map_evidence_frame`: they are entries in the `_AGENT_THREAD_NOTIFICATIONS` dispatch
table cit:(["codex app-server thread/started (sub-agent registration)"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:413-413), consulted once by `_map_codex_notification` cit:([`native_method`], mcp/src/agents_remember/serving/conversation/projectors/codex.py:210-210) after the silent-method
drop and before the params-shape fallthrough. `thread/started` →
cit:(["codex app-server thread/started (sub-agent registration)"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:413-413) (parent occurrences and context-less frames stay silent; a
proven non-parent registers the agent), `thread/status/changed` → `_map_agent_thread_status`
(cit:(["codex app-server thread/status/changed (sub-agent)"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:458-458)), `turn/started` → cit:(["def _map_agent_turn_started("], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:467-467), and `turn/completed` →
cit:(["def _map_agent_turn_completed(  # pragma: no cover"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:488-488), which mints a roster terminal status plus an
agent-bound `turn-result:{turnId}` item (carrying a `ConversationAgentRef`) but NEVER a
`MappedTurnOutcome`. cit:(["def _agent_notification_thread_id("], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:421-421) is the defense-in-depth guard:
the adapter already emits these methods as `codex-notification` only for non-parent threads, and
the `parent_thread_id` comparison ensures a parent occurrence could never mint a roster row for
the seat itself. On the item side, cit:([`_map_thread_item`], mcp/src/agents_remember/serving/conversation/projectors/codex.py:337-373) gained two collab types:
`collabAgentToolCall` → cit:(["def _map_collab_tool_call("], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:311-311) emits the collab call itself as a
parent-timeline tool-call item — tagged with a `ConversationAgentRef` only when it belongs to
exactly one receiver (`sendInput`/`resumeAgent`/`wait`/`closeAgent`); a `spawnAgent` call is the
parent's own act and stays untagged — plus one roster upsert per involved agent
(`receiverThreadIds` union `agentsStates` keys, with the agent's final message as a
`final-message` text block when the collab state carries one); `subAgentActivity` →
cit:(["def _map_sub_agent_activity("], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:356-356) upserts the same roster row, binding `agentPath`. Both
return `None` for off-shape items, which falls through to `MappedUnknownVendor` — degrade,
never fatal. cit:(["def _roster_item("], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:103-103) mints the shared `codex-agent-<threadId>` notice row
with a status-derived phase cit:(["_ROSTER_ITEM_PHASE: dict[ConversationAgentStatus"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:86-86); cit:(["\"errored\": \"failed\","], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:81-81) is the probe-locked collab/`subAgentActivity.kind` vocabulary — anything outside the
table stays honest `unknown` instead of a guess; cit:(["_THREAD_STATUS_ROSTER: dict[str"], mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:97-97) admits only
`active`→running and `systemError`→failed, because `idle` says only "no active turn" and mints
nothing rather than regressing a richer collab-derived roster status. `_map_thread_item` keys
every other item on its native `id` and maps `userMessage` (content parts to
text/file-reference/unknown blocks, `clientId` to request correlation, unknown-input
provenance), `agentMessage`/`plan` (markdown), `reasoning` (summary/content to thinking blocks),
`commandExecution` (tool input command + aggregated output, phase from native status via
`_tool_phase` L1206-L1215), `fileChange` (diff blocks), and `mcpToolCall` (input arguments +
result/error output). Every other item type returns `MappedUnknownVendor` with the native id and
turn preserved.

### Conventions

Parse by schema, never heuristic: exact required keys per shape; anything unrecognized becomes
unknown-vendor evidence with an opaque coordinate evidence handle — raw payloads never reach a
public item. Mappers are pure; the engine assigns ordinals, revisions, and provenance resolution.
Collab sub-agent mappers signal "not the documented shape" by returning `None` (never by
raising), so a malformed `collabAgentToolCall`/`subAgentActivity` degrades to `unknown-vendor`
evidence instead of breaking the mapping; roster status vocabularies are
lookup tables whose miss value is the honest `unknown`, not a nearest-match guess.

### Invariants And Boundaries

- Item identity is the native item id (turn parent on `nativeParentId`); never a content hash,
  timestamp, or array index. The one deliberate addition is the synthetic roster id
  `codex-agent-<threadId>`, keyed on the native agent thread id, upserted
  across the collab/lifecycle evidence stream.
- User messages mint with `unknown-input` provenance plus `clientId` correlation; the engine's
  provenance batch resolves the real producer.
- Full-item re-maps are idempotent under the store's tool-call block union (review F1 pin).
- Historical tool loss is a capability claim (`history.toolCompleteness=partial`), never patched
  over by invented tool detail.
- The startup/status/telemetry drop is keyed on the native method (`frame.native_method` against
  `_SILENT_NOTIFICATION_METHODS`), never on params shape — the drop-set is method-specific and
  item-less, so an item-bearing frame under any of those methods still reaches the shape branches
  and maps. A truly-unknown method never falls silently: it becomes `unknown-vendor` evidence with
  the method named in `vendor_type`/`safe_summary`.
- The roster is never optimistic: every upsert derives from one concrete piece
  of collab or lifecycle evidence, and identity fields (`agentPath`, status) carry only what that
  evidence — or a prior bound upsert — proved. `thread/started` without a `parent_thread_id`
  demux context keeps the pre-multiplexing silent behavior rather than guessing parent-ness from an
  ambiguous params shape.
- Parent-vs-agent is fail-closed: agent lifecycle notifications mint roster
  rows only for a thread id that is present AND differs from `parent_thread_id`
  (`_agent_notification_thread_id` is defense-in-depth behind the adapter's non-parent-only
  emission), so the seat's own thread can never appear on its own roster.
- An agent turn's completion NEVER mints a `MappedTurnOutcome`: the engine's
  pending-terminal slot and the canonical status service are parent-scoped, so a settling agent
  turn must not settle the parent conversation; only the parent `completed`-kind frame
  (`_map_turn_completed`) produces a turn outcome.
- Ambiguous status mints nothing: `thread/status/changed` type `idle` (or any
  undocumented type) is dropped rather than allowed to regress a richer collab-derived roster
  status; an undocumented agent `turn/completed` status raises `UnmappableShape` (engine-side it
  becomes preserved unknown-vendor evidence, never a guessed terminal state).

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authority named by the
module is the codex app-server v2 generated protocol plus the landed installed-runtime fixture
rows, both repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The generated v2 protocol types and the codex adapter's evidence emission are the frame
authorities; the installed-runtime fixture records which shapes are gate-observed; the engine
resolves bare-delta targets and provenance. The sub-agent mapping adds the roster grammar
(`ConversationAgentRef`/`ConversationAgentStatus` on the shared models), the multiplexed demux
seam (the engine passes the projection's vendor conversation id as `parent_thread_id`), the
store's roster-aware upsert rules, and a dedicated collab/engine test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The codex adapter sets `AR_EVIDENCE_METHOD_KEY: method` on the `codex-notification` emit so the method reaches this projector (the method-carry seam), and the same emit routes its params through the thread registry's router. | `route_delta_params` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:776-776 |
| The router itself moved out of the adapter in 260731-EFA-L6 and was renamed with it, so the adapter-private name is gone from the tree. | `route_delta_params` | mcp/src/agents_remember/serving/codex_app_server_threads.py:215-229 |
| `EvidenceFrame.native_method` is the typed field the bridge preserves and this projector switches on; `evidence_frame_json` serializes it as `nativeMethod` (wire contracts in models since L9). | "payload[\"nativeMethod\"]" | mcp/src/agents_remember/models/conversations/evidence.py:158-158 |
| `ConversationAgentRef`/`ConversationAgentStatus` are the roster identity/status grammar this projector emits; `ConversationItem.agent` is the optional field that carries it (absent = parent conversation). | `parent_agent_id` | mcp/src/agents_remember/models/conversations/content.py:156-156 |
| The engine passes the multiplexed demux context: the one mapper call site sets `parent_thread_id=self._identity.vendor_conversation_id` on `map_evidence_frame`. | `map_evidence_frame` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:159-200 |
| Historical evidence (retired with the d3610903 suite reduction): The codex fixture rows recorded the observed live item/notification shapes and native thread pages through the production seam. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |
| The store's tool-call block union keeps full-item re-maps byte-identical while converging partial-block tools; roster-aware rules preserve a roster notice's `final-message` block across later block-less lifecycle upserts, and a late `streaming` tagging upsert never regresses a terminal phase. | `apply_item` | mcp/src/agents_remember/serving/conversation/active/store.py:161-249 |
| The engine resolves bare-delta target blocks through the mapped item's kind. | `apply_delta` | mcp/src/agents_remember/serving/conversation/active/store.py:251-273 |


## Cross-Repo References

No cross-repository implementation participates in this mapper; the Codex app-server is a local
subprocess reached through this repository's own adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260727-CHATS-IM-L2 Current Delta

A persisted `subAgentActivity` spawn/start row proves historical existence but not present
liveness. Native-history mapping therefore emits `unknown` for registered/running historical
states; current adapter registry authority may overlay a live status during hydration.

## 260731-EFA-L2 Current Delta

The codex mapper was decomposed into a named router plus per-family item mappers, and three
concepts were introduced:

- **`ItemPlacement`** (`origin`, `live`, `turn_id`, `created_at`, `evidence_ref`) — where a mapped
  frame's items sit in the conversation, **before any item body is read**. It is the same for every
  item in the frame, which is why it arrives once instead of per item.
- **`_LiveItemContext`** (`item_id`, `origin`, `live`, `turn_id`, `created_at`, `phase`,
  `evidence_ref`) — what every item mapper needs about the frame besides the item body, so each
  type's mapper takes the item and this instead of seven positional facts threaded through every
  branch.
- **`_CollabCall`** (`tool`, `receiver_ids`, `agents_states`) — one `collabAgentToolCall` item's
  identity fields, **already proven well-typed**. Holding a `_CollabCall` means the item *was* the
  documented collab shape; `_collab_call_shape` is the one place that judgement is made.

Routing is now explicit: `_map_codex_notification` routes by native method first, then by params
shape; `_map_notification_params` discriminates by the schema-disjoint required keys of its params;
`_map_notification_item` maps a live item body (`startedAtMs` is what tells started from
completed); `_map_item_scoped_notification` handles a notification naming an existing item with no
body; `_map_block_delta` routes a text delta to the block it extends. Items are mapped by family:
`_map_prose_item` (the item types that are somebody's words — prompt, reply, plan, reasoning),
`_map_tool_item` (the agent acting on the world — shell, edits, MCP calls), `_map_collab_item` (the
parent-thread items that model the collaboration itself, minting roster rows), under
`_map_thread_item`, which still **preserves an unrecognized type rather than guessing it**.

Collab helpers are individually named: `_collab_receiver_ids` (`None` = present but not the
documented list shape), `_collab_call_input_block`, `_collab_call_agent` (the owning agent when
exactly one owns it), `_collab_roster_ids` (receivers union `agentsStates` keys — every agent the
item is evidence about) and `_collab_roster_upserts`. `_map_collab_tool_call` returns `None` for a
non-documented collab shape.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: now a facade over `_codex_collab.py`; the silent-notification set gained `turn/diff/updated` exactly (R16) while genuinely unknown vendor methods still mint addressable unknown-vendor evidence. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T21:21:38+02:00 — 260731-EFA-L6 curator W2-B10: repaired 24 citation findings (7 reference rows and 10 prose pointers); scoped recheck clean.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 6 stale self-citations in the sub-agent
  roster paragraph and rewrote the routing claim that was no longer true. The four agent-thread
  lifecycle methods are NOT four branches in `map_evidence_frame` any more: notification routing was
  extracted into `_map_codex_notification`, which looks the method up in the
  `_AGENT_THREAD_NOTIFICATIONS` dispatch table — so the "four new method
  branches" sentence was replaced with the table + router it actually is. The roster helpers all
  moved down: `_roster_item` L663-L699 → L722-L753, `_map_collab_tool_call` L731-L834 → L926-L968,
  `_map_sub_agent_activity` L837-L860 → L971-L999, `_agent_notification_thread_id` L894-L907 →
  L1035-L1048, `_map_agent_turn_started` L938-L955 → L1079-L1096, `_map_agent_turn_completed`
  L958-L1007 → L1099-L1150; the paragraph's opening span is L722-L1164, and the two co-cited
  neighbours in the same sentence were re-read as well (`_map_thread_started` L1002-L1032,
  `_map_agent_thread_status` L1051-L1076). The `MappedUnknownVendor` fall-through citation
  was verified as still exact and left alone; the top-of-file tables
  (`_SILENT_NOTIFICATION_METHODS` L83-L93, `_COLLAB_AGENT_STATUS` L101-L113, `_ROSTER_ITEM_PHASE`
  L115-L121, `_THREAD_STATUS_ROSTER` L126-L129) did not move. Behaviour claims re-verified against
  the source, including `_collab_call_agent`'s single-receiver / never-`spawnAgent` tagging rule.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations, one of them
  a repointed path. The adapter method-carry row cited L630-L638; L713-L721, neither of which
  contained the seam even at the pinned commit (they were exception handling and an
  `_emit_notification` call site); it now cites L845-L861 (`_emit_notification`, which sets
  `AR_EVIDENCE_METHOD_KEY: method`) and L1369-L1383 (`_route_delta_params`), and the claim's "a
  second emit" was corrected — the same emit routes its params, there is no second one. The demux
  row pointed at `serving/conversation/active/projector.py`, which no longer exists: that module is
  now the package `active/projector/`, and the single mapper call site carrying
  `parent_thread_id=self._identity.vendor_conversation_id` is `native_ingestion.py` L182-L186, so
  both link path and range were repointed.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ItemPlacement`, `_LiveItemContext`, `_CollabCall` and the named notification/item/collab routers; preserve-not-guess behaviour unchanged.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: persisted
  `subAgentActivity` spawn/start rows now hydrate with `unknown` liveness unless current adapter
  registry authority overlays a live status. Historical existence can no longer reopen a
  completed child. Verification metadata remains pinned until closeout.

- 2026-07-26T15:34 — 260718-CHATS-L7 curator: R2 sub-agent roster mapping — the projector gained
  the multiplexed demux context (`parent_thread_id` on `map_evidence_frame`), four agent-thread
  lifecycle method branches (`thread/started`, `thread/status/changed`, `turn/started`,
  `turn/completed`), collab item types (`collabAgentToolCall`, `subAgentActivity`) mapping to a
  shared `codex-agent-<threadId>` roster row, and `thread/settings/updated` joined the silent
  set while `thread/started` left it (now mapped, parent-silent). Corrected the now-false L5F
  claim that `thread/started` is blanket-dropped by `_SILENT_NOTIFICATION_METHODS`; refreshed
  every shifted def/citation line range; added L7 invariants (roster never optimistic,
  parent-only turn outcomes, fail-closed parent-vs-agent guard, degrade-not-fatal collab
  fall-through, `idle` mints nothing) and new repo-internal citations (models
  `ConversationAgentRef`, engine demux seam, store roster-aware upsert rules, the L7 collab test
  module). Verification metadata stays pinned: the L7 change is uncommitted, so no commit hash
  can attest it yet.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — corrected the now-false "method never
  crosses" claim: `map_evidence_frame` discriminates `codex-notification` frames on the carried
  `frame.native_method` first, `_SILENT_NOTIFICATION_METHODS` drops the codex 0.144.5 startup/
  status/telemetry burst (incl. the live-observed `configWarning`) by method so a stock open mints
  zero unknown-vendor rows, and a truly-unknown method is now NAMED in the unknown-vendor fallback;
  refreshed the shifted def line ranges and added the adapter method-carry + `native_method`
  citations. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the codex active
  projector — thread-item/notification mapping, schema-disjoint live discrimination, native
  identity, unknown-vendor preservation, honest historical tool loss. Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
