# mcp/src/agents_remember/serving/conversation/projectors/pi.py

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

cit:([`map_native_frame`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:56-109) maps one durable `SessionEntry`: `message` entries delegate to
`_map_message`; `compaction` and `thinking_level_change`/`model_change` entries become system
`notice` items; every other entry type becomes `MappedUnknownVendor` with the native id/parent
preserved. cit:([`_map_message`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:170-207) routes by role: user messages cit:([`_map_user_message`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:210-256) map string or
part-list content (unknown part types preserved) with unknown-input provenance; assistant
messages cit:([`_map_assistant_message`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:259-331) split text/thinking parts into blocks, mint one stable-ID tool-call item
per `toolCall` part (input block, phase `streaming`, parented on the message), classify the
message phase from `stopReason`, and emit terminal outcomes — `stop`/`toolUse`/cit:([`length`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:53-53)
complete the turn without a separate marker (the assistant message itself is the settlement),
while `aborted`/`error` mint an in-place `turn-result` item plus `MappedTurnOutcome`
cit:(["def _map_tool_result_message("], mcp/src/agents_remember/serving/conversation/projectors/pi.py:363-398) upsert the same `toolCallId`; `message_end` triggers the engine's native continuation item with the output
block. cit:([`map_evidence_frame`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:112-167) maps live `tool_execution_start` (with the input block),
`tool_execution_update`/`_end` (output only) to partial-block upserts by `toolCallId`;
`message_end`/`message_update`/`agent_end` mint nothing — completed messages mint from durable
entries via the engine's eager native continuation, and in-flight deltas stay in the substrate
buffer so no provisional identity is ever minted. Unknown live events become
`MappedUnknownVendor`. The signature also accepts the protocol-wide
`parent_thread_id` keyword cit:([`parent_thread_id`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:116-116) — the multiplexed-harness demux context — and deliberately
ignores it (`noqa: ARG001`): pi carries no sub-agent threads.

### Conventions

Durable entries are the only message identity; live frames carry tool lifecycle and nothing
else. The engine (`eager_native_continuation = True`) re-reads entries as messages complete so
live items always carry native identity. Split tool items (invocation first, result later)
converge through the store's block union (review F1 pin).

### Invariants And Boundaries

- Item identity is the durable entry id / native `toolCallId`; never a content hash or array
  index, and never a provisional id minted from an id-less `message_end` frame.
- Pi has no sub-agent threads: the protocol-wide `parent_thread_id` demux
  keyword is accepted and ignored, so pi item identity stays the durable entry id only — no
  agent attribution is ever fabricated for this harness.
- User messages always carry `unknown-input` provenance — Pi exposes no request-id correlation,
  so the producer is never defaulted to operator or agent-bus.
- Branch/label/custom entry types surface as unknown-vendor evidence; history completeness stays
  honestly `partial` in capabilities.
- Turn-result items mint only for failed/aborted turns; completed turns end in the assistant
  message (stopReason feeds canonical status).

### Todos

None.

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the locked Pi RPC documentation (`rpc.md`) and the pinned `SessionEntry`/message
shapes — are repository-owned and cited below.

No configured domain documentation was available for this mapper.

### Repo-Internal References

The Pi adapter reads durable entries and emits the RPC event surface; the pi fixture records the
observed entry/tool shapes; the store's block union converges the split tool items.

- The Pi RPC adapter streams live RPC events (tool lifecycle frames) and pages durable entries with native id/parent coordinates. [1]
Historical evidence (retired with the d3610903 suite reduction): The pi fixture recorded the observed message_end live frame and durable-entry native page rows through the production seam. These removed artifacts provide no current execution or capability-enablement proof.
- The store unions tool-call blocks by `block_id` so start → update → end keeps the input block. [2]
- The engine continues native reads eagerly for pi so live items always carry native identity. [3]

### Cross-Repo References

No cross-repository implementation participates in this mapper; the Pi process is a local
subprocess reached through this repository's own adapter.

No meaningful cross-repo references found.
