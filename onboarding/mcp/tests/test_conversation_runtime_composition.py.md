# mcp/tests/test_conversation_runtime_composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_runtime_composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `d7d85ca8e1abc0a09f8d71e03b555a81ad4734f1`|
| lastVerifiedCommitDate |  2026-07-19T00:41:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Composition contract suite for the app-scoped `ConversationRuntime` authority (260718-CHATS-L0,
leaf R1/R2/R3 and the R5 test mandate). It proves the one immutable runtime is installed exactly
once from the real production composition, that missing, duplicate, foreign, and missing-member
bindings fail closed, that child composition stays isolated per app, and that no import-time
mutable singleton or production identity-injection seam exists.

## Code Commentary

### Logic

The suite builds real `ConversationRuntime` bundles over `tmp_path` scopes with a minimal
`_NoSessionHost` host double and an empty harness registry, then drives both composition seams:
`register_harness_control_routes` (the production path, also via a live `create_app` build) and
`register_conversation_routes`. Field-identity assertions prove the runtime binds the exact
catalog/registry/clock/config objects the composition already holds. Failure-shape cases cover
retrieval before install (app-level and through the request dependency), duplicate installation at
both seams, a foreign object on the reserved `app.state` key, construction with a missing
authority, and frozen-instance mutation attempts on both the runtime and its scope.
`test_child_composition_is_isolated_per_app` mounts the shared module-level child routers on two
apps and proves over real HTTP (through `TestClient` probe routes owned by the test, never by the
shared child routers) that each app resolves its own runtime. Two source-scan cases close the
contract: `register_harness_control_routes` must accept no identity/resolver parameter, and the
four production conversation modules must contain no fixture, PTY, tmux, header-access, or
browser-identity tokens.

### Conventions

The suite uses plain `pytest` functions over `tmp_path`, hand-built ASGI `Request` scopes for the
request-dependency cases, and `TestClient` for the per-app isolation proof. Probe routes are added
only to test-owned apps so the shared child routers stay byte-clean.

### Invariants And Boundaries

- One typed runtime per app, installed once; retrieval returns the identical object.
- Missing, duplicate, foreign, and missing-member compositions fail with
  `ConversationCompositionError`, never silently.
- No module-level `ConversationRuntime`/resolver instance may exist in any conversation module.
- The production registration accepts no injected principal, tenant, resolver, or identity
  parameter.
- Production modules never rely on fixtures, PTY/tmux parsing, or raw browser identity claims.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation source is configured. The repository composition sources are direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The immutable runtime/scope types, install-once, and fail-closed retrieval under test. | L47-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The production seam constructs and installs the one runtime. | L144-L162 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| The root registration installs the runtime then mounts the unchanged root router. | L22-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The typed composition error asserted by every failure-shape case. | L30-L38 | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |

## Cross-Repo References

No neighboring repository participates in this composition suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the composition contract suite
  sidecar. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
