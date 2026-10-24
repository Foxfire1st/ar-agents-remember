# skills/w-02-light-task-workflow/template.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This file is the scaffold and render specification for JSON-primary `light` and `subTask`
documents: author through `task_doc` and do not hand-edit generated Markdown. For a new series,
create the JSON-primary master with `task_doc` `create` and `kind:"master"` first, then create its
indexed child documents before leaf `waitsFor` writes. Existing hand-authored Markdown remains
unchanged until intentionally migrated. The scaffold defines the stable section structure, live
checklist shape, and filtered requirement projection. [4]

## Current Source Qualification

Rule 3 now names this skill as the owner of the leaf contract a worktree-backed task stores at `<task-root>/<task-slug>/enclosures/<leaf-id>/series-contract.md`; the inherited wording that names a worktree-manager skill describes the retired owner.

## Code Commentary

### Logic

The task links each stable ID and exact approved version to its canonical packet and labels the
topology role. It records design, implementation steps, representative code examples, append-only
decisions, references to the corpus ruling, builder acceptance, and reviewer adjudication.

The references and usage rules now require one physical leaf Requirement Attempt Journal:
lightweight immutable worker records are created only at review handoff, carry exact
candidate/predecessor and requirement-specific evidence, and link content-addressed expanded
evidence. Independent reviewer records append acceptance or classified rejection to that same
ordered stream. Internal implementation/test/evidence reruns remain separate protocol events and
do not increment attempt IDs or semantic versions. Accepted attempts reopen only through the
bounded regression or approved-revision path; an unrelated later candidate is not a third
invalidation trigger.

### Conventions

- Edit tool-managed tasks through `task_doc`, not rendered Markdown.
- Put each checklist item on its own line and nest verification under its parent outcome.
- Keep standard sections even when one is explicitly not needed.
- Use only approved packet revisions in the requirement projection.

### Invariants And Boundaries

- Task prose never rewrites a requirement contract.
- A leaf has exactly one `primary` revision; adjacent revisions are dependency or preservation
  context only.
- A semantic change increments the requirement version and rebriefs affected work.
- Aggregate completion prose cannot replace per-revision evidence and adjudication.
- Worker/reviewer history is append-only; task prose and summaries cannot rewrite it or reopen
  accepted work.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source governs this render specification.

### Repo-Internal References

- The rendered task links exact approved requirement revisions. [1]

- Usage rules preserve one-primary ownership and per-revision evidence. [2]

- Usage rules separate semantic versions from immutable attempts and name both legal invalidation paths. [3]
### Cross-Repo References

Concrete repository fields and commands arrive through the resolved target-repository context.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

- Light/subTask render ownership, new-series master-first creation, children before waitsFor, and intentionally unmigrated existing Markdown. [4]

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # `w-02-light-task-workflow` template.md
>
> ## Purpose
>
> This template defines the required shape of `w-02-light-task-workflow` skill `task.md` artifacts inside task wrapper folders. Slice 3c makes it the **render spec** for the JSON-primary task document: the `task_doc` MCP tool renders an `ar-task-document/v1` JSON into exactly this shape (series master files stay hand-authored markdown).
>
> ## Code Commentary
>
> ### Logic
>
> The synchronized task template separates protocol events from review-handoff attempts and makes
> each attempt a lightweight content-addressed view rather than a duplicate master evidence body.
>
> The template includes status, repo, type, objective, requirements, a `## Design` section, implementation steps, examples, decision log, open questions, and references. The `## Design` section sits above implementation steps and holds the settled design sized to the request per the Task Collaboration Doctrine (`tasks/AGENTS.md`), or a note that no design reasoning is needed. Usage rules include resolved `c-08-ar-coordination-context-resolver` skill paths and the wrapper location `<task-root>/<task-slug>/task.md`; when worktrees are created, `c-09-git-worktree-manager` skill places `contract.md` beside that file.
>
> ### Conventions
>
> Task files use checkboxes for progress and a table for decisions. The template preserves sections even when a docs-only task does not need code examples; a planning slice that instead defers its examples to the plan gate sets `codeExamplesNote` so the section reads as deferred rather than none-needed. A leaf doc may also carry a `statusNote` suffix, `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References for bespoke prose — the escape hatch; the standard sections stay the backbone (R4).
>
> ### Invariants And Boundaries
>
> The template is a task artifact schema, not an onboarding schema. Its contents can cite onboarding but should not replace it.
>
> ### Todos
>
> No current template TODO beyond adding examples from a real task wrapped by the `c-09-git-worktree-manager` skill.
>
> ### Docs References
>
> No external domain documentation applies to this repository-local template.
>
> No relevant external documentation found.
>
> ## Evidence
>
> ### Repo-Internal References
>
> The template is the stable artifact shape for `w-02-light-task-workflow` skill.
>
> - The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references. (historical reference 1)
> - Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request. (historical reference 2)
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for the current template file.
>
> No meaningful cross-repo references found.
>
> ## Series-Contract Notes
>
> The light-task template's artifact guidance points worktree-backed tasks at the leaf enclosure contract path under `enclosures/<leaf-id>/series-contract.md`.
>
> ## M38 Stable-Requirement Template Projection
>
> The task scaffold now gives every requirement a stable ID and references the per-ID builder
> acceptance envelope and reviewer verdict. Usage rules require complete delivery/verification
> evidence and no overall pass with a rejected ID, while durable-evidence promotion remains separate.
> The installed file is a synchronized render/template projection and owns no independent schema.
> Each projection links the immutable version-addressed packet and its durable corpus ruling; the
> task document remains non-normative summary rather than a compatibility copy of the contract.
>
> ## M40-M43 Leaf-Template Projection
>
> The installed leaf template separates semantic versions from immutable exact-candidate attempts,
> requires separate reviewer records and closed failure classes, and preserves the two authorized
> invalidation paths.
>
> ## 2026-08-27 Attempt Boundary Clarification
>
> This packaged projection preserves the canonical phase boundary: validate before append; a
> malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
> a malformed handed-off attempt requires independent rejection before successor handoff.

Inherited reference 1 commentary (not a revalidated target):

> The template requires status metadata, objective, requirements, a `## Design` section (sized per `tasks/AGENTS.md`), implementation steps, examples, decision log, open questions, and references.
>
> Anchor: `# Light Task Template`

Inherited reference 2 commentary (not a revalidated target):

> Usage rules require `c-08-ar-coordination-context-resolver` skill resolved paths, wrapper-folder task placement, checklist progress, status changes, append-only decisions, and sizing the `## Design` section to the request.
>
> Anchor: "# Task: <Title>"

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [5]
