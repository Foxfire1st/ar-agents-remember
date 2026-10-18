# dashboard/src/data/conditionalReads.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Store-owned bounded conditional HTTP results, with pending sharing and retained display qualified by request facts.

## Code Commentary

`load` shares a URL's pending promise only for identical facts. A different facts identity aborts the older controller and starts a separate read; oldest pending reads are also aborted at capacity. Finalization removes only its own pending controller.

`peek` returns retained bytes only for matching facts. A revalidation sends the retained ETag; a valid 304 reuses parsed identity without decoding and binds it to the newly confirmed facts. A 304 without retained bytes is refused. Successful decoded results enter the bounded LRU, while failures drop history; aborted reads neither relabel/retain values nor evict a newer answer. Abort checks surround response/decode handling. This is a conditional HTTP cache, not an atomic workspace snapshot or a task-state authority.


## Current Behavior

the pending entry is now `{facts, controller, promise, waiters}` (`:10-18`). `load(url, decode, facts, signal)` (`:41-80`) joins only the same-facts entry; a facts change or capacity stop calls `stop(url)`, which deletes the entry before aborting it so nobody can join an aborted request; each caller gets `withAbort(joined.promise, signal)` and a `leave` that decrements `waiters` and calls `stop(url, joined)` at zero (`:82-88`). A joiner that did not leave keeps the fetch and its result. This supersedes 'A different facts identity aborts the older controller and starts a separate read' only in that the owner's wait, not the store's fetch, is what the signal ends, and the last waiter decides when the fetch stops.

## Evidence

- Same-facts sharing and bounded pending replacement. [1]
- Retained values are facts-qualified. [2]
- Conditional validation and late-abort retention guards. [3]