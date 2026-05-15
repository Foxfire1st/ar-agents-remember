# bootstrap-state-template.md

| Field                  | Value                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| repository             | agents-remember-md                                                                         |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md`         |
| doc_type               | `file-level-onboarding`                                                                    |
| lastUpdated            | 2026-05-14T21:16+02:00                                                                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964`                                                                                         |
| lastVerifiedCommitDate |                                                                                            2026-05-15T04:04:02+02:00|

## Purpose

This template defines the persistent bootstrap state file that allows C-03 runs to pause and resume across sessions, including existing-memory slice maintenance and the closeout boundary.

## Code Commentary

### Logic

The template tracks run metadata, onboarding root, source inventory gate status, phase status, areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and the next recommended action.

### Conventions

`bootstrap/STATE.md` is read first and updated last in each bootstrap session. It is state and coordination memory for the bootstrap, not file-level onboarding, and it records whether closeout has merely been requested after handoff.

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
| The state template records bootstrap mode, memory root, onboarding root, branch, topology, source inventory status, and phase status across the full C-03 lifecycle. | L1-L31    | [bootstrap-state-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md) |
| The state template tracks areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and next action. | L33-L88   | [bootstrap-state-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/bootstrap-state-template.md) |
| C-03 requires every bootstrap to maintain `bootstrap/STATE.md` from this template. | L411-L438 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T21:16+02:00: Refreshed for onboarding-root/source-inventory fields, existing-memory slice maintenance state, route cleanup statuses, and the separate closeout boundary. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the bootstrap state template. Verification metadata remains blank until the source file is committed.
