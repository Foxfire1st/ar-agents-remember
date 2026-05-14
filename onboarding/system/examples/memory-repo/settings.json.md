# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/memory-repo/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `6d413269e6f3b0317829def3b5c77b11631285ac` |
| lastVerifiedCommitDate | 2026-05-13T13:50:13+02:00                  |

## Purpose

This JSON example models machine-readable settings for a external memory repo.

## Code Commentary

### Logic

The example uses settings version 2, `memory-repo` onboarding storage, include/exclude path rules, and a branch-gated `crossRepo.allow` entry.

### Conventions

This file demonstrates memory-owned policy, not coordinator routing.

### Invariants And Boundaries

`onboarding.storage` decides where eligible onboarding lives, `onboarding.pathRules` decides eligibility, and `crossRepo.allow` opts into adjacent repositories.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The JSON example declares version 2 memory-repo storage and path-rule include/exclude filters. | L1-L17 | [system/examples/memory-repo/settings.json](agents-remember-md/system/examples/memory-repo/settings.json) |
| The JSON example shows a branch-gated cross-repo allowance with code and memory inclusion flags. | L18-L28 | [system/examples/memory-repo/settings.json](agents-remember-md/system/examples/memory-repo/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the memory-repo settings JSON example.
