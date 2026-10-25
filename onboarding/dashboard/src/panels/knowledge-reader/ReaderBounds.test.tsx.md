# dashboard/src/panels/knowledge-reader/ReaderBounds.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

New synthetic mounted reader controls cover commit/branch validation, prior-selection retention, bounded prose/whole-text single-read and deeper-family explanation, snapshot mismatch refusing mixed prose/references or timeline/record, 50-event continuation controls, attempt/path and legacy effect text, and late side-load suppression, the outline's whole-prose chapter enrichment and its clearing when a ready pane renders none. These are controlled component assertions, not a server timing result.

### Declared Assertions

- `it('resolves a typed memory branch before navigating and keeps the prior selection on invalid input', async () => {`
- `it('names truncated summary prose, loads its whole text and explains omitted deeper families', async () => {`
- `it.each(['published', 'leaf:active'])('rejects changed prose at %s', rejectChangedProse);`
- `it.each(['published', 'leaf:active'])('keeps the %s timeline snapshot', keepRecordSnapshot);`
- `it.each(['prose', 'timeline'])('drops late %s side loads after navigation', async (kind) => {`
- `it('lists the chapters the whole text renders beside the chapters the summary showed', async () => {`
- `it('clears the previous page chapters when the next ready pane renders none', async () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence




- Mounted reader controls cover typed commit/branch resolution retaining the prior selection on invalid input, truncated summary prose loading its whole text once with omitted deeper families explained, changed-prose and timeline snapshot mismatches refusing the new tree's bytes, continuation controls that restart or drop late side-loads after navigation, and the chapters the whole text lists beside the summary's. These are controlled component assertions, not a server timing result. [1]
