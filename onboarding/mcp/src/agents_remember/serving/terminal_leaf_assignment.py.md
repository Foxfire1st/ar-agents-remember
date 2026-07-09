# mcp/src/agents_remember/serving/terminal_leaf_assignment.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_leaf_assignment.py` |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-09T14:05+02:00                                  |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`              |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_leaf_assignment.py` is the shared server-side policy for moving an existing dashboard
terminal or hosted agent-chat session to a durable task leaf after creation. It keeps the FastAPI
dashboard route and the agent-facing MCP tool on the same catalog uniqueness rules instead of
duplicating conflict logic in separate call paths.

## Code Commentary

### Logic

`LeafAssignmentResult` is a small frozen result object carrying the requested session, target leaf,
status (`attached`, `leaf-taken`, or `unknown-session`), the previous leaf when known, the conflicting
owner when any, and the session role. `leaf_conflict_owner` is the reusable role-scoped lookup over
`TerminalCatalog.active_for_leaf`: no leaf means no conflict, the same session is allowed to re-own its
leaf, and only a different running owner of the same role returns a session id.

`assign_terminal_session_to_leaf` performs the durable move. It rejects a missing or non-running row as
`unknown-session`, reports `leaf-taken` without mutating the catalog when another running same-role
session owns the target leaf, and otherwise writes `entry.with_leaf_key(leaf_key)` back through
`TerminalCatalog.upsert`. A successful move records the previous leaf in the result so tool callers can
report what changed without re-reading the catalog.

### Conventions

This file sits in `serving/` because the durable catalog and role rules are serving-layer runtime state.
MCP tools may call it, but response shaping stays in `mcp/tools/terminal.py` and Pydantic modeling stays
in `models/terminal.py`.

### Invariants And Boundaries

- Reassignment is catalog-only: it does not spawn, terminate, attach tmux clients, inspect worktrees, or
  require a leaf enclosure.
- Conflict handling is server-authoritative and role-scoped through `TerminalCatalog.active_for_leaf`;
  frontend/store checks remain advisory.
- `leaf-taken` is a no-mutation result. Callers must not update local state or inject context after this
  status.
- Only running sessions can claim leaves. Landed, exited, and terminated rows follow existing catalog
  semantics and are not treated as active owners.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation defines the dashboard terminal catalog move policy; the
same-repository catalog, route, tool, and tests are the source of truth.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this local catalog reassignment policy. | L45-L83 | [terminal_leaf_assignment.py](terminal_leaf_assignment.py) |

## Repo-Internal References

The helper is intentionally shared by the dashboard HTTP route and the agent-facing MCP tool.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Catalog rows carry role-derived leaf ownership, a `with_leaf_key` copy helper, and a running-only role-scoped `active_for_leaf` uniqueness probe. | L14-L24; L131-L138; L169-L190 | [terminal_catalog.py](terminal_catalog.py) |
| The dashboard attach route delegates the existing-session leaf move to `assign_terminal_session_to_leaf` and maps its statuses to 404/409/200 HTTP responses. | L709-L733 | [app.py](app.py) |
| The MCP payload builder calls the same helper and returns previous leaf, owner, status, and role in one validated payload. | L16-L42 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| Unit tests cover successful move, leaf-taken no-mutation behavior, and the tool payload using the dashboard catalog path. | L54-L108 | [../../../tests/test_terminal_leaf_assignment.py](../../../tests/test_terminal_leaf_assignment.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This helper mutates only the local dashboard terminal catalog. | - | - |

## Update History

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: updated the assignment boundary from
  "missing or terminated" to "missing or non-running" to match landed archive semantics; landed rows
  are inspectable/non-active and cannot claim a new leaf. Verification metadata pinned until closeout
  stamps the HFX2-L11 commit.
- 2026-07-02T17:04+02:00 — L9: created as the shared hosted-chat leaf reassignment policy. It moves an
  existing catalog row to a new durable `leafKey`, reports `leaf-taken` without mutation, and is reused by
  both FastAPI and MCP call paths. Verification metadata pinned to the task base until closeout stamps the
  L9 commit.
