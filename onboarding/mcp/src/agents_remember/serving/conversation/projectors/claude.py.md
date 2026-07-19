# mcp/src/agents_remember/serving/conversation/projectors/claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Claude active projector: maps stream-json frames into normalized items — assistant text and
thinking blocks stay inline, `tool_use` blocks become stable-ID tool-call items, `tool_result`
blocks upsert the same item, and result frames mint turn-result items plus canonical terminal
evidence. Claude has no native history page (stream/replay-only by design); user submissions
arrive through the adapter's exact submission echo, never a flattened native projection.

## Code Commentary

### Logic

`map_evidence_frame` (L54-L75) dispatches on the frame `type`: `assistant` frames (L126-L193)
key on the message `uuid`, split content into markdown/thinking blocks, mint one
stable-ID tool-call item per `tool_use` block (keyed by the native block id, input block
carrying name + arguments, phase `streaming`, parented on the assistant item), and preserve
unknown block types as `UnknownVendorBlock`s; `result` frames (L310-L353) classify
completed/interrupted/failed from `subtype`/`is_error`/`terminal_reason` (cancel reasons
L51), mint a `turn-result` item, and emit `MappedTurnOutcome` with the stop reason; non-replay
`user` frames are tool-result carriers (L233-L307) that upsert the same tool item with the
output block (phase `failed` on `is_error`); `system` frames (api_retry/status) feed canonical
status via the snapshot and mint no items. Unknown frame types become `MappedUnknownVendor`.
`map_transcript_echo` (L78-L123) consumes only `role="user"` entries: the echo is the
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

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the locked stream-json fixtures (2.1.207/2.1.210) and the Anthropic content-block
grammar as parsed by this repository's adapter — are repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The adapter's stream state builds the exact submission echo and the parsed frame surface; the
claude fixture records the version-gate posture; the store's block union converges the split
tool items.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter builds the exact submission echo (original text, exact request id, replay uuid) this mapper consumes. | L439-L512 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| The claude fixture records the locked 2.1.211 gate and the installed 2.1.214 mismatch reason. | L37-L41 | [claude-2.1.211.json](agents-remember/mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json) |
| The store unions tool-call blocks by `block_id` so `tool_use` → `tool_result` keeps input and output. | L123-L126; L303-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The engine's echo zipper merges echo and frame channels by strict turn order. | L398-L447 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

No cross-repository implementation participates in this mapper; the Claude Code process is a
local subprocess reached through this repository's own adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the claude active
  projector — stream-json frame mapping, stable tool identity with split upserts, exact
  submission echo, terminal outcomes. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
