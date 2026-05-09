# W-02-light-task-workflow/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/W-02-light-task-workflow/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `f530ee29c986bdece55a39c1f97f7fc25e214d07` |
| lastVerifiedCommitDate | 2026-05-05T18:58                           |

## Purpose

This skill defines W-02, the light durable task workflow for medium-risk or multi-step changes that need a task artifact but not the full heavy workflow stack.

## Code Commentary

### Logic

W-02 creates or updates one task artifact under the C-08 resolved task root, stops for approval before implementation, and uses the artifact checklist as the live execution record.

### Conventions

The skill keeps planning and implementation in a single file. It requires explicit objective, requirements, steps, decision log, open questions, and references.

### Invariants And Boundaries

W-02 task artifacts are planning and execution state. They can trigger onboarding updates through C-05, but they should not be treated as onboarding content.

### Todos

Worktree support may change where task artifacts sit relative to `contract.md`. Update this file after the implemented task-contract flow exists.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

W-02 is the approved workflow used by the preliminary onboarding task and the worktree task stack.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill defines a task artifact as the durable plan/checklist for medium work. | L25-L34 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |
| Agent responsibilities include creating the artifact, stopping for approval, implementing checklist items, and closing out. | L38-L50 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |
| Invariants require resolved roots, no implementation before approval, and no stale task state. | L63-L72 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 skill documentation.
