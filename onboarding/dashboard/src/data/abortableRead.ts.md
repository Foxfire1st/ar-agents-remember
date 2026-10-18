# dashboard/src/data/abortableRead.ts

## Governing Overview

[data overview](overview.md)

## Purpose

One owner's cancellation vocabulary for dashboard reads. `abortedRead()` returns the `AbortError`
DOMException, `isAbortedRead(cause)` recognizes it, and `withAbort(promise, signal)` follows one
owner's signal without cancelling a shared read another reader still wants.

## Code Commentary

`withAbort` returns the original promise when no signal is given. Otherwise it rejects with
`abortedRead()` when the signal is already aborted, attaches a one-shot `abort` listener, and settles
the owner's promise from the shared promise; both settle paths remove the listener. A store's shared
fetch therefore keeps running for its other waiters, and a completed answer is retained for them.
`isAbortedRead` checks the DOMException name, so a page can tell an abandoned read from a failure.

## Invariants And Boundaries

- An owner's abort ends only that owner's wait; it does not cancel a shared fetch that another reader
  still wants.
- An aborted read is never rendered as a failure and never becomes a retained error.
- The helper owns no cache, no request and no retry policy.

## Evidence

- The production helper and its two call sites (`ConditionalReads.load`, `TaskDocumentResources.load`)
  in the candidate tree.
- `dashboard/src/data/readOwnership.test.ts` joins two owners to one fetch and checks the leaving
  owner's wait and the surviving joiner.
