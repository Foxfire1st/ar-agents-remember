# dev-skills/dashboard-experience-review/delegation-map.md

## Governing Overview

[overview.md](../overview.md)

## Purpose

The map from each bounded craft dimension to the installed skill / MCP tool the conductor delegates it
to, with per-delegate constraints, plus the optional off-the-shelf delegates.

## Code Commentary

### Logic

Lists what the conductor OWNS (no delegate exists), then a delegation table: glance/hierarchy →
gstack `design-review`; robustness/console/a11y → secondsky `design-review`; code WCAG →
`web-design-guidelines`; chart honesty → `tufte-data-viz`; color separation → `color-expert`; motion
feel/API → `emil-design-eng` + gsap/motion; live observation → Chrome MCP; doc grounding → Context7.
Closes with optional `mastepanoski` delegates (cognitive-walkthrough, ux-audit-rethink) and the
already-installed inventory it relies on.

### Conventions

Findings-only — disable each delegate's auto-fix loop. Hand each delegate a resolved, settled view and
fold its findings by reference rather than re-deriving them.

### Invariants And Boundaries

- A delegate missing at run time is recorded as a coverage gap, never silently skipped.
- Constraints are load-bearing (e.g. scope `tufte-data-viz` to real chart panels only; feed
  `color-expert` measured hex; tell `emil-design-eng` the stack is GSAP/Motion with no CSS animation).

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation found.

### Repo-Internal References

- The pipeline (Stage 4) that consumes this delegation map. [1]

### Cross-Repo References

The delegate skills are installed Claude Code skills / MCP servers in the harness, not repo files.

No meaningful cross-repo references found.
