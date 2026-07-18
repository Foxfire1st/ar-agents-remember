# mcp/src/agents_remember/serving/conversation/active/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Structured conversation contract overview](../overview.md)

## Purpose

Marks the package that owns active exact-session structured-conversation serving.

## Code Commentary

### Logic

Contains only a package docstring; route ownership is implemented by sibling `api.py`.

### Conventions

Keep the marker behavior-free and use `api.py` as the route entrypoint.

### Invariants And Boundaries

- Active conversation work is distinct from dormant native library and control routes.
- This marker must not become an import-time registration path.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sibling router reserves the current exact-session conversation prefix. | L1-L8 | [active/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the package-marker sidecar.
  Verification is blank until closeout commits and stamps the new source.
