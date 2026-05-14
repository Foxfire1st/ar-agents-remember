# route-local-overview-card-template.md

| Field                  | Value                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                                 |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-card-template.md`       |
| doc_type               | `file-level-onboarding`                                                                            |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                             |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                                 |
| lastVerifiedCommitDate |                                                                                                    2026-05-14T18:37:02+02:00|

## Purpose

This template defines the overview card used as a scoped work order before a route-local overview worker writes durable memory.

## Code Commentary

### Logic

The overview card records route metadata, why the overview exists, governed paths, what the overview must explain, required inputs, backlinks, downlinks, and open questions.

### Conventions

Overview cards are generated before overview waves. They constrain workers so route-local overview creation does not become broad repo rediscovery.

### Invariants And Boundaries

An overview card is a promotion artifact, not durable source onboarding. The durable output is the route-local `overview.md` produced from it.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                         | Citations | Source Path                                                                                              |
| ----------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------- |
| The overview card template records route metadata, governed paths, required explanation topics, inputs, links, and open questions. | L1-L61    | [route-local-overview-card-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/route-local-overview-card-template.md) |
| C-03 Phase 4C writes overview cards for each selected governing route before route-local overview waves. | L738-L762 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the route-local overview card template. Verification metadata remains blank until the source file is committed.
