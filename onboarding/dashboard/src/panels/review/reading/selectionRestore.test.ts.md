# dashboard/src/panels/review/reading/selectionRestore.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Guard exact hunk restoration against comparison and file-classification facts.

## Code Commentary

### Logic

Builds one comparison and a lane path with two classified spans. Pure restoreSelection cases wait for absent/reading classification, reject forged spans including an off-by-one count, admit the exact added hunk and deletion, preserve an unavailable-file reason, and reject foreign code trees before a file read is available.

### Invariants And Boundaries

The test supplies RestoreFacts directly and exercises the pure restore decision. It performs no fetch, mounts no page, and does not prove a native reload or scrolling behavior.

## Evidence

- Synthetic comparison, lane path and exact added/deleted hunk facts. [4]
- Wait/select/outside decisions preserve exact spans, file failures and comparison identity. [5]
