# mcp/src/agents_remember/serving/review_summary.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The route path and the port signature (repository, master, leaf). [1]
- The unwired answer: named, and never a zero. [2]
- Every typed state answered 200 with the body; 503 only without a port. [3]
- The route is registered from the app's collaborators. [4]
- The optional collaborator slot the route reads. [5]
- The case that pins 200 for every typed state and 503 when unwired. [6]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
