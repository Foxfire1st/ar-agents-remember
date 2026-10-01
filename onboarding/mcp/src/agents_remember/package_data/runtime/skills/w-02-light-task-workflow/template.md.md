# `w-02-light-task-workflow` template.md

## Purpose

This template defines the required shape of `w-02-light-task-workflow` skill `task.md` artifacts inside task wrapper folders. Slice 3c makes it the **render spec** for the JSON-primary task document: the `task_doc` MCP tool renders an `ar-task-document/v1` JSON into exactly this shape (series master files stay hand-authored markdown).

## Code Commentary

### Logic

The synchronized task template separates protocol events from review-handoff attempts and makes
each attempt a lightweight content-addressed view rather than a duplicate master evidence body.

The template includes status, repo, type, objective, requirements, a `## Design` section, implementation steps, examples, decision log, open questions, and references. The `## Design` section sits above implementation steps and holds the settled design sized to the request per the Task Collaboration Doctrine (`tasks/AGENTS.md`), or a note that no design reasoning is needed. Usage rules include resolved `c-08-ar-coordination-context-resolver` skill paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, `c-09-git-worktree-manager` skill places `contract.md` beside that file.

### Conventions

Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples; a planning slice that instead defers its examples to the plan gate sets `codeExamplesNote` so the section reads as deferred rather than none-needed. A leaf doc may also carry a `statusNote` suffix, `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References for bespoke prose — the escape hatch; the standard sections stay the backbone (R4).

### Invariants And Boundaries

The template is a task artifact schema, not an onboarding schema. Its contents can cite onboarding but should not replace it.

### Todos

No current template TODO beyond adding examples from a real task wrapped by the `c-09-git-worktree-manager` skill.

### Docs References

No external domain documentation applies to this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The template is the stable artifact shape for `w-02-light-task-workflow` skill.

- The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references. [1]
- Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request. [2]

### Cross-Repo References

No sibling repository evidence is needed for the current template file.

No meaningful cross-repo references found.

## Series-Contract Notes

The light-task template's artifact guidance points worktree-backed tasks at the leaf enclosure contract path under `enclosures/<leaf-id>/series-contract.md`.

## M38 Stable-Requirement Template Projection

The task scaffold now gives every requirement a stable ID and references the per-ID builder
acceptance envelope and reviewer verdict. Usage rules require complete delivery/verification
evidence and no overall pass with a rejected ID, while durable-evidence promotion remains separate.
The installed file is a synchronized render/template projection and owns no independent schema.
Each projection links the immutable version-addressed packet and its durable corpus ruling; the
task document remains non-normative summary rather than a compatibility copy of the contract.

## M40-M43 Leaf-Template Projection

The installed leaf template separates semantic versions from immutable exact-candidate attempts,
requires separate reviewer records and closed failure classes, and preserves the two authorized
invalidation paths.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
