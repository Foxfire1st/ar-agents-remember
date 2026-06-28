# `w-02-light-task-workflow` template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-19T06:03+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|

## Purpose

This template defines the required shape of `w-02-light-task-workflow` skill `task.md` artifacts inside task wrapper folders. Slice 3c makes it the **render spec** for the JSON-primary task document: the `task_doc` MCP tool renders an `ar-task-document/v1` JSON into exactly this shape (series master files stay hand-authored markdown).

## Code Commentary

### Logic

The template includes status, repo, type, objective, requirements, a `## Design` section, implementation steps, examples, decision log, open questions, and references. The `## Design` section sits above implementation steps and holds the settled design sized to the request per the Task Collaboration Doctrine (`tasks/AGENTS.md`), or a note that no design reasoning is needed. Usage rules include resolved `c-08-ar-coordination-context-resolver` skill paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, `c-09-git-worktree-manager` skill places `contract.md` beside that file.

### Conventions

Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples; a planning slice that instead defers its examples to the plan gate sets `codeExamplesNote` so the section reads as deferred rather than none-needed. A leaf doc may also carry a `statusNote` suffix, `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References for bespoke prose — the escape hatch; the standard sections stay the backbone (R4).

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
| The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references. | L8-L97 | [`w-02-light-task-workflow` template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md) |
| Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request. | L99-L114 | [`w-02-light-task-workflow` template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current template file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The light-task template's artifact guidance points worktree-backed tasks at the leaf enclosure contract path under `enclosures/<leaf-id>/series-contract.md`.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged light-task template now points worktree-backed tasks at `enclosures/<leaf-id>/series-contract.md` instead of sibling `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00: Slice 3c reopened (R4, leaf-doc fidelity) — extended the status Usage Rule to cover the leaf extensions: a `statusNote` suffix, `headerNotes`, and freeform `sections` after References (the escape hatch; standard sections stay the backbone). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15+02:00: Slice 3c reopened (R3, deferred-examples honesty) — added the Usage Rule for `codeExamplesNote` (a deferred planning slice sets it so the rendered Proposed Code Examples section says so instead of "none needed"). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — documented that this template is the render spec for the JSON-primary `task_doc` tool (renders `ar-task-document/v1` JSON into this `task.md` shape). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-05-31T01:06+02:00: Added a `## Design` section above implementation steps (settled design sized per the Task Collaboration Doctrine) plus a usage rule for it; corrected the earlier "design philosophy" description that did not match the actual template.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-10T00:47: Updated after the `w-02-light-task-workflow` skill template became the `task.md` file inside task wrapper folders.
- 2026-05-09T22:57: Refreshed verification metadata and tightened template citations.
- 2026-05-09T21:59: Updated after worktree task contracts became part of the light-task artifact placement rules.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `w-02-light-task-workflow` skill task template.
