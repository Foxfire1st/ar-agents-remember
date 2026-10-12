# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |

## Governing Overview

[application overview](../overview.md)

## What This Area Is

This package binds runtime configuration to the application's MCP startup, runtime-install and skill-install operations. It supplies the application seam between transport registration and the lower services; provider, benchmark, worktree, memory and task operations remain in their own application modules.

## Hot Path Summary

Use `startup.py` for trusted MCP process preparation, application collaborators and the typed serving-build gateway. Use `install.py` for runtime-install composition and `skills.py` for packaged skill deployment.

## How It Is Built

### Startup and measurement identity

Startup declares MCP process ownership before authority settings are loaded. Application initialization migrates control-plane identity logs without taking ownership of the agent notifier signals, installs the ambient lifecycle store and installs the tool-event writer. The event writer captures this server's caller from its launch binding; an unreadable binding is treated as an unbound chat for event recording rather than preventing startup. Optional dashboard supervision is separate from collaborator initialization.

`mcp_serving_build_payload()` exposes the process's cached boot identity to MCP registration. `measuring_build_stamp()` wraps that payload as `servingBuild`: version, boot time, source digest, Python executable, package root, commit and dirty state name the producer of a measurement. That producer can differ from the candidate being measured; a serving-build count must not be represented as execution by the candidate's code. The boot identity is resolved once, so requesting the stamp copies the payload rather than probing each time.

### Installation

Runtime installation delegates to the lower runtime service, then provisions or previews the configured host. The entry retains the earlier result, adds the host report as `host`, and conjoins the earlier and host `ok` values: a failed host step makes the combined result false without discarding the earlier steps.

Skill installation requires the configured harness skill root and passes the dry-run, overwrite and archive-existing choices to the lower copy service.

### File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`install.py.md`](install.py.md) — runtime installation and host-result composition.
- [`skills.py.md`](skills.py.md) — configuration-bound skill installation.
- [`startup.py.md`](startup.py.md) — MCP trust declaration, identity migration, ambient/event collaborators, measurement identity and optional supervision.

There are no child overviews. Begin with the operation's file card and follow its lower-service references; MCP payload and registration mechanics remain in their own routes.

## Invariants And Boundaries

- Keep these entry points focused; do not introduce a package-wide mega-facade or import-time process mutation.
- Keep live coordination ownership separate from the dashboard-owned agent notifier log.
- MCP adapters reach serving-build identity through this application seam, not by importing serving-domain owners directly.
- Installation accepts typed configuration/options, not arbitrary host roots that bypass resolved settings.
- A source checkout's execution mode is an authority boundary, not a diagnostic convenience. Undeclared primary-checkout execution refuses; undeclared linked-checkout execution selects disposable leaf-local coordination rather than live authority. An ordinary measurement must use its admitted producer, not imitate a trusted daemon or pytest declaration to reach another root. Checkout isolation does not claim to sandbox arbitrary Python or shell filesystem access.

No Domain Documentation source is configured. No cross-repository implementation dependency governs this route.

## Evidence

- Startup owns MCP process declaration, collaborator installation, and the serving-build payload gateway. [1]
- Measurement identity names the cached serving producer, not the candidate being measured. [5]
- Undeclared source-checkout execution is isolated or refused, rather than admitted to live coordination by a diagnostic workaround. [6]

- Runtime installation composes the lower service result with the public host step at the application entry. [2]
- Skill installation resolves the configured harness skill root and delegates the copy. [3]
- The composition with the host part. [4]
