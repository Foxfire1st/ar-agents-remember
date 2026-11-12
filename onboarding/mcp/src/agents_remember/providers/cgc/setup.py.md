# mcp/src/agents_remember/providers/cgc/setup.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`setup.py` retains CodeGraphContext setup helpers and isolated worktree settings generation. Ordinary provider install and preparation are disabled by the shared retired-provider gate.

## Code Commentary

### 260731-EFA-L2 Lifecycle Command Objects

Every `run_lifecycle(...)` call now passes a `setup_common.LifecycleCommand(provider=…, action=…,
extra_args=…)` in place of the positional `provider`/`action` plus the `extra_args=` keyword;
`timeout` and `dry_run` stay keywords. `extra_args` is a tuple (`tuple(cgc_extra_args(args))`)
because the command object is frozen. The argv is still built the same way (setup_common.py:186-229). Its former receiver, the provider lifecycle CLI, no longer exists: providers/lifecycle/ has no __main__.py and binds no main, which the non-dry branch still requests (setup_common.py:218). With both providers retired, that branch is not reached.

### Logic

It defines `IsolatedCgcOptions`, builds isolated CGC settings for worktree
provider runtimes, and writes those settings when requested.
`install_enabled_provider` and `prepare_enabled_provider` first call
`selected_provider_enabled`, which always returns false for
`codegraphcontext-code`; both return an empty result before installation, seed
or progress announcement. The retained code behind that gate describes the
former install-all and seed/fallback request flow, not an enabled product setup.
Isolated CGC watcher logs are written under the workflow-local central
`logs/providers/codegraphcontext/<instance>/<repoId>/watch.log` tree. Isolated
settings do not emit `venvRoot`; worktree CGC execution stays Docker-runner
owned. The provider sub-settings lookup uses the shared
`provider_settings(settings, CGC_PROVIDER_ID)` helper from `setup_common`; the
former local `_cgc_provider`/`context_providers` wrapper was removed.

The retained request branches use `setup_progress_from(args)` for
`install-all` and `seed`. If `_refresh_after_seed` is called directly with a
failed seed and explicit `cgc_refresh_fallback`, it announces `refresh-all` with
`seed_fallback={active, reason}` before constructing the lifecycle request.
`_seed_failure_reason` derives the reason from the seed result (`reason`, else
`stage`). Neither these announcements nor the request object establish an
available refresh operation or bypass the ordinary enablement gate.

### Invariants And Boundaries

- Isolated CGC runtime settings require an explicit target repository root.
- Isolated CGC logs should follow the same central `logs/providers/...` layout
  as workspace providers.
- Isolated CGC settings must not introduce host venv or executable install
  fields into the main coordination root.
- Seed orchestration and bundle rewriting live in `seed.py` and `bundle.py`; this file keeps provider-level setup flow only.
- The retained `_refresh_after_seed` helper returns a skipped result for successful seed, constructs a `refresh-all` request only for explicit `cgc_refresh_fallback`, and otherwise reports a disabled fallback. This request construction does not restore the removed refresh operation.

## Evidence

### Repo-Internal References

- The setup entry points return no CGC install or preparation work because their first selection check excludes the retired provider. [1]

- CGC seed orchestration lives in the seed module. [2]
- The retained helper constructs a refresh request only behind its explicit fallback switch; that construction is separate from current provider availability. [3]
