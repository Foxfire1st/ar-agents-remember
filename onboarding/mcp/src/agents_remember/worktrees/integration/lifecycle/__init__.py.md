# mcp/src/agents_remember/worktrees/integration/lifecycle/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Declares the durable lifecycle journal, control, worker, and location ownership package.

## Code Commentary

### Logic

The marker makes the root-journal authority route explicit without re-exporting the former flattened modules.

### Conventions

Locator-to-manifest-to-journal resolution, generation controls, worker proof, and public evidence belong together below the application layer.

### Invariants And Boundaries

- Queue projection is not lifecycle evidence authority.
- Do not add flat-path compatibility readers or duplicate journal owners.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this internal authority package.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring assigns durable lifecycle journal, control, worker, and location ownership. | "Durable lifecycle journal, control, worker, and location ownership." | mcp/src/agents_remember/worktrees/integration/lifecycle/__init__.py:1-1 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.