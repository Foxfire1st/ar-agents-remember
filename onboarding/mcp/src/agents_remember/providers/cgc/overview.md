# mcp/src/agents_remember/providers/cgc/ - CodeGraphContext Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/`   |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
Seeding treats a HEAD difference as a state to CATCH UP from, not a teardown
(260707-HFX-L2): a relatable divergence seeds anyway and records the changed
files for `provider_setup`'s post-watcher catch-up stage (the event-driven
watchers re-index just the touched delta; above the delta bound the clone
serves stale and surfaced), only UNRELATABLE heads refuse (a copied graph
must describe the same repository), and a from-zero reindex is explicit only
— `cgc refresh` or the opt-in refresh fallback; seed export/load is capped by
the configurable
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

## 260731-EFA-L2 — The Seed Reads As Source → Target

The behaviour recorded above — catch-up rather than teardown, unrelatable heads only refusing,
explicit-only from-zero reindex — is unchanged. What changed is that `seed.py` now says it.

**`_CgcSeedEnd` (frozen: `coordination_root`, `repo_id`, `repo_root`, `runtime_root`) names one end
of a seed.** Source and target are symmetric, and the seed previously carried them as four
interleaved pairs whose *argument order* was the only thing keeping the two ends apart — a
transposition would have seeded the wrong direction silently. `_validated_seed_context(args, source,
target)` now takes the two ends by name.

Resolution is staged so a half-resolved pair cannot reach validation:
`_seed_precondition_skip` answers "is there any reason to refuse before we read the source settings
at all?" (returns the skip payload or `None`), then `_seed_locations` resolves the repo root and
runtime root for both ends and returns either all four or the *first* side's skip payload — every
one of the four lookups reports failure the same way, so the first payload wins.

`setup.py` invokes lifecycle through `LifecycleCommand(provider=, action=, extra_args=,
native_args=)` from `providers/setup_common.py` rather than positional provider/action strings; the
type records that the provider CLI splits its arguments either side of the action (`extra_args`
precede it, `native_args` are the action's own).

The post-watcher catch-up in `provider_setup.py` is now three named stages rather than one
straight-line function — `_seed_touch_plan` splits the divergence into paths a touch can re-index
and *residual staleness it cannot* (deletions, the vanished half of a rename, paths absent from the
checkout have no file left to touch and stay in the graph as phantoms until an explicit refresh),
`_stale_index_skip` records a delta this run did not deliver, and `_deliver_seed_touches` claims
`caughtUp` **only with zero residuals**. That last rule is the one not to break.

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: seeding kept every rule and gained the vocabulary for
  them — `_CgcSeedEnd` names source and target instead of relying on argument order,
  `_seed_precondition_skip`/`_seed_locations` stage resolution so the first skip wins,
  `setup.py` dispatches via `LifecycleCommand`, and the catch-up stage split into
  plan/skip/deliver with `caughtUp` conditioned on zero residuals. Layout construction moved to
  the `CgcRepo`/`CgcInstance`/`CgcWatcher`/`CgcBackend` bundles (see the context route).
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 route impact (index lifecycle): the seed's HEAD-mismatch
  refusal narrowed to UNRELATABLE heads only — `seed.py` computes the relatable divergence (git
  diff in the source repo) and stashes it for the post-watcher catch-up stage, so small diffs
  become index updates via watcher events; the full-reindex fallback is opt-in and `cgc refresh`
  stays the explicit rebuild. Verification metadata pinned until closeout stamps the HFX-L2
  commit.
- 2026-07-03T01:55+02:00 — L12 route impact: compose memory caps across the CGC stack; watch hygiene fixes live in cgc/context (enriched cgcignore reaches the watch context, timer-pop patch, bundle exclusion).
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): restored the `_seed_skip` benchmark-scoped hermetic guard (task 260619 / MCP 2.9.2) that the series carryover had reverted. The merged tree at 84e95ad keeps main's hermetic seed behavior (the series did not touch this route's source).
- 2026-06-19T13:42 — `seed.py` now refuses a benchmark-scoped seed target (`_seed_skip`) before any source/backend work, mirroring the GrepAI guard (hermetic; task 260619).
- 2026-06-10T07:05+02:00 — Seed in-container argv (post-`--`) documented as container-form via `to_container_path` (GitHub #58: host-form Windows paths failed every seed into the silent reindex fallback).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.0/2.5.1: seed HEAD-match refusal with full-reindex fallback and the setup-cap-vs-uncapped-indexing boundary. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current CGC provider package; expanded the hot-path summary to include isolated worktree settings and CGC index bundle seeding.
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/cgc/`.
