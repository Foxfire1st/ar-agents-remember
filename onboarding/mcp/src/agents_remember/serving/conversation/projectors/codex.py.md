# mcp/src/agents_remember/serving/conversation/projectors/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The Codex active projector: maps app-server thread items (native `thread/read` pages) and live
notification frames into normalized items, blocks, deltas, and turn outcomes with stable native
identity — and preserves every unrecognized shape as `unknown-vendor` evidence instead of
guessing. Codex's documented historical tool loss stays visible through capabilities, never
hidden by a completeness claim. Since 260718-CHATS-L5F R1 the notification's native METHOD is
carried on `frame.native_method` (previously stripped before the projector), so the codex 0.144.5
fresh-open lifecycle/status burst is recognized and dropped by method instead of flooding one
`unknown-vendor` row per MCP server, and a truly-unknown method is named rather than anonymous.

## Code Commentary

### Logic

`map_native_frame` (L75-L86) parses one `thread/read` item frame and delegates to
`_map_thread_item`; turn parenting comes from the frame's `nativeParentId`. `map_evidence_frame`
(L89-L191) discriminates live evidence by adapter event kind, then — for `codex-notification`
frames — by the native METHOD the adapter now preserves on `frame.native_method` (L127; 260718-
CHATS-L5F R1: the method used to be dropped before the projector, so shapeless startup notices
flooded as one `unknown-vendor` row per configured MCP server). `_SILENT_NOTIFICATION_METHODS`
(L62-L72) drops the codex 0.144.5 session lifecycle/status/telemetry burst — `thread/started`,
one `mcpServer/startupStatus/updated` per configured MCP server, `remoteControl/status/changed`,
the `warning`/`configWarning` advisory family, plus the pre-existing `account/rateLimits/updated`
and `thread/tokenUsage/updated` — by method, recognized and never re-guessed, so a stock codex open
mints ZERO `unknown-vendor` rows (`configWarning` was the recovery seat's live-observed addition,
firing at open on setups with a config note). Frames without a known drop method fall through the
schema-disjoint params-shape branches: `completed` frames map `turn/completed` to a `turn-result`
item plus `MappedTurnOutcome` (via `_map_turn_completed`, L559-L601); `transcript` frames carry
full `item/completed` items; `state` frames feed canonical status only and mint no items;
item-bearing `startedAtMs` frames resolve item started/completed, indexed deltas
(`summaryIndex`/`contentIndex`) to their named blocks, bare deltas (agentMessage/plan/
commandExecution output share one shape) to an empty block id the engine resolves through the item
kind, `patchUpdated` change lists to diff-block tool items, and token-usage/rate-limit frames to
nothing (L3 telemetry evidence, never token-theater rows). A method that matches no drop and no
shape becomes `MappedUnknownVendor` (L179-L191) but now NAMES the method
(`codex:notification:<method>` / `unrecognized codex notification <method>`), so a genuinely novel
notification stays visible AND identifiable rather than anonymous. `_map_thread_item` (L194-L332)
keys every item on its native `id` and maps `userMessage`
(content parts to text/file-reference/unknown blocks, `clientId` to request correlation,
unknown-input provenance), `agentMessage`/`plan` (markdown), `reasoning` (summary/content to
thinking blocks), `commandExecution` (tool input command + aggregated output, phase from native
status via `_tool_phase` L603-L611), `fileChange` (diff blocks), and `mcpToolCall` (input
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
- The startup/status/telemetry drop is keyed on the native method (`frame.native_method` against
  `_SILENT_NOTIFICATION_METHODS`), never on params shape — the drop-set is method-specific and
  item-less, so an item-bearing frame under any of those methods still reaches the shape branches
  and maps. A truly-unknown method never falls silently: it becomes `unknown-vendor` evidence with
  the method named in `vendor_type`/`safe_summary`.

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
| The codex adapter now sets `AR_EVIDENCE_METHOD_KEY: method` on the `codex-notification` emit so the method reaches this projector (the R1 method-carry seam). | L598-L601 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| `EvidenceFrame.native_method` is the typed field the bridge preserves and this projector switches on; `evidence_frame_json` serializes it as `nativeMethod`. | L416-L420; L547-L548 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
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
