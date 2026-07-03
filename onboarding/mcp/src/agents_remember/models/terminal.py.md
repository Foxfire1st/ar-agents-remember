# mcp/src/agents_remember/models/terminal.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/models/terminal.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-02T17:04+02:00                       |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`   |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[models overview](overview.md)

## Purpose

`terminal.py` defines strict Pydantic response contracts for MCP tools that expose dashboard
terminal-session catalog operations. It currently models the hosted-chat/terminal leaf reassignment
tool added for L9.

## Code Commentary

### Logic

`LeafAssignmentStatus` is the closed response vocabulary for assignment attempts:
`attached`, `leaf-taken`, or `unknown-session`. `AttachTerminalSessionToLeafResponse` is a strict
`ToolResponse` with operation `attach_terminal_session_to_leaf`, the requested session and `leafKey`,
the optional prior binding (`previousLeafKey`), optional conflict owner (`ownerSession`), and optional
role (`chat` or `terminal`).

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
| The payload builder returns the exact fields modeled here: status, session, leafKey, previousLeafKey, ownerSession, and role. | L30-L42 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The response registry maps `attach_terminal_session_to_leaf` to this strict model. | L78-L82; L105-L111 | [tool_registry.py](tool_registry.py) |
| Conformance coverage includes a representative missing-session payload for the new model. | L88-L102 | [../../../tests/test_tool_response_conformance.py](../../../tests/test_tool_response_conformance.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The model validates a local MCP response and has no external boundary. | - | - |

## Update History

- 2026-07-02T17:04+02:00 — L9: created the strict `AttachTerminalSessionToLeafResponse` contract for
  the agent-facing terminal leaf reassignment tool. Verification metadata pinned to the task base until
  closeout stamps the L9 commit.
