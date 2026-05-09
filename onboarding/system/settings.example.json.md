# settings.example.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/settings.example.json`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

`settings.example.json` is the starter machine-readable settings example for memory roots.

## Code Commentary

### Logic

The file uses settings `version` 2 and keeps `onboarding.storage`, `onboarding.pathRules`, and `crossRepo.allow` as the core machine-readable shape. The generic example still uses repo-sidecar storage because it is the default internal memory shape.

### Conventions

Empty `crossRepo.allow` means cross-repo context is disabled. V2 object entries must include `repo` and `expectedBranch`.

### Invariants And Boundaries

The settings example is generic and should not include workspace-specific repositories or commands.

### Todos

Add a separate fixture if future tests need a populated cross-repo v2 allow list.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The example defines version 2 settings, repo-sidecar storage, path-rule include/exclude filters, and an empty `crossRepo.allow` list. | L1-L21 | [settings.example.json](agents-remember-md/system/settings.example.json) |
| The cross-repo design keeps `settings.json` plus `crossRepo.allow` as the machine-readable settings container. | L38-L73; L416-L457 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for this example.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:59: Created onboarding after settings examples moved to v2 vocabulary.
- 2026-05-09T22:57: Refreshed verification metadata and source-backed settings references.
