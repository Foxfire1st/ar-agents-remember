# dashboard/src/data/conditionalReads.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pin facts-qualified conditional result retention, bounded actual-store histories and current failures.

## Tested Boundary

Stubbed fetch/ETag responses distinguish parsed identity on 304, replacement on a new ETag, and `peek` only under the facts that read or revalidated an answer. Actual-store loops exercise entry and byte bounds, LRU reuse, oversized active results, same-facts pending sharing and late-aborted non-retention. Failures discard retained success and an unsolicited 304 is refused. These assertion definitions do not constitute a server/browser run or an elapsed-time guarantee.

## Evidence

- Facts-qualified 304 identity with no body decode. [1]
- Actual-store entry and byte bounds over growing histories. [2]
- Oversize, same-facts pending sharing, abort and current failure. [3]
