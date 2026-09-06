# mcp/src/agents_remember/serving/conversation/projectors/pi.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/pi.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T16:43+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authorities named by the
module — the locked Pi RPC documentation (`rpc.md`) and the pinned `SessionEntry`/message
shapes — are repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The Pi adapter reads durable entries and emits the RPC event surface; the pi fixture records the
observed entry/tool shapes; the store's block union converges the split tool items.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Pi RPC adapter streams live RPC events (tool lifecycle frames) and pages durable entries with native id/parent coordinates. | `_event_stream`; `read_native_page` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:268-305; mcp/src/agents_remember/serving/pi_rpc_adapter.py:576-611 |
| Historical evidence (retired with the d3610903 suite reduction): The pi fixture recorded the observed message_end live frame and durable-entry native page rows through the production seam. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |
| The store unions tool-call blocks by `block_id` so start → update → end keeps the input block. | `_union_blocks` | mcp/src/agents_remember/serving/conversation/active/store.py:466-482 |
| The engine continues native reads eagerly for pi so live items always carry native identity. | `poll_native_continuation` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:283-304 |

## Cross-Repo References

No cross-repository implementation participates in this mapper; the Pi process is a local
subprocess reached through this repository's own adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-09T16:43+02:00 — 260713-TES-L5 hotfix curator: re-read the eager Pi native-continuation
  claim after the shared identity-preserving fallback insertion and refreshed its moved range.
  Verification metadata remains pinned because `pi.py` itself did not change.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 4 citation rows (RPC adapter stream/paging, pi fixture rows, store `_union_blocks`, eager `poll_native_continuation`) and converted 6 superseded prose line citations plus 2 single-line parenthesized shorthand forms to cit: forms; all pi.py mapper ranges verified against the frozen source. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose target
  file no longer exists. `serving/conversation/active/projector.py` was split into the
  `active/projector/` package; the eager native continuation now lives in
  `projector/native_ingestion.py` — `poll_native_continuation` returns immediately unless
  `mapper.eager_native_continuation` and otherwise drains native pages
  cit:([`poll_native_continuation`], mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:283-304), and the lazy
  `native_dirty` path at L154-L156 is skipped for eager mappers. Re-verified that `_PiProjector`
  is the only projector setting `eager_native_continuation = True`
  cit:(["eager_native_continuation = True"], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:101-101).
  Repointed both the link path and the range; no claim text changed.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/projectors/pi.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 17 line(s), touching only magic
  trailing commas. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `store.py`, `pi_rpc_adapter.py`; those ranges shifted because this task
  edited those files, so treat the cited numbers as approximate and the linked cards as
  authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-26T15:34 — 260718-CHATS-L7: `map_evidence_frame` gained the protocol-wide optional
  `parent_thread_id` keyword cit:([`parent_thread_id`], mcp/src/agents_remember/serving/conversation/projectors/pi.py:116-116), accepted and ignored (`noqa: ARG001`) because pi carries
  no sub-agent threads. Sidecar: documented the ignored demux seam and the no-fabricated-agent-
  attribution invariant; refreshed body citations shifted by the signature growth (_map_message
  L170-L199, user L202-L250, assistant L251-L325, terminal outputs L326-L354, toolResult
  L355-L392, map_evidence_frame L112-L167) and re-pointed stale repo-internal citations:
  pi_rpc_adapter.py L468-L476 → L266-L305/L580-L612 (live event stream + native paging), fixture
  L36-L58 → L41-L61, store.py L123-L126/L303-L319 → L127-L136/L435-L452, projector.py
  L474-L496 → L580/L945-L947 (the L7 multiplexed rewrite had displaced them). Uncommitted;
  closeout re-stamps verification.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the pi active
  projector — durable-entry identity anchoring, live tool upserts by `toolCallId`, completion-
  anchored live text, honest unknown-input user provenance. Verification is blank because the
  new source file is uncommitted; closeout owns its first source stamp.
