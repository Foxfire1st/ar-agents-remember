# mcp/src/agents_remember/serving/changeset_cache.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Own one serving app’s bounded cache of native change-set reads and conditional response envelopes. Retained values are accelerators, not alternative change-set computation or review authority.

## Code Commentary

Observed reads stage newly computed values until fresh observations of all consumed generations agree at settlement. A route whose policy admits it may retain a typed refusal on a matching unknown working-status stamp. A success on that stamp stays uncached. Reads outside the app-owned context compute normally. Cached values are deep-copied so annotations cannot corrupt subsequent callers.

The serving cache retains result and repository-layout tables. A changing working result is keyed by its Git status and path observations. Ref-keyed and working-input routes re-observe their recorded inputs. An immutable ID-keyed hit uses its key without probing object availability or current diff presentation settings. Generic task and file diffs are process-local. The explicit master range can load an immutable answer after restart within its producing-source namespace and disk count and byte limits.

Successful HTTP bodies receive content-derived weak ETags; matching conditional requests return 304 without the body. Initial discovery, invalidation and native computation may run Git. Input observation still does filesystem work; “unchanged” is not a zero-work claim.


## Current Behavior

The pending-result policy determines which typed refusals can settle on a matching unknown working-status stamp. The read bounds its object observations by capacity and withdraws values it admitted when the read is abandoned.

Shared Git generation history keeps the latest counts, fixed-size alternate-path fingerprint and revision for each repository and addition policy. New revisions use the complete incoming census. A matching census, or a tolerated addition with the same alternate fingerprint, preserves the current revision.

## Evidence


- Observed reads admit results when the captured input generations still match, subject to the route-specific treatment of a matching unknown working-status stamp.



- The app's result and layout LRUs have configurable capacity. The shared object-history LRU has its own 1,024-entry capacity. [2]





- Observed ref-keyed and working reads re-observe their inputs. A route may retain a typed refusal on a matching unknown working stamp. An immutable ID hit skips object and presentation probes. The explicit master range can also use its bounded disk store. [3]



- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/changeset_cache.py:84-92 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361. Retired means the anchor no longer stands, not that the cited subject was deleted.
