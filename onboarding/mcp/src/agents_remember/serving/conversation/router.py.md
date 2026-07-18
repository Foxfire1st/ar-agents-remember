# mcp/src/agents_remember/serving/conversation/router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `d7d85ca8e1abc0a09f8d71e03b555a81ad4734f1`|
| lastVerifiedCommitDate |  2026-07-19T00:41:29+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal FastAPI composition seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The three child routers reserve disjoint route prefixes and are behavior-empty at this gate. | L31-L46 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The foundation topology pins the exact one-call registration carrying the runtime. | L50-L62 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| Harness-control route registration constructs the runtime and mounts this root exactly once. | L144-L162 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| The install-once and fail-closed retrieval semantics the seam delegates to. | L81-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |

## Cross-Repo References

No cross-repository boundary participates in local route composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-time composition binding —
  `register_conversation_routes(app, runtime)` now installs the immutable `ConversationRuntime`
  through `install_conversation_runtime` before mounting the unchanged root; the child tuple and
  public prefixes are byte-unchanged. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the root composition sidecar.
  Verification is blank until closeout commits and stamps the new source.
