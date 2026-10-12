# Active Conversation Projectors Route Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/projectors/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/projectors/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |

## What This Area Is

This route maps harness-native frames into normalized conversation outputs for the sibling active engine. Codex and Pi provide native-history frames and live evidence; Claude provides stream-json evidence and exact submission echoes; eve provides its durable session stream. The engine-facing protocol binds these channels to the registered projectors.

The standing design is schema-strict, vendor-honest mapping: recognize evidenced shapes, preserve unsupported shapes as unknown-vendor evidence, and leave source acquisition, canonical ordinals and revisions, provenance resolution, envelopes, and evidence handles to the engine. The existing purity promise is not fully realized: Claude keeps a bounded, module-level sub-agent binding registry. Construction and boundaries below describe that state explicitly rather than certifying the entire slice as stateless.

## Hot Path Summary

Start with `__init__.py` for the protocol, channel bindings, and registry, then `common.py` for parsing primitives, output types, and provenance builders. `codex.py` routes items, notifications, and deltas; `_codex_collab.py` owns its collaboration, roster, agent-thread, and settlement mapping. `claude.py` maps assistant/tool/result frames, submission echoes, and correlated sub-agent lifecycle evidence. `pi.py` maps durable entries and live tool events. `eve.py` maps durable stream envelopes, revises streamed text by channel identity, and separates turn settlements from session parking.

Every live mapper accepts optional parent-thread demux context. Only Codex consumes that argument; Claude reads sidechain identity in-band, and Pi and eve leave it unused.

## Construction And Mapping Flow

### Protocol And Shared Values

The protocol exposes native-frame, live-evidence, and transcript-echo mapping methods. Its bindings declare a harness identity and three boolean channel/continuation flags. Codex uses native pages without eager continuation; Pi uses native pages with eager continuation; Claude uses transcript echoes without native pages; eve uses neither auxiliary channel. Unsupported channels raise `NotImplementedError`.

The shared outputs are four frozen dataclasses: mapped items, block deltas, terminal outcomes, and unknown-vendor descriptions. Required-object, required-list, and required-text parsers raise `UnmappableShape` when their checks fail. The engine catches that exception at its ingestion boundary and constructs preserved malformed evidence rather than terminating projection for that parsing failure.

Items carry placeholder ordinal and revision values; the store assigns canonical values. Tool invocations and later results use the same item identity and converge through block union. Candidate blocks replace matching block IDs while existing sibling blocks survive; late streaming tool upserts do not regress terminal phases. Codex full-item re-maps use the same convergence path.

User-input attribution remains evidence-based. Codex user messages carry request correlation when `clientId` exists; Claude echoes carry their request ID and replay correlation UUID; Pi user messages and eve delivered operator records carry producer-less unknown-input provenance. Claude sidechain user frames are a distinct case: they map as harness-lane records of the sub-agent input. The engine resolves pending request provenance from the submission-provenance batch.

### Codex Items And Notifications

Native frames preserve the item's own ID and the native turn parent. The item router tries prose, tool, and collaboration routers in order. It maps user and agent messages, plans, reasoning, command execution, file changes, and MCP tool calls; an unclaimed item type becomes unknown-vendor evidence.

The notification cascade routes by carried native method first, then by params shape. Known silent methods include startup status, remote-control status, warnings, rate limits, token usage, thread settings, and `turn/diff/updated`. `thread/started` is not in this silent set: its dedicated handler suppresses missing, unproven, and parent-thread identities and registers a proven non-parent thread. The silent-method check occurs before item-shape routing, so the implementation does not promise that an item-bearing payload overrides a silent method. Unknown methods with recognized item or item-scoped params may still reach those shape branches; the final unknown-notification branch names the carried method.

Full item notifications establish placement and phase before mapping their body. Item-scoped notifications map deltas or file-change updates; other item-scoped shapes mint nothing there. Summary and content indices identify delta blocks; bare deltas leave block selection to the engine.

The facade imports collaboration helpers from `_codex_collab.py`. `ItemPlacement` carries frame-wide origin, live/history placement, turn, time, and evidence reference; `_LiveItemContext` adds item identity and phase. `_CollabCall` carries validated tool, receiver IDs, and agent-state fields. Its shape constructor is the intended validation boundary; a receiver field of the wrong container type returns no validated call and keeps unknown-vendor preservation reachable.

Collaboration items emit the tool call and roster upserts keyed by `codex-agent-<threadId>`. Non-parent lifecycle notifications update that roster; idle or undocumented thread-status types emit no transition. Agent turn completion emits an agent-bound turn-result and roster terminal status, never a parent-scoped mapped terminal outcome. Malformed collaboration shapes are preserved instead of acquiring invented agent semantics.

Persisted spawn/start activity must not by itself establish current liveness. The source implements this downgrade for native-history `subAgentActivity` registered/running states, and the engine can overlay current adapter-registry authority. The broader standing claim also covers persisted collaboration spawn/start activity, but `_collab_roster_upserts` still promotes an unknown spawn receiver to registered without a live/history guard. That discrepancy remains explicit.

The engine, rather than the mapper, suppresses native-history twins using recorded live turn IDs and user request IDs. The earlier account of live UUID/message IDs versus positional `item-N` IDs describes an observed topology, not a current universal parser rule: native acquisition requires the returned item IDs and does not manufacture positional identities.

### Claude Frames, Echoes, And Sub-Agents

Assistant frames map text and thinking blocks and split stable-ID tool-use items from their parent message. Tool-result carriers upsert the same tool IDs. Replayed user frames raise `UnmappableShape` because exact submission echoes own those parent user items. An echo uses its replay correlation UUID as item identity, original submission text as content, and request ID as correlation. The engine places echoes and evidence through its turn-order zipper.

Command-lifecycle frames require a command UUID and a state of queued, started, or completed; valid frames mint no timeline item. An undocumented state fails parsing and becomes visible malformed evidence at ingestion. Rate-limit frames require an object-valued rate-limit payload and then mint no timeline item.

Claude maps task-started, task-progress, task-notification, and background-task reconciliation system frames. It correlates task IDs and tool-use join keys in a registry bounded to 128 session buckets and 64 bindings per bucket, evicting oldest entries when limits are reached. Frames without a session ID share the empty-string bucket. This is retained mapper state, not an engine-owned stateless calculation.

The lifecycle path reads the previous binding, resolves identity, validates usage, decides status, records the replacement binding, and emits items. `_TaskIdentity` distinguishes the description displayed on the roster from the description retained in the binding: a progress label can be transient, while a sparse later notification keeps the previously evidenced task description and type. Absent evidence stays absent. Malformed task lifecycle shapes become unknown-vendor outputs locally; unrelated system subtypes currently mint nothing.

Edit, MultiEdit, Write, and NotebookEdit inputs delegate to focused mutation-diff parsers. Invalid or unsupported input shapes contribute no synthetic diff while the tool-input block keeps the raw input. MultiEdit diff IDs retain the original edit positions. Write and NotebookEdit expose the supplied new content without fabricating an unseen old file state.

Result classification first consumes the adapter-attributed terminal stamp when present. A cancelled stamp becomes interrupted; unstamped results use native success and cancellation-reason predicates, with other results classified failed. The adapter-correlation design distinguishes an accepted interrupt from an ordinary error, but the mapper itself also accepts native cancellation reasons on unstamped evidence; the original absolute requirement for accepted-interrupt correlation therefore needs this qualification. Result frames emit both a turn-result item and terminal evidence.

### Pi Durable Entries And Live Events

Durable message entries map by role; compaction and model/thinking changes map notices. Other entry types remain unknown-vendor evidence. Assistant tool-call parts and tool-result messages converge on their native tool-call identity. User messages stay unknown-input because this mapper receives no native request correlation.

Live tool-start, update, and end events upsert tool items by `toolCallId`. Message-end, message-update, and agent-end events mint nothing in this mapper; completed message identity comes from durable entries. Completed assistant stop reasons emit completed terminal evidence, while aborted and error reasons additionally emit turn-result items. The live fallback still maps unrecognized event types, including `turn_start` and `turn_end`, to unknown-vendor descriptions; this source observation does not establish an installed runtime version or fixture execution.

### Eve Durable Stream

Eve reads the event type from the diverted envelope's own `type` field and payload from `data`, rather than using the out-of-band native-method field. Named control events for session/turn/step framing, action-input streaming, compaction, and context clearing mint nothing. Unclassified event names become preserved unknown-vendor evidence.

Appended message or reasoning frames emit an empty channel item plus a block delta. Completion revises that same turn/channel item to authoritative text; intentional null completion stays empty. Tool requests and results converge by native call ID. Input requests, resolutions, authorization challenges and completions, and failed steps have dedicated mappings.

A turn boundary is not a session boundary. Turn completion, cancellation, and failure pass through `_settled`, emitting a turn-result item and terminal outcome; cancellation becomes interrupted. Session waiting produces one stable session-scoped parked notice with no turn ID and no terminal outcome, so it cannot overwrite a cancelled turn with a completed park. The adapter does report that park as completed, which makes this mapper distinction necessary.

The former claim that `_settled` is the only terminal-outcome constructor and is reached only by turn events is not the current implementation. Session completion directly emits a mapped terminal outcome, and session failure also calls `_settled`. The standing separation between turn and session boundaries remains; the prose does not certify the additional session outcomes as satisfying a turn-only settlement promise. Eve exposes no native-history page or transcript-echo channel; durable replay belongs to the adapter's stream route.

## Invariants And Boundaries

The standing purity rule says mapping owns no IO, clock, or engine state, and does not assign canonical ordinals, revisions, or envelopes. Preserve that intent while recognizing the Claude binding registry as an actual exception to stateless mapping. Source inspection alone does not prove byte-identical rehydration across registry histories.

Unknown-vendor handling must not guess semantics or publish raw payloads as unknown-vendor item bodies. Public unknown-vendor items contain summaries and opaque evidence references. Native-page parsing failures preserve transport item and parent identity; live parsing failures use engine-generated identity and may have no turn parent. Recognized silent events and several recognized non-content branches deliberately mint nothing, so the blanket promise that every other shape is preserved is too broad.

Native identity anchors items where available. Block IDs may use array positions, and unknown live events or eve delivered messages may use evidence sequence coordinates. The intended ban on manufactured content-hash or timestamp identity is distinct from an inaccurate ban on all indices or sequence-based identity.

Parent user-input records do not acquire an assumed producer. Missing provenance remains unknown-input; the engine owns subsequent exact source resolution. Claude replayed parent user frames belong to the echo channel. Pi does not invent provisional text-message identity from id-less live message frames.

Canonical ordinals, revisions, retention, envelopes, cursors, and gap mechanics belong to the active engine and store. Wire contracts live under `models/conversations/`; evidence acquisition belongs to the harness adapters and bridge; dormant native list/read normalization belongs to `conversation/library/`; projection readers live under `serving/projections/`.

## How To Use This Area

Read this overview and the relevant file card before changing grammar. The standing verification intent requires mapper and engine coverage for parsing and tool convergence and requires production-seam fixture evidence before capability promotion. This card does not assert that the former suites still exist, that any tests were executed, or that inspected code is qualified CODE evidence.

The capability owner still declares Codex reasoning/tools/diffs and Pi thinking/tool execution unverified, and declares Claude's surface unverified for a never-probed contract reason rather than a version-comparison reason. Those declarations are source facts, not independent confirmation of fixture qualification. No lifecycle authority was supplied for the retained pre-commit metadata or historical verification notes below.

## Retained Non-Operative Metadata

The following tables and historical status statements are preserved metadata. Their status cells and historical observations do not establish current coverage, acceptance, execution, or lifecycle state.

### What Belongs Here

| Path | Role |
| --- | --- |
| `__init__.py` | The engine-facing protocol, per-harness channel bindings, and the `PROJECTORS` registry. |
| `common.py` | Strict schema parsing, mapper output types, provenance builders. |
| `codex.py` | Codex thread items + notifications → items/blocks/tools/deltas/turn results. |
| `claude.py` | Claude stream-json frames → items/thinking/tools/results; exact submission echo. |
| `pi.py` | Pi durable entries → items/tools/notices/outcomes; live tool upserts. |
| `eve.py` | eve durable session stream → items/blocks/deltas/turn outcomes; the park is a notice. |

### What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Ordinals, revisions, retention, envelopes, cursor minting, gap mechanics | `mcp/src/agents_remember/serving/conversation/active/` (the engine route). |
| Strict wire grammar and provenance validation | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Native evidence emission and the IPC seam | `serving/harness_control_*.py` and the native adapters. |
| Dormant native list/read normalization | `mcp/src/agents_remember/serving/conversation/library/`. |

The retained contract-path row is historical; the operative contract location is `models/conversations/`, as stated above.

### Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `__init__.py` | protocol/registry | The only engine-facing surface; a harness without a projector fails closed typed. | covered |
| `common.py` | shared primitives | One parsing/provenance home so the four mappers cannot drift apart. | covered |
| `codex.py` | codex grammar | Native identity, tool/diff blocks, deltas, and honest historical tool loss. | covered |
| `claude.py` | claude grammar | Stream-json mapping plus the exact submission echo; no native page exists. | covered |
| `pi.py` | pi grammar | Entry-anchored identity, live tool upserts, honest unknown-input users. | covered |
| `eve.py` | eve grammar | Durable-stream mapping; one settlement per turn and the park is never one. | covered |

### File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Protocol, channel bindings, registry. |
| `common.py` | [`common.py.md`](common.py.md) | covered | Strict parsing, output types, provenance builders. |
| `codex.py` | [`codex.py.md`](codex.py.md) | covered | Codex frame grammar. |
| `claude.py` | [`claude.py.md`](claude.py.md) | covered | Claude frame grammar + submission echo. |
| `pi.py` | [`pi.py.md`](pi.py.md) | covered | Pi entry/event grammar. |
| `eve.py` | [`eve.py.md`](eve.py.md) | covered | eve durable-stream grammar; the park is a notice. |

### Historical Verification Notes

Historical evidence (retired with the d3610903 suite reduction): The runtime fixtures recorded the observed (never enabling) shapes per harness. These removed artifacts provide no current execution or capability-enablement proof.

Existing verification metadata remains pre-commit.

- Codex reasoning/diffs/MCP shapes and pi thinking/tool-execution shapes stay capability-`unverified`
  until installed-runtime fixtures observe them through the production seam. Claude's surface is now
  `unverified` for a NEVER-PROBED contract reason (the installed-vs-locked version
  gate was removed), not a version reason — the learned frame contracts map cleanly on installed
  2.1.216; promoting claude to `supported` needs a captured 2.1.216 runtime fixture.
- Reviewer F3: a stock pi 0.80.7 ordinary flow mints
  `pi:turn_start`/`pi:turn_end` unknown-vendor rows the pi mapper has never learned — the same
  fixture-drift class as the learned codex/claude frame contracts, on pi, to be taught in a follow-on.

The earlier facade and engine-suite references describe historical verification, including retired suites; they do not certify present execution. The old line-count comparison and unchanged-behavior assertions describe refactor history rather than guarantees of the present source. No current lifecycle disposition is inferred from these notes.

### Child Overviews

None are identified by the assigned overview. Per-harness detail belongs in file cards; `_codex_collab.py` is an additional current source owner alongside the six modules listed in the retained tables.

## Evidence

- The engine consumes mapper channel flags and converts parsing failures into unknown-vendor evidence. [1]
- The store converges split tool items by scoped block union. [2]
- Evidence/native frame products and submission-provenance products define the inputs used by this route. [3]
- Protocol bindings expose four registered projectors, three boolean flags, and fail-closed unsupported channels. [4]
- Shared mapping outputs, schema checks, and producer-less input provenance leave canonical projection work to the engine. [5]
- Codex uses method-first notification routing and shape-based item routing; its silent-method branch precedes item branches. [6]
- Codex collaboration validates shared identity fields, guards parent lifecycle notifications, keeps agent settlements parent-independent, and exposes the historical spawn-status discrepancy. [7]
- Claude owns a bounded binding registry, correlated task mapping, strict silent-frame contracts, exact echoes, mutation-diff parsers, and stamped/native result classification. [8]
- Pi uses durable entry identities and native tool-call IDs, delays live message mapping, and preserves unrecognized live events. [9]
- Eve revises text by channel, maps tools/interactions, keeps parking outcome-free, and also emits session terminal outcomes. [10]
- Native acquisition requires returned item identity; engine twin suppression uses live turn/request evidence rather than correlating channels in a mapper. [11]
- Capability source declares conservative unverified states and a contract-based Claude reason; inspection does not qualify fixture evidence. [12]
