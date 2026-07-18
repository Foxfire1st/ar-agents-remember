# mcp/src/agents_remember/serving/conversation/runtime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/runtime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `d7d85ca8e1abc0a09f8d71e03b555a81ad4734f1`|
| lastVerifiedCommitDate |  2026-07-19T00:41:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the one immutable app-scoped conversation runtime authority (260718-CHATS-L0). Before L0,
`create_app` / `register_harness_control_routes` constructed every server authority the structured
conversation services need — workspace/coordination scope, terminal catalog and liveness host,
effective harness registry, liveness clock/config, capability evidence — but those authorities died
inside the harness-control closure, so the mounted child routers had no production path to any of
them. `ConversationRuntime` binds exactly those existing authorities into one frozen typed value,
installed on the FastAPI app exactly once through the stable root composition. It deliberately adds
no behavior of its own: no conversation store or index, no lifecycle authority, no second terminal
opener, and no active/library/control service.

## Code Commentary

### Logic

`ConversationScope` is a frozen dataclass pairing the canonical `workspace_root` and
`coordination_root`. `ConversationRuntime` is a frozen dataclass bundling that scope with the
`TerminalCatalog`, `TerminalLivenessHost`, the effective `HarnessRegistry` callable, the liveness
`Clock` and `TerminalCatalogLivenessConfig`, the shared `HarnessCapabilityCatalog`, and the
`ConversationAuthorizationResolver`. Its `__post_init__` refuses construction when any authority is
missing, so a broken composition fails at startup rather than at first request.
`install_conversation_runtime` writes the bundle to `app.state` under
`CONVERSATION_RUNTIME_STATE_KEY` (`"conversation_runtime"`) and refuses a second install;
`conversation_runtime_from_app` retrieves it and fails closed when the key is absent or holds a
foreign object. All composition failures raise the typed `ConversationCompositionError`.
`HarnessRegistry` is a callable alias kept import-light through `TYPE_CHECKING`.

### Conventions

The module holds only composition types and two fail-closed functions; there is no module-level
runtime instance and no import-time mutable singleton. Child leaves never import this module's
state key to re-bind anything — they consume the installed runtime through the request dependencies
in `dependencies.py`.

### Invariants And Boundaries

- Exactly one runtime may be installed per app; a second install or a re-registration fails closed.
- The reserved `app.state.conversation_runtime` key may hold only a `ConversationRuntime`.
- The frozen bundle cannot drift after composition; every child sees one identical authority set.
- Construction binds only existing server authorities — nothing invented (no store, index,
  lifecycle authority, opener, projector, or child service).
- Do not add behavior methods here; behavior belongs to the child leaves that derive their own
  ports from this runtime.

### Todos

None; child endpoint implementations are independently owned by the L1/L2/L3 leaves.

## Docs References

No Domain Documentation source is configured for this internal composition authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The runtime is constructed once inside `register_harness_control_routes`, the only place where all
bound authorities are already in hand, and installed once by the root conversation composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The production composition constructs the one runtime from authorities already in hand and passes it to the root registration. | L144-L162 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| The root registration installs the runtime on `app.state` before mounting the unchanged root router. | L22-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The typed composition error covers missing, duplicate, foreign, and missing-member failures. | L30-L38 | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| Contract tests prove single installation at both seams, duplicate/missing/foreign failure, missing-authority construction failure, immutability, per-app isolation, and no import-time singleton. | L106-L215 | [test_conversation_runtime_composition.py](agents-remember/mcp/tests/test_conversation_runtime_composition.py) |

## Cross-Repo References

No cross-repository boundary participates in this app-local composition value.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the runtime authority sidecar for the
  immutable app-scoped composition repair. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
