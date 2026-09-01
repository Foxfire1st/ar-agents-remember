# mcp/tests/test_conversation_runtime_composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_runtime_composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T04:55+02:00 |
| lastVerifiedCommitHash |  `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate |  2026-09-01T12:17:08+02:00|
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
`_NoSessionHost` host double and an empty harness registry through one local `_runtime()` factory
(which takes optional `catalog`/`liveness_config` overrides so a test can hold the identical
objects it later asserts on), then drives both composition seams:
`register_harness_control_routes(app, runtime)` — the production path, which now RECEIVES the
already-constructed runtime as its single authority argument instead of seven loose ones, also
exercised via a live `create_app(config, cadence=ProjectionCadence(interval=100))` build — and
`register_conversation_routes`. Field-identity assertions prove the runtime binds the exact
catalog/registry/clock/config objects the composition already holds. Failure-shape cases cover
retrieval before install (app-level and through the request dependency), duplicate installation at
both seams, a foreign object on the reserved `app.state` key, construction with a missing
authority, and frozen-instance mutation attempts on both the runtime and its scope.
`test_child_composition_is_isolated_per_app` mounts the shared module-level child routers on two
apps and proves over real HTTP (through `TestClient` probe routes owned by the test, never by the
shared child routers) that each app resolves its own runtime. Two source-scan cases close the
contract: `register_harness_control_routes` must accept no identity/resolver parameter — and,
since the runtime moved out of that function, the paired scan now reads
`inspect.getsource(create_app)` for `LocalOperatorAuthorizationResolver`, because `create_app` is
where the production composition mints its own resolver — and the
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable runtime/scope types, install-once, and fail-closed retrieval under test. | `ConversationRuntime` | mcp/src/agents_remember/serving/conversation/runtime.py:55-78 |
| The production seam accepts the already-built runtime and installs it once. | `register_harness_control_routes` | mcp/src/agents_remember/serving/harness_control_api.py:182-217 |
| The live composition that constructs the runtime and mints the resolver the identity scan looks for. | `create_app` | mcp/src/agents_remember/serving/app.py:226-285 |
| The root registration installs the runtime then mounts the unchanged root router. | `register_conversation_routes` | mcp/src/agents_remember/serving/conversation/router.py:22-32 |
| The typed composition error asserted by every failure-shape case. | `ConversationCompositionError` | mcp/src/agents_remember/errors.py:246-253 |

## Cross-Repo References

No neighboring repository participates in this composition suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-29T04:55+02:00 — MCAR-L02 citation maintenance: shifted the central
  `ConversationCompositionError` range after a preceding typed error was added; suite behavior is
  unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:05:21+02:00 — W3-B05 curator: resolved 5 Tier-2 table findings with exact anchors and source paths; fixer generated all final ranges.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the production seam changed shape, so the
  Logic and reference rows were rewritten rather than attested.
  `register_harness_control_routes` now takes `(app, runtime)`; the seven-keyword form the card
  implied (`workspace_root`, `coordination_root`, `harness_registry`, `catalog`, `host`,
  `liveness_clock`, `liveness_config`) is gone, the runtime is built by `create_app`, and both
  the production-composition and duplicate-registration cases pass a `_runtime(...)` bundle (the
  local factory gained `catalog`/`liveness_config` overrides).
  `test_production_composition_accepts_no_injected_identity` still proves no identity parameter,
  but its paired source scan moved from `inspect.getsource(register_harness_control_routes)` to
  `inspect.getsource(create_app)`, and the live build now passes
  `cadence=ProjectionCadence(interval=100)`. The `harness_control_api.py` row was corrected to
  say the seam installs rather than constructs the runtime (L144-L162 to L166-L179) and an
  `app.py` row was added for the composition that does construct it. Every fail-closed invariant
  still holds.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the composition contract suite
  sidecar. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
