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

| Finding | Anchor | Source |
| --- | --- | --- |
| The cyan/amber/green grammar, observability-parity, and settled-beat rules the skill enforces. | `## 2 · Observability-parity (the dominant rule)`; `## 3 · The state-by-colour grammar`; `## 6 · Settled-beat sampling (reliability rule)` | docs/design/dashboard/review-doctrine.md:21-58; docs/design/dashboard/review-doctrine.md:78-84 |

## Repo-Internal References

The conductor references its companion docs and templates.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five encoded analysis passes + persona/severity model the pipeline runs. | `## Severity model`; `## Method 1 — Scenario-driven cognitive walkthrough (Stage 3a)`; `## Method 2 — Workflow × UI-state matrix → missing views (Stage 3b)`; `## Method 3 — Observability canon audit: RED/USE + altitude (Stage 3c)`; `## Method 4 — Motion-as-communication (Stage 3d)`; `## Method 5 — Task-6 TUI control-plane review (Stage 3e)` | dev-skills/dashboard-experience-review/owned-methods.md:7-21; dev-skills/dashboard-experience-review/owned-methods.md:33-111 |
| The per-dimension delegate map + constraints. | `## What the conductor OWNS (no delegate exists)`; `## Delegation table` | dev-skills/dashboard-experience-review/delegation-map.md:11-32 |

## Cross-Repo References

No relevant cross-repo evidence found.

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows with exact headings and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: a prose line had been hard-wrapped at a ` + ` conjunction, leaving the plus at column zero where markdown reads `+ ` as a list bullet, so a wrapped sentence rendered as a spurious new list item mid-thought. The plus moved to the end of the previous line; the rendered prose is character-for-character unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-23T05:31 — Created with the skill (issue #92); dogfooded against the live cockpit dashboard.
