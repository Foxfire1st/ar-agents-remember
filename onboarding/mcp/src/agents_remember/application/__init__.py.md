# mcp/src/agents_remember/application/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`__init__.py` marks `agents_remember.application` as an importable package.

## Code Commentary

The file currently contains no exported application-layer facade. Public MCP payload
builders import application entry point functions directly from their domain modules such as
`provider_tools.py`, `worktree_tools.py`, `memory_tools.py`, and
`coordination_tools.py`.

## Invariants And Boundaries

- Keep this package initializer empty unless there is a concrete import-surface
  requirement.
- Do not use it to recreate the old `skill_tools.py` mass facade.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route overview documents the split application package layout. | "Hot Path Summary" | onboarding/mcp/src/agents_remember/application/overview.md:26-38 |
| Public payload builders import application entry points from their owning modules. | `codex_benchmark_prepare_tool` | mcp/src/agents_remember/mcp/tools/__init__.py:1-6; mcp/src/agents_remember/mcp/tools/benchmark.py:7-16 |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 2 citation rows to plain
  sources; the route-overview row cites the memory-repo overview with a literal anchor ("Hot Path
  Summary") because `#`-heading anchors do not resolve against memory-repo targets. Zero findings
  remain.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-06T12:28+02:00: Corrected the public payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created when the controllers route overview made the package initializer part of the explicit route coverage.
