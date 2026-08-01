# mcp/src/agents_remember/serving/conversation/library/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:18+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Owns the five implemented native conversation library routes — list, read, open, open-status,
and open-reconcile — on the L9 harness-scoped prefix, plus the reviewer-O4 mapping authority
that renders every typed refusal as one precise HTTP status instead of a raw 500.

## Code Commentary

### 260731-EFA-L4 Current Delta — Declared Responses, And A Removed 500 Fallback

**All five routes now declare a `response_model`:** `ConversationLibraryPage` on `GET ""`
(L109), `HistoricalConversationPage` on `GET /{conversation_key}` (L133-L137), and
`OpenConversationOperation` with `status_code=201` on each of the open trio (L169-L174,
L202-L207, L224-L229). `LIBRARY_RESPONSES` is `_ERROR_STATUS_TABLE` plus `_error_response`'s
`LibraryCapabilityError` branch transcribed: every entry in that table lands on one of six
statuses (400 / 403 / 404 / 409 / 422 / 503).

**The open trio answer with TWO families on the same statuses**, which is why they spread
`{**LIBRARY_RESPONSES, **OPEN_OUTCOME_RESPONSES}`. `_OPEN_STATUS_BY_OUTCOME` reads the
operation's own `outcome` to pick 201/202/409/422/503, and each of those carries an
`OpenConversationOperation` — the outcome IS the body, not an error. But `_error_response` still
maps typed library errors onto 400/403/404/409/422/503 with refusal bodies, so 409/422/503 carry
*either*.

**`{**a, **b}` is a dict merge, not a union** — a bare `{409: OpenConversationOperation}` entry
would have *deleted* `LIBRARY_RESPONSES[409]` rather than joining it, declaring on nine (route,
status) pairs a model the route cannot produce. `OPEN_OUTCOME_RESPONSES` therefore unions the
shared table's refusal member into each overlapping status itself.

**The `.get(..., 500)` fallback in `_open_call` was REMOVED rather than declared.**
`_OPEN_STATUS_BY_OUTCOME` (L75-L84) is now typed `dict[str, int]` and indexed directly, and it
is **TOTAL** over `OpenConversationOperation.outcome`'s eight-member `Literal`
(`conversation/models.py` L856-L865): `opened`, `pending`, `timeout-unknown`, `unsupported`,
`stale-identity`, `request-conflict`, `launch-failed`, `identity-mismatch`. A ninth outcome added
without a status here is a loud `KeyError` at the one place that can fix it — the same posture as
`_error_response`, which re-raises rather than inventing a status. The old default answered an
unmapped outcome with a 500 carrying a full operation body: a shape no `responses` table
declares, on a status no test could ever drive, silently.
`test_serving_response_conformance` asserts that set equality against the `Literal`.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

Each handler resolves the L0 runtime and authorization inside the handler (the exact same calls
the two request dependencies make), narrows the raw path segment through
`require_normalized_harness`, and builds caller-bound services from the factories. GET `""`
lists the native catalog with optional cwd/cursor/limit; GET `/{conversation_key}` reads one
historical page; POST `/open` requires `expectedIdentityDigest` and drives the idempotent open;
POST `/open-status` and `/open-reconcile` re-observe one retained operation by requestId. The
outcome→status table maps open outcomes to 201/202/422/409/503 exactly — and since
**260731-EFA-L4** it is total over the outcome `Literal` and indexed directly, with no 500
default; `_error_response`
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
- **`_OPEN_STATUS_BY_OUTCOME` must stay total** over `OpenConversationOperation.outcome`. Adding
  an outcome without a status here is a `KeyError` by design; restoring a `.get(..., 500)`
  default would re-introduce an undeclared, undrivable status carrying a full operation body.
- **Outcome tables union, never overwrite.** The open trio spread
  `{**LIBRARY_RESPONSES, **OPEN_OUTCOME_RESPONSES}`, and a dict merge replaces the shared entry —
  so every overlapping status in `OPEN_OUTCOME_RESPONSES` has to carry the refusal model as well
  as the operation.
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
| The eight-member `outcome` `Literal` that `_OPEN_STATUS_BY_OUTCOME` must stay total over. | L856-L865 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The `LIBRARY_RESPONSES` and `OPEN_OUTCOME_RESPONSES` tables these routes declare, and the dict-merge rule that makes the outcome table union in each refusal model. | `LIBRARY_RESPONSES`; `OPEN_OUTCOME_RESPONSES` | [../response_contract.py](../response_contract.py.md) |
| The suite that drives all five routes, validates the real bodies, and asserts the status-map/`Literal` set equality. | `test_serving_response_conformance` | [test_serving_response_conformance.py](agents-remember/mcp/tests/test_serving_response_conformance.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

The open route now builds one `OpenRequest(request_id=…, expected_identity_digest=…, cwd=…,
launch_context=…)` and passes it to the open service instead of four parallel keywords. The wire
body is unchanged; `_launch_context(body)` still assembles the launch context. See
[open_service.py](open_service.py.md) for why the four form one fingerprinted value.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-01T09:18+02:00 — 260731-EFA-L4 curator: recorded the five `response_model`
  declarations with their lines, the `LIBRARY_RESPONSES` table (a transcription of
  `_ERROR_STATUS_TABLE` plus the `LibraryCapabilityError` 422 branch), and the two-family answer
  on the open trio — `_OPEN_STATUS_BY_OUTCOME` picks the status off the operation's own outcome
  and the body IS that operation, while `_error_response` still answers the same statuses with
  refusals, so `OPEN_OUTCOME_RESPONSES` must UNION the refusal member into each overlapping
  status because `{**a, **b}` is a dict merge. Recorded the removal of `_open_call`'s
  `.get(..., 500)` fallback: `_OPEN_STATUS_BY_OUTCOME` (L75-L84) is now indexed directly and is
  total over the eight-member `outcome` `Literal` (`models.py` L856-L865), so a ninth outcome is
  a loud `KeyError` instead of a silent, undeclared, undrivable 500 carrying a full operation
  body. Corrected the Logic sentence about the outcome table and added both as invariants.
  Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `OpenRequest` call shape (wire body unchanged).
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: rewrote the route-shell sidecar for the
  implemented leaf — five routes, strict request models, the outcome→status table, and the
  subclass-before-base O4 error ladder — and re-pointed the governing overview to the new
  library route overview. Verification stays pinned at the L9 shell commit until closeout
  stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the native-library route-shell
  sidecar. Verification is blank until closeout commits and stamps the new source.
