# dev-skills/dashboard-experience-review/delegation-map.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/delegation-map.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pipeline (Stage 4) that consumes this delegation map. | "Stage 4" | dev-skills/dashboard-experience-review/SKILL.md:46-106 |

## Cross-Repo References

The delegate skills are installed Claude Code skills / MCP servers in the harness, not repo files.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04: anchored the governing Stage 4 delegation
  reference to the local skill source.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the skill (issue #92).
