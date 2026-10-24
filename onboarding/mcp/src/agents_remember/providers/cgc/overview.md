# mcp/src/agents_remember/providers/cgc/ - CodeGraphContext Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/`   |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`cgc/` contains the provider-owned CodeGraphContext implementation: isolated settings, graph seeding, runtime layout, materialization, patching, backend management, installation, status, and process operations. CGC-specific implementation is grouped here, with shared provider helpers outside the package.

## Hot Path Summary

`setup.py` retains isolated-settings and gated install/seed preparation helpers. `seed.py` retains source/target bundle request construction and path rewriting through `bundle.py`; that code does not establish a working public export/import command. `context/` retains layout, materialization, cleanup and patch helpers. The lifecycle facade enumerates exactly `core`, `compose`, `backend`, `runner`, `installation` and `process_control`; no query or refresh module remains.

Ordinary enabled-provider setup skips CGC: `providers/setup_common.py::provider_enabled` returns `False` for `codegraphcontext-code`, regardless of its settings block, and install/preparation consult that gate first. The typed lifecycle service admits only all-provider `stop` and `shutdown-all`; watcher aggregation maps both CGC actions to `cgc_stop_all`. Retained backend, status and layout functions remain internal implementation and do not restore provider start, query, refresh or MCP display.

## How It Is Built

### Source And Target Seeding

`_CgcSeedEnd` is a frozen value holding `coordination_root`, `repo_id`, `repo_root`, and `runtime_root`. `_validated_seed_context(args, source, target)` receives the two ends separately, so their direction is explicit.

Resolution precedes validation. `_seed_precondition_skip` checks refusal conditions before reading source settings, including the benchmark-scope guard that prevents seeding from a live workspace stack. `_seed_locations` resolves both repository roots and both runtime roots; a failed lookup returns its skip payload instead of sending a partially resolved pair to validation.

The retained bundle pipeline constructs source-backend, export and load requests around the source-root path rewrite. Those requests do not establish a working provider lifecycle command. Seed arguments intended for the former Linux runner use `to_container_path` from `providers/context_common.py`, converting host paths to POSIX form and stripping a Windows drive prefix. When isolated settings supply a target bundle runtime root, the helper resolves its bundle under that root.

### Lifecycle Commands And Shared Helpers

Setup and seed operations describe lifecycle requests with `LifecycleCommand(provider, action, extra_args, native_args)` from `providers/setup_common.py`. The helper places provider-level `extra_args` before the action and action-specific `native_args` after it.

`setup.py` imports instance identity and naming helpers directly from `kernel/primitives/identity.py`. Provider-agnostic context and lifecycle helpers remain outside `cgc/`; the current package does not directly import all three primitive modules named by the former route-impact note.

### Divergence And Catch-Up

In the retained seed implementation, differing readable HEADs are compared through `seed_commit_divergence`. A computable diff is recorded for the post-watcher catch-up stage rather than causing a full rebuild. A diff that cannot be computed produces the foreign-graph refusal. The commit comparison is bypassed when commit mismatch is explicitly allowed or either HEAD is unavailable; other seed preconditions and same-coordination-root restrictions can also refuse a seed.

`providers/provider_setup.py` retains the catch-up stages. `_seed_touch_plan` separates files that can be touched from residual staleness: deleted paths, rename-source paths, and paths missing from the checkout. Above the configurable delta bound, the result reports a served stale index; the default bound is 200 changed entries. Within the bound, catch-up waits for the watcher's readiness marker before touching files. Failure to reach readiness reports stale state without delivering the touches. `_stale_index_skip` records an undelivered delta; `_deliver_seed_touches` reports `caughtUp` only when there are no residuals after the touch pass.

## Invariants And Boundaries

- CGC-specific behavior belongs in this package; shared provider helpers belong in the shared context or lifecycle routes. `providers.provider_setup` remains the setup facade, with CGC implementation delegated here.
- Ordinary setup's CGC enablement gate must be distinguished from the retained seed and direct lifecycle implementations. Their presence alone is not a promise that normal setup installs, seeds, or starts CGC.
- The retained seed policy favors a graph-copy request plus bounded catch-up. `_refresh_after_seed` returns a skipped result for a successful seed and constructs a `refresh-all` request only with explicit `cgc_refresh_fallback`; otherwise it reports the disabled fallback. This helper does not restore the removed refresh operation.
- A touch pass cannot remove phantom graph entries left by deletions or rename sources. Those residuals remain explicitly stale until refresh; they must not be reported as `caughtUp`. That field records the touch-delivery result, not independently observed completion of watcher indexing.
- Seed HEAD and divergence reads use `kernel/git_command.py::run_git`, which removes the eight ambient repository selectors: `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, and `GIT_PREFIX`. The divergence read supplies a 60-second timeout, below the runner's 300-second general local bound.
- Retained seed helpers construct lifecycle requests with `args.timeout`. The gated `_refresh_after_seed` helper likewise passes `args.timeout` when it constructs a `refresh-all` request; the removed CGC refresh module supplies no current operation to execute that request. These request shapes establish neither provider setup nor a working provider CLI entry point.
- Compose assets impose memory limits of 2g on FalkorDB, 1g on the batch runner, and 512m on each rendered watcher. FalkorDB and watchers have `restart: unless-stopped`; the batch runner does not inherit that restart promise. These limits bound container memory rather than guaranteeing that the host cannot exhaust resources.

## Historical provider-surface wording

The following earlier wording is retained as provenance, not a current consumer or operation contract:

> `setup.py` constructs isolated worktree settings and contains install and seed preparation entry points. `seed.py` exports a source graph, delegates path rewriting to `bundle.py`, and imports the rewritten graph into the target runtime. `context/` exposes layout, materialization, cleanup, and patch helpers; `lifecycle/` exposes backend, compose, runner, installation, process, query, and refresh implementations.
>
> These are retained implementation routes. Ordinary enabled-provider setup currently skips CGC: `providers/setup_common.py::provider_enabled` returns `False` for `codegraphcontext-code`, regardless of its settings block. The CGC install and preparation entry points consult that gate before doing their work. This boundary does not establish that every direct lifecycle caller is disabled; `lifecycle_service.py` still contains direct CGC action dispatch.
>
> - Seed export and import pass `args.timeout` through the lifecycle request to the bounded runner operation. The retained forced-index refresh implementation instead passes `UNLIMITED_TIMEOUT`, which the command runner translates to no subprocess duration limit. These implementation details do not establish a current `providerSetupSeconds` settings authority or a working provider CLI entry point.

> The bundle pipeline starts the source backend, exports the source graph, rewrites source-root paths to target-root paths, and imports the rewritten bundle. Seed arguments intended for the Linux runner container use `to_container_path` from `providers/context_common.py`. It converts host paths to POSIX form and strips a Windows drive prefix. For an isolated worktree, the target bundle runtime root is resolved from the isolated settings when those settings can supply it, keeping the bundle under the runtime mounted by that runner.
>
> - The retained seed policy favors a graph copy plus a bounded delta over an automatic full rebuild. Successful seeding skips refresh; unsuccessful seeding invokes `refresh-all` only when `cgc_refresh_fallback` is explicitly enabled. Otherwise it reports that the fallback is disabled.

## Evidence

- CGC setup orchestration lives in the provider-owned setup module. [1]

- Ordinary enabled-provider setup excludes CGC even with retained settings; direct lifecycle implementation is a separate route. [2]
- Seed resolution separates source and target ends, preserves precondition refusals, and records computable commit divergence for catch-up. [3]
- Catch-up waits for watcher readiness, retains untouchable residuals as stale, and calls the touch-delivery result caughtUp only without residuals. [4]
- Container memory caps and restart policies distinguish the backend and watchers from the batch runner. [5]

- The facade enumerates core, compose, backend, runner, installation and process_control only. [6]
- The typed watcher service admits only stop and shutdown-all. [7]
- Watcher aggregation maps both CGC stop-class actions to cgc_stop_all. [8]
- CGC preparation returns before seed work when the selected-provider predicate is false. [9]
- The retained opt-in refresh request uses args.timeout and is not a restored refresh implementation. [10]
