# mcp/src/agents_remember/serving/conversation/router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Owns the single stable FastAPI composition seam for active-conversation, native-library, and
structured-control child routers.

## Code Commentary

### Logic

Imports the three child routers in a fixed tuple, includes each on one package root `APIRouter`,
and exposes `register_conversation_routes(app)` to mount that root once.

### Conventions

Later leaves add endpoints only to their owned child `api.py`; global application registration
does not change again for each child.

### Invariants And Boundaries

- Preserve the active, library, control composition order and one root mount.
- Do not add route behavior here.
- Do not create a second registration call in `app.py` or another serving module.

### Todos

None; child endpoint implementations are independently owned.

## Docs References

No Domain Documentation source is configured for this internal FastAPI composition seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The three child routers reserve disjoint route prefixes and are behavior-empty at this gate. | L31-L47 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| Harness-control route registration mounts this root exactly once. | L19-L19; L125-L140 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |

## Cross-Repo References

No cross-repository boundary participates in local route composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the root composition sidecar.
  Verification is blank until closeout commits and stamps the new source.
