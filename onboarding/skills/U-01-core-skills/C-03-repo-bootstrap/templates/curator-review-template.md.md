# curator-review-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                      |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/curator-review-template.md`      |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                  |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-05-14T18:37:02+02:00|

## Purpose

This template defines the review artifact used after route-overview or file-onboarding waves.

## Code Commentary

### Logic

The curator review records wave status, files reviewed, compliance checks, reference health issues, bucket corrections, required fixes, developer questions, and next-wave recommendation.

### Conventions

Curator reviews are quality gates. They verify route-local placement, strict one-to-one file onboarding, backlinks, reference buckets, source evidence, no absolute paths, append-only history, and low-confidence handling.

### Invariants And Boundaries

Automated bootstrap mode may skip pauses, but it must not skip curator review artifacts. A curator review may require fixes before a wave is treated as complete.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                   | Citations | Source Path                                                                              |
| ----------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------- |
| The curator template records wave metadata, reviewed files, and a compliance checklist for placement, references, links, history, low-confidence claims, and state updates. | L1-L38    | [curator-review-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/curator-review-template.md) |
| The template captures reference-health issues, bucket corrections, required fixes, developer questions, and next-wave recommendations. | L40-L62   | [curator-review-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/curator-review-template.md) |
| C-03 Phase 4I requires a curator review after each overview or onboarding wave. | L918-L942 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the curator review template. Verification metadata remains blank until the source file is committed.
