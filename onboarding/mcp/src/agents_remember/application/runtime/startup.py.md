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
the serving domain directly. The tool-event writer stays at startup as boot-time caller identity capture: its ToolEventWriter and EventStore constructors retain references, a lock and a counter; those constructors start no thread, poll or write. This account is bounded to these collaborators.

`measuring_build_stamp` is the second reader of that same process-cached identity, and it
exists because of the measurement D-33 recorded: the MCP surface answers a tool call from a **fixed**
serving build while the candidate under curation may carry different code, and until this stamp existed
a checklist reader could not tell a candidate-ruler count from a serving-build-ruler count. It returns
`{"servingBuild": <resolved payload as wire JSON>}` — a dict copy of the identity
`process_serving_build()` resolved once per process, not a probe — with `dirty` riding along so an
uncommitted serving tree reads as such instead of being taken for the commit it names. Its consumers are
the memory-quality controller's three public entry points and the two citation tools; the omission of
`drift_check` is deliberate, because a tree-integrity count is not a curation count.

### Conventions

MCP process ownership is declared before authority settings load. `prepare_mcp_process()` only repeats that declaration. After producing a tools/list answer, the server schedules `start_after_discovery(config)` with `loop.call_soon`; a client that never lists reaches the same owner at its first tool call. `_PostDiscoveryStartLatch` marks one process attempt under a lock, starts the outside-scratch reconciliation, and then invokes optional dashboard autostart only when a config is present. The sweep starts even for a bare no-config server, which consumes the same latch; without a config it starts no dashboard. Later lists or calls launch neither piece again. Application collaborator installation is not a removed-store migration path.

### Invariants And Boundaries

- MCP startup neither reads nor migrates the retired notifier/seat stores. The post-discovery outside-scratch reconciliation reads product root markers and retained terminal records in its child process to decide which generations are proven ended.
- The workspace Event River writer is the application collaborator; session lifecycle state is not installed.
- No dual-schema reader is installed.
- MCP transport reaches serving identity through this application entry point only.

### Todos

None.

## Evidence

- The workspace tool writer installs without an ambient lifecycle or removed-store migration. [1]
- Tool-event startup retains boot-time caller identity through light constructors, with no constructor write or thread. [3]


## Outside-scratch reconciliation

`start_after_discovery` reaches `start_outside_scratch_reconcile()` once after discovery or through the first-call fallback. The latter starts the daemon thread named `outside-scratch-reconcile`. Its wrapper calls `reconcile_outside_scratch_roots()`, which runs the heavy worktree-owned sweep in a one-shot child process through the same Python executable, with stdin disconnected from the MCP transport, a 600-second timeout and a captured JSON report. The heavy worktree import occurs in that child, so this serving process does not import the package as part of the sweep. Thread-launch and sweep failures are caught and logged rather than refusing server service; a nonzero child result is raised into that contained wrapper. A pass deletes a root only when its marker, the retained contract record and a terminal-archived locator agree that the generation ended; other roots are reported with a reason and retained. Sorted JSON is logged only when the report contains removed or reported roots.

- Process preparation only declares ownership. A produced tools/list answer schedules the one joint post-discovery start; a first tool call is its fallback. The first attempt starts the sweep even without config and consumes the latch; dashboard supervision needs config and respects autoStart. The sweep runs in a child with MCP stdin disconnected, keeping the heavy worktree owner out of the serving process. [2]
