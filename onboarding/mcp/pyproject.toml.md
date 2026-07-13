# mcp/pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/pyproject.toml`                       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-12T20:24+02:00 |
| lastVerifiedCommitHash | `b120efbfda76931cfa8eb9f24c9a808a62c10d1e` |
| lastVerifiedCommitDate | 2026-07-13T12:33:57+02:00|
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
`pydantic`, `tiktoken`, and — for the slice-04 dashboard serving layer —
`fastapi` (built-in `fastapi.sse`), `uvicorn`, and — for the slice 6d-2 Mode B2
terminal — `websockets`: Pydantic owns public response validation, tiktoken
backs response token accounting, FastAPI/uvicorn serve the local dashboard, and
`websockets` is uvicorn's WebSocket protocol implementation for the
`/api/terminal/{session}` terminal bridge (plain `uvicorn` ships no WS impl, so a
live WebSocket needs it). Slice 6f adds `python-multipart`, which FastAPI requires to
parse the `multipart/form-data` upload on `POST /api/terminal/{session}/image` (its
`UploadFile`/`File` form support fails without it). 260712-PTS-L3 adds `watchfiles`
(`>=1.1,<2`), the inotify-backed filesystem watcher behind the dashboard's change-driven
projection pacing (`serving/change_watcher.py`) — a decision-logged new runtime dependency
(neither `watchfiles` nor `watchdog` existed in the tree before); the serving layer degrades
loudly to fixed-interval ticking when it is missing, so the dep is core for the adaptive
behaviour, not for the daemon to run at all. The webstack is a **core** dependency (not an optional
extra) so `agents-remember dashboard` works on a plain install. Development-only
quality tools live under the `dev` optional dependency group: Coverage.py, httpx
(the FastAPI `TestClient` backend), pytest, pytest-cov, Pyright, Radon, and Ruff.

Two console scripts are declared: the umbrella `agents-remember`
(`agents_remember.cli.__main__:main`, the front door for subcommands such as
`dashboard`) and the unchanged `agents-remember-mcp`
(`agents_remember.mcp.__main__:main`, the MCP server — kept standalone because
harness MCP configs launch it by that exact name). setuptools discovers import
packages from `mcp/src`. The `[tool.setuptools.package-data]` block ships the installable
runtime scaffold — `package_data/**/*` (AGENTS.md templates, skills, provider
assets, system defaults) plus the benchmark `package_data/benchmarks/.gitignore`
— so `runtime_install` can reconcile those package-owned assets into a
coordinator from a pip/uvx install with no source checkout.

The package `version` tracks the release line. Its exact current value lives in
the source rather than being repeated here; it is the same string
`runtime_install` and `server_info` report, and it stays aligned with
`agents_remember.mcp.SERVER_VERSION` (see invariant below).

### Invariants And Boundaries

- Runtime package dependencies should stay separate from source-development
  quality dependencies; Pydantic and tiktoken are runtime dependencies because
  modeled responses and token metadata are part of normal tool output, and
  FastAPI/uvicorn are runtime dependencies because the dashboard ships in the
  package and must run on a plain install. httpx, by contrast, is dev-only — it
  only backs the FastAPI `TestClient` in tests.
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

- 2026-07-12T20:24+02:00 — 260712-PTS-L3: added `watchfiles` (`>=1.1,<2`) as a **core** runtime
  dependency — the inotify backend for `serving/change_watcher.py`'s change-driven projection
  pacing (decision-logged; no prior watch library in the tree). Missing-wheel behaviour is a loud
  fixed-interval fallback, never a crash. Verification metadata pinned until closeout stamps the
  PTS-L3 commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 bumps version 3.0.0rc4 -> 3.0.0rc5 (PEP 440 prerelease)
  with no dependency, entry-point, package-data, or build-system contract change. Corrected the stale
  `2.9.3` commentary to version-generic wording so later release bumps do not drift it.

- 2026-07-08T15:45+02:00 — No content impact: 260707-HFX2-L7 bumps version 3.0.0rc3 ->
  3.0.0rc4 (PEP 440 prerelease) for the hotfix release tail; no dependency, entry point, package
  data, or build-system contract changed.
- 2026-07-07T21:10+02:00 — No content impact: release 4922146 bumped version 3.0.0rc2 -> 3.0.0rc3 (PEP 440 prerelease); no dependency or build-system change. (Reconciliation: direct owner commit between the L17 and L18 closeouts.)
- 2026-07-03T12:05+02:00 — No content impact: 260703 L4 bumped version 3.0.0rc1 -> 3.0.0rc2 (PEP
  440 prerelease); no dependency or build-system change.
- 2026-07-03T11:20+02:00 — No content impact: L14 bumped version 2.9.3 -> 3.0.0rc1 (PEP 440 prerelease); no dependency or build-system change.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): version reflects the main releases merged onto the series — `2.9.2` (benchmark provider-isolation / hermetic setup) and `2.9.3` (resolve a worktree contract from `worktree_name`); no packaging-contract change, and the documented `version` still tracks `SERVER_VERSION`. Corrected the stale `2.7.0` verification note in the body to `2.9.3`.
- 2026-06-19T20:30 — Task 6 slice 6f: added `python-multipart` (`>=0.0.9,<1`) as a **core** runtime dependency — FastAPI needs it to parse the `multipart/form-data` `UploadFile` on `POST /api/terminal/{session}/image` (the screenshot upload). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: added `websockets` (`>=12,<16`) as a **core** runtime dependency — uvicorn's WebSocket protocol impl for the Mode B2 `/api/terminal/{session}` bridge (plain `uvicorn` ships none). Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4a: added `fastapi` + `uvicorn` as **core** runtime dependencies (the dashboard webstack, forced core so `agents-remember dashboard` works on a plain install), `httpx` to the `dev` group (FastAPI `TestClient`), and the umbrella `agents-remember` console script alongside the unchanged `agents-remember-mcp`. Verification metadata pinned until closeout stamps the 4a code commit.
- 2026-06-12T19:06+02:00 — No content impact: version bumped to 2.9.1 for the issue #83 closeout committed-range fix release; packaging contract unchanged.
- 2026-06-11T15:20+02:00 — No content impact: version bumped to 2.9.0 for the carryover artifact coverage release; packaging contract unchanged.
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
