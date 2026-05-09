# settings.example.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/settings.example.md`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

`settings.example.md` explains the human-facing settings file and gives JSON examples for internal and shared memory roots.

## Code Commentary

### Logic

The file now teaches `ar-memory/system/` for internal mode, `ar-management/memory-repos/ar-<repo-name>/system/` for shared mode, v2 JSON examples, and a separate local coordinator scaffold.

### Conventions

The example preserves `system/settings.md` and `system/settings.json` rather than switching to a top-level `settings/` directory.

### Invariants And Boundaries

Cross-repo policy belongs in committed memory settings, not local coordinator settings.

### Todos

Update this file if the project later chooses a storage mode name other than `memory-repo` for shared memory roots.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The settings prose defines internal and shared topology locations and keeps machine-readable settings in sibling `system/settings.json`. | L1-L9 | [settings.example.md](agents-remember-md/system/settings.example.md) |
| Internal settings use version 2 repo-sidecar storage, path rules, and empty `crossRepo.allow`. | L18-L43 | [settings.example.md](agents-remember-md/system/settings.example.md) |
| Shared memory settings use `memory-repo` storage under `ar-management/memory-repos/ar-<repo-name>/system/settings.json` and keep cross-repo policy in committed memory settings. | L45-L82 | [settings.example.md](agents-remember-md/system/settings.example.md) |
| The prose separates storage mode from path-rule eligibility and shows the internal memory and local coordinator scaffold shapes. | L86-L115 | [settings.example.md](agents-remember-md/system/settings.example.md) |

## Cross-Repo References

No sibling repository evidence is needed for this example.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:59: Created onboarding after settings prose moved to the split memory/coordination model.
- 2026-05-09T22:10: Updated summary to call out v2 JSON examples for internal and shared settings.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-file citation with current settings prose evidence.
