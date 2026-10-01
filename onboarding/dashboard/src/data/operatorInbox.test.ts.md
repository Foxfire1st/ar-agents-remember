# dashboard/src/data/operatorInbox.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Focused Vitest coverage for the dashboard external-inbox client helper.

## Code Commentary

### Logic

The first test stubs `fetch` with an `ok: true` response, calls `postOperatorInbox`, and asserts the
same-origin `/api/operator-inbox` POST body keeps the lifecycle id, gate id, ask text, and response
text intact. The second test pins the UI contract for unsuccessful delivery: both a non-ok HTTP
response and a thrown fetch resolve to `"error"`. Task 23/24 adds `dismissOperatorInboxEntry` coverage:
the helper POSTs to `/api/operator-inbox/{entryId}/dismiss`, returns `"queued"` on a 2xx response, and
maps non-ok or thrown fetches to `"error"` so a stale `check chat` warning remains retryable.

### Conventions

Tests stub `fetch` globally and un-stub it in the same test body, matching the lightweight data-client
test style in this dashboard package.

### Invariants And Boundaries

- The tests cover the client helper only. Server-side attribution and persistence are covered in
  `mcp/tests/test_serving.py`.
- The helper deliberately exposes no retry loop or store mutation; caller UI state is tested with
  `GateResponder.test.tsx`.

### Todos

None.

## Evidence

### Docs References

No relevant external documentation beyond the repository's observable-lifecycle design was needed for
this client helper test; the behavior is pinned by same-repository code and tests.

None.

### Repo-Internal References

- The tests pin the POST body, posted/error return contract, and dismiss helper endpoint mapping. [1]
- The helper under test owns the fetch call and response mapping. [2]
- Component-level tests pin how the helper is used from Gate Respond. [3]

### Cross-Repo References

No meaningful cross-repo references found.

None.
