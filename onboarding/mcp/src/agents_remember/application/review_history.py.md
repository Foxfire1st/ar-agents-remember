# mcp/src/agents_remember/application/review_history.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Share after-tree owner-history acquisition and raw record identity recovery between meaning steps and the judgment pane.

## Code Commentary

`raw_subject` resolves the after index’s UUID reverse map, then uses a supplied baseline solely for identity recovery when after lacks it; raw row subjects remain raw. `owner_rows` asks history_rows_of(owner), refuses when the returned index state is incomplete, and admits only paths recognized as that owner’s attempt files. The query is owner-filtered, but its Answer carries global index state: this function does not establish that unrelated parse failures are excluded from unavailability. No history is read from the baseline, no row is authored, and no new store or route is added.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- Baseline fallback recovers identity only; history remains after-tree. [1]
- Rows are owner/attempt-path filtered, with explicit incomplete-index refusal. [2]
- Unavailable history names failed paths and never claims no rows. [3]
