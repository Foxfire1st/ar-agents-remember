# dev-skills/dashboard-experience-review/owned-methods.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/owned-methods.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

The analysis passes the skill runs itself (Stage 3 of `SKILL.md`), plus the persona model and the 0–4
severity model used to consolidate findings (Stage 5).

## Code Commentary

### Logic

Defines the severity model (frequency × impact × persistence, mean across personas); the three personas
(operator / incident-responder / expert); and six runnable methods — (1) scenario-driven cognitive
walkthrough (4 Wharton questions/step), (2) workflow × UI-state matrix → missing views, (3) observability
canon audit (RED/USE + altitude + parity + stale-honesty), (4) motion-as-communication, (5) Task-6 TUI
control-plane review, (6) information-scent / 5-second / progressive-disclosure — plus a re-weighted
Nielsen-10 heuristic backbone.

### Conventions

Each method is a numbered, runnable procedure driven through the Chrome MCP; the settled-beat rule
applies to every visibility/state check.

### Invariants And Boundaries

- A scenario step with no control is a **missing-view** finding (Method 2), Blocker/High if it blocks a
  catalogued scenario.
- A doctrine violation scores one severity tier higher than the same defect in the abstract.
- A control mid-transition is not "absent" — re-check at a settled beat before recording STUCK.

### Todos

No open file-local todos.

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pipeline that invokes these passes at Stage 3, and the OWNED-vs-DELEGATE split. | whole file | [SKILL.md](agents-remember/dev-skills/dashboard-experience-review/SKILL.md) |
| The doctrine whose violations raise severity by a tier. | whole file | [docs/design/dashboard/review-doctrine.md](agents-remember/docs/design/dashboard/review-doctrine.md) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the skill (issue #92).
