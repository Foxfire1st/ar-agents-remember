# dashboard/src/panels/review/reading/reviewPage.test-utils.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Provide traceable review-page fixtures, held transport and intersection control.

## Code Commentary

### Logic

Routes page fetches over the captured L181 card entries/outline and L37 task/member answers moved into the test comparison context. Summary, leaf-wide trees, one 45-line unexplained added lane file and its text/classification are composed locally. servePage records every URL, optionally holds matching responses and returns 404 for an unknown route; helpers classify page/file reads and drive either explicit or first-paint intersections. Adapters replace lane text or selected-subject payloads, while renderPage mounts ReviewSurface with a fixed place and optional props.

### Invariants And Boundaries

The composed and moved responses are explicitly test data, not new captures from the server. engage only dispatches a wheel event; it does not define the read-gate policy, and in-view lane reads can begin without it once opening completes.

## Evidence

- Captured inputs, moved subject/task answers and deliberately composed summary/tree/lane routes. [4]
- Recorded/held fetch transport and controlled IntersectionObserver implementations. [5]
- Answer adapters, gesture dispatch and ReviewSurface rendering. [6]
