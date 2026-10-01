# mcp/src/agents_remember/serving/conversation/projectors/claude.py

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Claude active projector: maps stream-json frames into normalized items — assistant text and
thinking blocks stay inline, `tool_use` blocks become stable-ID tool-call items, `tool_result`
blocks upsert the same item, and result frames mint turn-result items plus canonical terminal
evidence. Claude has no native history page (stream/replay-only by design); user submissions
arrive through the adapter's exact submission echo, never a flattened native projection. The
mapper learns the installed Claude Code 2.1.216 frame contracts as first-class typed frames — the
`command_lifecycle` slash-command lifecycle and `rate_limit_event` telemetry — so an ordinary
session mints zero unknown-vendor rows for them instead of one `claude:{type}` box per frame.
The mapper also projects harness sub-agents as
first-class roster participants: Agent-tool inner frames stream as ordinary assistant/user frames
distinguished by `parent_tool_use_id` (the spawning Agent tool_use id, carrying
`subagent_type`/`task_description`), and the agent lifecycle rides `system` frames
`task_started`/`task_progress`/`task_notification` plus `background_tasks_changed`, driving one
roster item per agent through a bounded session-keyed `task_id` ↔ `tool_use_id` binding registry.
All sub-agent shapes are probe-locked on the installed claude 2.1.220 (2026-07-26 live stream-json
probes, foreground and `run_in_background` Agent calls).

## Code Commentary

### Logic

cit:([`map_evidence_frame`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:210-239) dispatches on the frame `type`; it also
accepts an optional `parent_thread_id` demux context from the multiplexed-harness path, which the
claude mapper deliberately ignores because sub-agent identity is encoded in-band via
`parent_tool_use_id`. `assistant` frames cit:([`_map_assistant`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:665-735)
key on the message `uuid`, split content into markdown/thinking blocks, mint one
stable-ID tool-call item per `tool_use` block (keyed by the native block id, input block
carrying name + arguments, phase `streaming`, parented on the assistant item), and preserve
unknown block types as `UnknownVendorBlock`s; `result` frames cit:([`_map_result`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:1021-1074) classify
completed/interrupted/failed from the adapter-attributed terminal stamp or
`subtype`/`is_error`/`terminal_reason` (cancel reasons L76), mint a `turn-result` item, and emit
`MappedTurnOutcome` with the stop reason; non-replay
`user` frames are tool-result carriers cit:([`_map_tool_carrier`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:887-975) that upsert the same tool
item with the output block (phase `failed` on `is_error`); `system` frames dispatch through
cit:([`_map_system`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:269-302): api_retry/status still feed the canonical status service via the
snapshot, and every other subtype observed on 2.1.220 (init, task_updated, hook_*, ...) still
drops silently exactly as before, but the agent-lifecycle subtypes now mint roster items (see the
sub-agent paragraph below); `command_lifecycle` frames (L228-L229 →
`_map_command_lifecycle` L245-L259) are the installed 2.1.216 slash-command lifecycle — strictly
validated against the captured 3-state contract (`command_uuid` present, `state ∈
{queued,started,completed}`) and minting NO timeline item, so an ordinary session no longer floods
with `claude:command_lifecycle` boxes (native `result`/history already renders the command), while
a state outside the contract raises `UnmappableShape` and surfaces as visible drift instead of
silent tolerance; `rate_limit_event` frames (recognized by the `_SILENT_FRAME_CONTRACTS` lookup
L220-L223, table L263-L266 → `_require_rate_limit_event` L253-L256) are shape-validated
(`rate_limit_info` required) then dropped as telemetry, exactly like codex rateLimits. Genuinely unknown frame types
still become `MappedUnknownVendor`.

Sub-agents: `_map_system` routes `task_started`/`task_progress`/
`task_notification` to cit:([`_map_task_lifecycle`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:305-385) and `background_tasks_changed` to
cit:([`_map_background_tasks_changed`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:557-618). `_map_task_lifecycle` upserts ONE roster item per
agent (`claude-agent-<task_id>`, role `system`, kind `notice`) across started → progress →
notification, carrying description/summary/usage blocks and a `ConversationAgentRef` whose status
comes from the probe-locked `task_notification.status` vocabulary (`_NOTIFICATION_AGENT_STATUS`
L92-L108 — anything outside the table stays honest as `unknown`). `task_started` additionally
emits a block-less upsert on the spawning Agent tool-call item (item id = the join key) tagging it
with the bound roster identity; the 2.1.220 probes show task_started preceding the Agent
tool_result carrier in both foreground and `run_in_background` orderings, so the tool call is
honestly still streaming and the later tool_result upsert settles it. Every task_* frame records a
`_AgentBinding` in the bounded session-keyed `_AgentBindingRegistry` (L111-L162; caps L89-L90,
128 sessions × 64 bindings, LRU eviction), binding `task_id` ↔ `tool_use_id`; `task_started` is
the binding authority and REQUIRES both ids. `_map_background_tasks_changed` carries the full
running background-task set with no join key and no status, so it can only honestly REGISTER a
task the task_* evidence never bound (a replay window that opened mid-agent); already-bound tasks
and an empty set mint nothing. On the content path, cit:([`_sidechain_agent_ref`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:172-193) attaches
the roster identity to assistant/user frames keyed by `parent_tool_use_id` — the bound `task_id`
wins once task_* evidence bound the join key, otherwise the join key itself is the honest
`agent_id` with status `unknown` and the frame's own `subagent_type` as role — and
cit:([`_spawned_agent_ref`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:196-207) tags a parent-timeline `tool_result` that settles a bound Agent
call. Sidechain user-frame text blocks become the sub-agent's own user message item (L932-L972 —
the probe shows the task prompt echo as the first sidechain user frame; with
`--forward-subagent-text` its replies cross too), while parent user text keeps the
  unknown-vendor/replay-echo path. A MALFORMED task_* frame enters `_map_system`'s `UnmappableShape`
  branch and is labeled `claude-system:<subtype>` (cit:([`_map_system`; "if subtype in ("; "return mapper(raw)"; "vendor_type=f\"claude-system:{subtype}\","; "except UnmappableShape"; "claude-system:"], mcp/src/agents_remember/serving/conversation/projectors/claude.py:269-302)).

cit:([`map_transcript_echo`], mcp/src/agents_remember/serving/conversation/projectors/claude.py:621-662) consumes only `role="user"` entries: the echo is the
authority's own submission record (original text, exact request id, replay correlation uuid), so
the user item keys on the replay uuid and carries unknown-input provenance until the engine's
provenance batch resolves the real source — replayed user frames on the evidence channel raise
`UnmappableShape` because they are consumed as echoes, never double-minted.

### Conventions

The mapper never invents native history: hydration comes from the live evidence window only,
and the echo zipper in the engine merges the two channels by strict turn order without
timestamps. Tool items deliberately split invocation (`tool_use`) and result (`tool_result`)
into partial-block upserts of one stable id; the store's block union converges them (review F1).
The roster identity rides an optional `agent=` (`ConversationAgentRef`)
parameter threaded through `_map_assistant`/`_map_tool_use`/`_map_tool_carrier`/`_map_tool_result`
(default `None` = the parent conversation) — additive grammar, never a new item kind — and the
session-keyed binding registry enriches that dimension ONLY from the harness's own task_*
evidence, with session-less frames (older fixtures) sharing one honest bucket rather than
cross-session guesses.

### Invariants And Boundaries

- Item identity is the message uuid / native `tool_use` id / replay correlation uuid; never a
  content hash or array index.
- The submission echo is the only user-message channel; native `user` replay frames must never
  mint a second item.
- Unknown assistant/user block types are preserved as unknown-vendor evidence with the native
  block coordinate, never dropped and never guessed.
- Result frames classify terminal outcome from native fields only; unknown evidence never
  becomes `ready` (the canonical status service enforces this downstream).
- The 2.1.216 `command_lifecycle` is recognized as a first-class contract (the three documented
  states) and mints no timeline row; a state outside the contract raises `UnmappableShape` (visible
  drift), never a silently tolerated stranger and never a stream kill. `rate_limit_event` is
  shape-validated then dropped as telemetry. These two frames must never fall to the
  `MappedUnknownVendor` fallback on the installed harness. The captured 3-state specimen is
  preserved as prior art for the later native slash-command surface, which
  will consume the lifecycle as settlement evidence correlated by `command_uuid`.
- Sub-agent identity is evidence-bound, never fabricated: the binding
  registry only ever ENRICHES the agent dimension from the harness's own task_* frames; an
  unbound `parent_tool_use_id` frame keeps `agent_id` = the join key with status `unknown`, and a
  `task_notification.status` outside the probed vocabulary maps to `unknown`, not a guess.
- A MALFORMED task_* frame degrades to preserved unknown-vendor (`claude-system:<subtype>`),
  never a bridge-fatal error — a frame that fires on every agent spawn must never kill the
  projection (the string-content precedent).
- The binding registry is bounded (128 sessions × 64 bindings per session, LRU eviction) so a
  long-lived multiplexed session cannot grow it without limit; `task_started` is the binding
  authority and requires BOTH `task_id` and `tool_use_id`.
- `background_tasks_changed` can only REGISTER a never-bound task; it reconciles nothing — an
  empty running set asserts "nothing running" without distinguishing completed from killed, so it
  mints no terminal claims.
- The `task_started` tagging upsert on the spawning Agent tool-call item carries EMPTY blocks, so
  the store's block union preserves the tool_use/tool_result blocks the parent timeline already
  minted, and a `streaming`-phase tagging upsert never regresses a settled terminal phase.

### Todos

None.

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the surviving 2.1.210 turn/interaction fixtures and 2.1.217 interrupt fixture, the
Anthropic content-block grammar as parsed by this
repository's adapter, the installed 2.1.216 `command_lifecycle`/`rate_limit_event` contracts
(the captured 3-state slash-command specimen is preserved as prior art for the later slash-command
consumers), and the 2.1.220 sub-agent frame shapes (`parent_tool_use_id` sidechains, the
task_* lifecycle, `background_tasks_changed`) probe-locked in the module docstring from the
2026-07-26 live probes — are repository-owned and cited below.

No configured domain documentation was available for this mapper.

### Repo-Internal References

The adapter's stream state builds the exact submission echo and the parsed frame surface; the
claude runtime fixture records the claude evidence rows (informational version metadata only —
every version gate is removed, so the fixture no longer drives a demotion); the
store's block union converges the split tool items and absorbs the block-less task_started tagging
upsert; the conversation grammar carries the roster identity as `ConversationAgentRef` on
`ConversationItem`.

- The adapter defines replay-user and transcript-entry handlers together with a 128 KiB transcript-text bound and clipping helper. [1]
Historical evidence (retired with the d3610903 suite reduction): The Claude runtime fixture recorded runtime/helper versions and sets `enablesCapabilities` to false. These removed artifacts provide no current execution or capability-enablement proof.
- The store unions tool-call blocks by `block_id` so `tool_use` → `tool_result` keeps input and output, and a late tagging upsert does not regress a terminal phase. [2]
- The engine's echo zipper merges echo and frame channels by strict turn order. [3]
- The conversation grammar declares the `ConversationAgentRef` roster-reference model. [4]

### Cross-Repo References

No cross-repository implementation participates in this mapper; the Claude Code process is a
local subprocess reached through this repository's own adapter.

No meaningful cross-repo references found.

## Mutation-Diff Facade Delta

The Claude projector maps newly observed native interaction and interrupt evidence into the normalized active-conversation grammar. Unknown vendor shapes remain preserved evidence rather than guessed transcript semantics.

The mutation-diff path now keeps `_tool_mutation_diff_blocks` as a stable facade and delegates
Edit, MultiEdit, Write, and NotebookEdit to responsibility-specific parsers. All diff content comes
only from the observed `tool_use.input`; malformed or unsupported vendor shapes retain their raw
`ToolInputBlock` and produce no invented diff. MultiEdit identifiers preserve original positions
when invalid entries are skipped.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

The `task_*` (sub-agent roster) mapping was decomposed into named readers, and one concept was
introduced:

- **`_TaskIdentity`** (`join_key`, `subagent_type`, `description`, `retained_description`) — the
  roster identity one `task_*` frame resolves to, **frame evidence over binding**.
  `retained_description` is deliberately what the replacing binding record keeps, which is NOT
  always what the roster row displays; `_resolve_task_identity` is the one place that difference is
  decided.
- `_task_lifecycle_state(subtype, …)` — the join key, agent status and item phase a lifecycle
  subtype settles on.
- `_require_task_usage(subtype, raw)` — the frame's optional `usage` telemetry, validated as the
  vendor-owned object it is.
- `_task_usage_block(...)` — the roster row's telemetry block, or `None` when the frame carried
  neither half.
- `_task_lifecycle_blocks(...)` — the roster row's content blocks, in the order every upsert
  re-emits them.
- `_agent_identity_tag_item(...)` — the `task_started` upsert that tags the spawning `Agent`
  tool-call with the bound identity.

Two strictness checks were also named: `_require_command_lifecycle` (strictly recognize the 3-state
slash-command lifecycle) and `_require_rate_limit_event` (strictly recognize rate-limit telemetry,
which feeds L3 exactly like codex `rateLimits`). The mapped output is unchanged — an unrecognized
shape is still preserved, never guessed.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
