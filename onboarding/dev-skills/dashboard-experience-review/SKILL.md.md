# dev-skills/dashboard-experience-review/SKILL.md

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

## Evidence

### Docs References

The review doctrine + scenario catalog the skill enforces live in the repo (outside onboarding scope).

- The cyan/amber/green grammar, observability-parity, and settled-beat rules the skill enforces. [1]

### Repo-Internal References

The conductor references its companion docs and templates.

- The five encoded analysis passes + persona/severity model the pipeline runs. [2]
- The per-dimension delegate map + constraints. [3]

### Cross-Repo References

No relevant cross-repo evidence found.
