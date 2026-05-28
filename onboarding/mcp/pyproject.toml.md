# mcp/pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/pyproject.toml`                       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T15:43+02:00                     |
| lastVerifiedCommitHash | `9680d150ac9d2e6c1ae04dbab42eac0088dceef8`                      |
| lastVerifiedCommitDate | 2026-05-28T15:55:29+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/pyproject.toml` defines the installable MCP package metadata, PyPI README
metadata, package version, runtime dependency boundary, optional development
dependencies, console script, and setuptools package discovery root.

## Code Commentary

### Logic

The package builds with `setuptools`, publishes as `agents-remember-mcp`, uses
`mcp/README.md` as its package README, and requires Python 3.11 or newer.
Runtime dependencies stay intentionally narrow: only `mcp` is required for
normal server installation. Development-only quality tools live under the
`dev` optional dependency group: Coverage.py, pytest, pytest-cov, Radon, and
Ruff.

The `agents-remember-mcp` console script points at
`agents_remember.mcp.__main__:main`, while setuptools discovers import packages
from `mcp/src`.

### Invariants And Boundaries

- Runtime package dependencies should stay separate from source-development
  quality dependencies.
- Release version bumps should keep this project version aligned with
  `agents_remember.mcp.SERVER_VERSION` so installed server payloads report the
  same version that PyPI installs.
- CRAP-Calculator and the source quality wrapper rely on the `dev` optional
  dependency group, not the base MCP runtime dependency set.
- The package discovery root is `src`; package modules should remain under
  `mcp/src/agents_remember/`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper uses pytest, pytest-cov, Radon, Ruff, and CRAP-Calculator during development checks. | [check.py](agents-remember-md/mcp/src/agents_remember/code_quality/check.py) |
| CRAP-Calculator imports Radon at runtime for development scoring, so Radon belongs in the development dependency group. | [crap_calculator.py](agents-remember-md/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| The MCP console entry point resolves through `agents_remember.mcp.__main__`. | [__main__.py](agents-remember-md/mcp/src/agents_remember/mcp/__main__.py) |
| MCP server payloads report the package-level `SERVER_VERSION`. | [__init__.py](agents-remember-md/mcp/src/agents_remember/mcp/__init__.py) |
| The package README documents the installable MCP command and setup-oriented tool surface for PyPI/package readers. | [README.md](agents-remember-md/mcp/README.md) |

## Update History

- 2026-05-28T15:43+02:00: Updated while preparing MCP package release `0.2.0`, documenting package/server version alignment, and wiring the dedicated MCP README into package metadata. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-24T06:43+02:00: Created after the MCP package gained explicit development dependencies for the source quality suite.
