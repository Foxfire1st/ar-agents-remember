# mcp/src/agents_remember/providers/cgc/setup.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`setup.py` owns provider-level CodeGraphContext setup orchestration and isolated worktree settings generation.

## Code Commentary

### 260731-EFA-L2 Lifecycle Command Objects

Every `run_lifecycle(...)` call now passes a `setup_common.LifecycleCommand(provider=…, action=…,
extra_args=…)` in place of the positional `provider`/`action` plus the `extra_args=` keyword;
`timeout` and `dry_run` stay keywords. `extra_args` is a tuple (`tuple(cgc_extra_args(args))`)
because the command object is frozen. The argv the lifecycle CLI receives is unchanged.

### Logic

It defines `IsolatedCgcOptions`, builds isolated CGC settings for worktree
provider runtimes, writes those settings when requested, runs `cgc install-all`,
and runs CGC prepare by attempting seed first and then refresh fallback when
allowed. Isolated CGC watcher logs are written under the workflow-local central
`logs/providers/codegraphcontext/<instance>/<repoId>/watch.log` tree. Isolated
settings do not emit `venvRoot`; worktree CGC execution stays Docker-runner
owned. The provider sub-settings lookup uses the shared
`provider_settings(settings, CGC_PROVIDER_ID)` helper from `setup_common`; the
former local `_cgc_provider`/`context_providers` wrapper was removed.

Setup phases announce through `setup_progress_from(args)` (GitHub #53):
`install-all`, `seed`, and — the headline — `_refresh_after_seed(args, seed,
progress)` announces `refresh-all` with `seed_fallback={active, reason}`
BEFORE the reindex runs, because a refused seed changes the expected duration
from ~1 minute to N minutes and the reindex emits nothing observable.
`_seed_failure_reason` derives the reason from the seed result (`reason`,
else `stage`).

### Invariants And Boundaries

- Isolated CGC runtime settings require an explicit target repository root.
- Isolated CGC logs should follow the same central `logs/providers/...` layout
  as workspace providers.
- Isolated CGC settings must not introduce host venv or executable install
  fields into the main coordination root.
- Seed orchestration and bundle rewriting live in `seed.py` and `bundle.py`; this file keeps provider-level setup flow only.
- A successful seed skips refresh with an explicit skipped result; a failed seed falls back to refresh only when `cgc_refresh_fallback` is enabled.

## Evidence

### Repo-Internal References

- The provider setup facade dispatches CGC install and preparation through this module. [1]
- CGC seed orchestration lives in the seed module. [2]
- CGC lifecycle install and refresh commands are dispatched through the lifecycle facade. [3]
