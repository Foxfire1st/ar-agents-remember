# skills/w-02-light-task-workflow/template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/w-02-light-task-workflow/template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `onboarding/overview.md` |

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

## Docs References

No external Domain Documentation source governs this render specification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The rendered task links exact approved requirement revisions. | `## Requirement Projection` | skills/w-02-light-task-workflow/template.md:25-39 |
| Usage rules preserve one-primary ownership and per-revision evidence. | `## Usage Rules` | skills/w-02-light-task-workflow/template.md:91-149 |
| Usage rules separate semantic versions from immutable attempts and name both legal invalidation paths. | `## Usage Rules` | skills/w-02-light-task-workflow/template.md:110-175 |

## Cross-Repo References

Concrete repository fields and commands arrive through the resolved target-repository context.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2: separated internal protocol events from review-handoff attempts
  and replaced per-record evidence duplication with content-addressed expanded-evidence links.
- 2026-08-27T20:45+02:00 — Made the detailed leaf journal a single physical append-only record
  stream rather than a pair of potentially divergent report copies.
- 2026-08-27T19:59+02:00 — M42 clarification: scoped successor attempts to unadjudicated changes,
  rejected repairs, and corrections while preserving unrelated accepted work.
- 2026-08-27T18:06+02:00 — M40-M43: added leaf-journal references, immutable candidate-bound
  attempts, independent classified adjudication, successor lineage, and bounded invalidation.
- 2026-08-27T14:52+02:00 — Created onboarding for filtered requirement projections, one-primary
  leaves, and exact-version acceptance evidence.
