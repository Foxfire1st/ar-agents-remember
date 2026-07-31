# dashboard/src/data/operatorInbox.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/operatorInbox.test.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash |                                                  `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                                  2026-06-28T18:49:06+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No relevant external documentation beyond the repository's observable-lifecycle design was needed for
this client helper test; the behavior is pinned by same-repository code and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests pin the POST body, posted/error return contract, and dismiss helper endpoint mapping. | L5-L65 | [operatorInbox.test.ts](agents-remember/dashboard/src/data/operatorInbox.test.ts) |
| The helper under test owns the fetch call and response mapping. | L1-L25 | [operatorInbox.ts](agents-remember/dashboard/src/data/operatorInbox.ts) |
| Component-level tests pin how the helper is used from Gate Respond. | L53-L84 | [GateResponder.test.tsx](agents-remember/dashboard/src/panels/GateResponder.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 line citation that ran past the end of
  the file (cited L5-L67; the file is 65 lines). The two `describe` blocks the row names span
  L5-L65 — `postOperatorInbox` L5-L45 and `dismissOperatorInboxEntry` L47-L65 — read back and
  corrected. Noted while verifying, not changed: the Code Commentary still says the dismiss helper
  returns `"queued"`, but the tests at L52 and L59 assert `"dismissed"` and `"not-found"`.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-25T13:20+02:00 — Task 23/24: added coverage for `dismissOperatorInboxEntry`, the client-side delete path for stale pickup warnings.
- 2026-06-23T15:05+02:00 — Created for task 10 dashboard fallback: coverage for the `postOperatorInbox` request body and error mapping.
