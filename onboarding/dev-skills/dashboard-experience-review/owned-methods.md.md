# dev-skills/dashboard-experience-review/owned-methods.md

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

## Evidence

### Docs References

No relevant external documentation found.

### Repo-Internal References

- The pipeline that invokes these passes at Stage 3, and the OWNED-vs-DELEGATE split. [1]
- The doctrine whose violations raise severity by a tier. [2]

### Cross-Repo References

No meaningful cross-repo references found.
