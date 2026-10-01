# mcp/src/agents_remember/serving/conversation/__init__.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal package facade.

No configured domain documentation was available.

### Repo-Internal References

- The root function installs the one runtime and mounts the composed router once. [1]
- The two re-exported request dependencies are the child-facing consumption seam. [2]


### Cross-Repo References

No meaningful cross-repo boundary exists for this repository-local facade.

No meaningful cross-repo references found.
