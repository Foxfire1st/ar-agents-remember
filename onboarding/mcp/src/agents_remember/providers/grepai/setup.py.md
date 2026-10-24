# mcp/src/agents_remember/providers/grepai/setup.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`setup.py` retains the GrepAI-specific install, prepare/clone and refresh helpers. All three entry points are disabled by the shared retired-provider selection gate.

## Code Commentary

### 260731-EFA-L2 Lifecycle Command Objects

Every `run_lifecycle(...)` call passes a `setup_common.LifecycleCommand(provider="grepai",
action=…, extra_args=tuple(grepai_extra_args(args)))` in place of the positional
`provider`/`action` plus the `extra_args=` keyword; `timeout` and `dry_run` stay keywords. The argv is still built the same way (setup_common.py:186-229). Its former receiver, the provider lifecycle CLI, no longer exists: providers/lifecycle/ has no __main__.py and binds no main, which the non-dry branch still requests (setup_common.py:218). With both providers retired, that branch is not reached.

### Logic

Each entry point first calls `selected_provider_enabled`, which always returns false for `grepai-memory`; install, prepare and refresh therefore return an empty result before their work or progress announcements. The retained branches behind that gate construct lifecycle `install`/`refresh` requests or perform the prepare-time clone. Their Docker-owned implementation remains in the GrepAI lifecycle modules, without establishing an available product provisioning route.

The code behind the selection checks retains `setup_progress_from(args)`
announcements for `grepai install` and `grepai clone-db` (GitHub #53). Ordinary
setup reaches neither announcement because the retired provider is never enabled.

### Invariants And Boundaries

- GrepAI setup remains Docker-owned; this module does not introduce host binary setup.
- `skip_grepai` is still a selection operand, but clearing it cannot enable the retired provider: the shared `provider_enabled` check returns false for `grepai-memory`.
- Watcher orchestration remains in the `provider_setup.py` facade because it spans providers.

## Evidence

### Repo-Internal References

- The retained install, prepare/clone and refresh entry points all return no work at the shared retired-provider gate. [1]

- Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. [2]
