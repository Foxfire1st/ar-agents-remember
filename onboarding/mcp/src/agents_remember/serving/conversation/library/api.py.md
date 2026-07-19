# mcp/src/agents_remember/serving/conversation/library/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Owns the five implemented native conversation library routes — list, read, open, open-status,
and open-reconcile — on the L9 harness-scoped prefix, plus the reviewer-O4 mapping authority
that renders every typed refusal as one precise HTTP status instead of a raw 500.

## Code Commentary

### Logic

Each handler resolves the L0 runtime and authorization inside the handler (the exact same calls
the two request dependencies make), narrows the raw path segment through
`require_normalized_harness`, and builds caller-bound services from the factories. GET `""`
lists the native catalog with optional cwd/cursor/limit; GET `/{conversation_key}` reads one
historical page; POST `/open` requires `expectedIdentityDigest` and drives the idempotent open;
POST `/open-status` and `/open-reconcile` re-observe one retained operation by requestId. The
outcome→status table maps open outcomes to 201/202/422/409/503 exactly; `_error_response`
walks the subclass-before-base typed error table, renders `LibraryCapabilityError` as 422 with
the exact capability state, and re-raises genuinely unexpected exceptions so they stay loud.

### Conventions

Request bodies are strict extra-forbid Pydantic models serialized once with camel-case aliases;
null is meaningful on this wire (cursor/identity absence is contract-significant). Page sizes
clamp through one bounded rule (default 50, max 100).

### Invariants And Boundaries

- Every typed refusal — loopback violation, composition failure, scope escape, cursor misuse,
  capability gate, conflict — maps to its precise status here; a raw 500 for a routine refusal
  violates the O4 contract.
- Open requires `expectedIdentityDigest`; the service, not the route, owns identity re-proof.
- Keep active exact-session events and control actions out of this module; the prefix stays
  harness-scoped and authorization-bound.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal route module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ASGI suite drives these routes through the real FastAPI composition with a loopback peer;
the foundation pin asserts exactly this five-route surface; the parent contract owns the wire
models these handlers serialize.

| Finding | Citations | Source Path |
| --- | --- | --- |
| List/read routes return wire pages, narrow scope, and map every refusal class to its exact status. | L323-L432 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |
| Open/status/reconcile routes map outcomes to 201/202/409/422/503 and fail closed off loopback. | L445-L703 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |
| The foundation suite pins exactly the five owned library routes inside the child router. | L32-L56 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The L0 request dependencies are the only consumption seam the handlers use. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: rewrote the route-shell sidecar for the
  implemented leaf — five routes, strict request models, the outcome→status table, and the
  subclass-before-base O4 error ladder — and re-pointed the governing overview to the new
  library route overview. Verification stays pinned at the L9 shell commit until closeout
  stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the native-library route-shell
  sidecar. Verification is blank until closeout commits and stamps the new source.
