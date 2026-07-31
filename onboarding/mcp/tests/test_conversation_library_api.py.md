# mcp/tests/test_conversation_library_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Registered-route tests for the 260718-CHATS-L2 native conversation library: drives the actual
FastAPI composition (root router + L0 runtime) through its ASGI interface with a loopback peer
so routing, validation, camel-case wire shape, and the precise O4 error-status ladder are all
covered on the production path.

## Code Commentary

### Logic

Thirteen async tests build the real app composition with doubled native boundaries (ports,
opener, proof, retire — the installed-runtime suite covers those live). List/read cases prove
wire pages, scope narrowing, limit clamping, the null-byte cwd typed refusal (review F2), scope
escapes, unknown harness, malformed cursors, capability gates, per-harness store-error 503
mapping, and foreign-principal key rejection. Open cases prove 201 creation with idempotent
replay, focus-only-on-proven-identity, stale digest, unknown request, timeout-unknown, launch
failure, and identity-mismatch statuses. A non-loopback peer fails closed on every route.

### Conventions

ASGI-level requests against the real routers keep the test honest about registration,
serialization (null-meaningful camel-case bodies), and status mapping; no TestClient shortcut
bypasses the peer classification. Every call goes through `asgi_request`, which takes a frozen
`AsgiClient` binding the app to the peer address the connection will report — loopback
`127.0.0.1:5000` by default, so the fail-closed case changes only the peer by passing
`AsgiClient(self.app, peer=("10.0.0.5", 9000))` while the requests stay identical. The doubled
open service is built from a `LibraryBinding(runtime=..., shared=..., authorization=...)`
parameter object beside its `library`, `port_builder`, `opener`, and `proof_wait_seconds` seams.

### Invariants And Boundaries

- Every typed refusal lands on its exact documented status; no case may pass with a raw 500.
- Open responses publish session identity only beside an exact proven identity.
- Doubled boundaries stay doubles: this suite never spawns a real harness or helper.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources and installed-runtime
fixture contract are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The route module and its outcome/error mapping authority under test. | L93-L259 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |
| The foundation pin asserting exactly the five owned routes this suite exercises. | L32-L56 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The installed-runtime suite covering the same routes' live native boundaries. | L1-L9 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository participates in this route suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: named the new request seam the card's peer
  claims now depend on. `asgi_request` no longer takes the app and a `client=(host, port)` keyword
  separately; it takes one frozen `AsgiClient` dataclass that binds the app to the peer address the
  connection reports, with loopback as the default, and the non-loopback fail-closed case supplies
  `AsgiClient(self.app, peer=("10.0.0.5", 9000))`. The doubled `ConversationOpenService` is now
  constructed from a `LibraryBinding` parameter object. Rewrote the Conventions paragraph to say
  both; the thirteen async cases and the whole status ladder are unchanged. Verification metadata
  stays pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the library ASGI route suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
