# dashboard/src/panels/review/ReviewChangePage.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

Hook scheduling controls use real comparison operands: an already open change page gains only same-comparison worklist, never another comparison answer.

### Declared Assertions

- `it('enriches an already open change page when its same-comparison worklist arrives', () => {`
- `it('never borrows an answered worklist from a different comparison', () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence

- Hook scheduling controls use real comparison operands: an already open change page gains only same-comparison worklist, never another comparison answer. [1]
