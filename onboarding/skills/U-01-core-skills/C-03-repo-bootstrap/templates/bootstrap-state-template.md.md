# bootstrap-state-template.md

| Field                  | Value                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| repository             | agents-remember-md                                                                         |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md`         |
| doc_type               | `file-level-onboarding`                                                                    |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                     |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                                                                                         |
| lastVerifiedCommitDate |                                                                                            2026-05-14T20:13:45+02:00|

## Purpose

This template defines the persistent bootstrap state file that allows C-03 runs to pause and resume across sessions.

## Code Commentary

### Logic

The template tracks run metadata, phase status, areas, governing routes, waves, decisions, parking lot items, blockers, deferred files, and the next recommended action.

### Conventions

`bootstrap/STATE.md` is read first and updated last in each bootstrap session. It is state and coordination memory for the bootstrap, not file-level onboarding.

### Invariants And Boundaries

The state file must preserve decisions, blockers, and low-confidence parking-lot items rather than promoting them into durable facts.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                  | Citations | Source Path                                                                                  |
| ---------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
| The state template records bootstrap mode, memory root, branch, topology, and phase status across the full C-03 lifecycle. | L1-L29    | [bootstrap-state-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md) |
| The state template tracks areas, governing routes, waves, decisions, parking lot items, blockers, deferred files, and next action. | L31-L74   | [bootstrap-state-template.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md) |
| C-03 requires every bootstrap to maintain `bootstrap/STATE.md` from this template. | L385-L412 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the bootstrap state template. Verification metadata remains blank until the source file is committed.
