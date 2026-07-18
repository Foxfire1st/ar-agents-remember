# mcp/src/agents_remember/serving/conversation/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the package's deliberately small public facade: consumers mount structured-conversation
routes through `register_conversation_routes` without depending on child-router layout.

## Code Commentary

### Logic

Imports the root registration function from `router.py` and exposes only that symbol through
`__all__`.

### Conventions

The package facade is composition-only. Stable wire types are imported from `models.py` explicitly
by consumers rather than re-exported wholesale.

### Invariants And Boundaries

- Keep one public route-registration seam.
- Do not add projector, library, control, or store behavior here.
- Do not re-export child routers and thereby create alternate mounting paths.

### Todos

None; later behavior belongs to the owned child modules and focused services.

## Docs References

No Domain Documentation source is configured for this internal package facade.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The root function mounts the composed router once. | L7-L24 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The foundation test requires one stable inclusion seam. | L50-L60 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this repository-local facade.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the facade sidecar. Verification is
  blank until closeout commits and stamps the new source.
