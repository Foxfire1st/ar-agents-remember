# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Hot Path Summary

Use `startup.py` for trusted MCP process preparation and application collaborators, `install.py`
for the typed runtime-install delegation, and `skills.py` for packaged skill deployment.

## What Belongs Here

Focused application entry points that bind runtime configuration to startup, runtime installation,
or skill installation. Provider, benchmark, worktree, memory, and task operations remain in their
own application modules.

## Operating Model

Startup declares process trust before configuration-backed authority is used, migrates the
MCP-owned durable logs, installs ambient lifecycle state, and optionally starts dashboard
supervision. Installation modules remain thin translations into their service owners.

## Local Invariants And Traps

- Do not introduce a package-level mega-facade or import-time process mutation.
- Keep live coordination ownership separate from the dashboard-owned notifier log.
- Runtime and skill install entry points accept typed config/options; they do not accept arbitrary
  host roots that bypass resolved settings.

## File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`install.py.md`](install.py.md) — runtime installation application entry point.
- [`skills.py.md`](skills.py.md) — skill installation application entry point.
- [`startup.py.md`](startup.py.md) — MCP process trust, migration, ambient state, and supervision.

## Child Overviews

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Startup owns MCP process declaration and collaborator installation. | `declare_mcp_process`; `initialize_mcp_application`; `prepare_mcp_process` | mcp/src/agents_remember/application/runtime/startup.py:20-36 |
| Runtime installation is a thin typed delegation. | `run_runtime_install` | mcp/src/agents_remember/application/runtime/install.py:15-19 |
| Skill installation resolves the configured harness skill root and delegates the copy. | `skills_install_tool` | mcp/src/agents_remember/application/runtime/skills.py:13-30 |

## Docs References

No Domain Documentation source is configured.

## Cross-Repo References

No cross-repository implementation dependency governs this route.

## How To Use This Area

Start from the operation-specific sidecar, then follow its service-layer references for mechanics.
Keep MCP payload/registration concerns at their own routes.

## Update History

- 2026-08-13T08:40+02:00 — Created for the L23 package move that groups runtime startup, runtime install, and skill install application operations without adding a new facade. Verification metadata remains closeout-owned.
