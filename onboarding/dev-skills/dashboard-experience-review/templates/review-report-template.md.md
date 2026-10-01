# dev-skills/dashboard-experience-review/templates/review-report-template.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The shape of the per-run review report the skill emits inline at Stage 6 (findings only).

## Code Commentary

### Logic

Six sections: Scenario Coverage Matrix; State Coverage Matrix (blanks = missing views); ranked
Missing-View backlog; a severity-rated findings table with a `delegated-to` column; a glance /
self-explanatory verdict; and a Delegations section folding sub-skill outputs by reference. Plus a
severity key.

### Conventions

Mirrors the design-review triage convention so the report slots into the gated fix pipeline. The
`delegated-to` column records OWNED vs which sub-skill owns each detail.

### Invariants And Boundaries

- Findings only — the report records issues for a separate gated fix job; nothing is changed.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation found.

### Repo-Internal References

- Stage 6 of the pipeline, which emits this report. [1]

### Cross-Repo References

No meaningful cross-repo references found.
