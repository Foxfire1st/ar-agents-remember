# dashboard/src/panels/review/worklistState.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

Synthetic gate-owned worklist states check rendered answered ROW witness text, stale and undecided reasons, legacy-side explanation and comparison-bound per-file/worklist summaries. The helper case supplies witness='counted change' but asserts only the verdict-state result '1 open'; it does not assert rendering of that witness text. Client presentation never decides gate acceptance.

### Declared Assertions

- `it('states the verdict on each line including stale and undecided reasons, and explains legacy sides', () => {`
- `it('adds file states only for answered matching work, never claiming undecided work is answered', () => {`
- `it('does not mark items from a stored worklist belonging to another comparison', () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence


- Synthetic gate-owned worklist states check rendered answered ROW witness text, stale and undecided reasons, legacy-side explanation and comparison-bound per-file/worklist summaries. The helper case supplies witness='counted change' but asserts only the verdict-state result '1 open'; it does not assert rendering of that witness text. Client presentation never decides gate acceptance. [1]

