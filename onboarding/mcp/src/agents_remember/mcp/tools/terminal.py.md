# mcp/src/agents_remember/mcp/tools/terminal.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/tools/terminal.py`   |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-02T17:04+02:00                            |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`        |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

`terminal.py` contains MCP payload builders for dashboard terminal-session catalog operations. It
currently exposes the agent-facing path for moving an already-created hosted terminal/chat session to a
durable task leaf.

## Code Commentary

### Logic

`attach_terminal_session_to_leaf_payload(config, session_id, leaf_key)` opens the dashboard terminal
catalog at `terminal_catalog_path(config.coordination_root)`, calls the serving-layer
`assign_terminal_session_to_leaf` helper, and returns the result through `_tool_payload` under the
`attach_terminal_session_to_leaf` operation. The payload reports `ok` only for `attached`, and always
includes the requested session/leaf plus optional `previousLeafKey`, `ownerSession`, and role.

### Conventions

Builders stay transport-thin: durable behavior lives in `serving.terminal_leaf_assignment`, response
validation is `_tool_payload` + `models/terminal.py`, and server registration lives in `mcp/server.py`.

### Invariants And Boundaries

- This tool mutates the same dashboard catalog as the browser route; it does not create a new terminal,
  open a WebSocket, or require a worktree enclosure.
- `leaf-taken` and `unknown-session` are successful tool responses with `ok: false`; callers branch on
  `status`, not exceptions.
- The response remains AR-owned and strict; provider-flexible models are not used here.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; this is a local MCP wrapper around the dashboard
catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The operation is defined by same-repository serving/catalog behavior rather than external documentation. | L16-L42 | [terminal.py](terminal.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The payload builder delegates durable assignment to the shared serving helper and returns previous leaf, owner, status, and role. | L16-L42 | [terminal.py](terminal.py) |
| The public tool tuple advertises `attach_terminal_session_to_leaf`. | L13-L20 | [base.py](base.py) |
| The facade re-exports `attach_terminal_session_to_leaf_payload`. | L67-L72; L86-L94 | [__init__.py](__init__.py) |
| The FastMCP server registers `attach_terminal_session_to_leaf(session_id, leaf_key)` and documents that it does not spawn or require an enclosure. | L130-L142 | [../server.py](../server.py) |
| The strict response model is registered for conformance validation. | L78-L82; L105-L111 | [../../models/tool_registry.py](../../models/tool_registry.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tool operates on the local dashboard terminal catalog only. | - | - |

## Update History

- 2026-07-02T17:04+02:00 — L9: created the agent-facing `attach_terminal_session_to_leaf` payload
  builder so agents can move their own hosted dashboard chats between task leaves without raw dashboard
  curl or browser clicks. Verification metadata pinned to the task base until closeout stamps the L9
  commit.
