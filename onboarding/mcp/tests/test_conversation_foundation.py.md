# mcp/tests/test_conversation_foundation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_foundation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins the cross-route foundation of structured Chats: exact two-port shape, three owned child
routers (the library child now carrying exactly its five L2 behavior routes while active and
control stay behavior-empty), one global registration seam, repository-owned helper dependency
resolution with the exact helper source set, and allow-listed installed-runtime fixtures that
cannot enable capabilities.

## Code Commentary

### Logic

The suite introspects exported port types and router objects, reads the global serving source to
prove one registration call — since 260718-CHATS-L0 pinning the exact
`register_conversation_routes(app, conversation_runtime)` call that carries the immutable runtime
through the same single seam — parses the helper manifest/lock to prove exact pins, scans production
helper TypeScript for forbidden ambient resolution, validates all three runtime fixtures through
the production Pydantic contract, and rejects raw secret/path/conversation material by pattern.
Since 260718-CHATS-L2 the child-router assertion pins the library child's exact five-route surface
(GET list, GET read, POST open/open-status/open-reconcile) by method+path while active and control
remain behavior-empty, and the helper-source listing expects exactly `claude.ts`, `pi.ts`,
`protocol.ts`, and `protocol.test.ts`.

### Conventions

Source-level topology checks are intentional because this leaf establishes ownership and absence of
behavior as part of the contract. Runtime fixtures are parsed data, not snapshots copied into test
expectations wholesale.

### Invariants And Boundaries

- Exactly two conversation read ports; no native control port.
- Child ownership stays disjoint at this gate: only the library child carries behavior routes
  (exactly its five), and all three mount through one root seam.
- Helper dependencies resolve only from this repository package/lock, and production helper source
  contains no incidental module resolution.
- All runtime fixtures are allow-listed, redacted, and explicitly non-enabling.
- Claude helper history remains `not-exercised` until a real installed 2.1.211 history passes the
  replay gate; observed codex/pi rows record evidence shape only.

### Todos

Later leaves should replace behavior-empty assertions for the active/control children only when
they own and test the corresponding production endpoints.

## Docs References

No Domain Documentation source is configured. The repository sources and installed-runtime fixture
contract are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Root conversation composition defines the exact child tuple and single registration function. | L7-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The library child owns exactly the five L2 routes this suite pins by method and path. | L93-L198 | [library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |
| The helper manifest owns the exact direct runtime dependencies checked against the lock. | L1-L22 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| Runtime fixture DTOs force allowlist-v1 and `enablesCapabilities=false`. | L1233-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

No neighboring repository participates in this topology suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the renamed
  `test_root_composes_three_owned_child_routers` pin — the library child now asserts exactly its
  five owned routes while active/control stay behavior-empty — and the helper-source listing
  extended by `claude.ts`/`pi.ts`; the two-port, registration-seam, dependency-lock, and fixture
  redaction invariants are unchanged. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the updated registration-seam
  assertion pinning the exact `register_conversation_routes(app, conversation_runtime)` call after
  the L0 one-time binding; both other invariants (no `register_conversation_routes`, no
  `include_router` in `app.py`) are unchanged. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the structured-conversation foundation
  test sidecar. Verification is blank until closeout commits and stamps the new source.
