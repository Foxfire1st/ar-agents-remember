# mcp/src/agents_remember/serving/conversation/router.py

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Owns the single stable FastAPI composition seam for active-conversation, native-library, and
structured-control child routers, and — since 260718-CHATS-L0 — installs the one immutable
app-scoped `ConversationRuntime` authority on the app before mounting the root.

## Code Commentary

### Logic

Imports the three child routers in a fixed tuple, includes each on one package root `APIRouter`,
and exposes `register_conversation_routes(app, runtime)`. The function first installs the passed
runtime on `app.state` through `install_conversation_runtime` (fail-closed on a second install),
then mounts the unchanged root once. The runtime binding lives inside this same single seam, so
the L0 repair did not add a second registration path.

### Conventions

Later leaves add endpoints only to their owned child `api.py`; global application registration
does not change again for each child. Children consume the installed runtime through the request
dependencies in `dependencies.py`; they never edit this composition or re-bind the runtime.

### Invariants And Boundaries

- Preserve the active, library, control composition order and one root mount.
- The runtime is installed exactly once per app through this seam; a second registration fails
  closed with `ConversationCompositionError`.
- Do not add route behavior here.
- Do not create a second registration call in `app.py` or another serving module.

### Todos

None; child endpoint implementations are independently owned.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal FastAPI composition seam.

No configured domain documentation was available.

### Repo-Internal References

- The root installs one runtime before mounting the owned child routes; endpoint behavior belongs to child modules. [1]

| Harness-control route registration constructs the runtime and mounts this root exactly once. | `register_harness_control_routes` | mcp/src/agents_remember/serving/harness_control_api.py:182-217 |
| The install-once and fail-closed retrieval semantics the seam delegates to. | `install_conversation_runtime`, `conversation_runtime_from_app` | mcp/src/agents_remember/serving/conversation/runtime.py:81-87; mcp/src/agents_remember/serving/conversation/runtime.py:90-101 |

### Cross-Repo References

No cross-repository boundary participates in local route composition.

No meaningful cross-repo references found.
