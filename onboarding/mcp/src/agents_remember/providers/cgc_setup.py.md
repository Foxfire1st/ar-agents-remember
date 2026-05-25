# mcp/src/agents_remember/providers/cgc_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`cgc_setup.py` owns provider-level CodeGraphContext setup orchestration and isolated worktree settings generation.

## Code Commentary

### Logic

It defines `IsolatedCgcOptions`, builds isolated CGC settings for worktree provider runtimes, writes those settings when requested, runs `cgc install-all`, and runs CGC prepare by attempting seed first and then refresh fallback when allowed.

### Invariants And Boundaries

- Isolated CGC runtime settings require an explicit target repository root.
- Seed orchestration and bundle rewriting live in `cgc_seed.py` and `cgc_bundle.py`; this file keeps provider-level setup flow only.
- A successful seed skips refresh with an explicit skipped result; a failed seed falls back to refresh only when `cgc_refresh_fallback` is enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider setup facade calls this module for CGC install, prepare, and isolated settings. | [provider_setup.py](provider_setup.py.md) |
| CGC seed orchestration lives in the seed module. | [cgc_seed.py](cgc_seed.py.md) |
| CGC lifecycle install and refresh commands are dispatched through the lifecycle facade. | [lifecycle.py](lifecycle.py.md) |

## Update History

- 2026-05-25T19:50+02:00: Created when CGC provider-level setup behavior was extracted out of `provider_setup.py`.
