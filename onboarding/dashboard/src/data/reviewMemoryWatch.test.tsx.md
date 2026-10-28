# dashboard/src/data/reviewMemoryWatch.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

Synthetic EventSource exercises a single shared SSE connection: exact live context, readiness reconciliation, duplicate silence, reconnect, superseded connection rejection, recorded/retired/unmounted lifetime and target-scoped watch failure. Native filesystem timing is not proved here.

### Declared Assertions

- `it('owns one existing SSE scope only while a live review is mounted', () => {`
- `it('reconciles after native EventSource reconnect without accepting an old connection', () => {`
- `it('does not watch a recorded review or keep a watch after its live enclosure retires', () => {`
- `it('reports a same-target watch failure, not an unrelated target or empty success', () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence

- Synthetic EventSource exercises a single shared SSE connection: exact live context, readiness reconciliation, duplicate silence, reconnect, superseded connection rejection, recorded/retired/unmounted lifetime and target-scoped watch failure. Native filesystem timing is not proved here.

- Retired at the fifth freeze d59c3493: dashboard/src/data/reviewMemoryWatch.test.tsx:1-116 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848. Retired means the anchor no longer stands, not that the cited subject was deleted.
