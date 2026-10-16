# dashboard/src/data/taskDocuments.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin revision-owned task bodies across reader navigation and bounded resource retention.

## Tested Boundary

Real hooks/resource classes consume stubbed Responses. Current summaries retain fresh facts; late/crossing revisions cannot replace the selected body. Unauthored entries request nothing; oversized bodies may render without retention. LRU/byte/preparation bounds are not an elapsed-time or producer test.

## Evidence

- Revision identity and crossing responses [1]
- Unmount, selection, summary/failure and unauthored controls [2]
- Oversized current body and retained-resource bounds [3]
