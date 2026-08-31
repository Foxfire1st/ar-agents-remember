# scenario_control.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/scenario_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Provides bounded public control submissions and state/inbox convergence waits for the scenario.

## Code Commentary

### Logic

`submit_control` waits for a real running endpoint and live idle bridge, reads its submission
authority, then submits a request with the exact bridge epoch. Typed wait helpers poll catalog and
inbox projections until one precise state exists or raise an actionable timeout with the last
observation.

### Conventions

The live control socket, not the catalog's launch-time cached state, owns readiness. All waits share
one generic bounded polling primitive.

### Invariants And Boundaries

- Control prompts require current epoch authority and explicit accepted/queued receipts.
- A missing seat or dispatch-brief row fails rather than becoming an empty success.
- Polling catches only expected transient observation errors; other defects cross immediately.
- Timeout is bounded and includes the last observed value.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| Public control admission is guarded by current live endpoint authority. | `submit_control` | scripts/e2e_harness/scenario_control.py:25-59 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog, brief, and inbox waits name their exact convergence target. | `wait_for_seat` | scripts/e2e_harness/scenario_control.py:62-156 |
| Generic polling is bounded and exposes the last observation on failure. | `wait_until` | scripts/e2e_harness/scenario_control.py:159-175 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Control stimulus uses only repository-owned public serving APIs. | `submit_control` | scripts/e2e_harness/scenario_control.py:25-50 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for bounded public control and convergence helpers. Verification metadata remains closeout-owned.
