# mcp/src/agents_remember/providers/grepai/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The setup facade calls this module during install and prepare. | `install_enabled_provider` | mcp/src/agents_remember/providers/provider_setup.py:210-230 |
| Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. | "Docker-owned" | onboarding/mcp/src/agents_remember/providers/grepai/lifecycle/core.py.md:17-20 |

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 2 citation rows: the facade-call row now cites the calling code (providers/provider_setup.py L210-L230, `install_enabled_provider`) and the lifecycle-modules row cites the core.py.md card L17-L20. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update for `run_lifecycle`'s new
  `LifecycleCommand` signature. Same argv, same results. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-06-10T07:30+02:00 — `install_enabled_provider` and `prepare_enabled_provider` announce their phases (`grepai install`, `grepai clone-db`) through `setup_progress_from(args)` so background worktree setup is observable mid-run (GitHub #53). Behavior and return shapes unchanged.
- 2026-05-31T12:50+02:00 — `prepare_enabled_provider` dropped the leading `args.coordination_root` argument from its `load_settings(...)` call to match `setup_common.load_settings`/`settings_path`, which no longer take a `coordination_root` parameter; behaviour-preserving, no documented prose named the call so no prose corrected (1.0.0 review remediation).
- 2026-05-25T19:50+02:00: Created when GrepAI setup orchestration was extracted out of `provider_setup.py`.
