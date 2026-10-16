# mcp/src/agents_remember/serving/review_summary.py

## Governing Overview

[serving route overview](overview.md)

## Purpose

The transport for `GET /api/review/intent/summary?repo=&master=&leaf=`: the one small read the task
entry makes before the reviewer opens (`ICR-R24@v3`, leaf `260921-ICR-L47`). It takes task context
only (never a path), calls the `ReviewIntentSummaryPort` the composition root wires, and serializes the
typed [`ReviewIntentSummaryResult`](../models/knowledge/review_intent_summary.py.md) through the app-owned conditional reader.

## Code Commentary

### Logic

`register_review_summary_route(app, port, cache)` registers the route before the greedy static mount. With a port, the shared `IntentSummaryCache` validates the captured inputs and supplies typed counted, partial or unavailable bodies as HTTP 200, or bodyless HTTP 304 when the conditional ETag still matches. Without a port, it answers HTTP 503 with `_UNWIRED_SUMMARY`: an unwired process is not a measured zero. Cache ownership and generation capture remain outside the transport.

### Conventions

It is its own module, not a fourth route in `serving/review.py`, because that module is past the
repository's size rail. Like the other review routes it is transport only; no selection happens here.

### Invariants And Boundaries

- **Status idiom differs from the catalogue on purpose (worker observation O2, review F6).** The other
  review routes answer a refusal with its own non-2xx status. This route does not: an uninitialized
  leaf is the ordinary state of a new leaf, and a 404 would put a console error on every such task page.
  The reviewer route itself still refuses with its own status when opened.
- Unwired is the error response; an unchanged conditional representation may instead be bodyless 304. Neither is a counted zero.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The transport uses the task-context summary port and the shared conditional cache. [1]
- The unwired answer: named, and never a zero. [2]
- The route delegates typed-body or conditional-304 responses, with 503 when unwired. [3]

- App composition registers the collaborator summary port with the app-owned change-set cache. [4]

- The optional collaborator slot the route reads. [5]

- The fixture checks counted and unavailable bodies as 200, and the unwired process as 503; it is not a separate partial-state or conditional-304 test. [6]


### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
