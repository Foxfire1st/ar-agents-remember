# bootstrap-handoff-template.md

| Field                  | Value                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                           |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-handoff-template.md`         |
| doc_type               | `file-level-onboarding`                                                                      |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                       |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                           |
| lastVerifiedCommitDate |                                                                                              2026-05-14T18:37:02+02:00|

## Purpose

This template defines the final or pause-point bootstrap handoff artifact.

## Code Commentary

### Logic

The template records run mode, current status, completed coverage, deferred coverage, open questions, risks, completed waves, recommended next waves, developer decisions, and instructions for future agents.

### Conventions

The handoff is a bootstrap-level artifact under `bootstrap/handoff.md`, not durable source-file onboarding. It uses concise tables so a later agent can resume without rereading every intermediate report.

### Invariants And Boundaries

The handoff summarizes trusted and deferred bootstrap coverage; it should not turn unresolved `[LOW]` questions into durable facts. It should point future agents toward state, overviews, boundary packs, and docs packs.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                       | Citations | Source Path                                                                                  |
| --------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
| The handoff template records run status and artifact coverage across root overview, plans, maps, packs, route overviews, and file onboarding. | L1-L20    | [bootstrap-handoff-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-handoff-template.md) |
| The handoff captures trusted/deferred coverage, open questions, risks, waves, decisions, and future-agent usage order. | L22-L68   | [bootstrap-handoff-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-handoff-template.md) |
| C-03 Phase 5 writes `bootstrap/handoff.md` from this template when pausing or completing bootstrap. | L960-L968 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the bootstrap handoff template. Verification metadata remains blank until the source file is committed.
