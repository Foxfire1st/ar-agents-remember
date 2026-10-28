# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |

## Governing Overview

[application overview](../overview.md)

## What This Area Is

This package binds runtime configuration to the application's MCP startup and runtime-install operations. It supplies the application seam between transport registration and the lower services; provider, benchmark, worktree, memory and task operations remain in their own application modules.

## Hot Path Summary

Use `startup.py` for trusted MCP process preparation, application collaborators and the typed serving-build gateway. Use `install.py` for runtime-install composition; the skill-install entry point that used to live here is removed, because the tool server serves the canonical skills from its package copy.

## How It Is Built

### Startup and measurement identity

Startup declares MCP process ownership before authority settings are loaded. Application initialization installs the workspace tool-event writer only; it neither creates an ambient lifecycle collaborator nor migrates identity logs. The event writer captures this server's caller from its launch binding; an unreadable binding is treated as an unbound chat for event recording rather than preventing startup. Outside-scratch reconciliation and optional dashboard supervision are separate from collaborator initialization. Process preparation only declares ownership. After producing a tools/list answer, the server schedules the joint `start_after_discovery` owner with `loop.call_soon`; a first tool call reaches the same once-per-process latch for a client that never lists. The first attempt starts the sweep even without config, while dashboard autostart requires config/settings. The sweep's heavy worktree owner runs in a one-shot child with stdin disconnected from the MCP protocol; later lists or calls start neither piece again. Producing the answer is the scheduling boundary; this source order does not establish when protocol bytes reach the client.

`mcp_serving_build_payload()` exposes the process's cached boot identity to MCP registration. `measuring_build_stamp()` wraps that payload as `servingBuild`: version, boot time, source digest, Python executable, package root, commit and dirty state name the producer of a measurement. That producer can differ from the candidate being measured; a serving-build count must not be represented as execution by the candidate's code. The boot identity is resolved once, so requesting the stamp copies the payload rather than probing each time.

### Installation

Runtime installation delegates to the lower runtime service, then provisions or previews the configured host. The entry retains the earlier result, adds the host report as `host`, and conjoins the earlier and host `ok` values: a failed host step makes the combined result false without discarding the earlier steps.

Skill installation has no entry point in this package: `skills.py` was removed with the skill-install surface, and no harness skill root is resolved or written anywhere in the install path.

### File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`install.py.md`](install.py.md) — runtime installation and host-result composition.
- [`startup.py.md`](startup.py.md) — MCP trust declaration, launch-bound workspace event collaborator, measurement identity and optional supervision.

There are no child overviews. Begin with the operation's file card and follow its lower-service references; MCP payload and registration mechanics remain in their own routes.

## Invariants And Boundaries

- Keep these entry points focused; do not introduce a package-wide mega-facade or import-time process mutation.
- Keep live coordination ownership separate from the dashboard-owned agent notifier log.
- MCP adapters reach serving-build identity through this application seam, not by importing serving-domain owners directly.
- Installation accepts typed configuration/options, not arbitrary host roots that bypass resolved settings.
- A source checkout's execution mode is an authority boundary, not a diagnostic convenience. Undeclared primary-checkout execution refuses; undeclared linked-checkout execution selects disposable leaf-local coordination rather than live authority. An ordinary measurement must use its admitted producer, not imitate a trusted daemon or pytest declaration to reach another root. Checkout isolation does not claim to sandbox arbitrary Python or shell filesystem access.

No Domain Documentation source is configured. No cross-repository implementation dependency governs this route.

## Evidence

- Preparation is declaration-only. list_tools produces its answer before scheduling start_after_discovery, and call_tool reaches the same latch as fallback. The sweep attempt consumes the latch even without config; dashboard autostart needs config/settings. The heavy sweep owner is imported only in a one-shot child with stdin=DEVNULL. Source order does not attest client receipt.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py:93-127 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit dc03c64a91947cee470622c560c516854eec86b5. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Startup owns MCP process declaration, collaborator installation, and the serving-build payload gateway. [1]

- Measurement identity names the cached serving producer, not the candidate being measured. [5]

- Undeclared source-checkout execution is isolated or refused, rather than admitted to live coordination by a diagnostic workaround. [6]

- Runtime installation composes the lower service result with the public host step at the application entry. [2]

- The composition with the host part. [4]

- Startup installs only the workspace tool writer, snapshots its launch-bound caller once and falls back to an unbound chat when that binding cannot be read. [7]

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py:93-127 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit dc03c64a91947cee470622c560c516854eec86b5. Retired means the anchor no longer stands, not that the cited subject was deleted [8]
