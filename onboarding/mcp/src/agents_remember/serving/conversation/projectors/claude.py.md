# mcp/src/agents_remember/serving/conversation/projectors/claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

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
session mints zero unknown-vendor rows for them instead of one `claude:{type}` box per frame
(260718-CHATS-L5F R3).

## Code Commentary

### Logic

`map_evidence_frame` (L64-L92) dispatches on the frame `type`: `assistant` frames (L126-L193)
key on the message `uuid`, split content into markdown/thinking blocks, mint one
stable-ID tool-call item per `tool_use` block (keyed by the native block id, input block
carrying name + arguments, phase `streaming`, parented on the assistant item), and preserve
unknown block types as `UnknownVendorBlock`s; `result` frames (L310-L353) classify
completed/interrupted/failed from `subtype`/`is_error`/`terminal_reason` (cancel reasons
L51), mint a `turn-result` item, and emit `MappedTurnOutcome` with the stop reason; non-replay
`user` frames are tool-result carriers (L233-L307) that upsert the same tool item with the
output block (phase `failed` on `is_error`); `system` frames (api_retry/status) feed canonical
status via the snapshot and mint no items; `command_lifecycle` frames (L78-L79 →
`_map_command_lifecycle` L95-L109) are the installed 2.1.216 slash-command lifecycle — strictly
validated against the captured 3-state contract (`command_uuid` present, `state ∈
{queued,started,completed}`) and minting NO timeline item, so an ordinary session no longer floods
with `claude:command_lifecycle` boxes (native `result`/history already renders the command), while
a state outside the contract raises `UnmappableShape` and surfaces as visible drift instead of
silent tolerance; `rate_limit_event` frames (L80-L84) are shape-validated (`rate_limit_info`
required) then dropped as telemetry, exactly like codex rateLimits. Genuinely unknown frame types
still become `MappedUnknownVendor`.
`map_transcript_echo` (L112-L157) consumes only `role="user"` entries: the echo is the
authority's own submission record (original text, exact request id, replay correlation uuid), so
the user item keys on the replay uuid and carries unknown-input provenance until the engine's
provenance batch resolves the real source — replayed user frames on the evidence channel raise
`UnmappableShape` because they are consumed as echoes, never double-minted.

### Conventions

The mapper never invents native history: hydration comes from the live evidence window only,
and the echo zipper in the engine merges the two channels by strict turn order without
timestamps. Tool items deliberately split invocation (`tool_use`) and result (`tool_result`)
into partial-block upserts of one stable id; the store's block union converges them (review F1).

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
  preserved as prior art for the second-half native slash-command surface (leaves 07/08), which
  will consume the lifecycle as settlement evidence correlated by `command_uuid`.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the stream-json fixtures, the Anthropic content-block grammar as parsed by this
repository's adapter, and the installed 2.1.216 `command_lifecycle`/`rate_limit_event` contracts
(the captured 3-state slash-command specimen is preserved in the leaf's authoring diagnosis note as
L7/L8 prior art) — are repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The adapter's stream state builds the exact submission echo and the parsed frame surface; the
claude runtime fixture records the claude evidence rows (informational version metadata only —
260718-CHATS-L5F R4 removed every version gate, so the fixture no longer drives a demotion); the
store's block union converges the split tool items.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter builds the exact submission echo (original text, exact request id, replay uuid) this mapper consumes. | L439-L512 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| The claude runtime fixture records the claude evidence rows; version strings are informational metadata, never a capability gate (R4). | L37-L41 | [claude-2.1.211.json](agents-remember/mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json) |
| The store unions tool-call blocks by `block_id` so `tool_use` → `tool_result` keeps input and output. | L123-L126; L303-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The engine's echo zipper merges echo and frame channels by strict turn order. | L398-L447 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

No cross-repository implementation participates in this mapper; the Claude Code process is a
local subprocess reached through this repository's own adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded R3 — the mapper now learns the
  installed Claude Code 2.1.216 frame contracts as first-class typed frames. `command_lifecycle` is
  strictly validated against the captured 3-state contract (`command_uuid` + `state ∈
  {queued,started,completed}`) and mints no timeline item (native history renders the command), so
  an ordinary session no longer floods with `claude:command_lifecycle` boxes; a drifted state
  raises `UnmappableShape` and surfaces as visible drift, never a silently tolerated stranger.
  `rate_limit_event` is shape-validated then dropped as telemetry. Corrected the Repo-Internal
  claude-fixture finding to metadata-only language (R4 removed the version gate). Verification
  metadata stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the claude active
  projector — stream-json frame mapping, stable tool identity with split upserts, exact
  submission echo, terminal outcomes. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
