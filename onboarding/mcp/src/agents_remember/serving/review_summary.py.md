# mcp/src/agents_remember/serving/review_summary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review_summary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:21+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

The transport for `GET /api/review/intent/summary?repo=&master=&leaf=`: the one small read the task
entry makes before the reviewer opens (`ICR-R24@v3`, leaf `260921-ICR-L47`). It takes task context
only (never a path), calls the `ReviewIntentSummaryPort` the composition root wires, and serializes the
typed [`ReviewIntentSummaryResult`](../models/knowledge/review_intent_summary.py.md) once.

## Code Commentary

### Logic

`register_review_summary_route(app, port)` registers the route (before the greedy static mount).
With a port, every typed answer — `counted`, `partial`, `unavailable` — is **HTTP 200** with the state
in the body (`model_dump(mode="json", exclude_none=True)`). Without a port, it answers **503** with
`_UNWIRED_SUMMARY`, because "this process cannot count" is a different fact from "nothing changed".

### Conventions

It is its own module, not a fourth route in `serving/review.py`, because that module is past the
repository's size rail. Like the other review routes it is transport only; no selection happens here.

### Invariants And Boundaries

- **Status idiom differs from the catalogue on purpose (worker observation O2, review F6).** The other
  review routes answer a refusal with its own non-2xx status. This route does not: an uninitialized
  leaf is the ordinary state of a new leaf, and a 404 would put a console error on every such task page.
  The reviewer route itself still refuses with its own status when opened.
- Unwired is the only non-2xx answer, and it never reads as zero.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route path and the port signature (repository, master, leaf). | `KNOWLEDGE_REVIEW_SUMMARY_ROUTE`; `ReviewIntentSummaryPort` | mcp/src/agents_remember/serving/review_summary.py:35-37 |
| The unwired answer: named, and never a zero. | `_UNWIRED_SUMMARY` | mcp/src/agents_remember/serving/review_summary.py:41-48 |
| Every typed state answered 200 with the body; 503 only without a port. | `register_review_summary_route`; `status_code=503` | mcp/src/agents_remember/serving/review_summary.py:51-59 |
| The route is registered from the app's collaborators. | `register_review_summary_route` | mcp/src/agents_remember/serving/app.py:303-303 |
| The optional collaborator slot the route reads. | `review_intent_summary` | mcp/src/agents_remember/serving/_app_common.py:492-499 |
| The case that pins 200 for every typed state and 503 when unwired. | `test_the_route_answers_every_typed_state_in_the_body` | mcp/tests/test_review_intent_summary.py:421-457 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the changed-intent summary route (`ICR-R24@v3`), including the deliberate 200-for-every-typed-state idiom. The verification pair names the code base; closeout owns the real stamp.
