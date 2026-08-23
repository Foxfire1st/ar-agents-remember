# mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Declares the integration subpackage that owns direct-landing execution and recovery.

## Code Commentary

### Logic

The marker groups direct-landing errors, accepted operation state, execution, and recovery without creating another landing entrypoint.

### Conventions

Public application routing stays above this package; durable evidence and Git reconciliation stay here.

### Invariants And Boundaries

- Direct landing remains journaled and recoverable; no unjournaled compatibility path belongs in this marker.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this package marker.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The package docstring assigns direct-landing execution and recovery ownership. | L1 | `mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py` |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
