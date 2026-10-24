# docs/reference/runtime-layout.md

## Governing Overview

[Repository overview](../../overview.md) — governed by the route-local
[docs/reference overview](overview.md).

## Purpose

The runtime-layout reference: what the source checkout holds, what `runtime_install`
reconciles into `ar-coordination/`, and what the installed tree owns — including what the
`providers/` subtree is now, which callers may stop a provider, and the skill-install
contract.

## What The Page Establishes

- Source checkout: canonical skills at repository root, runtime and benchmark assets under
  `mcp/src/agents_remember/package_data/`, generated skill copies and harness starter packages
  refreshed only by `scripts/sync-skills.py`, and provider Docker topology (Dockerfiles, base
  Compose files, override templates) kept as source-controlled package data.
- Installed runtime: one `ar-coordination/` tree holding `AGENTS.md`, `providers/`
  (`requirements/`, `patches/`, `runners/<provider>/<instance-id>/`, `data/<provider>/`,
  `logs/<provider>/`), `skills/`, `system/AGENTS.md`, `tasks/AGENTS.md`, `memory-repos/`,
  `benchmarks/`, `notes/`, `worktrees/` and `temp/`.
- `runtime_install` reconciles the coordinator `AGENTS.md` templates, skills, provider defaults
  (pinned requirement files and patch assets) and, with `--include-benchmarks`, benchmark
  fixtures; it then provisions the build-pinned host and product Node from the packaged
  contract and whole npm lock, preserving a running host when a transition needs a stop. It
  reads the shared host authority per call, never writes live settings, and does not own
  notes, tasks, worktrees, memory or onboarding content, or provider databases.
- `ar-coordination/providers/` is leftover provider runtime state from older installations.
  No product path installs, starts, indexes or queries a provider, so the tree survives only
  where an older install left it. `runtime_install` still reconciles package-owned defaults
  and preserves whatever Docker runner instances, image build roots, data and logs are
  already present, but it never deletes the tree: it reports the leftover folders with their
  sizes, and only the explicit `agents-remember providers-remove` removes them. Durable
  provider data stays under `providers/data/` until that removal.
- The provider topology paragraph now describes rendered Compose overrides in the past tense:
  they were passed through stdin as execution input only, never written into
  `ar-coordination/` or the model workspace, with status/debug payloads reporting only the
  rendered override hash plus Compose/image/container state.
- The per-provider layout is retained as a record of what the leftovers hold: GrepAI's
  workspace config, runtime state, cache, mirrors and `index-roots/` under
  `providers/runners/grepai/` with logs under `logs/providers/grepai/` and a PostgreSQL/pgvector
  data root at `providers/data/grepai/postgres/`; CodeGraphContext's per-repo instance roots
  under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/` with a FalkorDB data
  root at `providers/data/codegraphcontext/falkordb/`. Removal is explicit and reports first:
  `providers-remove --dry-run` names folders and sizes and stops nothing; without `--dry-run`
  it removes the provider folders, printing each folder's size and the total bytes freed.
- No provider install, status or start flow remains. Three callers ask for a provider stop and
  none starts one: the old-watcher stop inside `runtime_install` before the runtime tree is
  refreshed; the explicit `providers-remove` cleanup; and the provider-degradation safety loop
  the dashboard's serving process runs while the dashboard is up — every 30 seconds it samples
  the Docker state of the labelled provider containers, records and compacts the sample under
  `logs/observer/providers/`, evaluates the recent window, and on the transition into
  `critical`, and only while `providerDegradation.failSafeEnabled` is true, calls the same
  watcher stop. The page states it starts nothing, installs nothing, indexes nothing and
  queries nothing, and is independent of any install or cleanup.
- All three read the same settings document for that decision: the authority settings file's
  own `contextProviders` block, which still parses legacy provider keys. The generated
  lifecycle document is not that document — it declares no providers
  (`{"enabled": false, "providers": {}}`) because a generated install must not re-create the
  retired block; it is what an install writes, not what a stop reads. With no provider
  declared, a stop selects nothing and stops nothing, the safety loop still records the attempt
  and its result in the degradation event, and `providers-remove` additionally refuses while a
  live process still holds a provider folder.
- The benchmark and skill-install sections keep their contracts: benchmark content reconciles
  under `ar-coordination/benchmarks/` with user runs preserved, each generated case workspace
  keeps `workspaces/<case-id>/repos/` and its own coordination root; `skills_install` copies
  packaged skills flat into a harness skill root for maintenance and non-package installs and
  never creates symlinks, while the package-based first-run path gets skills from the copied
  starter package.

## Boundaries

The page describes a layout contract, not a live directory listing: it does not claim a given
machine has any of these folders, that a particular leftover exists, or that a stop ran. Its
degradation-loop numbers (the 30-second cadence, the `critical` transition, the fail-safe flag)
are the page's account of that loop, not a measured cadence.

Two places on the page sit beside the leftover account without being rewritten by it: the
runtime-install bullet list still names "installed provider defaults" among reconciled assets,
and the installed-runtime tree still shows `providers/`. The page treats both as package data
and leftover paths, not as a live provider surface, but it does not reconcile the wording for
the reader.

Nothing here is a build, test, install or acceptance claim.

## Evidence

- Source checkout keeps canonical skills, package data and provider Docker topology as source-controlled assets. [1]
- The installed runtime tree, including the `providers/` subtree paths. [2]
- `runtime_install` reconciles templates, skills, provider defaults and optional benchmarks, then provisions the pinned host; it writes no live settings and owns no provider database. [3]
- `providers/` is leftover state: no product path installs, starts, indexes or queries a provider; `runtime_install` reports folders and sizes but never deletes them. [4]
- Compose overrides are described as past-tense execution input that was never written into the coordination tree or workspace. [5]
- Per-provider leftover layout and the `providers-remove` dry-run/report-first removal. [6]
- Three stop callers, none of which starts a provider, including the dashboard safety loop's 30-second sampling and fail-safe transition. [7]
- All three read the authority settings `contextProviders` block, not the generated document that declares no providers. [8]
- Benchmark and skill-install contracts. [9]
