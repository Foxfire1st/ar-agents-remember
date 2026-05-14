# file-level-onboarding-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T18:00+02:00                     |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b` |
| lastVerifiedCommitDate | 2026-05-14T18:37:02+02:00|

## Purpose

This workflow defines how C-05 creates and maintains onboarding for one concrete source file, including the new governing-overview backlink that connects file-level onboarding to route-local overview context.

## Code Commentary

### Logic

The workflow selects external sidecar or inline storage, enforces metadata and required sections, discovers the nearest governing route-local overview, reads source and existing onboarding, verifies references, writes concise commentary, and updates verification metadata.

### Conventions

External onboarding mirrors the repo-relative source path under the onboarding root and appends `.md`. The required sections now include metadata with `governingOverview`, `## Governing Overview`, purpose, code commentary, repo-internal references, cross-repo references, and update history, with docs references under code commentary.

### Invariants And Boundaries

File-level onboarding must describe current source-file behavior and remain useful when opened directly. It should not absorb active task plans, should not cite registries where actual evidence files are available, and should update the governing overview link when the nearest route-local overview changes.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This workflow is the primary schema source for mirrored file-level onboarding.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Scope and placement rules require one onboarding unit per source file and record the nearest governing route-local overview. | L11-L44 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Section rules require metadata with `governingOverview`, a governing overview section, code commentary, repo-internal references, cross-repo references, and update history. | L52-L85 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Creation steps now identify/read the nearest governing overview before filling the file-level template and cross-checking all reference sections. | L87-L98 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Maintenance steps require re-reading source and onboarding, refreshing changed sections and citations, applying inline syntax rules, and appending update history. | L100-L114 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T18:00+02:00: Refreshed for governing overview metadata, route-local overview discovery, canonical reference sections, and self-sufficient file-level onboarding. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 file-level workflow.
