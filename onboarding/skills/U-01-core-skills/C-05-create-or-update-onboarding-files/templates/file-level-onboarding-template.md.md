# file-level-onboarding-template.md

| Field                  | Value                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| repository             | agents-remember-md                                                                                           |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md` |
| doc_type               | `file-level-onboarding`                                                                                      |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                                       |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                                                                   |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

`file-level-onboarding-template.md` is the canonical Markdown template for external file-level onboarding units. C-05 uses it to keep sidecar onboarding structurally consistent across source files and now includes governing-overview metadata plus a `## Governing Overview` backlink section.

## Code Commentary

### Logic

The template defines the required metadata table, governing overview backlink, semantic commentary sections, reference sections, and append-only update-history convention for one concrete source file. It tells maintainers to use the resolved C-08 `system/sources.md` only as a discovery aid for documentation evidence, to cite actual proving sources, and to keep reference sections explanation-first rather than citation-only.

### Conventions

The template uses placeholder text in angle brackets and keeps the generated artifact in plain Markdown. Reference tables are preserved even when no relevant external, same-repository, or cross-repo evidence exists, because the absence of evidence is itself useful context for future maintenance. The governing overview section links to the nearest route-local overview when one exists, otherwise an ancestor or root overview.

### Invariants And Boundaries

This file defines structure and wording for generated onboarding; it does not decide which source paths are eligible, resolve storage roots, or perform drift classification. C-08 owns context resolution, C-02 owns drift classification, and C-05 workflows own when this template is applied.

### Todos

After this working-tree update lands, refresh verification metadata to the committed template revision.

### Docs References

No external domain documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The template is governed by C-05's onboarding-maintenance contract and is consumed when creating file-level sidecars.

| Finding                                                                                                                      | Citations | Source Path                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-05 routes file-level onboarding creation to this template and requires strict one-to-one mirroring with source files and route-local governing overview links. | L19-L51 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| The template defines metadata including `governingOverview`, the governing overview section, purpose, code commentary, reference sections, and append-only update-history guidance. | L1-L68 | [file-level-onboarding-template.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Refreshed for governing overview metadata and backlink guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T11:30: Created onboarding for the file-level onboarding template after its update-history wording was clarified.
