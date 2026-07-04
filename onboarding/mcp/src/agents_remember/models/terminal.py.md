# mcp/src/agents_remember/models/terminal.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/models/terminal.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-04T11:10+02:00                       |
| lastVerifiedCommitHash | `3c592f76ed607e4c0391fd26d77b869ee837a5af`   |
| lastVerifiedCommitDate | 2026-07-04T11:44:59+02:00|
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
`attached`, `leaf-taken`, or `unknown-session`. `AttachTerminalSessionToLeafResponse` is a strict
`ToolResponse` with operation `attach_terminal_session_to_leaf`, the requested session and `leafKey`,
the optional prior binding (`previousLeafKey`), optional conflict owner (`ownerSession`), and optional
role (`chat` or `terminal`).

`SpawnAgentSessionStatus` is the L2 vocabulary: `spawned` (the only `ok: true` case), `leaf-taken`
(the server-arbitrated refusal, never overridden), and the pre-spawn validation refusals
`harness-unknown` / `harness-not-detected` / `bad-kind`. `SpawnAgentSessionResponse` is a strict
`ToolResponse` with operation `spawn_agent_session`, the `session`, optional `harness`/`kind`/`leafKey`/
`label`/`cwd`/`tmuxName`, the spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`) recorded
on the catalog row for the dashboard orchestration tree, the `ownerSession` set on `leaf-taken`, the
context-delivery outcome (`contextDelivered` / `submitted`), and a `detail` for the refusals.

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
| The attach payload builder returns the exact fields modeled here: status, session, leafKey, previousLeafKey, ownerSession, and role. | L39-L51 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The spawn payload builder returns the `SpawnAgentSessionResponse` fields incl. spawned-by provenance and context-delivery outcome. | L171-L211 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The response registry maps `attach_terminal_session_to_leaf` and `spawn_agent_session` to these strict models. | L82-L88; L111-L114 | [tool_registry.py](tool_registry.py) |
| Conformance coverage includes a representative missing-session (attach) and unknown-harness (spawn) refusal payload for the models. | L88-L107 | [../../../tests/test_tool_response_conformance.py](../../../tests/test_tool_response_conformance.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The model validates a local MCP response and has no external boundary. | - | - |

## Update History

- 2026-07-04T11:10+02:00 — L2: added `SpawnAgentSessionStatus` + the strict `SpawnAgentSessionResponse`
  contract for the agent-facing `spawn_agent_session` dispatch tool (spawned-by provenance,
  context-delivery outcome, and the server-arbitrated `leaf-taken` / pre-spawn refusal statuses). Follows
  the existing strict `ToolResponse` pattern. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-02T17:04+02:00 — L9: created the strict `AttachTerminalSessionToLeafResponse` contract for
  the agent-facing terminal leaf reassignment tool. Verification metadata pinned to the task base until
  closeout stamps the L9 commit.
