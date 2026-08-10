# mcp/src/agents_remember/application/server_startup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/server_startup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-10T18:31+02:00 |
| lastVerifiedCommitHash | `7b6c8d8eee67c654a11a58ed1d3476db004b8d6e` |
| lastVerifiedCommitDate | 2026-08-10T22:27:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Application-owned startup operations for MCP trust declaration, application composition, and
optional dashboard supervision.

## Code Commentary

### Logic

Module-level surface:

- `initialize_mcp_application` (function, lines 15-17) — Install the process-wide application collaborators used by registered operations.
- `declare_mcp_process` (function, lines 22-24) — Declare trusted MCP execution before authority settings are loaded.
- `prepare_mcp_process` (function, lines 27-30) — Idempotently retain the MCP declaration, then start optional dashboard supervision.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- `mcp/server.py::main` calls `declare_mcp_process` before `load_config`; moving the declaration
  after config loading would route worktree-hosted MCP code into checkout CLI mode.
- `prepare_mcp_process` deliberately reasserts the same idempotent declaration before supervision,
  preserving the application operation for existing callers without a second source of state.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `initialize_mcp_application` (lines 15-17) — Install the process-wide application collaborators used by registered operations.. | `initialize_mcp_application` | mcp/src/agents_remember/application/server_startup.py:15-17 |
| Declares trusted MCP execution before config loading. | `declare_mcp_process` | mcp/src/agents_remember/application/server_startup.py:22-24 |
| Reasserts MCP trust and starts optional dashboard supervision. | `prepare_mcp_process` | mcp/src/agents_remember/application/server_startup.py:27-30 |

## Update History

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: split out the idempotent pre-config MCP trust
  declaration while preserving `prepare_mcp_process` as the supervision operation. Verification
  metadata remains pinned until approved closeout.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
