# mcp/src/agents_remember/providers/cgc/ - CodeGraphContext Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/`   |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-03T01:55+02:00 |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`cgc/` is the provider-owned home for CodeGraphContext setup, seeding,
context layout, patching, and lifecycle operations. Since L12 every CGC compose
service ships an explicit memory cap (falkordb 2g, batch runner 1g, per-repo
watchers 512m) so a runaway container OOM-recycles itself under unless-stopped
instead of exhausting the host — the 2026-07-03 swap-exhaustion incident defense. The package replaces the
former top-level `cgc_*` modules and mixed `context_modules/cgc` plus
`lifecycle_modules/cgc` routes.

## Hot Path Summary

Use `setup.py` for enabled-provider wiring and isolated worktree settings,
`seed.py` plus `bundle.py` for CGC index export/rewrite/import seeding, and
`context/` for runtime layout, materialization, cleanup, and patch helpers.
Use `lifecycle/` for backend, install/status, and process/watch commands.
Seeding refuses when the workspace and worktree repository HEADs differ (a
copied graph must match the code it describes) and the worktree then falls
back to a full reindex; seed export/load is capped by the configurable
`providerSetupSeconds`, while actual indexing is never duration-capped.
Seed argv after `--` executes inside the Linux runner container and is
rendered via `to_container_path` (`providers/context_common.py`) — host-form
`C:/` paths made every Windows seed fail into the silent reindex fallback
(GitHub #58).

## Route Model

- `bundle.py`, `seed.py`, and `setup.py` own package/setup-time CGC behavior,
  including worktree graph seeding from an existing provider index. A
  benchmark-scoped target is refused before any seed work (`_seed_skip`),
  mirroring the GrepAI guard (hermetic; task 260619).
- `context/` owns CGC runtime layout and upstream patch behavior.
- `lifecycle/` owns CGC backend, installation, status, and process lifecycle.

## Invariants And Boundaries

- CGC-specific behavior belongs under this package, not in GrepAI modules or
  shared lifecycle helpers.
- Shared helpers should stay provider-agnostic and live under
  `providers/context/` or `providers/lifecycle/`.
- The public setup facade remains `providers.provider_setup`; the provider
  implementation lives here.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC setup orchestration lives in the provider-owned setup module. | [setup.py](agents-remember/mcp/src/agents_remember/providers/cgc/setup.py) |
| CGC context behavior is grouped under the provider-owned context package. | [context overview](context/overview.md) |
| CGC lifecycle behavior is grouped under the provider-owned lifecycle package. | [lifecycle overview](lifecycle/overview.md) |

## Update History

- 2026-07-03T01:55+02:00 — L12 route impact: compose memory caps across the CGC stack; watch hygiene fixes live in cgc/context (enriched cgcignore reaches the watch context, timer-pop patch, bundle exclusion).
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): restored the `_seed_skip` benchmark-scoped hermetic guard (task 260619 / MCP 2.9.2) that the series carryover had reverted. The merged tree at 84e95ad keeps main's hermetic seed behavior (the series did not touch this route's source).
- 2026-06-19T13:42 — `seed.py` now refuses a benchmark-scoped seed target (`_seed_skip`) before any source/backend work, mirroring the GrepAI guard (hermetic; task 260619).
- 2026-06-10T07:05+02:00 — Seed in-container argv (post-`--`) documented as container-form via `to_container_path` (GitHub #58: host-form Windows paths failed every seed into the silent reindex fallback).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.0/2.5.1: seed HEAD-match refusal with full-reindex fallback and the setup-cap-vs-uncapped-indexing boundary. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current CGC provider package; expanded the hot-path summary to include isolated worktree settings and CGC index bundle seeding.
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/cgc/`.
