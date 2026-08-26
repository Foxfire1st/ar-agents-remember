# mcp/src/agents_remember/models/declared_caller.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/declared_caller.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

The single shared model for ambient caller identity supplied as request data. A caller without a
plane-injected hosted seat (an external or ambient agent) declares its structural identity — role +
canonical task document — as request data; every consuming tool validates that declaration against
its own policy before any mutation. This is the L16 (260815-DAG-L16) reversal of the earlier
"identity is never request data" invariant: the declaration grants no authority the same
role/document pair would not have from a seat.

## Code Commentary

### Logic

`DeclaredCaller` is a strict frozen pydantic model (`extra="forbid"`, `frozen=True`) carrying
`role` (≤ `MAX_DECLARED_ROLE_LENGTH` = 64, stripped and non-blank via `_nonblank_role`) and a
canonical `TaskDocumentRef`. It only bounds the *shape* of what an ambient caller may supply —
semantic authorization (may this role grade, select, decide, or declare) stays in the consuming
mechanism.

### Conventions

One shared model consumed by both fallback seams (`application/closeout_queue.py`,
`application/structural/gate_tools.py`, and their registration layers) so the request-carried
identity is validated identically everywhere. No copied validators.

### Invariants And Boundaries

- The declaration is assertion, not plane proof: the residual trust risk is deployment-level
  (who may reach the MCP server), and the mechanism grants no more than a seat with the same
  role/document pair (the L16 F5 trust model, documented at each exposure surface).
- Hosted seats win; a request-carried caller that contradicts the seat refuses (conflict), and
  only `ambient-seat-unavailable` triggers the fallback.
- Role is bounded (64 chars) and non-blank; the document ref is canonicalized by
  `TaskDocumentRef`.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is an internal authority-boundary model.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict bounded shape of a request-carried ambient identity. | `DeclaredCaller`; `_nonblank_role` | mcp/src/agents_remember/models/declared_caller.py:19-39 |
| Consumed by the closeout-queue ambient fallback. | `_declared_queue_actor` | mcp/src/agents_remember/application/closeout_queue.py:61-71 |
| Consumed by the structural gate-tools ambient fallback (duck-typed `DeclaredGateCaller`). | `_context`; `DeclaredGateCaller` | mcp/src/agents_remember/application/structural/gate_tools.py:36-51; mcp/src/agents_remember/application/structural/gate_tools.py:63-88 |
| The request field that carries the declaration on the queue wire model. | "caller: DeclaredCaller" | mcp/src/agents_remember/models/queue/closeout_queue.py:38-38 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the seat-independent task-execution
  fallback (L16-R2/R3): the typed request-carried ambient caller identity shared by the
  closeout-queue and structural gate-tools fallbacks. Verified at code commit a9d50e08.
