# mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper owns one public SDK catalog lifetime and agent/workspace-specific Parent composer pills.

## Code Commentary

Initial/continuation directories use PAGE_SIZE=200 and unique nonempty cursors. Subscriptions publish allowed canonical/native-parent labels and normalized native activity. Replacement snapshots clear older queued deltas only for their directory; generation checks suppress older loads. Parent pills track native relation/workspace and disappear for root/missing/archived rows.

## Invariants And Boundaries

Errors remain explicit; native membership is transported without inventing AR grouping. Pinned request bounds require revalidation on upstream changes. Teardown releases listeners/subscriptions/pills.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `PAGE_SIZE` | `mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts:60-90` |
| Current source owner or exact assertion described above. | `allEntries` | `mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts:62-74` |
| Current source owner or exact assertion described above. | `startHierarchy` | `mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts:76-211` |
| Deferred lookup is ignored after tab/relation changes; a still-visible split-pane caller can open its current parent, and missing/archived parents or root transitions do not replace the child. | `checks current visible caller and parent relation, including deferred navigation, unavailable parents and root transitions` | `dashboard/src/cockpit/paseoHierarchy.test.ts:134-164` |
| Overlapping replacement snapshots suppress old queued/late actor results, preserve unrelated and newer updates, and release project listeners, SDK subscriptions and Parent pills. | `replaces directory snapshots on reconnect and releases subscriptions and buttons on teardown` | `dashboard/src/cockpit/paseoHierarchy.test.ts:188-218` |
