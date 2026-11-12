# dashboard/src/panels/review/walkUnavailable.refused.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The genuine HTTP 400 refusal of the review route for an invariant selector absent from the comparison, as served. It is the controlled refused answer of the status-reveal cases of `ReviewSurface.walkUnavailable.test.tsx` (OR-R042).

## Code Commentary

### What the body holds

- `state` is `refused`; `operation` is `read_knowledge_review`; `repository_id` is `agents-remember`.
- `refusal.code` is `comparison_refused`; `detail` begins `selector_absent: the selector names no invariant identity in the selected snapshot` and names the requested identity and the same absence for both sides.
- `refusal.next_action` says to select an identity or revision the snapshot records, and that this is a fact about the snapshot: nothing was read from a working tree or a Markdown document to answer it.
- `offending_input` is `invariant`.

### Use

`ReviewSurface.walkUnavailable.test.tsx` serves it for the target subject when a refused read is under test, in place of the failure `TypeError` the failed cases use.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkUnavailable.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (927 bytes).
- The refusal is of the captured comparison at source commit `beb9473e21f3e173094da4f1437798660c3abb52` and of one absent selector, not a statement about the requested obligation.
- The body was captured, not composed: replaying it is evidence of the refusal only.

## Evidence

- The served refusal body, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
