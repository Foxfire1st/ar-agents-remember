# governing-route-map-template.md

| Field                  | Value                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                          |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/governing-route-map-template.md`      |
| doc_type               | `file-level-onboarding`                                                                     |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                      |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                          |
| lastVerifiedCommitDate |                                                                                             2026-05-14T18:37:02+02:00|

## Purpose

This template defines the governing route map that decides where durable route-local `overview.md` files should live.

## Code Commentary

### Logic

The route map records placement principles, proposed governing routes, deferred routes, cross-cutting concept anchors, parent/child overview relationships, and developer questions.

### Conventions

The map chooses local anchors in the mirrored onboarding hierarchy and avoids creating an overview merely because a folder exists.

### Invariants And Boundaries

Route-local overviews are durable memory, but they must remain local to source traversal and must not replace file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                      | Citations | Source Path                                                                                  |
| -------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
| The governing route map template defines placement principles for route-local overviews and keeps file-level onboarding separate. | L1-L13    | [governing-route-map-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/governing-route-map-template.md) |
| The template records proposed routes, deferred routes, cross-cutting concepts, parent/child overview relationships, and developer questions. | L15-L43   | [governing-route-map-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/governing-route-map-template.md) |
| C-03 Phase 4B writes `bootstrap/governing-route-map.md` from this template before overview cards and waves. | L711-L736 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the governing route map template. Verification metadata remains blank until the source file is committed.
