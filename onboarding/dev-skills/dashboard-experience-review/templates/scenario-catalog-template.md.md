# dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../../overview.md` |

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

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The live catalog instantiated from this template. | whole file | [docs/design/dashboard/scenario-catalog.md](agents-remember/docs/design/dashboard/scenario-catalog.md) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the skill (issue #92).
