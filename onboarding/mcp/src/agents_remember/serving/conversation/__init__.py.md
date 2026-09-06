# mcp/src/agents_remember/serving/conversation/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the package's deliberately small public facade: consumers mount structured-conversation
routes through `register_conversation_routes` without depending on child-router layout, and — since
260718-CHATS-L0 — child leaves consume the composition through the re-exported `ConversationRuntime`
type and the two request dependencies `get_conversation_runtime` /
`resolve_conversation_authorization`.

## Code Commentary

### Logic

Imports the root registration function from `router.py`, the runtime authority type from
`runtime.py`, and the two request-level dependencies from `dependencies.py`, exposing exactly those
four symbols through `__all__`.

### Conventions

The package facade is composition-only. Stable wire types are imported from `models.py` explicitly
by consumers rather than re-exported wholesale; the authorization resolver and scope types are
likewise imported from their owning modules, not through this facade.

### Invariants And Boundaries

- Keep one public route-registration seam.
- The re-exported dependencies are the only supported way for child modules to reach the installed
  runtime; do not re-export the `app.state` key or install/retrieval functions.
- Do not add projector, library, control, or store behavior here.
- Do not re-export child routers and thereby create alternate mounting paths.

### Todos

None; later behavior belongs to the owned child modules and focused services.

## Docs References

No Domain Documentation source is configured for this internal package facade.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The root function installs the one runtime and mounts the composed router once. | `register_conversation_routes` | mcp/src/agents_remember/serving/conversation/router.py:22-32 |
| The two re-exported request dependencies are the child-facing consumption seam. | `get_conversation_runtime`; `resolve_conversation_authorization` | mcp/src/agents_remember/serving/conversation/dependencies.py:21-23; mcp/src/agents_remember/serving/conversation/dependencies.py:26-36 |


## Cross-Repo References

No meaningful cross-repo boundary exists for this repository-local facade.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T02:51:52+02:00 — W3-B01 curator: curated 3 Repo-Internal table citations with exact router, dependency, and foundation-test anchors. Verification metadata remains unchanged for closeout.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the facade's new re-exports —
  `ConversationRuntime`, `get_conversation_runtime`, and `resolve_conversation_authorization` —
  beside the unchanged registration seam. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the facade sidecar. Verification is
  blank until closeout commits and stamps the new source.
