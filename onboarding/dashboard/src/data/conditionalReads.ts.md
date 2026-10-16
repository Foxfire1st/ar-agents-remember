# dashboard/src/data/conditionalReads.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Store-owned bounded conditional HTTP results, with pending sharing and retained display qualified by request facts.

## Code Commentary

`load` shares a URL's pending promise only for identical facts. A different facts identity aborts the older controller and starts a separate read; oldest pending reads are also aborted at capacity. Finalization removes only its own pending controller.

`peek` returns retained bytes only for matching facts. A revalidation sends the retained ETag; a valid 304 reuses parsed identity without decoding and binds it to the newly confirmed facts. A 304 without retained bytes is refused. Successful decoded results enter the bounded LRU, while failures drop history; aborted reads neither relabel/retain values nor evict a newer answer. Abort checks surround response/decode handling. This is a conditional HTTP cache, not an atomic workspace snapshot or a task-state authority.

## Evidence

- Same-facts sharing and bounded pending replacement. [1]
- Retained values are facts-qualified. [2]
- Conditional validation and late-abort retention guards. [3]
