# mcp/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/README.md`                            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T14:15+02:00                     |
| lastVerifiedCommitHash | `412342847484b23136bdc7a41a0d3ec8804a761b` |
| lastVerifiedCommitDate | 2026-05-29T16:22:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package and the de-facto pre-MCP bootstrap doc. It opens
with an agent-driven Quickstart, then documents requirements, install/run
(uvx-first), a starter settings block, harness registration, the first setup MCP
calls, and the high-level tool surface.

## Code Commentary

### Logic

The README is self-contained for the bootstrap so it works from the rendered
PyPI page without a source checkout. It leads with a three-step "ask your agent
to" Quickstart — (1) wire the MCP via
`uvx agents-remember-mcp --config <abs settings.json>` + author the settings +
restart; (2) `runtime_install` then `skills_install`; (3) run the
`C-13-install-and-onboard` skill — then gives `uvx` as the primary install/run
path (pip as alternative), an inline minimal starter `settings.json`, the harness
registration JSON (using `uvx`), the first setup MCP calls, and the tool surface.
Project-doc links are absolute GitHub URLs so they resolve from PyPI.

### Invariants And Boundaries

- Keep this README focused on the MCP package and its bootstrap, not the whole
  product manual.
- Keep it self-contained for pip/PyPI readers: inline the starter settings and
  use absolute GitHub URLs (no source-checkout-relative `../` links that 404 on
  the PyPI page).
- Keep the run command aligned with `agents_remember.mcp.server.main()`, which
  requires `--config`; both `uvx agents-remember-mcp` and the pip console command
  invoke it.
- Keep requirements practical and package-level: Python 3.11+, uv/pip, an
  MCP-capable harness, Git, and Docker (plus Ollama for the grepai embedder) only
  when provider tools are enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The run command requires an absolute `--config` path and rejects coordinator `system/settings.json`; `uvx agents-remember-mcp` and the pip console script both call `server.main()`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. | [pyproject.toml](agents-remember-md/mcp/pyproject.toml) |
| The Quickstart hands post-scaffolding setup off to the C-13 install-and-onboard skill. | [C-13 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-13-install-and-onboard/SKILL.md) |
| The tool surface the README summarizes is exposed by the server/payload layer and catalogued in the tool reference. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [mcp-tools.md](agents-remember-md/docs/reference/mcp-tools.md) |

## Update History

- 2026-05-29T14:15+02:00: Rewrote the README as a self-contained, uvx-first bootstrap — added the 3-step "ask your agent to" Quickstart (hands off to C-13), inlined a starter `settings.json`, switched project-doc links to absolute GitHub URLs, and linked the MCP tool reference. Metadata pending closeout refresh.
- 2026-05-28T15:52+02:00: Updated after the MCP package README added the canonical source checkout link.
- 2026-05-28T15:43+02:00: Created after the MCP package gained a dedicated README and `pyproject.toml` started using it as package metadata. Verification metadata remains pinned until closeout commits the source change.
