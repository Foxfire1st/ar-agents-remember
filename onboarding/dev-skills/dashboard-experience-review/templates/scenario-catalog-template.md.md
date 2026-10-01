# dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The per-scenario shape for the durable Workflow Scenario Catalog that Stage 1 authors/refreshes.

## Code Commentary

### Logic

Defines a `W<N>` heading per scenario with persona, a user-language job story, steps → serving view →
stuck risk, the forced UI-states the scenario must verify, and known carried defects; plus the
conventions (GAP = missing view; keep job stories in user language).

### Conventions

One numbered scenario per heading; a step whose serving view is **GAP** must also appear in the
missing-view matrix and as a finding.

### Invariants And Boundaries

- When Stage 1 finds a reachable entity state with no scenario, add one rather than dropping it.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation found.

### Repo-Internal References

- The live catalog instantiated from this template. [1]

### Cross-Repo References

No meaningful cross-repo references found.
