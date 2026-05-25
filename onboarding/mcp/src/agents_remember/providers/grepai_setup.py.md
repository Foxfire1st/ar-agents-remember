# mcp/src/agents_remember/providers/grepai_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`grepai_setup.py` owns the GrepAI-specific provider setup branch for install and prepare refresh orchestration.

## Code Commentary

### Logic

It checks whether `grepai-memory` is selected and enabled, then returns lifecycle `install` or `refresh` command payloads for the Docker-owned GrepAI provider. The actual lifecycle behavior remains under `providers.lifecycle` and its GrepAI lifecycle modules.

### Invariants And Boundaries

- GrepAI setup remains Docker-owned; this module does not introduce host binary setup.
- `skip_grepai` suppresses GrepAI setup through the shared provider-selection helper.
- Watcher orchestration remains in the `provider_setup.py` facade because it spans providers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The setup facade calls this module during install and prepare. | [provider_setup.py](provider_setup.py.md) |
| Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. | [lifecycle_modules/grepai/core.py](lifecycle_modules/grepai/core.py.md) |

## Update History

- 2026-05-25T19:50+02:00: Created when GrepAI setup orchestration was extracted out of `provider_setup.py`.
