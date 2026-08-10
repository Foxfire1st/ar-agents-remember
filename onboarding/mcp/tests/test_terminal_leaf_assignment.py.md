# mcp/tests/test_terminal_leaf_assignment.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_leaf_assignment.py`      |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_leaf_assignment.py` covers the shared catalog reassignment helper and its MCP payload
wrapper. It is pure filesystem/unit coverage for moving a hosted terminal/chat session's durable
`leafKey` without spawning a session or touching tmux.

## Code Commentary

### 260707-HFX2-L17 Attach Pair Regressions

Tests cover spawn-role defaulting, explicit role claim for a hand-opened harness, `role-required`
when untyped, atomic role changes, different-role coexistence, live same-role refusal, and dead
same-role supersession with the stale row marked exited.

### Logic

The `_entry` helper seeds running harness catalog rows with deterministic timestamps. The tests cover
three L9 contracts: `assign_terminal_session_to_leaf` moves an existing row and reports the previous
leaf; a same-role `leaf-taken` conflict reports the owner without mutating the seeker row; and
`attach_terminal_session_to_leaf_payload` uses `terminal_catalog_path(config.coordination_root)`, first
normalizes the requested leaf ref against a real temp task tree, and returns the modeled `attached`
payload fields while updating the dashboard catalog. HFX-L4 also pins the invalid-ref path: a missing leaf
returns `leaf-ref-not-found` with expected-form detail and leaves the existing catalog row unchanged.

### Conventions

Uses `unittest`, `tempfile.TemporaryDirectory`, and the same `sys.path` insertion pattern as adjacent MCP
tests.

### Invariants And Boundaries

- This file intentionally does not exercise FastAPI, WebSocket, tmux, or browser state.
- The conflict regression must assert no mutation of the previous leaf, since callers rely on
  `leaf-taken` not changing local state or injecting context.
- The payload test proves the agent-facing tool and browser-facing route share the same catalog path and
  assignment helper.
- Payload-level assignment persists canonical qualified leaf keys, not legacy stems.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; the behavior is local catalog/tool policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests pin internal dashboard catalog reassignment behavior, not an external protocol. | `TerminalLeafAssignmentTests` | mcp/tests/test_terminal_leaf_assignment.py:109-250 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared assignment helper under test returns `attached`, `leaf-taken`, or `unknown-session` and mutates only on success. | `assign_terminal_session_to_leaf` | mcp/src/agents_remember/serving/terminal_leaf_assignment.py:53-114 |
| The MCP payload builder under test opens the dashboard catalog path and validates the response through `_tool_payload`. | `attach_terminal_session_to_leaf_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:26-43 |
| The shared leaf-ref resolver and serving adapter normalize accepted refs before catalog writes. | `resolve_catalog_leaf_key` | mcp/src/agents_remember/serving/leaf_ref_validation.py:18-46 |
| Existing catalog behavior provides the `with_leaf_binding` write point and role-scoped active owner lookup these tests exercise indirectly. | "def with_leaf_binding(" | mcp/src/agents_remember/models/terminal_catalog.py:382-399 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests cover local MCP/serving behavior only. | - | - |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 4 citation claims; scoped recheck clean (0 findings).

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: expanded assignment coverage across role resolution,
  pair arbitration, dead-holder replacement, and atomic rebind.

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: added task-doc fixtures so the MCP attach payload
  normalizes a legacy leaf slug to the canonical qualified key, and added invalid-ref no-mutation
  coverage. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-02T17:04+02:00 — L9: created focused regression coverage for successful reassignment,
  `leaf-taken` no-mutation behavior, and the agent-facing payload builder using the dashboard catalog.
  Verification metadata pinned to the task base until closeout stamps the L9 commit.
