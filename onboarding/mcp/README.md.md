# mcp/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/README.md`                            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T15:52+02:00                     |
| lastVerifiedCommitHash | `9680d150ac9d2e6c1ae04dbab42eac0088dceef8` |
| lastVerifiedCommitDate | 2026-05-28T15:55:29+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package. It documents the package-local runtime contract:
the source checkout link, Python and host requirements, the console command,
trusted MCP settings, harness restart expectations, the first setup-oriented MCP
calls, and the high-level tool surface.

## Code Commentary

### Logic

The README is deliberately narrower than the repository root README. It links
to the canonical source checkout before routing readers to the fuller project
documentation, then orients someone who is looking at the package on PyPI or
inside the `mcp/` package directory and needs to know how to run the MCP server:

```text
agents-remember-mcp --config /absolute/path/to/agents-remember-settings.json
```

The settings file is described as trusted authority that must live outside the
`ar-coordination/` runtime folder. Harness setup is shown as a generic command
plus args registration, followed by an explicit harness restart note so users
do not expect a changed MCP registration to appear in an already-running code
harness.

The README keeps manual tool names visible for setup and troubleshooting while
stating that normal use should be agent-driven once the MCP is up.

### Invariants And Boundaries

- Keep this README focused on the MCP package, not the whole product manual.
- Do not make this README the source of truth for full installation workflows;
  link to the root README and docs for the complete guide.
- Keep the checkout link pointed at the canonical public repository.
- Keep the command example aligned with
  `agents_remember.mcp.server.main()`, which requires `--config`.
- Keep the requirements practical and package-level: Python 3.11+, MCP-capable
  harness, Git, and Docker only when provider tools are enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP server command requires an absolute `--config` path and rejects coordinator `system/settings.json` as an authority settings file. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The PyPI package exposes the `agents-remember-mcp` console script and now declares this README as project metadata. | [pyproject.toml](agents-remember-md/mcp/pyproject.toml) |
| The public tool surface includes server info, runtime install, skills install, context packets, memory tools, providers, worktrees, direct closeout, and benchmarks. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| The source checkout keeps the starter MCP settings example under `examples/mcp/settings.example.json`. | [settings.example.json](agents-remember-md/examples/mcp/settings.example.json) |

## Update History

- 2026-05-28T15:52+02:00: Updated after the MCP package README added the canonical source checkout link.
- 2026-05-28T15:43+02:00: Created after the MCP package gained a dedicated README and `pyproject.toml` started using it as package metadata. Verification metadata remains pinned until closeout commits the source change.
