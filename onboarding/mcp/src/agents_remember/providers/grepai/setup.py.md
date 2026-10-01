# mcp/src/agents_remember/providers/grepai/setup.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`setup.py` owns the GrepAI-specific provider setup branch for install and prepare refresh orchestration.

## Code Commentary

### 260731-EFA-L2 Lifecycle Command Objects

Every `run_lifecycle(...)` call passes a `setup_common.LifecycleCommand(provider="grepai",
action=…, extra_args=tuple(grepai_extra_args(args)))` in place of the positional
`provider`/`action` plus the `extra_args=` keyword; `timeout` and `dry_run` stay keywords. The
argv the lifecycle CLI receives is unchanged.

### Logic

It checks whether `grepai-memory` is selected and enabled, then returns lifecycle `install` or `refresh` command payloads for the Docker-owned GrepAI provider. The actual lifecycle behavior remains under `providers.lifecycle` and its GrepAI lifecycle modules.

`install_enabled_provider` and `prepare_enabled_provider` announce their
phases (`grepai install`, `grepai clone-db`) through
`setup_progress_from(args)` so background worktree setup is observable mid-run
(GitHub #53); return shapes are unchanged.

### Invariants And Boundaries

- GrepAI setup remains Docker-owned; this module does not introduce host binary setup.
- `skip_grepai` suppresses GrepAI setup through the shared provider-selection helper.
- Watcher orchestration remains in the `provider_setup.py` facade because it spans providers.

## Evidence

### Repo-Internal References

- The setup facade calls this module during install and prepare. [1]
- Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. [2]
