# mcp/src/agents_remember/serving/conversation/router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three child routers reserve disjoint route prefixes and are behavior-empty at this gate. | `test_exactly_two_conversation_ports_exist` | mcp/tests/test_conversation_foundation.py:22-29 |
| The foundation topology pins the exact one-call registration carrying the runtime. | `test_root_composes_three_owned_child_routers` | mcp/tests/test_conversation_foundation.py:32-107 |
| Harness-control route registration constructs the runtime and mounts this root exactly once. | `register_harness_control_routes` | mcp/src/agents_remember/serving/harness_control_api.py:182-217 |
| The install-once and fail-closed retrieval semantics the seam delegates to. | `install_conversation_runtime`, `conversation_runtime_from_app` | mcp/src/agents_remember/serving/conversation/runtime.py:81-87; mcp/src/agents_remember/serving/conversation/runtime.py:90-101 |

## Cross-Repo References

No cross-repository boundary participates in local route composition.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 8 initial citation findings (4 anchor, 0 prose, 4 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-time composition binding —
  `register_conversation_routes(app, runtime)` now installs the immutable `ConversationRuntime`
  through `install_conversation_runtime` before mounting the unchanged root; the child tuple and
  public prefixes are byte-unchanged. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the root composition sidecar.
  Verification is blank until closeout commits and stamps the new source.
