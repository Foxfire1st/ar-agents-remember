# dashboard/src/data/readOwnership.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pin the shared-read ownership rule for both dashboard stores: one owner's abort ends only that
owner's wait, and a replacement after the last waiter starts a new request.

## Tested Boundary

For `ConditionalReads`, two same-facts loads share one fetch but return distinct owner promises; the
first owner's abort settles that wait as `AbortError` while the joiner still receives the fetch's
answer, and the fetch is not cancelled. When the last waiter leaves, the pending entry is removed at
once, so an immediate replacement starts a second fetch instead of joining an aborted one. The same
two cases run for `TaskDocumentResources` with a body fetch. This is a store-level assertion
definition, not a browser run or a lifecycle result.

## Evidence

- The two production stores and `withAbort`.
- The cases named `settles the joiner from the same fetch and keeps the fetch alive`, `ends the
  request with its last waiter and never rejoins an aborted one`, `settles the joiner from the same
  body fetch and keeps it alive`, and `starts a new body fetch for an immediate replacement after an
  abort`.
