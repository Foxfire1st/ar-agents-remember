# cross-repo-boundary-pack-template.md

| Field                  | Value                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                                 |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/cross-repo-boundary-pack-template.md`        |
| doc_type               | `file-level-onboarding`                                                                            |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                             |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                                 |
| lastVerifiedCommitDate |                                                                                                    2026-05-14T18:37:02+02:00|

## Purpose

This template defines the evidence pack for allowed cross-repo or external-system boundaries discovered during bootstrap.

## Code Commentary

### Logic

The boundary pack records adjacent repos, branch status, boundary summary, confirmed interfaces, shared contracts, branch/topology notes, same-repo facts that must stay out of cross-repo buckets, risks, and low-confidence ties.

### Conventions

Boundary packs use adjacent repos as read-only evidence when allowed by topology and branch safeguards. Same-repo implementation facts are explicitly routed to `Repo-Internal References`.

### Invariants And Boundaries

The template must not let naming-only or low-confidence ties become durable cross-repo facts. It documents evidence for boundary claims; it does not authorize updating adjacent repo memory.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                  | Citations | Source Path                                                                                               |
| ---------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------- |
| The boundary pack records allowed adjacent repos, boundary summaries, confirmed interfaces, and shared contracts. | L1-L31    | [cross-repo-boundary-pack-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/cross-repo-boundary-pack-template.md) |
| The template records branch/topology notes, same-repo facts that must not be classified as cross-repo, boundary risks, and developer-confirmation needs. | L33-L51   | [cross-repo-boundary-pack-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/cross-repo-boundary-pack-template.md) |
| C-03 Phase 4F writes boundary packs for priority routes with inbound or outbound cross-repo signals. | L837-L859 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the cross-repo boundary pack template. Verification metadata remains blank until the source file is committed.
