# mcp/src/agents_remember/observer/projection_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/observer/projection_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Define observer nodes for closeout-projection problems and discarded-task history.

## Code Commentary

### Logic

The models project bounded non-admitting queue repair evidence and the durable proof/audit fields retained after an unstarted subtask is discarded.

### Invariants And Boundaries

- Observer nodes are read-only projections.
- Discarded task history remains visible after the live child sources are removed.
- Projected queue problems do not become lifecycle authority.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection problem nodes expose bounded repair evidence. | `CloseoutProjectionProblemNode` | mcp/src/agents_remember/observer/projection_closeout.py:10-19 |
| Discard proof and audit nodes retain the historical task truth. | `DiscardUnstartedProofNode`; `DiscardedSubTaskNode` | mcp/src/agents_remember/observer/projection_closeout.py:22-39; mcp/src/agents_remember/observer/projection_closeout.py:42-54 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.