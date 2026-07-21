# mcp/tests/test_conversation_active_projectors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_projectors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Per-harness projector frame-mapping tests for 260718-CHATS-L1 (R2): proves stable native
identity, block/tool mapping, provenance honesty, turn outcomes, and unknown-shape preservation
for the codex, claude, and pi mappers — without any engine or IPC.

## Code Commentary

### Logic

`CodexMapperTests` (L49-L270): native user messages carry unknown-input provenance with
`clientId` correlation; agent messages map to markdown; reasoning maps summary/content thinking
blocks; command executions map input+output tool blocks with phase from native status; file
changes map diff blocks; MCP tool calls map input/output; unknown native item types keep their
native id as unknown-vendor evidence; live item started/completed phases; indexed and bare
deltas target the right block ids; `turn/completed` maps the turn-result item plus outcome;
usage/rate frames mint no items; unknown notifications are preserved.
`ClaudeMapperTests` (L272-L388): assistant frames split text/thinking and mint stable-ID tool
items; `tool_result` upserts the same item; result frames classify terminal outcomes; the
transcript echo is the exact submission user item (replay uuid identity, request-id
correlation, unknown-input until the batch resolves); system frames mint nothing; unknown frame
types are preserved. `PiMapperTests` (L389-L553): entry user messages stay unknown-input;
assistant entries split blocks and tools; `toolResult` messages converge by `toolCallId`;
aborted assistants mint the in-place turn-result; compaction/model entries are notices; unknown
entry types keep their native id; live tool-execution events upsert by `toolCallId`;
`message_end`/`message_update`/`agent_end` mint no live items.

### 260718-CHATS-L5F additions (R1 codex notification identity + R3 claude frame contracts)

`CodexMapperTests` gains the R1 notification-identity coverage now that the native method name is
carried onto the evidence frame instead of stripped: `test_fresh_open_startup_burst_mints_zero_unknown_vendor_rows`
(the stock codex 0.144.5 open burst — `mcpServer/startupStatus/updated`, `thread/started`,
`remoteControl/status/changed`, `warning`, `configWarning` — each maps to `[]` by method through the
`_SILENT_NOTIFICATION_METHODS` drop-set, so an open produces zero unknown-vendor rows),
`test_item_notification_still_maps_when_method_is_carried` (a real item-bearing frame still reaches
the shape branches — the drop-set is method-specific and item-less), and
`test_truly_unknown_notification_names_the_method` (a genuinely novel method still falls to
unknown-vendor but WITH the method named, `codex:notification:<method>`). `ClaudeMapperTests` gains
the R3 frame-contract coverage: `test_command_lifecycle_is_recognized_and_mints_no_unknown_vendor`
(the 3-state queued/started/completed lifecycle is validated first-class and mints no timeline row),
`test_command_lifecycle_unknown_state_surfaces_as_drift` (a drifted state raises `UnmappableShape` →
a VISIBLE malformed row, never silent tolerance), and `test_rate_limit_event_mints_no_items`
(`rate_limit_event` is shape-validated then dropped as telemetry).

### Conventions

Mapper-pure tests: frames are constructed as `EvidenceFrame`/`NativeEvidenceFrame` values and
outputs asserted structurally — no projector engine, no store, no socket.

### Invariants And Boundaries

- Identity assertions always name the native id/uuid/toolCallId; never content hashes or
  indices.
- Unknown shapes are asserted as preserved unknown-vendor evidence, never dropped or guessed.
- User-role items never gain a default producer.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the mapper schema authorities are
repository-owned and cited in the mapper sidecars.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The codex mapper under test: live discrimination, thread items, deltas, turn outcomes. | L66-L159; L162-L299 | [codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/codex.py) |
| The claude mapper under test: frame mapping plus the exact submission echo. | L54-L123 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/claude.py) |
| The pi mapper under test: entry mapping plus live tool upserts. | L56-L162 | [pi.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/pi.py) |
| The mapper output vocabulary the assertions match. | L55-L94 | [common.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/common.py) |
| The evidence frame products constructed by the suite. | L310-L350 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R1/R3 mapper regressions this
  leaf added — the codex startup-burst-mints-zero, method-carried-still-maps, and truly-unknown-names-the-method
  identity tests (`CodexMapperTests`), and the claude command_lifecycle recognized/drift and
  rate_limit_event drop tests (`ClaudeMapperTests`). Verification metadata stays pinned (the L5F
  change is uncommitted); closeout re-stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the per-harness
  mapper suite — identity/blocks/tools/provenance/outcomes/unknown preservation (26 tests).
  Verification is blank because the new source file is uncommitted; closeout owns its first
  source stamp.
