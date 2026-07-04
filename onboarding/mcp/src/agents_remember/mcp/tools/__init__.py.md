# mcp/src/agents_remember/mcp/tools/__init__.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/mcp/tools/__init__.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-04T12:31+02:00                     |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141`                                        |
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Facade that preserves the public import surface of the former `mcp/tools.py`.
L11 re-exports `task_reopen_payload` from `.task_doc` — the task-domain payload
module — not from `.worktree`.

## Code Commentary

### Logic

Re-exports the shared constants and `_tool_payload` from `base`, and every
`*_payload` builder from the domain submodules (`core`, `gates`, `lifecycle`,
`lifecycle_finalize`, `memory`, `operator_inbox`, `orchestration`, `providers`, `terminal`, `worktree`, `benchmark`,
`task_doc`).
Task 25 keeps the split gate/block/wait builders re-exported for internal
compatibility and tests while making `lifecycle_gate_payload` the only public
agent-facing gate junction. `__all__` lists the full builder import surface, not
only the advertised MCP tools.

### Invariants And Boundaries

- Consumers import builders from `agents_remember.mcp.tools` regardless of which
  submodule owns them; the facade must keep re-exporting the full set.
- Re-exporting a builder here does not make it an advertised MCP tool; `server.py`
  and `PUBLIC_TOOLS` define that public surface.
- `_tool_payload` is re-exported with `from .base import _tool_payload as
  _tool_payload` so the conformance test's `tools._tool_payload` attribute
  access resolves and Ruff/Pyright treat it as an intentional re-export.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Conformance test reaches `tools._tool_payload`. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |
| `gate_response_wait_payload` is imported from `gates` and listed in `__all__`. | [__init__.py](agents-remember/mcp/src/agents_remember/mcp/tools/__init__.py) |
| The gate response wait payload builder owned by the `gates` submodule. | [gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The inbox payload builders re-exported by this facade. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The orchestration nudge payload builder re-exported by this facade. | [orchestration.py](agents-remember/mcp/src/agents_remember/mcp/tools/orchestration.py) |
| The lifecycle finalizer payload builder re-exported by this facade. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py) |
| The terminal payload builders (`attach_terminal_session_to_leaf_payload`, `spawn_agent_session_payload`) re-exported by this facade. | [terminal.py](terminal.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: the new `orchestration` tools submodule joins
  the facade exports with `orchestration_nudge_manager_payload`, preserving the
  package-wide import surface pattern. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — No content impact: L2 adds `spawn_agent_session_payload` to the `terminal`
  import block and `__all__` exactly per the documented re-export pattern; the facade contract this
  sidecar describes — re-export every `*_payload` builder regardless of owning submodule — is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:30+02:00 — L11 re-exports `task_reopen_payload` from the task-domain payload module.
- 2026-07-02T17:04+02:00 — L9: the new `terminal` tools submodule joins the facade exports with
  `attach_terminal_session_to_leaf_payload`, preserving the package-wide import surface pattern.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — No content impact: task 28 adds `lifecycle_turn_end_notification_payload` (the NOTIFY-AND-CONTINUE turn-end builder) to the `lifecycle` import block and `__all__` exactly per the documented re-export pattern; the facade contract this sidecar describes — re-export every `*_payload` builder regardless of owning submodule — is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: documented that the facade still exports split gate/block/wait compatibility builders while the advertised MCP surface uses `lifecycle_gate` for live agent gate choreography.
- 2026-06-25T07:17+02:00 — Task 19: the `gates` submodule facade exports now include `gate_response_wait_payload` alongside create/decide/wait/list. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: the new `lifecycle_finalize` submodule joined the facade exports (`lifecycle_finalize_task_payload`). Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: the new `operator_inbox` submodule joined the facade exports (`operator_inbox_post_payload`/`operator_inbox_poll_payload`/`operator_inbox_consume_payload`). Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: the new `gates` submodule joined the facade exports (`gate_create_payload`/`gate_decide_payload`/`gate_wait_payload`/`gate_list_payload`); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: the new `task_doc` submodule joined the facade exports (`task_doc_payload`); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: the new `lifecycle` submodule joined the facade exports (the six `lifecycle_*` builders); added it to the documented submodule list. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — No content impact: `direct_closeout_preview_payload`/`direct_closeout_apply_payload` left the facade exports (issue #62 worktree-only closeout) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-10T09:56+02:00 — No content impact: `worktree_sync_payload` joined the facade exports (GitHub #54 sub-task D) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_payload` to the tools-package facade exports for the new abandon tool.
- 2026-05-29T18:35+02:00: Created as the package facade when `mcp/tools.py` was split (commit `01f503d`).
