# mcp/src/agents_remember/mcp/tools/__init__.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Facade that preserves the public import surface of the former `mcp/tools.py`.
L11 re-exports `task_reopen_payload` from `.task_doc` — the task-domain payload
module — not from `.worktree`.

## Code Commentary

### Logic

Re-exports the shared constants and `_tool_payload` from `base`, and every
`*_payload` builder from the domain submodules (`core`, `gates`, `lifecycle`,
`lifecycle_finalize`, `memory`, `operator_inbox`, `orchestration`, `providers`, `terminal`, `worktree`, `benchmark`,
`task_doc`). 260707-HFX-L8 adds `session_rename_payload`/`session_retire_payload` to the `terminal`
import block and `__all__`, exactly per the documented re-export pattern.
Task 25 keeps the split gate/block/wait builders re-exported for internal
compatibility and tests while making `lifecycle_gate_payload` the only public
agent-facing gate junction. `__all__` lists the full builder import surface, not
only the advertised MCP tools. 260713-TES-L4 adds `operator_inbox_supersede_payload` to the
`operator_inbox` import block and `__all__`, exactly per the documented re-export pattern.
260815-DAG-L16 adds `direct_landing_payload` to the import block and `__all__` per the same pattern.
260815-DAG-L15 adds `memory_quality_check_start_payload` / `memory_quality_check_poll_payload` to
the `memory` import block and `__all__` per the same pattern (the async quality surface, L15-R7).
260831-LOCR-L30 adds `worktree_checkpoint_landing_payload` to the `.worktree` import block and
`__all__` per the same pattern, so the partial-master landing builder is reachable from the package
boundary the registrar imports. 260831-LOCR-L37 adds `worktree_pause_payload` the same way (import
block at `:104`, `__all__` at `:196` inside the `:115-201` extent), so the stop's payload builder is
reachable from the same boundary as the publication's.

### Invariants And Boundaries

- Consumers import builders from `agents_remember.mcp.tools` regardless of which
  submodule owns them; the facade must keep re-exporting the full set.
- Re-exporting a builder here does not make it an advertised MCP tool; `server.py`
  and `PUBLIC_TOOLS` define that public surface.
- `_tool_payload` is re-exported with `from .base import _tool_payload as
  _tool_payload` so the conformance test's `tools._tool_payload` attribute
  access resolves and Ruff/Pyright treat it as an intentional re-export.

## Evidence

### Repo-Internal References

- `gate_response_wait_payload` is imported from `gates`. [1]
- `gate_response_wait_payload` is listed in `__all__`. [2]
- The gate response wait payload builder is owned by the `gates` submodule. [3]
- The post payload builder is owned by the `operator_inbox` submodule. [4]
- The poll payload builder is owned by the `operator_inbox` submodule. [5]
- The consume payload builder is owned by the `operator_inbox` submodule. [6]
- The inbox payload builders (post/poll/consume/supersede since 260713-TES-L4) are re-exported by this facade. [7]
- The orchestration nudge payload builder is owned by the `orchestration` submodule. [8]
- The orchestration nudge payload builder is re-exported by this facade. [9]
- The lifecycle finalizer payload builder is owned by the `lifecycle_finalize` submodule. [10]
- The lifecycle finalizer payload builder is re-exported by this facade. [11]
- The terminal payload builders (`attach_terminal_session_to_task_payload`, `spawn_agent_session_payload`, `session_retire_payload`, `session_rename_payload`) are owned by the `terminal` submodule. [12]
- The terminal payload builders are re-exported by this facade. [13]

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260815-DAG-L3 Queue Payload Export

The tool package now exports `closeout_queue_payload`, keeping the registered task-tool import on
the same curated payload surface as the other public MCP tools.

## 260815-DAG-L15 Async Memory-Quality Exports

The facade re-exports `memory_quality_check_start_payload` and `memory_quality_check_poll_payload`
(the async quality surface, L15-R7) from `.memory` in the import block and `__all__`, exactly per
the documented re-export pattern.

## 260821-CLIVE-L2 Current Contract

The current source seams include the module-level vocabulary. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- The current module exposes the module-level vocabulary at this ownership boundary; the anchor is the stop builder's own `__all__` entry, which pins the list this claim is about. [14]
- The pause payload builder is re-exported by this facade from the `.worktree` import block and listed in the `__all__` extent, exactly per the documented pattern. [15]

## 260821-CLIVE Closeout-Door Export

The tools package now exports `closeout_door_payload` alongside the disposable
`closeout_queue_payload`. The former publishes or observes canonical contract-owned scheduling
intent; the latter only reads/rebuilds its current projection. Exporting both does not merge their
authority or introduce a compatibility alias.

## MCAR-L02 Adapter Export

The package exports `curator_coherence_payload` alongside the existing task/door adapters so the
task registrar imports the one canonical payload boundary. This is wiring only; it creates no
second action implementation.

## 260831-CCR-L15 Status-Wait Export

**Superseded.** The `worktree_status_wait_payload` builder and its tool were removed; this facade
re-exports no wait payload today. Recorded so the paragraph above is not read as current.
