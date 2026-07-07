# mcp/src/agents_remember/models/terminal.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/models/terminal.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-07T20:50+02:00                       |
| lastVerifiedCommitHash | `52911a15091de8d065afc6cbc0f8d6ac34690039`   |
| lastVerifiedCommitDate | 2026-07-07T22:29:35+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[models overview](overview.md)

## Purpose

`terminal.py` defines strict Pydantic response contracts for MCP tools that expose dashboard
terminal-session catalog operations. It models the hosted-chat/terminal leaf reassignment tool (L9) and
— since L2 — the agent-facing `spawn_agent_session` dispatch tool.

## Code Commentary

### Logic

`LeafAssignmentStatus` is the closed response vocabulary for assignment attempts:
`attached`, `leaf-taken`, `unknown-session`, `leaf-ref-not-found`, or `leaf-ref-ambiguous`.
`AttachTerminalSessionToLeafResponse` is a strict
`ToolResponse` with operation `attach_terminal_session_to_leaf`, the requested session and `leafKey`,
the optional prior binding (`previousLeafKey`), optional conflict owner (`ownerSession`), optional
role (`chat` or `terminal`), and optional `detail` for validation refusals.

`SpawnAgentSessionStatus` is the L2 vocabulary: `spawned` (the only `ok: true` case), `leaf-taken`
(the server-arbitrated refusal, never overridden), and the pre-spawn validation refusals
`harness-unknown` / `harness-not-detected` / `effort-invalid` (L16 — effort outside the resolved
harness's vocabulary, or any effort for a mapping-less settings-defined harness) / `model-invalid`
(L16 — model knob for a settings-defined harness with no modelFlag) / `level-invalid` (L16 — a
dispatch level outside leaf|master|portfolio) / `bad-kind`. `SpawnAgentSessionResponse` is a strict
The HFX-L4 leaf-ref refusals (`leaf-ref-not-found` / `leaf-ref-ambiguous`) are also modeled for spawn
because a bad leaf key is refused before tmux or catalog mutation.
`SpawnAgentSessionResponse` is a strict
`ToolResponse` with operation `spawn_agent_session`, the `session`, optional `harness`/`kind`/`leafKey`/
`label`/`cwd`/`tmuxName`, the spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`) recorded
on the catalog row for the dashboard orchestration tree, the optional `spawnRole` (L14 — the
`AR_SPAWN_ROLE` persisted on the row, the Chats command-tree grouping key), the L16 level provenance
(`spawnLevel` + `spawnLevelSource` — the resolved dispatch level and whether it was explicit or
defaulted), the L16 free-form spawn provenance as recorded on the row (`launchArgs` verbatim argv,
`promptKeywords` prepended to the brief, `sessionCommands` — the RESOLVED post-launch paste list —
plus `sessionCommandsDelivered`, whether every session command was capture-verified AND submitted),
the `ownerSession` set on `leaf-taken`, the context-delivery outcome (`contextDelivered` /
`submitted` — `contextDelivered` is true ONLY after a pane capture proves the payload landed, the
260707-HFX-L3 contract; the SF-1 blind seat was a `true` here over a clean-booted pane), the
`deliveryCapture` loud-failure evidence (the final pane capture, attached whenever any delivery
outcome reports `False`; absent on full success — a blind seat is diagnosed from the payload
itself, never trusted from a bare boolean), and a `detail` for the refusals.

### Conventions

The model duplicates the status literal locally rather than importing the serving helper, keeping the
response-model layer independent of serving implementation code.

### Invariants And Boundaries

- This is an AR-owned response shape and should stay strict.
- Nullable fields default to `None` so `_tool_payload(..., exclude_none=True)` can omit absent
  previous-owner/conflict data without failing validation.
- `ok` and token metadata come from the inherited `ToolResponse` envelope.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; this is an internal response contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The response fields are defined by the local MCP payload and catalog assignment behavior. | L9-L21 | [terminal.py](terminal.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The attach payload builder returns the exact fields modeled here, including leaf-ref refusal statuses and details. | attach_terminal_session_to_leaf_payload | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The spawn payload builder returns the `SpawnAgentSessionResponse` fields incl. leaf-ref refusals, spawned-by provenance, and context-delivery outcome. | spawn_agent_session_payload | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The response registry maps `attach_terminal_session_to_leaf` and `spawn_agent_session` to these strict models. | L82-L88; L111-L114 | [tool_registry.py](tool_registry.py) |
| Conformance coverage includes a representative missing-session (attach) and unknown-harness (spawn) refusal payload for the models. | L88-L107 | [../../../tests/test_tool_response_conformance.py](../../../tests/test_tool_response_conformance.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The model validates a local MCP response and has no external boundary. | - | - |

## Update History

- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `SpawnAgentSessionResponse`
  gained `deliveryCapture` (`str | None = None`) — the final pane capture attached whenever any
  delivery outcome reports `False`, absent on full success — and the delivery-field comments now
  state the capture-verified contract. Additive; omitted when `None`. Verification metadata pinned
  until closeout stamps the HFX-L3 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: terminal response models gained the strict leaf-ref refusal
  statuses (`leaf-ref-not-found` / `leaf-ref-ambiguous`), and attach responses gained optional `detail`
  for resolver errors. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `SpawnAgentSessionStatus` gained the
  pre-spawn refusals `effort-invalid` / `model-invalid` / `level-invalid`;
  `SpawnAgentSessionResponse` gained the free-form spawn provenance (`launchArgs` /
  `promptKeywords` / `sessionCommands` / `sessionCommandsDelivered`) and the level provenance
  (`spawnLevel` / `spawnLevelSource`) — all additive `None`-default fields omitted when absent.
  Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:58:30+02:00 — 260703-L14 (visual hierarchy + chat grouping): `SpawnAgentSessionResponse`
  gained the optional `spawnRole` field (`str | None = None`) mirroring the new catalog column —
  additive, omitted from payloads when the spawn carried no AR_SPAWN_ROLE.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2: added `SpawnAgentSessionStatus` + the strict `SpawnAgentSessionResponse`
  contract for the agent-facing `spawn_agent_session` dispatch tool (spawned-by provenance,
  context-delivery outcome, and the server-arbitrated `leaf-taken` / pre-spawn refusal statuses). Follows
  the existing strict `ToolResponse` pattern. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-02T17:04+02:00 — L9: created the strict `AttachTerminalSessionToLeafResponse` contract for
  the agent-facing terminal leaf reassignment tool. Verification metadata pinned to the task base until
  closeout stamps the L9 commit.
