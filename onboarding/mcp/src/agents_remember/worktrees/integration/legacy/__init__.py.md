# mcp/src/agents_remember/worktrees/integration/legacy/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/legacy/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Declares the isolated package for the explicit bounded legacy lifecycle bridge.

## Code Commentary

### Logic

The marker makes the removable compatibility boundary visible; it does not widen legacy schema admission.

### Conventions

Legacy schema parsing, authority, failures, bridge logic, and public translation stay isolated under this route.

### Invariants And Boundaries

- Normal lifecycle readers must not import this package as a fallback.
- The bridge remains bounded and removable.

### Todos

Remove with the legacy bridge when its bounded migration window closes.

## Docs References

No configured Domain Documentation source applies to this internal migration boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring declares explicit bounded legacy lifecycle bridge ownership. | "Explicit bounded legacy lifecycle bridge ownership." | mcp/src/agents_remember/worktrees/integration/legacy/__init__.py:1-1 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.