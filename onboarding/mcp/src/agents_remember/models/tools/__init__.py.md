# mcp/src/agents_remember/models/tools/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

Declares the package that owns registered tool request and response models.

## Code Commentary

### Logic

This marker groups the tool registry and strict response-model vocabulary without re-exporting the former flat module paths.

### Conventions

Tool wire models remain separate from application response projection and MCP registration.

### Invariants And Boundaries

- Do not add compatibility imports for the removed `models.tool_registry` or `models.tool_response` paths.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this package marker.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring names registered tool request and response models as its scope. | "Registered tool request and response models." | mcp/src/agents_remember/models/tools/__init__.py:1-1 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the exact package-marker sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.