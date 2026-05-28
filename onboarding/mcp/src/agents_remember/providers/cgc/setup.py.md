# mcp/src/agents_remember/providers/cgc/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T13:40+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`setup.py` owns provider-level CodeGraphContext setup orchestration and isolated worktree settings generation.

## Code Commentary

### Logic

It defines `IsolatedCgcOptions`, builds isolated CGC settings for worktree
provider runtimes, writes those settings when requested, runs `cgc install-all`,
and runs CGC prepare by attempting seed first and then refresh fallback when
allowed. Isolated CGC watcher logs are written under the workflow-local central
`logs/providers/codegraphcontext/<instance>/<repoId>/watch.log` tree. Isolated
settings do not emit `venvRoot`; worktree CGC execution stays Docker-runner
owned.

### Invariants And Boundaries

- Isolated CGC runtime settings require an explicit target repository root.
- Isolated CGC logs should follow the same central `logs/providers/...` layout
  as workspace providers.
- Isolated CGC settings must not introduce host venv or executable install
  fields into the main coordination root.
- Seed orchestration and bundle rewriting live in `seed.py` and `bundle.py`; this file keeps provider-level setup flow only.
- A successful seed skips refresh with an explicit skipped result; a failed seed falls back to refresh only when `cgc_refresh_fallback` is enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider setup facade calls this module for CGC install, prepare, and isolated settings. | [provider_setup.py](provider_setup.py.md) |
| CGC seed orchestration lives in the seed module. | [seed.py](seed.py.md) |
| CGC lifecycle install and refresh commands are dispatched through the lifecycle facade. | [lifecycle package](../lifecycle/__init__.py.md) |

## Update History

- 2026-05-28T13:40+02:00: Updated after isolated CGC settings stopped emitting `venvRoot`.
- 2026-05-28T12:32+02:00: Updated after isolated CGC settings moved watcher logs under `logs/providers/`.
- 2026-05-25T19:50+02:00: Created when CGC provider-level setup behavior was extracted out of `provider_setup.py`.
