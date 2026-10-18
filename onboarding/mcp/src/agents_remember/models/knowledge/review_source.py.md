# mcp/src/agents_remember/models/knowledge/review_source.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Owns the source-pane value shapes extracted from review.py: a whole-comparison code inventory plus separately scoped attribution and recorded source locations.

## Code Commentary

`ReviewSourcePane.inventory` is required and independent of the selected knowledge subject. Locations retain claim/invariant identity, recorded and observed source identity, role/rationale, resolution, transition, recorded side and the whole movement; a single counterpart path is optional rather than guessed when movement has multiple addresses. Relationship rows can have no source address. Attribution and the three changed-path buckets are distinct from inventory.

`ReviewSourceInventory.state` is `measured` or `unavailable`; partial classification is the separate `partial` boolean, not a third literal. `listed_total` must equal the text-representable `entries` count. Non-UTF-8 path names travel in `unrepresentable_paths` as exact ASCII-safe byte spellings; their presence requires a measured partial inventory rather than hiding paths or re-encoding them. An unavailable inventory has no entries and is not partial. `ReviewChangedFile.detail` is present exactly for unknown content. `ReviewRemainingCount` has a nonnegative measured value or a reason for absence, never both.

These source contracts survive the old record-channel retirement. review.py imports/re-exports them; their extraction is not a replacement implementation for verification observations or applicability.

## Invariants And Boundaries

The source inventory is not filtered down to selected realization locations. Model declarations do not themselves measure Git, prove disjoint attribution, resolve counterpart cardinality or render missing roles: producers and renderers own those operations. listed_total counts entries, not entries plus unrepresentable_paths.

## Evidence

- Absent counts require a reason; measured counts cannot carry a not-applicable reason. [1]
- Recorded source locations preserve independent movement and identity fields. [2]
- Content classification has detail exactly when unknown. [3]
- Unrepresentable path names retain raw bytes in a safe text spelling. [4]
- Inventory has two states, a partial flag and explicit count/unavailable/unrepresentable-path checks. [5]
- Whole-comparison inventory is separate from selected attribution and relationship/location collections. [6]
