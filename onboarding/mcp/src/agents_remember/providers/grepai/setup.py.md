# mcp/src/agents_remember/providers/grepai/setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7` |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`setup.py` owns the GrepAI-specific provider setup branch for install and prepare refresh orchestration.

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
| Docker-owned GrepAI lifecycle behavior lives in the GrepAI lifecycle modules. | [core.py](lifecycle/core.py.md) |

## Update History

- 2026-05-25T19:50+02:00: Created when GrepAI setup orchestration was extracted out of `provider_setup.py`.
