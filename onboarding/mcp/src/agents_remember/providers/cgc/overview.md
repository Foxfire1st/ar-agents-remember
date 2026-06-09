# mcp/src/agents_remember/providers/cgc/ - CodeGraphContext Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/`   |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-06T12:15                           |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`cgc/` is the provider-owned home for CodeGraphContext setup, seeding,
context layout, patching, and lifecycle operations. The package replaces the
former top-level `cgc_*` modules and mixed `context_modules/cgc` plus
`lifecycle_modules/cgc` routes.

## Hot Path Summary

Use `setup.py` for enabled-provider wiring and isolated worktree settings,
`seed.py` plus `bundle.py` for CGC index export/rewrite/import seeding, and
`context/` for runtime layout, materialization, cleanup, and patch helpers.
Use `lifecycle/` for backend, install/status, and process/watch commands.

## Route Model

- `bundle.py`, `seed.py`, and `setup.py` own package/setup-time CGC behavior,
  including worktree graph seeding from an existing provider index.
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
| CGC setup orchestration lives in the provider-owned setup module. | [setup.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/setup.py) |
| CGC context behavior is grouped under the provider-owned context package. | [context overview](context/overview.md) |
| CGC lifecycle behavior is grouped under the provider-owned lifecycle package. | [lifecycle overview](lifecycle/overview.md) |

## Update History

- 2026-06-06T12:15: Re-verified against the current CGC provider package; expanded the hot-path summary to include isolated worktree settings and CGC index bundle seeding.
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/cgc/`.
