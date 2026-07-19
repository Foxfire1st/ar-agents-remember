# mcp/src/agents_remember/serving/conversation/projectors/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Codex active projector: maps app-server thread items (native `thread/read` pages) and live
notification frames into normalized items, blocks, deltas, and turn outcomes with stable native
identity — and preserves every unrecognized shape as `unknown-vendor` evidence instead of
guessing. Codex's documented historical tool loss stays visible through capabilities, never
hidden by a completeness claim.

## Code Commentary

### Logic

`map_native_frame` (L52-L63) parses one `thread/read` item frame and delegates to
`_map_thread_item`; turn parenting comes from the frame's `nativeParentId`. `map_evidence_frame`
(L66-L159) discriminates live evidence by adapter event kind plus the schema-disjoint required
keys of each params shape — the notification method string never crosses the evidence payload:
`completed` frames map `turn/completed` to a `turn-result` item plus `MappedTurnOutcome`
(L527-L568); `transcript` frames carry full `item/completed` items; `state` frames feed canonical
status only and mint no items; `codex-notification` frames resolve item started/completed by the
`startedAtMs` key, indexed deltas (`summaryIndex`/`contentIndex`) to their named blocks, bare
deltas (agentMessage/plan/commandExecution output share one shape) to an empty block id the
engine resolves through the item kind, `patchUpdated` change lists to diff-block tool items, and
token-usage/rate-limit frames to nothing (L3 telemetry evidence, never token-theater rows).
`_map_thread_item` (L162-L299) keys every item on its native `id` and maps `userMessage`
(content parts to text/file-reference/unknown blocks, `clientId` to request correlation,
unknown-input provenance), `agentMessage`/`plan` (markdown), `reasoning` (summary/content to
thinking blocks), `commandExecution` (tool input command + aggregated output, phase from native
status via `_tool_phase` L571-L580), `fileChange` (diff blocks), and `mcpToolCall` (input
arguments + result/error output). Every other item type returns `MappedUnknownVendor` with the
native id and turn preserved.

### Conventions

Parse by schema, never heuristic: exact required keys per shape; anything unrecognized becomes
unknown-vendor evidence with an opaque coordinate evidence handle — raw payloads never reach a
public item. Mappers are pure; the engine assigns ordinals, revisions, and provenance resolution.

### Invariants And Boundaries

- Item identity is the native item id (turn parent on `nativeParentId`); never a content hash,
  timestamp, or array index.
- User messages mint with `unknown-input` provenance plus `clientId` correlation; the engine's
  provenance batch resolves the real producer.
- Full-item re-maps are idempotent under the store's tool-call block union (review F1 pin).
- Historical tool loss is a capability claim (`history.toolCompleteness=partial`), never patched
  over by invented tool detail.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The schema authority named by the
module is the codex app-server v2 generated protocol plus the landed installed-runtime fixture
rows, both repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this mapper. | — | — |

## Repo-Internal References

The generated v2 protocol types and the codex adapter's evidence emission are the frame
authorities; the installed-runtime fixture records which shapes are gate-observed; the engine
resolves bare-delta targets and provenance.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The codex app-server adapter emits the evidence/native-page frames this module maps. | L310-L350 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The codex fixture rows record the observed live item/notification shapes and native thread pages through the production seam. | L34-L58 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |
| The store's tool-call block union keeps full-item re-maps byte-identical while converging partial-block tools. | L123-L126; L303-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The engine resolves bare-delta target blocks through the mapped item's kind. | L296-L300 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |

## Cross-Repo References

No cross-repository implementation participates in this mapper; the Codex app-server is a local
subprocess reached through this repository's own adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the codex active
  projector — thread-item/notification mapping, schema-disjoint live discrimination, native
  identity, unknown-vendor preservation, honest historical tool loss. Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
