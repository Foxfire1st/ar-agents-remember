# mcp/tests/test_session_start_hook.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects generated startup hooks: a host-recorded product role receives no ambient free-chat directive; every indeterminate case receives the directive without failing session start.

## Code Commentary

### Logic

The tests run committed Claude, Codex, Cursor and VSCode hook processes with made-up PASEO_HOME and PASEO_AGENT_ID and compare exact generated text. Suppression requires the selected agent’s host record with ar.role; absent labels, another agent’s record, unreadable/wrong-shaped JSON, missing host variables and malformed IDs all speak. AR tool-server binding variables alone are not hook identity.

### Invariants And Boundaries

The hook must not expose unrelated host-record title text or accept path-traversal-shaped agent IDs. These fixtures prove the hook-process boundary only, not host execution or every provider’s MCP policy.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Generated session-start hook process tests: implementation/assertion boundary described above. [1]
