# dashboard/src/panels/review/ReviewOutcome.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

Current-shape synthetic outcome cases distinguish measured-empty judgment/proofs/source from missing/unavailable/failed reads, mandatory judgment absence as failure, and coherent retained empty versus retained-generation states. Not captured API production evidence.

### Declared Assertions

- `it('claims known empty only for an answered empty judgment and proofs with measured zero source paths', () => {`
- `path: 'test.py',`
- `it('reports a missing required judgment as a visible failed read rather than known empty', () => {`
- `it('keeps retained empty answers distinct from unavailable judgment after a failed refresh', () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence

- Current-shape synthetic outcome cases distinguish measured-empty judgment/proofs/source from missing/unavailable/failed reads, mandatory judgment absence as failure, and coherent retained empty versus retained-generation states. Not captured API production evidence. [1]
