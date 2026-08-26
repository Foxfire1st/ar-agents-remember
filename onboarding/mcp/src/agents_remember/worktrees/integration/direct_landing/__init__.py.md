# mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring assigns direct-landing execution and recovery ownership. | "Direct-landing execution and recovery ownership." | mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py:1-1 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.