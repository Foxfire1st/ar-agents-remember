# dev-skills/dashboard-experience-review/templates/review-report-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/dashboard-experience-review/templates/review-report-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `../../overview.md` |

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

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stage 6 of the pipeline, which emits this report. | whole file | [SKILL.md](agents-remember/dev-skills/dashboard-experience-review/SKILL.md) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the skill (issue #92).
