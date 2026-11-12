# mcp/tests/test_enclosure_doctrine_parity.py

## Governing Overview

[overview](overview.md)

## Purpose

Holds the doctrine parity a scoped repair needs: the MCP tool reference's cleanup and abandon rows name the
bounded pre-locator exception, and every next action a document names exists as a registered operation.

## Code Commentary

### Logic

`MCP_TOOLS` names `docs/reference/mcp-tools.md`.

- **References.** `test_mcp_reference_rows_name_exception` keeps the cleanup and abandon reference rows naming
  the bounded pre-locator path and the recorded why, and `test_documented_next_actions_are_registered` requires
  `worktree_enclosure_adopt`, `worktree_cleanup`, `worktree_abandon` and `task_doc` in `public_roster` and the
  `archive_sprint` operation in the task tool registration.

### Conventions

The cases read the reference document and the task registration source by path rather than a copy in the test.

### Invariants And Boundaries

- A documented next action that is not a registered operation is a defect.

## Evidence


- The MCP reference rows' bounded pre-locator exception and the registration of every documented next action are pinned. [1]
