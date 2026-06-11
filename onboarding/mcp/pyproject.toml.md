# mcp/pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/pyproject.toml`                       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T10:26+02:00     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46` |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
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
Runtime dependencies stay intentionally narrow but now include `mcp`,
`pydantic`, and `tiktoken`: Pydantic owns public response validation and
tiktoken backs response token accounting. Development-only quality tools live
under the `dev` optional dependency group: Coverage.py, pytest, pytest-cov,
Pyright, Radon, and Ruff.

The `agents-remember-mcp` console script points at
`agents_remember.mcp.__main__:main`, while setuptools discovers import packages
from `mcp/src`. The `[tool.setuptools.package-data]` block ships the installable
runtime scaffold — `package_data/**/*` (AGENTS.md templates, skills, provider
assets, system defaults) plus the benchmark `package_data/benchmarks/.gitignore`
— so `runtime_install` can reconcile those package-owned assets into a
coordinator from a pip/uvx install with no source checkout.

The package `version` tracks the release line; at this verification it is
`2.7.0`. It is the same string `runtime_install` and `server_info` report, and
it stays aligned with `agents_remember.mcp.SERVER_VERSION` (see invariant below).

### Invariants And Boundaries

- Runtime package dependencies should stay separate from source-development
  quality dependencies; Pydantic and tiktoken are runtime dependencies because
  modeled responses and token metadata are part of normal tool output.
- Release version bumps should keep this project version aligned with
  `agents_remember.mcp.SERVER_VERSION` so installed server payloads report the
  same version that PyPI installs.
- Pyright, CRAP-Calculator, and the source quality wrapper rely on the `dev`
  optional dependency group, not the base MCP runtime dependency set.
- The package discovery root is `src`; package modules should remain under
  `mcp/src/agents_remember/`.
- The installable runtime scaffold is shipped as `package-data` under
  `agents_remember/package_data/`; assets `runtime_install` reconciles into a
  coordinator must live inside that tree to be packaged by a pip/uvx install.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper uses pytest, pytest-cov, Radon, Ruff, and CRAP-Calculator during development checks. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| Public response contracts depend on Pydantic and token accounting depends on tiktoken. | [models overview](agents-remember/mcp/src/agents_remember/models/overview.md) |
| CRAP-Calculator imports Radon at runtime for development scoring, so Radon belongs in the development dependency group. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| The MCP console entry point resolves through `agents_remember.mcp.__main__`. | [__main__.py](agents-remember/mcp/src/agents_remember/mcp/__main__.py) |
| MCP server payloads report the package-level `SERVER_VERSION`. | [__init__.py](agents-remember/mcp/src/agents_remember/mcp/__init__.py) |
| The package README documents the installable MCP command and setup-oriented tool surface for PyPI/package readers. | [README.md](agents-remember/mcp/README.md) |
| `runtime_install` reconciles the `package_data/` runtime scaffold shipped by this `package-data` declaration into a coordinator. | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-06-10T10:26+02:00 — No content impact: version bumped to 2.8.0 for the GitHub #54 release (lifecycle-long stale-base prevention); the packaging contract this sidecar describes is unchanged.
- 2026-06-10T08:15+02:00 — Version bumped to 2.7.0 for the GitHub #53/#58 release (async worktree provider setup + Windows seed fix).
- 2026-06-10T06:05+02:00 — No content impact: version bumped to 2.6.0 for the memory-integrity release (GitHub #56); package metadata semantics unchanged.
- 2026-06-10T05:45+02:00 — Version bumped to 2.5.2 for the carryover response compaction patch (GitHub #52).
- 2026-06-10T05:30+02:00 — Version bumped to 2.5.1 for the tool-reliability release (stdio subprocess hygiene #49, seed stall watchdog, runner-image derivation #50, GrepAI indexing parity, crash-loop readiness, response token budgets).
- 2026-06-09T22:10+02:00 — Version bumped to 2.5.0 for the CGC persistence/readiness release (FalkorDB `dataDestination` mount fix, graph-content readiness probe with `indexing` state, degraded-state propagation, summary `indexing` list, watcher self-heal entrypoint, `--remove-orphans` hygiene).
- 2026-06-09T15:39+02:00: Bumped the documented package `version` to `2.4.2` for the L-01 lifecycle skill consolidation patch release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-08T12:22+02:00: Bumped the documented package `version` to `2.4.1`
  for the runtime asset sync and provider validation patch release; still
  tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-08T08:33+02:00: Bumped the documented package `version` to `2.4.0` for the harness-local starter renderer and Python hook command rendering release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-04T23:15+02:00: Bumped the documented package `version` to `2.3.3` for the provider watcher rebind and Docker-safe provider identity patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-04T18:52+02:00: Bumped the documented package `version` to `2.3.2` for the runtime skill refresh patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T19:25+02:00: Bumped the documented package `version` to `2.3.1` for the MCP package README correction patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T18:58+02:00: Bumped the documented package `version` to `2.3.0` for the harness starter-package / package-first install ergonomics release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T04:25+02:00: Bumped the documented package `version` to `2.2.0` (mcp 2.2.0 release for the lifecycle collaboration loop and C-09 source-branch contract refresh); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T18:35+02:00: Bumped the documented package `version` to `2.1.0` (mcp 2.1.0 release); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T05:10+02:00: Bumped the documented package `version` to `2.0.0` (mcp 2.0.0 — the `l-01-session-job-lifecycle` skill lifecycle reshape, a major/breaking release); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T03:30+02:00: Bumped the documented package `version` to `1.0.2` (mcp 1.0.2 — git-workflow.md + PR-gated landing); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the documented package `version` to `1.0.1` (mcp 1.0.1 — worktree cgc DNS-label fix); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-05-31T12:30+02:00 — Bumped the documented package `version` to `1.0.0` (1.0.0 review remediation); still tracks `SERVER_VERSION`.
- 2026-05-31T01:06+02:00: Bumped the documented package `version` to `0.9.6` (MCP 0.9.6, `w-02-light-task-workflow` skill design section); still tracks `SERVER_VERSION`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped the documented package `version` to `0.9.5` for the S6 token-counter release; still tracks `SERVER_VERSION`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:22+02:00: Realigned to MCP `0.9.4` after the 0.9.0–0.9.4 run; version still tracks `SERVER_VERSION`. Documented the `package-data` runtime-scaffold packaging block (the card body previously described the `0.3.0` release).
- 2026-05-29T21:00+02:00: Bumped the package `version` to `0.3.0` for the MCP `0.3.0` release (act-by-default `dry_run` flip), kept aligned with `SERVER_VERSION`.
- 2026-05-28T19:52+02:00: Updated after Pydantic and tiktoken became MCP runtime dependencies and Pyright joined the dev quality dependency group.
- 2026-05-28T15:43+02:00: Updated while preparing MCP package release `0.2.0`, documenting package/server version alignment, and wiring the dedicated MCP README into package metadata. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-24T06:43+02:00: Created after the MCP package gained explicit development dependencies for the source quality suite.
