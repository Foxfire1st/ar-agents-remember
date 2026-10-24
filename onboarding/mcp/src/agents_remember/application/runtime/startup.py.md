# mcp/src/agents_remember/application/runtime/startup.py

## Governing Overview

[overview](overview.md)

## Purpose

Initializes MCP-process application collaborators and owns the one application-layer gateway that
hands the MCP adapter its boot-resolved serving-build payload. Since `260915-KS-L23` it also owns the
**ruler stamp** the measuring surfaces carry, so a memory-quality or citation count says which build
produced it.

## Code Commentary

### Logic

`initialize_mcp_application` installs the workspace-river tool writer (`build_tool_event_writer`)
without installing ambient session state or reading or migrating removed durable stores: the launch binding and its task
document are snapshotted once here, so a server started a second ago writes at its first
call; an unreadable binding changes nothing about startup. `mcp_serving_build_payload` converts the cached serving
stamp to the strict shared wire model at the application boundary; MCP registration never imports
the serving domain directly. Dashboard autostart remains a separate startup hook.

`measuring_build_stamp` (`:36-51`) is the second reader of that same process-cached identity, and it
exists because of the measurement D-33 recorded: the MCP surface answers a tool call from a **fixed**
serving build while the candidate under curation may carry different code, and until this stamp existed
a checklist reader could not tell a candidate-ruler count from a serving-build-ruler count. It returns
`{"servingBuild": <resolved payload as wire JSON>}` — a dict copy of the identity
`process_serving_build()` resolved once per process, not a probe — with `dirty` riding along so an
uncommitted serving tree reads as such instead of being taken for the commit it names. Its consumers are
the memory-quality controller's three public entry points and the two citation tools; the omission of
`drift_check` is deliberate, because a tree-integrity count is not a curation count.

### Conventions

MCP process ownership is declared before authority settings load; `prepare_mcp_process` starts the outside scratch reconcile on its own daemon thread and then runs optional dashboard autostart. Application collaborator installation is not a removed-store
migration path.

### Invariants And Boundaries

- MCP startup neither reads nor migrates the retired notifier/seat stores, and the outside scratch reconcile it starts on another thread reads the product's own root markers and the retained terminal records that prove a generation ended.
- The workspace Event River writer is the application collaborator; session lifecycle state is not installed.
- No dual-schema reader is installed.
- MCP transport reaches serving identity through this application entry point only.

### Todos

None.

## Evidence

- The workspace tool writer installs without an ambient lifecycle or removed-store migration. [1]
- MCP ownership declaration and optional dashboard autostart precede application initialization. [2]

## 260928-MIK-L198 — The tool-server start sweeps roots off the startup thread

`prepare_mcp_process` calls `start_outside_scratch_reconcile()` after `declare_mcp_process()` and before `maybe_autostart_dashboard(config)`. `start_outside_scratch_reconcile` starts a daemon thread named `outside-scratch-reconcile` that runs `reconcile_outside_scratch_roots()` from `outside_scratch_reconcile.py`, so the scan never runs on the startup thread and cannot delay or break the stdio handshake. `_reconcile_outside_scratch_roots` catches any exception, logs it with `logger.exception`, and returns, so a failed sweep is never a reason for a server not to start. A pass deletes a root only when the marker inside it, the retained contract record and a terminal-archived locator agree that the generation ended; every other root is reported with one reason and left in place. The report is logged as sorted JSON only when it removed or reported something.
