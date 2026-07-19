# mcp/src/agents_remember/serving/conversation/library/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The one orchestration boundary where every library list/read re-authorizes: caller binding
against token-bound scope, narrow-only canonical project scope, recomputed native identity
digest, and the harness's live capability gate — before any native store is touched.

## Code Commentary

### Logic

`ConversationLibraryService` is constructed per request with the L0 runtime, the per-app
`LibraryShared` bundle, the caller's server-resolved authorization binding, and a port builder
injected by the dormant resolver factory (no import cycle). `list` re-derives the canonical
scope, requires the live gate's `list` feature `supported` (else `LibraryCapabilityError` with
the exact reason/state), guards against a wrong-harness port, and delegates. `resolve_key`
re-authorizes one opaque conversation key: malformed keys, cross-principal bindings
(`AuthorityError`), wrong harness, and a recomputed identity digest that no longer matches all
fail closed. `read` resolves the key, gates `read`, and delegates to the port.

### Conventions

The `LibraryPort` protocol mirrors the dormant resolver shape (list/read/resolve_resume_target)
without importing the factory. Cursors and keys are never authorization by themselves; the
service is the re-authorization point on every call.

### Invariants And Boundaries

- The live gate must report the feature `supported` before any native store is touched;
  unavailable/unverified demotes with the exact reason.
- A resolver factory returning a wrong-harness port is a typed failure, never a silent swap.
- The recomputed identity digest is the stale-row authority: a changed native identity fails as
  `StaleNativeIdentityError` and the caller refreshes the library row.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal orchestration service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The dormant port protocol this service orchestrates is fixed by the parent contract; the ASGI
suite drives the service through the real FastAPI composition with doubled native boundaries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dormant library port defines scoped list, historical read, and server-private resume-target resolution. | L59-L84 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| List/read routes return wire pages, narrow scope, and map capability/cursor/store refusals to exact statuses. | L323-L432 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |
| The per-app `LibraryShared` bundle and caller-bound builders construct this service. | L127-L159 | [factories.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/factories.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local orchestration service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the list/read re-authorization
  service sidecar. Verification is blank until closeout commits and stamps the new source.
