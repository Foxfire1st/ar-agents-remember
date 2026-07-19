# mcp/src/agents_remember/serving/conversation/projectors/pi.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/pi.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Pi active projector: maps durable session entries (the identity anchor) and live RPC events
into normalized items, tools, notices, and outcomes. Messages mint from durable entries with
native identity — never from id-less live frames — and live `tool_execution_*` events upsert
tool-call items by the native `toolCallId`. Pi has no request-id correlation for user messages;
they honestly carry `unknown-input` provenance.

## Code Commentary

### Logic

`map_native_frame` (L56-L109) maps one durable `SessionEntry`: `message` entries delegate to
`_map_message`; `compaction` and `thinking_level_change`/`model_change` entries become system
`notice` items; every other entry type becomes `MappedUnknownVendor` with the native id/parent
preserved. `_map_message` (L165-L194) routes by role: user messages (L197-L243) map string or
part-list content (unknown part types preserved) with unknown-input provenance; assistant
messages (L246-L318) split text/thinking parts into blocks, mint one stable-ID tool-call item
per `toolCall` part (input block, phase `streaming`, parented on the message), classify the
message phase from `stopReason`, and emit terminal outcomes — `stop`/`toolUse`/`length` (L53)
complete the turn without a separate marker (the assistant message itself is the settlement),
while `aborted`/`error` mint an in-place `turn-result` item plus `MappedTurnOutcome`
(L321-L347); `toolResult` messages (L350-L385) upsert the same `toolCallId` item with the output
block. `map_evidence_frame` (L112-L162) maps live `tool_execution_start` (with the input block),
`tool_execution_update`/`_end` (output only) to partial-block upserts by `toolCallId`;
`message_end`/`message_update`/`agent_end` mint nothing — completed messages mint from durable
entries via the engine's eager native continuation, and in-flight deltas stay in the substrate
buffer so no provisional identity is ever minted. Unknown live events become
`MappedUnknownVendor`.

### Conventions

Durable entries are the only message identity; live frames carry tool lifecycle and nothing
else. The engine (`eager_native_continuation = True`) re-reads entries as messages complete so
live items always carry native identity. Split tool items (invocation first, result later)
converge through the store's block union (review F1 pin).

### Invariants And Boundaries

- Item identity is the durable entry id / native `toolCallId`; never a content hash or array
  index, and never a provisional id minted from an id-less `message_end` frame.
- User messages always carry `unknown-input` provenance — Pi exposes no request-id correlation,
  so the producer is never defaulted to operator or agent-bus.
- Branch/label/custom entry types surface as unknown-vendor evidence; history completeness stays
  honestly `partial` in capabilities.
- Turn-result items mint only for failed/aborted turns; completed turns end in the assistant
  message (stopReason feeds canonical status).

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the locked Pi RPC documentation (`rpc.md`) and the pinned `SessionEntry`/message
shapes — are repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The Pi adapter reads durable entries and emits the RPC event surface; the pi fixture records the
observed entry/tool shapes; the store's block union converges the split tool items.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Pi RPC adapter reads durable entries with native id/parent coordinates and emits live tool-execution events. | L468-L476 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |
| The pi fixture records the observed message_end live frame and durable-entry native page rows through the production seam. | L36-L58 | [pi-0.80.7.json](agents-remember/mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json) |
| The store unions tool-call blocks by `block_id` so start → update → end keeps the input block. | L123-L126; L303-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The engine continues native reads eagerly for pi so live items always carry native identity. | L474-L496 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

No cross-repository implementation participates in this mapper; the Pi process is a local
subprocess reached through this repository's own adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the pi active
  projector — durable-entry identity anchoring, live tool upserts by `toolCallId`, completion-
  anchored live text, honest unknown-input user provenance. Verification is blank because the
  new source file is uncommitted; closeout owns its first source stamp.
