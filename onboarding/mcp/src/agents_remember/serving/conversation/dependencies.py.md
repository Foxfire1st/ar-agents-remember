# mcp/src/agents_remember/serving/conversation/dependencies.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/dependencies.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `d7d85ca8e1abc0a09f8d71e03b555a81ad4734f1`|
| lastVerifiedCommitDate |  2026-07-19T00:41:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the two narrow request-level FastAPI dependencies through which conversation child routers
consume the installed `ConversationRuntime` (260718-CHATS-L0). Child leaves `Depends(...)` on these
functions — or derive their child-owned ports from the runtime they return — and never reach into
`app.state` themselves or re-bind the composition.

## Code Commentary

### Logic

`get_conversation_runtime(request)` returns the one app-scoped runtime installed by the root
composition, delegating to `conversation_runtime_from_app(request.app)`; a missing or foreign
binding fails closed with the typed `ConversationCompositionError`.
`resolve_conversation_authorization(request)` retrieves the same runtime and calls its bound
authorization resolver with the real ASGI TCP peer address (`request.client.host`, or `None` when
the peer is absent). No other request fact is consulted: headers and any browser-supplied
principal/tenant claim are never read, so identity cannot be forged from the wire; non-loopback
peers fail closed inside the resolver.

### Conventions

Both functions are plain request-scoped callables shaped for `fastapi.Depends`; they hold no state
and add no caching. The package facade re-exports them so child modules import the seam from
`agents_remember.serving.conversation` directly.

### Invariants And Boundaries

- Child leaves consume the runtime only through these dependencies; they never touch `app.state`
  or the composition.
- The only request fact used for authorization is the TCP peer; request metadata is never an
  identity input.
- Do not add principal, tenant, header, or cookie parameters here — the authorization ruling keeps
  resolution free of browser-supplied identity channels.
- Do not add behavior routes, stores, or opener logic to this seam module.

### Todos

None; child endpoint implementations are independently owned by the L1/L2/L3 leaves.

## Docs References

No Domain Documentation source is configured for this internal request-dependency seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The dependencies are thin fail-closed adapters over the runtime authority and its bound resolver;
contract tests drive both through real requests and prove per-app isolation over HTTP.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Fail-closed runtime retrieval and the reserved `app.state` key live in the runtime module. | L90-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The bound resolver's loopback-only ruling is what the authorization dependency delegates to. | L90-L97 | [authorization.py](agents-remember/mcp/src/agents_remember/serving/conversation/authorization.py) |
| The package facade re-exports both dependencies beside `ConversationRuntime` and `register_conversation_routes`. | L3-L15 | [__init__.py](agents-remember/mcp/src/agents_remember/serving/conversation/__init__.py) |
| Composition tests drive `get_conversation_runtime` through per-app probe routes over `TestClient` and prove missing-install failure. | L96-L103; L164-L170; L218-L231 | [test_conversation_runtime_composition.py](agents-remember/mcp/tests/test_conversation_runtime_composition.py) |
| Authorization tests prove forged browser identity headers are never read and the dependency fails closed off loopback. | L160-L195 | [test_conversation_authorization.py](agents-remember/mcp/tests/test_conversation_authorization.py) |

## Cross-Repo References

No cross-repository boundary participates in this request-local dependency seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the request-dependency seam sidecar.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
