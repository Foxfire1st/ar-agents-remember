# mcp/src/agents_remember/serving/conversation/response_contract.py

| Field                  | Value                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| repository             | agents-remember                                                      |
| path                   | `mcp/src/agents_remember/serving/conversation/response_contract.py`  |
| doc_type               | `file-level-onboarding`                                              |
| lastUpdated            | 2026-08-01T08:18+02:00                                               |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`                           |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                                        |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

`conversation/response_contract.py` is the declared response contract for the 25
structured-conversation routes — the three active routes, the five native-library routes, and
the seventeen control routes. It is the conversation half of the app-wide "every HTTP route
declares what it answers with" contract; the other half is `serving/response_contract.py`.

What these routes already had, and what they did not: all 25 *dump* a strict `WireModel`, so a
model existed for nearly every body — but not one route **declared** it, and three bodies (the
staging answer, the submit answer, the agent-history answer) are assembled at the route and had
no model at all. Those three are declared here; the rest reuse the models the handlers already
dump.

## Code Commentary

### Logic

**Three route-assembled shapes get their first model**: `StagedAttachments`
(`/conversation/attachments` and `/attachments/rebind` — the operation plus its receipts),
`ConversationSubmitted` (`/conversation/submit`), and `AgentHistoryHydrated`
(`/agents/{agent_id}/history`, where a typed child failure is a successful 200 local outcome, so
the failure vocabulary lives inside the body's `status`).

**`WithdrawQueueAnswer`** is the plain union
`WithdrawnQueueResponse | FailedWithdrawalResponse`: `withdrawals.withdraw_http_status` picks the
status from which one it built, so a failed withdrawal is still this route's own answer.

**Four shared `responses={...}` tables, each transcribed from one real mapper:**

- cit:([`CONTROL_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:95-108) — `control/api._map_typed_error` is the single mapper for the
  control surface, so its six statuses (400 / 403 / 404 / 409 / 422 / 503) are the complete
  refusal surface of all 17 control routes.
- cit:([`CONVERSATION_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:113-120) — the active routes, which add the cursor refusals: the
  only refusals on this surface that carry a machine-readable `reason`.
- cit:([`LIBRARY_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:125-135) — `library/api._ERROR_STATUS_TABLE` and `_error_response`
  transcribed; every entry in that table lands on one of these six statuses.
- Plus the three **outcome** tables below.

**The outcome tables exist because a non-200 status here is often not a refusal at all.**
cit:([`INTERRUPT_OUTCOME_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:140-153), cit:([`WITHDRAW_OUTCOME_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:160-173) and
cit:([`OPEN_OUTCOME_RESPONSES`], mcp/src/agents_remember/serving/conversation/response_contract.py:178-198) each declare statuses whose body is the operation's own
outcome. `operations.interrupt_http_status` picks 200/202/422/503 off the operation's own
`acknowledgement`/`settlement`, so three of those statuses carry an `InterruptOperation` and not
a refusal body — declaring them as refusals, which the shared table alone would have done, was
wrong, and the conformance suite caught it on the real 422.

**Every outcome table unions in the refusal model the shared table declares for the same
status**, and that is the load-bearing detail: routes spread these tables as
`{**LIBRARY_RESPONSES, **OPEN_OUTCOME_RESPONSES}`, and `{**a, **b}` is a **dict merge, not a
union**. A bare `{409: OpenConversationOperation}` *deletes* `LIBRARY_RESPONSES[409]` rather than
joining it, while `_error_response` still answers 409/422/503 with those refusals on all three
open routes — so an overwriting entry would have named, on nine (route, status) pairs, a model
the route cannot produce. `/conversation/submit` had the same defect and is fixed the same way at
its own route (its 422 unions `ConversationSubmitted | StatusRefusal`, because
`CapabilityRefusedError` and `OperationRejectedError` both carry `http_status = 422`).

### Conventions

Models here derive from `WireResponse` (imported from `serving/response_contract.py`) — strict,
frozen, camel-aliased — while the reused route bodies stay `WireModel` from
`conversation/models.py`. Each table is documented by naming the *mapper* it transcribes, so the
table and its source cannot drift silently.

### Invariants And Boundaries

- **The split from `serving/response_contract.py` is a package boundary, not a convenience.**
  Everything here needs `conversation/models.py`; importing that from the app-level module would
  make it import `serving.conversation`, whose package `__init__` mounts the routers, which
  import the contract back. `serving/app.py` registers the files / change-set / notes routes
  first, so the app-level module must stay importable first.
- **A table is only ever as complete as the mapper it transcribes.** Adding a status to
  `_map_typed_error`, `_ERROR_STATUS_TABLE`, `interrupt_http_status`, `withdraw_http_status` or
  `_OPEN_STATUS_BY_OUTCOME` without adding it here leaves a route emitting an undeclared status.
- **Outcome statuses are success shapes.** A `pending` open, an acknowledged-but-unsettled
  interrupt, and a not-withdrawable withdrawal are answers with their own bodies; mapping them
  onto refusal models alone would be a lie about what the route emits.
- **Spreading tables must union, never overwrite** — see the dict-merge rule above; this is the
  shape every outcome table has to have.

### Todos

None specific to this module.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this internal wire contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Each table here is a transcription of one real mapper in a sibling route module, and the models
it reuses are owned by the parent contract module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict base and the shared refusal models this module imports and extends. | `WireResponse`; `StatusRefusal`; `CursorRefusal`; `CapabilityUnavailableRefusal`; `BridgeEpochMismatchRefusal` | mcp/src/agents_remember/serving/response_contract.py:88-100; mcp/src/agents_remember/serving/response_contract.py:111-115; mcp/src/agents_remember/serving/response_contract.py:152-158; mcp/src/agents_remember/serving/response_contract.py:170-175; mcp/src/agents_remember/serving/response_contract.py:178-183 |
| The wire models the 25 routes already dumped, reused here as declarations. | `AttachmentOperationProjection`; `InterruptOperation`; `OpenConversationOperation`; `WithdrawnQueueResponse`; `FailedWithdrawalResponse` | mcp/src/agents_remember/serving/conversation/models.py:831-932; mcp/src/agents_remember/serving/conversation/models.py:935-960; mcp/src/agents_remember/serving/conversation/models.py:1024-1031; mcp/src/agents_remember/serving/conversation/models.py:1034-1046; mcp/src/agents_remember/serving/conversation/models.py:1165-1202 |
| The one mapper `CONTROL_RESPONSES` transcribes, and the submit route whose 422 unions the answer with the shared refusal. | `_map_typed_error`; `conversation_submit` | mcp/src/agents_remember/serving/conversation/control/api.py:124-141; mcp/src/agents_remember/serving/conversation/control/api.py:635-682 |
| The cursor refusals `CONVERSATION_RESPONSES` adds for the active routes. | `_map_typed_error`; `_resume_cursor` | mcp/src/agents_remember/serving/conversation/active/api.py:77-99; mcp/src/agents_remember/serving/conversation/active/api.py:111-123 |
| The library error table `LIBRARY_RESPONSES` transcribes and the total outcome map `OPEN_OUTCOME_RESPONSES` pairs with. | `_error_response`; `_OPEN_STATUS_BY_OUTCOME` | mcp/src/agents_remember/serving/conversation/library/api.py:75-84; mcp/src/agents_remember/serving/conversation/library/api.py:271-286 |
| The status pickers whose non-200 answers carry the operation body rather than a refusal. | `interrupt_http_status` | mcp/src/agents_remember/serving/conversation/control/operations.py:552-561 |
| The suite that drove the real 422 and caught the interrupt table declaring a refusal where an operation body is emitted. | `ServingResponseConformanceTests` | mcp/tests/test_serving_response_conformance.py:783-1861 |

## Cross-Repo References

No external repository boundary is declared here; these are bodies this repository's own
conversation routes emit.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 5 repeated path:start-end Citation objects from 2 same-claim citation group(s) at card line(s) 116, 118; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 1 repository-reference citation and normalized 2 prose citations (1/1 anchored and sourced; scoped citation check clean).

- 2026-08-01T08:18+02:00 — 260731-EFA-L4 curator: created for the new
  `serving/conversation/response_contract.py`. Documented the three route-assembled shapes that
  had no model (`StagedAttachments`, `ConversationSubmitted`, `AgentHistoryHydrated`), the
  `WithdrawQueueAnswer` union, and the four shared `responses={...}` tables with the mapper each
  transcribes. Recorded the dict-merge rule that makes every outcome table union in the shared
  table's refusal model for overlapping statuses — `{**LIBRARY_RESPONSES,
  **OPEN_OUTCOME_RESPONSES}` deleted refusal models on three statuses across the open trio, and
  `/conversation/submit` had the same defect — and the package-boundary import-order reason this
  module is split from `serving/response_contract.py`. Verification metadata is a placeholder
  pinned to the leaf base `abc7cbcc`; closeout stamps the real commit.
