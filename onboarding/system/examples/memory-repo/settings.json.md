# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/memory-repo/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T21:38+02:00                     |
| lastVerifiedCommitHash | `4a7c82ddab26013f0cad740227b6896f9bc41aed` |
| lastVerifiedCommitDate | 2026-05-14T21:53:38+02:00|

## Purpose

This JSON example models machine-readable settings for a external memory repo.

## Code Commentary

### Logic

The example uses settings version 2, `memory-repo` onboarding storage, include/exclude path rules with common generated/vendor/build/local excludes, and a branch-gated `crossRepo.allow` entry.

### Conventions

This file demonstrates memory-owned policy, not coordinator routing.

### Invariants And Boundaries

`onboarding.storage` decides where eligible onboarding lives, `onboarding.pathRules` decides eligibility, the standard excludes prevent common generated or local-machine artifacts from being selected, and `crossRepo.allow` opts into adjacent repositories.

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
| The JSON example declares version 2 memory-repo storage and path-rule include/exclude filters with common generated/vendor/build/local exclusions. | L1-L33 | [system/examples/memory-repo/settings.json](agents-remember-md/system/examples/memory-repo/settings.json) |
| The JSON example shows a branch-gated cross-repo allowance with code and memory inclusion flags. | L35-L45 | [system/examples/memory-repo/settings.json](agents-remember-md/system/examples/memory-repo/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T21:38+02:00: Refreshed after the example gained the standard path-rule exclusion baseline for generated/vendor/build/local artifacts. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T13:38: Created onboarding for the memory-repo settings JSON example.
