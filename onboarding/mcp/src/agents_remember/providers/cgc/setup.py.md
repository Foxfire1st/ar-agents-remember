# mcp/src/agents_remember/providers/cgc/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7` |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`setup.py` owns provider-level CodeGraphContext setup orchestration and isolated worktree settings generation.

## Code Commentary

### Logic

It defines `IsolatedCgcOptions`, builds isolated CGC settings for worktree provider runtimes, writes those settings when requested, runs `cgc install-all`, and runs CGC prepare by attempting seed first and then refresh fallback when allowed.

### Invariants And Boundaries

- Isolated CGC runtime settings require an explicit target repository root.
- Seed orchestration and bundle rewriting live in `seed.py` and `bundle.py`; this file keeps provider-level setup flow only.
- A successful seed skips refresh with an explicit skipped result; a failed seed falls back to refresh only when `cgc_refresh_fallback` is enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider setup facade calls this module for CGC install, prepare, and isolated settings. | [provider_setup.py](provider_setup.py.md) |
| CGC seed orchestration lives in the seed module. | [seed.py](seed.py.md) |
| CGC lifecycle install and refresh commands are dispatched through the lifecycle facade. | [lifecycle package](../lifecycle/__init__.py.md) |

## Update History

- 2026-05-25T19:50+02:00: Created when CGC provider-level setup behavior was extracted out of `provider_setup.py`.
