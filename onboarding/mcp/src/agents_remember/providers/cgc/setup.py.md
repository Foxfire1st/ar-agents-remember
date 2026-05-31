# mcp/src/agents_remember/providers/cgc/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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
owned. The provider sub-settings lookup uses the shared
`provider_settings(settings, CGC_PROVIDER_ID)` helper from `setup_common`; the
former local `_cgc_provider`/`context_providers` wrapper was removed.

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

- 2026-05-31T12:50+02:00 — Removed local `_cgc_provider` helper; provider sub-settings now read via shared `provider_settings(settings, CGC_PROVIDER_ID)` from `setup_common` (import swapped from `context_providers`), behaviour-preserving; noted the helper source in Logic (1.0.0 review remediation).
- 2026-05-28T13:40+02:00: Updated after isolated CGC settings stopped emitting `venvRoot`.
- 2026-05-28T12:32+02:00: Updated after isolated CGC settings moved watcher logs under `logs/providers/`.
- 2026-05-25T19:50+02:00: Created when CGC provider-level setup behavior was extracted out of `provider_setup.py`.
