# dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The live catalog instantiated from this template. | `# Cockpit Dashboard — Workflow Scenario Catalog` | docs/design/dashboard/scenario-catalog.md:1-166 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 1 citation row; scoped citation fixing regenerated the source range.
- 2026-06-23T05:31 — Created with the skill (issue #92).
