# skills/l-01-agent-lifecycles/roles/system-specialist.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/system-specialist.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T14:15+02:00 |
| lastVerifiedCommitHash | `a06d2ffcfae2c277f2ae19330c17d09c616b77e8` |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

The optional sprint-bound, investigate-first provider-degradation seat.

## Code Commentary

### Logic

The system specialist binds to `(sprint document, system-specialist)` and investigates one provider
degradation event from durable event, state, metric, log, and runtime evidence. It writes the report
before any fix. Only an explicit orchestrator order authorizes the bounded provider remediation;
otherwise it recommends an action or provider stop. `message_parent` resolves the current sprint
orchestrator without exposing occupant identity.

### Invariants And Boundaries

- Provider-only scope: no task, memory, ledger, lifecycle, or product-code mutation.
- Report before remediation; investigation alone never implies fix authority.
- Completion is the report/fix artifact plus terminal/finalizer truth, not a parallel row.
- Canonical lifecycle doctrine owns this source; generated copies are synchronization outputs.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

`skills/l-01-agent-lifecycles/roles/system-specialist.md` is the canonical role contract; provider
degradation state and the orchestrator brief supply the concrete event evidence.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-28T14:15+02:00 — Replaced the generic dispatch placeholder with the current sprint-bound
  provider-degradation role, report-before-fix rule, structural parent messaging, explicit fix
  authority, and provider-only mutation boundary; stamped the landed candidate.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
