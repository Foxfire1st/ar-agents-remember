# file-level-onboarding-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `6b6b80fc358a8717f1a9d6e0f9d16e64fc93820c` |
| lastVerifiedCommitDate | 2026-05-08T19:14                           |

## Purpose

This workflow defines how C-05 creates and maintains onboarding for one concrete source file.

## Code Commentary

### Logic

The workflow selects external sidecar or inline storage, enforces metadata and required sections, reads source and existing onboarding, verifies references, writes concise commentary, and updates verification metadata.

### Conventions

External onboarding mirrors the repo-relative source path under the onboarding root and appends `.md`. The required sections are purpose, code commentary, docs references, repo-internal references, cross-repo references, and update history.

### Invariants And Boundaries

File-level onboarding must describe current source-file behavior. It should not absorb active task plans, and it should not cite registries where actual evidence files are available.

### Todos

Review storage-placement wording after the worktree memory split is implemented.

### Docs References

No external domain documentation is required for this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This workflow is the primary schema source for mirrored file-level onboarding.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Placement rules, metadata fields, and required sections define the file-level onboarding model. | L28-L59 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Section rules define commentary, documentation references, repo-internal references, and cross-repo references. | L48-L82 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Creation and maintenance steps require source inspection, existing-content preservation, and metadata refresh. | L82-L108 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 file-level workflow.
