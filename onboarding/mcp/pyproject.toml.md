# mcp/pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/pyproject.toml`                       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T06:43+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90`                      |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/pyproject.toml` defines the installable MCP package metadata, runtime
dependency boundary, optional development dependencies, console script, and
setuptools package discovery root.

## Code Commentary

### Logic

The package builds with `setuptools`, publishes as `agents-remember-mcp`, and
requires Python 3.11 or newer. Runtime dependencies stay intentionally narrow:
only `mcp` is required for normal server installation. Development-only quality
tools live under the `dev` optional dependency group: Coverage.py, pytest,
pytest-cov, Radon, and Ruff.

The `agents-remember-mcp` console script points at
`agents_remember.mcp.__main__:main`, while setuptools discovers import packages
from `mcp/src`.

### Invariants And Boundaries

- Runtime package dependencies should stay separate from source-development
  quality dependencies.
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

## Update History

- 2026-05-24T06:43+02:00: Created after the MCP package gained explicit development dependencies for the source quality suite.
