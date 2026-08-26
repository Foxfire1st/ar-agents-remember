# mcp/src/agents_remember/worktrees/modules/startup/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree modules overview](../overview.md)

## Purpose

Declares the worktree-start package for contract, provider, leaf-reference, and result collaborators.

## Code Commentary

### Logic

The marker groups the start collaborators below the `start.py` coordinator without adding another start entrypoint.

### Conventions

Contract derivation and start result shaping stay separate from the coordinating mutation flow.

### Invariants And Boundaries

- Do not restore the removed flattened module paths through compatibility exports.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this package marker.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring names start contract, provider, leaf-ref, and result collaborators. | "Worktree-start contract, provider, leaf-ref, and result collaborators." | mcp/src/agents_remember/worktrees/modules/startup/__init__.py:1-1 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.