# `w-02-light-task-workflow` template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T01:06+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This template defines the required shape of `w-02-light-task-workflow` skill `task.md` artifacts inside task wrapper folders.

## Code Commentary

### Logic

The template includes status, repo, type, objective, requirements, a `## Design` section, implementation steps, examples, decision log, open questions, and references. The `## Design` section sits above implementation steps and holds the settled design sized to the request per the Task Collaboration Doctrine (`tasks/AGENTS.md`), or a note that no design reasoning is needed. Usage rules include resolved `c-08-ar-coordination-context-resolver` skill paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, `c-09-git-worktree-manager` skill places `contract.md` beside that file.

### Conventions

Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples.

### Invariants And Boundaries

The template is a task artifact schema, not an onboarding schema. Its contents can cite onboarding but should not replace it.

### Todos

No current template TODO beyond adding examples from a real task wrapped by the `c-09-git-worktree-manager` skill.

### Docs References

No external domain documentation applies to this repository-local template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The template is the stable artifact shape for `w-02-light-task-workflow` skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references. | L8-L97 | [`w-02-light-task-workflow` template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md) |
| Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request. | L99-L114 | [`w-02-light-task-workflow` template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current template file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-31T01:06+02:00: Added a `## Design` section above implementation steps (settled design sized per the Task Collaboration Doctrine) plus a usage rule for it; corrected the earlier "design philosophy" description that did not match the actual template.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-10T00:47: Updated after the `w-02-light-task-workflow` skill template became the `task.md` file inside task wrapper folders.
- 2026-05-09T22:57: Refreshed verification metadata and tightened template citations.
- 2026-05-09T21:59: Updated after worktree task contracts became part of the light-task artifact placement rules.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `w-02-light-task-workflow` skill task template.
