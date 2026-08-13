# mcp/src/agents_remember/application/runtime/install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/runtime/install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-13T08:40+02:00                     |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runtime overview](overview.md)

## Purpose

`runtime/install.py` is the thin application layer for the MCP
`runtime_install` operation.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the safe model-facing install flags:
`dry_run`, `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). It does not accept host paths or provider path overrides.

The dataclass is **defined in `agents_remember.install.runtime`** and this
module re-exports it (`__all__ = ["RuntimeInstallRequest", "run_runtime_install"]`) for its
runtime application surface. `run_runtime_install(config, request)` is
now a one-line delegation — `install_runtime_from_config(config, request)` — because the service
takes the request object itself rather than four unpacked keywords. The application entry point therefore no
longer restates the flag list, which is what used to make the two definitions drift.

### Invariants And Boundaries

- Keep this application entry point thin; install mechanics **and now the request type itself** belong in
  `agents_remember.install.runtime`. This module is a re-export plus one delegation.
- Do not add path fields to `RuntimeInstallRequest`; keep it to typed install
  booleans (`no_cache` forces a from-scratch provider image rebuild downstream).
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation; the packaged install skills tell the agent to preview first.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. | `runtime_install_payload` | mcp/src/agents_remember/mcp/tools/core.py:76-102 |
| The tool declaration exposes `runtime_install` as a public tool. | `runtime_install` | mcp/src/agents_remember/mcp/registration/core.py:119-146 |
| The service layer defines `RuntimeInstallRequest` and performs the actual runtime install. | `RuntimeInstallRequest` | mcp/src/agents_remember/install/runtime.py:105-119 |

## Update History

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved the preserved card with the pure source move into the cohesive `application/runtime/` package, rebound it to the new governing overview, and removed the obsolete flat-module import claim. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 1 citation claim; scoped recheck clean (0 findings).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `RuntimeInstallRequest`'s definition moved to
  `agents_remember.install.runtime` and this module re-exports it; `run_runtime_install` became a
  single delegation passing the request object through. Corrected the stale reference to `server.py`
  — tool registration now lives in `mcp/registration/core.py`. Verification metadata pinned until
  closeout stamps the L2 code commit.

- 2026-05-30T21:33+02:00: Added the `no_cache` flag to `RuntimeInstallRequest` (forwarded to `install_runtime_from_config`) and repaired the builder reference — `runtime_install_payload` now lives in `tools/core.py` after the `01f503d` `mcp/tools.py` split. Verified against `8927f03`.
- 2026-05-24T00:37+02:00: Refreshed verification after MCP command capture callers moved to service-backed controllers; the runtime install controller contract stayed unchanged.
- 2026-05-23T04:29+02:00: Created for the MCP runtime install tool controller.
