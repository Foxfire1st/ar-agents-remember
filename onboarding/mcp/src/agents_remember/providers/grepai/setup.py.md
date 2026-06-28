# mcp/src/agents_remember/providers/grepai/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`setup.py` owns the GrepAI-specific provider setup branch for install and prepare refresh orchestration.

## Code Commentary

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The setup facade calls this module during install and prepare. | [provider_setup.py](provider_setup.py.md) |
| Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. | [core.py](lifecycle/core.py.md) |

## Update History

- 2026-06-10T07:30+02:00 — `install_enabled_provider` and `prepare_enabled_provider` announce their phases (`grepai install`, `grepai clone-db`) through `setup_progress_from(args)` so background worktree setup is observable mid-run (GitHub #53). Behavior and return shapes unchanged.
- 2026-05-31T12:50+02:00 — `prepare_enabled_provider` dropped the leading `args.coordination_root` argument from its `load_settings(...)` call to match `setup_common.load_settings`/`settings_path`, which no longer take a `coordination_root` parameter; behaviour-preserving, no documented prose named the call so no prose corrected (1.0.0 review remediation).
- 2026-05-25T19:50+02:00: Created when GrepAI setup orchestration was extracted out of `provider_setup.py`.
