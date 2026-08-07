# Active Conversation Projectors Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/projectors/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/projectors/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-08-07T23:35:00+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|

## What This Area Is

This route is the per-harness active projector slice: the pure frame
grammars that map each harness's native frames — live evidence frames and native-history page
frames — into normalized conversation mapping outputs for the engine in the sibling `active/`
route. Mappers are schema-strict and vendor-honest: every item type with exact field evidence
maps to a typed item, and every other shape becomes `unknown-vendor` evidence with its native
id/turn parent preserved and its raw payload kept server-side.

The slice is deliberately pure. Mappers hold no IO, no clock, no engine state; the engine
assigns ordinals, revisions, provenance resolution, envelopes, and unknown-vendor evidence
handles. One protocol (`HarnessProjector`) plus channel flags is the only engine-facing
surface, so the engine never special-cases a harness.

## Hot Path Summary

Start with `__init__.py` for the `HarnessProjector` protocol, channel flags, and registry.
`common.py` holds the strict parsing primitives, the four mapper output types, and the honest
provenance builders. `codex.py` maps thread items and notifications (items/blocks/tools/
deltas/turn results, plus the collab/sub-agent roster rows), `claude.py`
maps stream-json frames (text/thinking/tools/results, the exact submission echo, and the
`task_*` sub-agent lifecycle correlated by `parent_tool_use_id`), and
`pi.py` maps durable entries and live RPC events (messages/tools/
notices/outcomes anchored on native entry identity). Every mapper takes
the optional `parent_thread_id` demux context; only codex consumes it — claude's sub-agent
identity arrives in-band and pi has no sub-agent threads.

## What Belongs Here

| Path | Role |
| --- | --- |
| `__init__.py` | The engine-facing protocol, per-harness channel bindings, and the `PROJECTORS` registry. |
| `common.py` | Strict schema parsing, mapper output types, provenance builders. |
| `codex.py` | Codex thread items + notifications → items/blocks/tools/deltas/turn results. |
| `claude.py` | Claude stream-json frames → items/thinking/tools/results; exact submission echo. |
| `pi.py` | Pi durable entries → items/tools/notices/outcomes; live tool upserts. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Ordinals, revisions, retention, envelopes, cursor minting, gap mechanics | `mcp/src/agents_remember/serving/conversation/active/` (the engine route). |
| Strict wire grammar and provenance validation | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Native evidence emission and the IPC seam | `serving/harness_control_*.py` and the native adapters. |
| Dormant native list/read normalization | `mcp/src/agents_remember/serving/conversation/library/`. |

## Structures Found Here

- A `HarnessProjector` protocol with four channel flags (`uses_native_pages`,
  `uses_transcript_echo`, `eager_native_continuation`, `harness_id`) the engine reads to choose
  hydration, zipper, and continuation behavior.
- Parse-by-schema primitives (`required_object`/`required_list`/`required_text`) whose
  `UnmappableShape` failure becomes preserved unknown-vendor evidence at the engine — malformed
  known shapes never kill the stream and never guess semantics.
- Four frozen mapper output types: `MappedItem`, `MappedBlockDelta`, `MappedTurnOutcome`,
  `MappedUnknownVendor`.
- Stable native identity per harness: codex item ids (turn parent on `nativeParentId`), claude
  message uuids / `tool_use` ids / replay correlation uuids, pi durable entry ids and native
  `toolCallId`s. No content hashes, timestamps, or array indices anywhere.
- Split tool items (invocation first, result later) keyed by one stable id, converged by the
  store's block union; codex full-item re-maps are identical under union.
- Honest user-input provenance: `unknown-input` with request correlation where the harness
  carries one (codex `clientId`, claude echo request id), always unknown-input for pi (no native
  correlation exists); the engine's provenance batch resolves exact sources exactly once.
- Sub-agent mapping: codex `collabAgentToolCall`/`subAgentActivity` items
  and the agent-lifecycle notification methods upsert a shared `codex-agent-<threadId>` roster —
  never optimistic (the parent thread can never roster itself, `idle`/unknown statuses mint
  nothing, and an agent `turn/completed` mints an agent-bound turn-result but NEVER a
  parent-scoped `MappedTurnOutcome`); claude correlates `task_*` frames by `parent_tool_use_id`
  through a bounded binding registry, and off-shape collab/task frames degrade to preserved
  unknown-vendor evidence, never a stream kill. `thread/started` left the codex silent set:
  parent boot/resume silence now comes from `_map_thread_started`'s guards, not the drop table.

## Operating Model

1. The engine feeds a native-history page frame or a live evidence frame to the harness mapper
   with an opaque evidence ref.
2. The mapper parses the frame against its documented schema with exact required keys and emits
   mapping outputs; unrecognized shapes return `MappedUnknownVendor` with a safe summary.
3. Turn settlements emit `MappedTurnOutcome`, which the engine feeds to the canonical status
   service as exact terminal evidence.
4. Channels a harness does not have raise `NotImplementedError` through the bound protocol
   (claude native pages fail closed stream/replay-only; codex/pi have no echo channel).

## Main Flows

### Native history mapping (codex, pi)

1. Codex `thread/read` items map by type (user/agent message, plan, reasoning, command
   execution, file change, MCP tool call); turn results mint `turn-result` items plus outcomes.
2. Pi durable entries map by type (messages by role, compaction/model/thinking notices);
   assistant `toolCall` parts and `toolResult` messages converge on the native `toolCallId`.

### Live frame mapping

1. Codex notifications discriminate on the CARRIED native method first (the
   adapter carries `EvidenceFrame.native_method`), then params-key shape. `_SILENT_NOTIFICATION_METHODS`
   drops the known codex 0.144.5 startup/lifecycle/status/telemetry burst BY METHOD
   (`mcpServer/startupStatus/updated`, `thread/started`, `remoteControl/status/changed`, `warning`,
   `configWarning`) → zero unknown-vendor rows on a stock open; a truly-unknown method still becomes
   unknown-vendor WITH the method NAMED. Bare deltas resolve their target block through the item kind
   at the engine.
2. Claude assistant frames split text/thinking and mint stable-ID tool items; `tool_result`
   carriers upsert the same item; result frames classify terminal outcomes. The mapper learns
   the two installed-2.1.216 frame contracts first-class: `command_lifecycle` is strictly validated
   against the captured 3-state contract (`command_uuid` + `state ∈ {queued,started,completed}`) and
   mints NO timeline item (native history renders the command; the 3-state specimen is preserved as
   prior art for the later slash-command consumers), a drifted state raising `UnmappableShape` → a VISIBLE malformed
   row; `rate_limit_event` is shape-validated then dropped as telemetry (like codex rateLimits).
3. Pi `tool_execution_*` events upsert live tool items by `toolCallId`; `message_end`/
   `message_update` mint nothing — completed messages mint from durable entries.

### Claude submission echo

1. User submissions arrive through the adapter's exact submission echo (original text, exact
   request id, replay uuid), mapped to user items keyed by the replay uuid.
2. Replayed user frames on the evidence channel are refused here so no item is ever double-
   minted; the engine zips echoes and frames by strict turn order.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `__init__.py` | protocol/registry | The only engine-facing surface; a harness without a projector fails closed typed. | covered |
| `common.py` | shared primitives | One parsing/provenance home so the three mappers cannot drift apart. | covered |
| `codex.py` | codex grammar | Native identity, tool/diff blocks, deltas, and honest historical tool loss. | covered |
| `claude.py` | claude grammar | Stream-json mapping plus the exact submission echo; no native page exists. | covered |
| `pi.py` | pi grammar | Entry-anchored identity, live tool upserts, honest unknown-input users. | covered |

## Local Invariants And Traps

- A mapper never assigns ordinals/revisions/envelopes and never performs IO — purity is what
  makes rehydration byte-identical.
- Unknown shapes are preserved with native coordinates, never dropped and never guessed; raw
  payloads never reach public items.
- User-role items never gain a default producer; absent provenance records stay unknown-input.
- Claude replayed user frames must raise `UnmappableShape` here — the echo channel owns them.
- Pi live text is completion-anchored: no provisional identity is ever minted from an id-less
  `message_end` frame.
- Turn-result items mint only where a native settlement exists (codex/claude always; pi only
  for failed/aborted turns).
- Codex notification identity: the native notification METHOD is preserved end-to-end as
  typed `EvidenceFrame.native_method` and is the primary discriminator — the known lifecycle/status/
  telemetry burst is classified/dropped by method (never shape-guessed), and a truly-unknown method
  is NAMED in the unknown-vendor summary rather than one anonymous "unrecognized params" box. The
  drop-set is method-specific and item-less, so an item-bearing frame still reaches the shape branches.
- Claude frame contracts: `command_lifecycle` and `rate_limit_event` are recognized-first-
  class against their captured contracts (not tolerated strangers); `command_lifecycle` mints no
  timeline row and a drifted state surfaces VISIBLY as a malformed row, never a silent tolerance and
  never a stream kill.
- Codex's live notification channel and its `thread/read` native pages emit DISJOINT id namespaces
  for the SAME settled turn (live UUID/`msg_*` item ids vs positional `item-N`). The mapper faithfully
  emits both and correlates NO channels (purity), so the native-history twin can only arise on this
  codex hosted topology; the ENGINE, not the mapper, suppresses the twin of an already-live turn
  (review finding F1, in `active/projector.py`, keyed on the shared `turnId`/`clientId`). Pi shares one namespace
  across channels and claude has no native pages, so neither can produce the twin.

## Repo-Internal References

The engine route drives these mappers and owns everything stateful; the strict contract
validates every emitted product; the evidence substrate defines the frame products; the runtime
fixtures record which shapes are gate-observed. The mapper suite pins every grammar.

| Finding | Anchor | Source |
| --- | --- | --- |
| The engine consumes the mapper channel flags (`uses_native_pages`, `uses_transcript_echo`, `eager_native_continuation`) and converts `UnmappableShape` into preserved unknown-vendor evidence. | `uses_native_pages`; `uses_transcript_echo`; `eager_native_continuation`; `UnmappableShape` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:106-114; mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:148-200; mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py:64-75; mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py:165-178 |
| The store converges the split tool items these mappers emit. | `apply_item`; "tool-call"; `_union_blocks` | mcp/src/agents_remember/serving/conversation/active/store.py:161-249; mcp/src/agents_remember/serving/conversation/active/store.py:466-482 |
| The evidence/native frame products the mappers parse. | `EvidenceFrame`; `EvidencePage`; `NativeEvidenceFrame`; `NativeEvidencePage`; `SubmissionProvenance`; `SubmissionProvenanceBatch` | mcp/src/agents_remember/serving/harness_control_models.py:455-478; mcp/src/agents_remember/serving/harness_control_models.py:481-489; mcp/src/agents_remember/serving/harness_control_models.py:492-500; mcp/src/agents_remember/serving/harness_control_models.py:503-510; mcp/src/agents_remember/serving/harness_control_models.py:513-524; mcp/src/agents_remember/serving/harness_control_models.py:527-530 |
| The runtime fixtures record the observed (never enabling) shapes per harness. | "active-projector/items-events"; "substrate-evidence/native-page-thread-read" | mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:34-62 |
| The mapper suite pins identity, blocks, tools, provenance, and preservation for all three. | `CodexMapperTests`; `ClaudeMapperTests`; `PiMapperTests` | mcp/tests/test_conversation_active_projectors.py:84-404; mcp/tests/test_conversation_active_projectors.py:407-710; mcp/tests/test_conversation_active_projectors.py:713-901 |

## Cross-Repo References

No cross-repository implementation participates in this route. All three harnesses are local
subprocesses reached through this repository's own adapters.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. Each mapper names its schema
authority (the codex app-server v2 generated protocol, the locked claude stream-json fixtures,
the locked Pi RPC documentation); those are repository-owned and cited in the file sidecars.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this projector gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Protocol, channel bindings, registry. |
| `common.py` | [`common.py.md`](common.py.md) | covered | Strict parsing, output types, provenance builders. |
| `codex.py` | [`codex.py.md`](codex.py.md) | covered | Codex frame grammar. |
| `claude.py` | [`claude.py.md`](claude.py.md) | covered | Claude frame grammar + submission echo. |
| `pi.py` | [`pi.py.md`](pi.py.md) | covered | Pi entry/event grammar. |

## Child Overviews

None. The five modules form one coherent mapper slice; per-harness detail lives in the file
sidecars, not in nested overviews.

## How To Use This Area

Read this overview and the exact file sidecar first. Any grammar change requires the mapper
suite plus the engine suite (tool convergence pins), and belongs behind the fixture gate:
shapes without installed-runtime fixture evidence stay `unverified` in capabilities even when
they map correctly.

## Needs Verification

- Codex reasoning/diffs/MCP shapes and pi thinking/tool-execution shapes stay capability-`unverified`
  until installed-runtime fixtures observe them through the production seam. Claude's surface is now
  `unverified` for a NEVER-PROBED contract reason (the installed-vs-locked version
  gate was removed), not a version reason — the learned frame contracts map cleanly on installed
  2.1.216; promoting claude to `supported` needs a captured 2.1.216 runtime fixture.
- Reviewer F3: a stock pi 0.80.7 ordinary flow mints
  `pi:turn_start`/`pi:turn_end` unknown-vendor rows the pi mapper has never learned — the same
  fixture-drift class as the learned codex/claude frame contracts, on pi, to be taught in a follow-on.

## Claude Interaction-Shape And Mutation-Diff Route Impact

Claude projection now recognizes the native structured-interaction and interrupt frame shapes needed by the active/control contracts. Accepted interrupt correlation is required before an abort-style terminal result is classified as interrupted; other error evidence stays failed or unknown rather than being rewritten. Its stable mutation-diff facade now delegates Edit, MultiEdit, Write, and NotebookEdit to focused parsers over observed `tool_use.input`; malformed vendor shapes preserve raw input without inventing diffs, and MultiEdit identifiers retain original edit positions. Existing verification metadata remains pre-commit.

## Sub-Agent Mapping Route Impact

The mappers learned sub-agent frames: codex maps collab/roster items and agent-lifecycle
notification methods into a shared per-thread roster (never optimistic — the parent can never
roster itself, and an agent settlement never becomes a parent-scoped turn outcome), claude
correlates `task_*` lifecycle frames by `parent_tool_use_id` through a bounded binding
registry, and every mapper accepts the optional `parent_thread_id` demux context (only codex
consumes it; claude identity is in-band, pi has no sub-agent threads). `thread/started` left
the codex silent set — parent boot/resume silence is now guard-derived, not table-derived.
Mappers stay pure; malformed agent frames degrade to preserved unknown-vendor evidence, never
a stream kill.

## 260727-CHATS-IM-L2 Route Impact

Codex native-history mapping no longer treats persisted sub-agent spawn/start activity as proof of
current liveness. Those rows hydrate as `unknown` until adapter registry authority overlays
current status. Pure mapping, item identity, and unknown-vendor preservation remain unchanged.

## 260731-EFA-L2 — The Routers Are Flat, And "Well-Typed" Is A Value You Hold

This is the route where the complexity limits bit hardest: a frame router is naturally a long
`if type == …` chain, and both mappers had grown one. Neither was listed in a baseline — they were
split. **Purity, schema-strictness and the vendor-honest fallback are unchanged**, and no frame maps
differently than it did.

**Codex (`codex.py`).** The single notification router became a cascade of narrow routers —
`_map_codex_notification` → `_map_notification_params` → `_map_notification_item` /
`_map_item_scoped_notification` / `_map_block_delta` — and the item router split by *kind* into
`_map_thread_item`, `_map_prose_item`, `_map_tool_item` and `_map_collab_item`, each with per-type
leaves (`_user_message_item`, `_reasoning_item`, `_mcp_tool_call_item`, `_markdown_item`). Two
values carry what used to be threaded through every branch:

- **`ItemPlacement`** (`origin`, `live`, `turn_id`, `created_at`, `evidence_ref`) — where a mapped
  frame's items sit in the conversation, **before any item body is read**. It is the same for every
  item in the frame, which is why it arrives once instead of per item.
- **`_LiveItemContext`** — the same facts plus `item_id` and `phase`, i.e. what each individual
  item mapper needs about the frame besides the item body itself.

**`_CollabCall`** is the one to understand before touching the sub-agent path. It holds a
`collabAgentToolCall`'s three identity fields — which collab tool ran, which agent threads it
addressed, and what the item said about their states — **already proven well-typed**. Its purpose
is to keep the shape check in exactly one place: *a `_CollabCall` in hand means the item was the
documented collab shape*. `_collab_receiver_ids` returns `None` to mean "present but not the
documented list shape", which is how the honest-fallback path stays reachable. Do not construct a
`_CollabCall` outside `_collab_call_shape`; doing so would let an unchecked payload past the only
gate.

**Claude (`claude.py`).** The `task_*` sub-agent lifecycle split into `_resolve_task_identity`,
`_task_lifecycle_state`, `_task_usage_block`, `_task_lifecycle_blocks` and `_agent_identity_tag_item`,
with two schema assertions named as their own guards (`_require_command_lifecycle`,
`_require_rate_limit_event`) and `_require_task_usage` returning the usage mapping or `None`.

**`_TaskIdentity` carries a distinction the code previously kept only in local variable names**, and
it is the fact a future change is most likely to break: it holds `join_key`, `subagent_type`,
`description` **and** `retained_description`, because *what the replacing binding record keeps is
deliberately not always what the roster row displays*. Every field prefers the frame's own evidence
and falls back to what earlier `task_*` evidence already proved — a `task_notification` carries
neither `subagent_type` nor `description`, and its roster upsert **must not blank what `task_started`
filled in**. Nothing is guessed; absent evidence stays absent.

## 260731-EFA-L7 — Codex Projector Facade And R16

`projectors/codex.py` (1,223 → 704) is now a facade over `_codex_collab.py` (collab/roster/agent-thread/turn-completed mapping), with the full surface pinned by `mcp/tests/test_facade_surface.py`. The silent-notification set gained `turn/diff/updated` exactly (R16): it routes to the non-transcript state and mints zero unknown-vendor items, while genuinely unknown vendor methods still produce addressable unknown-vendor evidence; pinned by `test_conversation_projector_codex_agents_engine_1.py`/`_2.py`.

## Update History

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the codex facade split and the `turn/diff/updated` silent-method routing. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 5 table citations and normalized 6 source paths; no unresolved Tier-3 claims.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. The engine row
  was repointed off the deleted `active/projector.py` onto the package that replaced it: channel-flag
  consumption plus the `UnmappableShape` → `MappedUnknownVendor` conversion now reads at
  `projector/native_ingestion.py` L148-L200 and `projector/echo_ingestion.py` L64-L66, L165-L178, and
  the claim was reworded to name the three flags (`uses_native_pages`, `uses_transcript_echo`,
  `eager_native_continuation`) it actually consumes. The mapper suite row now spans L84-L901 (the three
  mapper test classes) in `test_conversation_active_projectors.py`, was L49-L553.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: both mappers' routers were split into narrow per-kind
  routers with per-type leaves, and the facts they threaded became values — `ItemPlacement` and
  `_LiveItemContext` (codex frame placement vs per-item context), `_CollabCall` (the single proof
  that an item matched the documented collab shape), `_TaskIdentity` (claude, preserving the
  displayed-vs-retained description distinction and the sparse-frame fallback rule). Purity,
  schema-strictness, the `unknown-vendor` fallback and every mapped output are unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: Codex persisted
  sub-agent activity now records historical existence without claiming current liveness;
  `registered`/`running` becomes `unknown` on native-history hydration until current adapter
  registry authority overlays status. Mapper purity and native item identity are unchanged.
  Verification metadata remains pinned until closeout.

- 2026-07-26T15:52 — 260718-CHATS-L7 curator: documented the sub-agent mapping grammars (codex
  roster/collab, claude `task_*` correlation, the `parent_thread_id` demux context, the
  `thread/started` silent-set change) in the Hot Path Summary and Structures list. Mappers stay
  pure; protocol surface unchanged apart from the additive keyword. Aggregate route-index
  generation remains manager-owned; verification metadata stays pinned (L7 uncommitted).
- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP curation: recorded the
  stable Claude mutation-diff facade, focused parser split, malformed-input
  preservation, and original-position MultiEdit identity. Verification metadata
  remains pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the half-time frame-contract truths.
  R1 (codex notification identity) — the native method is preserved as `EvidenceFrame.native_method`
  and is the primary discriminator; `_SILENT_NOTIFICATION_METHODS` drops the known 0.144.5 startup/
  status/telemetry burst by method (zero unknown-vendor rows on a stock open) and truly-unknown
  methods are NAMED. R3 (claude 2.1.216) — `command_lifecycle` (strict 3-state, mints no row, drift →
  visible malformed) and `rate_limit_event` (dropped telemetry) are learned first-class. Corrected the
  Needs-Verification claude line to the never-probed contract reason (L5F R4 removed the version gate)
  and recorded reviewer F3 (pi `turn_start`/`turn_end` unlearned rows) as a follow-on. Mappers stay
  pure. Verification stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: added the durable disjoint-id-namespace invariant
  (no mapper source changed) — codex's live notification channel emits UUID/`msg_*` ids while
  `thread/read` returns positional `item-N` for the same settled turn, so the native-history twin the
  engine's F1 filter suppresses can only arise on the codex hosted topology; the mappers stay pure and
  correlate no channels (pi shares one namespace, claude has no native pages). The suppression itself
  lives in `active/projector.py`, not here. Verification metadata stays pinned until L5 closeout
  stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the governing overview for the
  per-harness active projectors — the pure mapper protocol/registry, shared strict-parsing and
  provenance primitives, and the codex/claude/pi frame grammars with native identity and
  unknown-vendor preservation — after same-reviewer PASS-WITH-NOTES closed findings F1–F3.
  Verification is blank because the new source route is uncommitted; closeout owns its first
  source stamp.
