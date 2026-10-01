# scenario_control.py

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

## Evidence

### Docs References

No Domain Documentation source is configured.

- Public control admission is guarded by current live endpoint authority. [1]

### Repo-Internal References

- Catalog, brief, and inbox waits name their exact convergence target. [2]
- Generic polling is bounded and exposes the last observation on failure. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- Control stimulus uses only repository-owned public serving APIs. [4]
