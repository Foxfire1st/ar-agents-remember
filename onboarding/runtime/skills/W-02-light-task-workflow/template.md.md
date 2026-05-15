# W-02 template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/W-02-light-task-workflow/template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This template defines the required shape of W-02 `task.md` artifacts inside task wrapper folders.

## Code Commentary

### Logic

The template includes status, repo, type, objective, design philosophy, requirements, implementation steps, examples, decision log, open questions, and references. Usage rules include resolved C-08 paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, C-09 places `contract.md` beside that file.

### Conventions

Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples.

### Invariants And Boundaries

The template is a task artifact schema, not an onboarding schema. Its contents can cite onboarding but should not replace it.

### Todos

No current template TODO beyond adding examples from a real C-09-wrapped task.

### Docs References

No external domain documentation applies to this repository-local template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The template is the stable artifact shape for W-02.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The template requires status metadata, objective, design philosophy, requirements, implementation steps, examples, decision log, open questions, and references. | L8-L86 | [W-02 template.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/template.md) |
| Usage rules require C-08 resolved paths, wrapper-folder task placement, checklist progress, status changes, and append-only decisions. | L91-L105 | [W-02 template.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/template.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current template file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:47: Updated after the W-02 template became the `task.md` file inside task wrapper folders.
- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 task template.
- 2026-05-09T21:59: Updated after worktree task contracts became part of the light-task artifact placement rules.
- 2026-05-09T22:57: Refreshed verification metadata and tightened template citations.
