# mcp/src/agents_remember/install/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/install/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00|
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/runtime.py` is the package-local runtime installer service used by the
`runtime_install` MCP tool. It reconciles runtime assets into the configured
coordinator root, delegates provider watcher rebind orchestration to
`install/provider_watchers.py`, and can run provider dependency installation
through package-local lifecycle functions.

## Code Commentary

### 260731-EFA-L2 Install Request And Tree-Sync Objects

Three frozen dataclasses carry what an install is asked to do:

- **`RuntimeTreeSync(source_root, destination_root, preserve=frozenset(), prune_ignore=frozenset(),
  copy_ignore=frozenset())`** — one packaged runtime tree mirrored into the coordination root.
  **The ownership rules travel with the pair of roots because they are what makes the mirror
  non-destructive**: `preserve` names destination paths a prune never removes (user-owned
  coordinator state), `prune_ignore` names paths pruned even when the packaged source still carries
  them, and `copy_ignore` names source paths the copy never writes. Note the split — the old single
  `ignore=` keyword meant different things to `prune_tree` and `copy_tree`, and now says which.
  Signatures: `prune_tree(sync, summary, dry_run)` and `copy_tree(sync, summary, dry_run)`.
- **`ProviderDependencyInstall(settings, timeout, enabled=True, no_cache=False)`** — the
  provider-dependency step: whether it runs at all, the live provider settings it installs against,
  the per-provider budget, and whether caches may be reused. `install_runtime(source_root,
  coordination_root, dry_run, *, provider_deps, include_benchmarks=False)` takes it, and the
  watcher rebind is derived from the same object because it is the same step's stop/start cycle.
- **`RuntimeInstallRequest(dry_run=False, include_benchmarks=False, install_provider_deps=True,
  no_cache=False, provider_deps_timeout=None, source_root=None)`** — what one install is asked to
  do. `install_runtime_from_config(config, request)` takes it. `provider_deps_timeout` and
  `source_root` stay unset for MCP callers: the timeout then falls back to the config's provider
  setup cap and the source to the packaged runtime tree.

Defaults are unchanged, including `dry_run=False` (act-by-default) on both entry points and the
`no_cache` pass-through into the provider lifecycle install calls.

### Logic

The service copies package runtime skills, provider defaults, and runtime
`AGENTS.md` templates from the source/package runtime tree into the configured
coordinator. After the `AGENTS.md` copies and the user-owned directory ensures,
`seed_agentic_settings` (260703-L13) seeds the GLOBAL agentic settings file at
`<coordinationRoot>/system/settings.json` COPY-IF-MISSING with the documented
defaults (`kernel/agentic_settings.default_agentic_settings_seed_text` —
all-human gate delegation, the L12 loop defaults, no spawn preference): an
existing file is never touched whatever it contains (user-owned posture, like
`memory-repos/`), a missing one counts as a copied file in the summary, and
dry-run reports without writing. The c-13 install skill's Stage 2 interview
then edits the seeded file with the developer. Runtime sync removes stale coordinator `scripts/` remnants because
the old source-side installer and skill-install script are no longer valid
runtime entry points. Dependency-skipped syncs preserve live provider runner
state under `providers/runners`, while stale `providers/_bin` and
`providers/_venvs` content is pruned because host provider binaries and venvs
are not part of the managed runtime contract. Explicit provider dependency
installs reconcile supported provider paths through package-local lifecycle
code. When provider dependencies are installed, the service stops enabled
provider watchers before runner scaffolding can be pruned, refreshes managed
provider runtime files and dependencies, then starts and checks the watchers so
containers rebind to the current runner roots. If the first post-install status
is still degraded, it records one non-destructive restart/rebind attempt and
reports recovery guidance if readiness is still not restored. All installs
preserve durable `providers/data` and central logs under `logs/`.

`source_root_from_package()` locates the packaged runtime assets by walking
upward from the installed module until it finds the source/runtime asset tree.
`install_runtime_from_config()` is the MCP entrypoint: it derives the target root
from `McpRuntimeConfig`, generates provider lifecycle settings from the LIVE
on-disk provider authority (`reload_provider_authority(config).apply(config)`;
containment R1, 260707-HFX-L1 — the watcher rebind's stop→start cycle is a
launch path, so it must never run off a stale boot snapshot; an empty or
unreadable fail-closed live map yields disabled settings that turn the rebind
off while the runtime install itself proceeds), and calls package-local
provider lifecycle install functions when
provider deps are enabled. It threads `no_cache` through to the provider
lifecycle install calls:
by default image builds skip any image whose tag already exists, and
`no_cache=true` forces a from-scratch rebuild. The optional `source_root`
parameter is an internal development/test hook, not a public MCP path field.

The module is intentionally not a second runtime-install command surface. MCP
clients reach it through the `runtime_install` tool.

### Invariants And Boundaries

- MCP callers do not provide `coordinationRoot` or `sourceRoot`.
- The MCP package path is the runtime-install owner; source checkout installer
  scripts must not remain as a parallel route.
- MCP provider dependency install must use generated settings from
  `McpRuntimeConfig`, with the providers map re-read from the on-disk
  authority (containment R1): the watcher rebind is a launch path, so a
  disk-disabled or unreadable authority disables the rebind while the install
  itself still proceeds.
- Full provider reinstall can replace Docker runner instances and image build
  roots, but must stop/restart enabled watchers around that replacement and
  must preserve `providers/data` and central logs under `logs/`.
- `providers/_bin` is not preserved or recreated as a managed provider runtime
  path.
- `providers/_venvs` is not preserved or recreated as a managed provider
  runtime path.
- This service must not execute coordinator-local `scripts/provider-setup.py`
  for the MCP path.
- Coordinator runtimes do not receive source scripts; provider, benchmark, and
  install helpers stay in MCP package-owned code.
- `install_runtime_from_config`'s `dry_run` defaults to `False` (act-by-default),
  matching the `runtime_install` MCP tool; `dry_run=true` reports the reconcile
  plan without performing the reconcile.
- Provider watcher rebind reporting belongs in the install summary and response
  payload; the detailed lifecycle sequencing belongs in `install/provider_watchers.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP application entry point exposes only typed install booleans. | `run_runtime_install` | mcp/src/agents_remember/application/runtime/install.py:13-17 |
| Provider settings generation derives lifecycle settings from MCP authority. | `lifecycle_settings_from_config` | mcp/src/agents_remember/providers/settings.py:25-39 |
| `install_runtime` stores a provider watcher rebind report, stops watchers before provider refresh, starts/checks them afterward, and includes rebind/recovery details in the MCP payload. | `install_runtime` | mcp/src/agents_remember/install/runtime.py:462-553 |
| Provider watcher lifecycle orchestration and recovery-action construction live in the extracted install helper. | `complete_provider_watcher_rebind` | mcp/src/agents_remember/install/provider_watchers.py:144-166 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 8 initial citation findings (4 anchor, 0 prose, 4 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912`/`PLR0915`/`PLR0913`
  armed with no exemptions): added the frozen `RuntimeTreeSync`, `ProviderDependencyInstall` and
  `RuntimeInstallRequest`; `prune_tree`/`copy_tree` take a `RuntimeTreeSync` (whose single
  `ignore=` keyword became the explicit `prune_ignore` / `copy_ignore` pair), `install_runtime`
  takes `provider_deps: ProviderDependencyInstall`, and `install_runtime_from_config` takes a
  `RuntimeInstallRequest`. Preserved paths, pruned paths, copied files and the emitted payload are
  unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `install_runtime_from_config`
  now derives the rebind `provider_settings` from the live on-disk authority
  (`reload_provider_authority(config).apply(config)`) instead of the boot snapshot, so the
  watcher stop→start rebind cannot launch off stale config; a disabled/unreadable live map
  disables the rebind while the install proceeds. Verification metadata pinned until closeout
  stamps the HFX-L1 commit.

- 2026-07-06T22:40+02:00 — 260703-L13 (settings unification): added `seed_agentic_settings`
  — the global agentic settings file is seeded copy-if-missing at the user-owned insertion
  point (after AGENTS.md targets + user-owned dirs), sharing the seed content with the
  kernel loader so installer and parser cannot drift. Verification metadata pinned until
  closeout stamps the L13 commit.

- 2026-06-04T22:15+02:00 — Documented provider watcher rebind orchestration for `install_provider_deps=true`, including the extracted helper, non-destructive retry, recovery reporting, and preserved provider data.
- 2026-05-31T12:30+02:00 — Dropped the provider runner integrity-manifest write from `install_runtime_from_config` and the `integrity` return field, and removed the stale integrity.py reference (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` flag threaded through `install_runtime_from_config` into the provider lifecycle install calls — image builds skip existing tags by default, `no_cache=true` forces a from-scratch rebuild. Verified against `8927f03`.
- 2026-05-29T18:35+02:00: Extracted `_remove_with_retry` from `remove_path` to drop cyclomatic complexity below 11; behavior-preserving (commit `e3dab63`).
- 2026-05-28T12:32+02:00: Updated after runtime install moved operator logs from `providers/logs/` into the central `logs/` tree.
- 2026-05-26T12:51+02:00: Updated after runtime install stopped preserving provider venvs and CGC provider dependencies became Docker-owned.
- 2026-05-25T18:07+02:00: Updated after runtime install stopped preserving `providers/_bin`; Docker-owned GrepAI keeps binaries inside the runner image.
- 2026-05-24T00:37+02:00: Refreshed verification and documented that packaged asset discovery owns normal runtime source selection, with `source_root` reserved for internal development/test use.
- 2026-05-23T14:20+02:00: Updated after `runtime_install` stopped requiring or copying `runtime/scripts/install-skills.sh` and began removing stale coordinator `scripts/` remnants.
- 2026-05-23T05:32+02:00: Clarified the earlier intermediate state where runtime sync still installed only `scripts/install-skills.sh` into coordinators while MCP provider installs used package-local lifecycle code.
- 2026-05-23T04:43+02:00: Clarified that MCP install is exposed through the typed tool, not a package-local wrapper command.
- 2026-05-23T04:29+02:00: Created when runtime installation moved behind the MCP/package-local boundary.
