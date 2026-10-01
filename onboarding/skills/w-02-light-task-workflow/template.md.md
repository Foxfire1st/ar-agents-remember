# skills/w-02-light-task-workflow/template.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This file is both the human scaffold and render specification for a JSON-primary light task. It
defines the stable section structure, live checklist shape, and filtered requirement projection.

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
