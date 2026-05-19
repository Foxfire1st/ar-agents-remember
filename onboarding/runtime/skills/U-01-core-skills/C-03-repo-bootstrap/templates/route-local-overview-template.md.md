# route-local-overview-template.md

| Field                  | Value                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                            |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-template.md`       |
| doc_type               | `file-level-onboarding`                                                                       |
| lastUpdated            | 2026-05-19T02:45+02:00                                                                        |
| lastVerifiedCommitHash | `5b26015bb3e9deec8113b1a69a12608bba82cc27`                                                                                            |
| lastVerifiedCommitDate |                                                                                               2026-05-19T03:27:34+02:00|

## Purpose

This template defines durable route-local overview files that live in the mirrored onboarding hierarchy and act as construction pillars for nearby file-level onboarding.

## Code Commentary

### Logic

The template records route metadata, route-based verification fields, parent overview, area explanation, hot-path summary, scope boundaries, structures, operating model, flows, load-bearing files, local invariants, canonical reference sections, file-level onboarding map, child overviews, usage guidance, verification needs, and update history.

### Conventions

Route-local overviews use canonical `Repo-Internal References`, `Cross-Repo References`, and `Docs References` buckets. Their `## Hot Path Summary` stays short because it is copied into generated route indexes for C-04 discovery. Links from nested route-local overviews to root `bootstrap/` evidence packs must be calculated relative to the overview's depth. Their `sourceRoute`, `lastVerifiedCommitHash`, and `lastVerifiedCommitDate` fields give C-02 the deterministic route scope to compare later.

### Invariants And Boundaries

Route-local overviews are durable memory, but they are not replacements for file-level onboarding. They provide local area context and must keep file-specific facts in file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                           | Citations | Source Path                                                                                         |
| ------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------- |
| The route-local overview template defines route metadata, route verification fields, hot-path summary, scope, structures, flows, load-bearing files, local invariants, and traps. | L1-L59    | [route-local-overview-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-template.md) |
| The template uses canonical repo-internal, cross-repo, and docs reference sections, with depth-aware evidence-pack link placeholders. | L60-L81   | [route-local-overview-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-template.md) |
| The template maps file-level onboarding, child overviews, usage order, needs verification, and update history. | L83-L111  | [route-local-overview-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-template.md) |
| C-03 Phase 4D writes route-local overviews in mirrored source folders using this template. | L764-L812 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-19T02:45+02:00: Added `## Hot Path Summary` to the route-local overview template so generated route indexes can expose compact route summaries and source anchors.
- 2026-05-15T11:46+02:00: Updated after the template added `lastVerifiedCommitDate` for deterministic route-local overview drift checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T18:00+02:00: Created onboarding for the route-local overview template and canonical reference-section/depth-aware evidence-link guidance. Verification metadata remains blank until the source file is committed.
