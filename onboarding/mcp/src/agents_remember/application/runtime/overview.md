# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-30T17:08:05+02:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5` |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Hot Path Summary

Use `startup.py` for trusted MCP process preparation, application collaborators, and the typed
serving-build gateway used by MCP registration; use `install.py` for runtime-install delegation
and `skills.py` for packaged skill deployment.

## What Belongs Here

Focused application entry points that bind runtime configuration to startup, runtime installation,
or skill installation. Provider, benchmark, worktree, memory, and task operations remain in their
own application modules.

## Operating Model

Startup declares process trust before configuration-backed authority is used, migrates the
MCP-owned durable logs, installs ambient lifecycle state, exposes the cached serving-build as a
strict wire payload to the higher-ranked MCP adapter, and optionally starts dashboard supervision.
Installation modules remain thin translations into their service owners.

## Local Invariants And Traps

- Do not introduce a package-level mega-facade or import-time process mutation.
- Keep live coordination ownership separate from the dashboard-owned notifier log.
- MCP adapters do not import serving-domain owners directly; startup owns that application seam.
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
| Startup owns MCP process declaration, collaborator installation, and the serving-build payload gateway. | `declare_mcp_process`; `initialize_mcp_application`; `mcp_serving_build_payload`; `prepare_mcp_process` | mcp/src/agents_remember/application/runtime/startup.py:22-44 |
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

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: recorded the typed application boundary
  between MCP registration and serving-build ownership. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — Created for the L23 package move that groups runtime startup, runtime install, and skill install application operations without adding a new facade. Verification metadata remains closeout-owned.
