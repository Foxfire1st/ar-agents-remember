# dev-skills/dashboard-experience-review/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

The conductor entry point of the `dashboard-experience-review` skill: it reviews a live cockpit
dashboard like a user, owning the workflow-completeness layer and delegating craft dimensions to
installed skills. Findings only.

## Code Commentary

### Logic

Standard skill frontmatter (`name`, `description`) + a body that defines: when-to-use; the two
invocation modes (standalone vs final-step-inside-an-ongoing-task, which reviews the WIP dashboard via
that worktree's same-branch backend); the seven-stage pipeline (Stage 0 scope → 1 ground-truth entity +
scenario model → 2 live observation → 3 owned analyses → 4 delegate → 5 consolidate/severity → 6 emit
report); the OWNED-vs-DELEGATE split; the cross-cutting settled-beat rule; and the outputs (the durable
scenario catalog + a per-run report).

### Conventions

`name` + `description` frontmatter and a `# <name> <Title>` heading, matching the canonical `skills/`
house style even though this skill is not distributed.

### Invariants And Boundaries

- **Findings only** — never edits the dashboard; a fix is a separate gated build job.
- Sample motion/DOM only at a **paused settled beat**; confirm state via CSS class, not opacity.
- Delegate craft/a11y/data/motion-feel; own scenario discovery, missing-view detection,
  observability-parity, motion-as-communication, and Task-6 TUI UX.

### Todos

No open file-local todos.

## Docs References

The review doctrine + scenario catalog the skill enforces live in the repo (outside onboarding scope).

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cyan/amber/green grammar, observability-parity, and settled-beat rules the skill enforces. | whole file | [docs/design/dashboard/review-doctrine.md](agents-remember/docs/design/dashboard/review-doctrine.md) |

## Repo-Internal References

The conductor references its companion docs and templates.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The five encoded analysis passes + persona/severity model the pipeline runs. | whole file | [owned-methods.md](agents-remember/dev-skills/dashboard-experience-review/owned-methods.md) |
| The per-dimension delegate map + constraints. | whole file | [delegation-map.md](agents-remember/dev-skills/dashboard-experience-review/delegation-map.md) |

## Cross-Repo References

No relevant cross-repo evidence found.

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: a prose line had been hard-wrapped at a ` + ` conjunction, leaving the plus at column zero where markdown reads `+ ` as a list bullet, so a wrapped sentence rendered as a spurious new list item mid-thought. The plus moved to the end of the previous line; the rendered prose is character-for-character unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-23T05:31 — Created with the skill (issue #92); dogfooded against the live cockpit dashboard.
