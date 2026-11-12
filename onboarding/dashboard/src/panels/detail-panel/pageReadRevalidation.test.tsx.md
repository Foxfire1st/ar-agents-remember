# dashboard/src/panels/detail-panel/pageReadRevalidation.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin retained page-read display and visibility revalidation.

## Tested Boundary

Stubbed responses retain counters/intent synchronously on return while ETags validate, use the current click callback and replace stale success with current refusal. Shown-again counters re-read; working availability comes only from this entry’s worktrees, not a global enclosure join. No test execution is claimed.

## Evidence

- Retained counters/current callback [1]
- Intent refusal and mounted-show revalidation [2]
- Entry-owned working availability [3]
