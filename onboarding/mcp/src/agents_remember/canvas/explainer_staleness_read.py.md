# mcp/src/agents_remember/canvas/explainer_staleness_read.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One staleness read of one retained revision — its parts, its grades, the trusted view and the regeneration message — against the one comparison the route decides is on screen.

## Code Commentary

- `screen_target` chooses the comparison on screen, then the live environment's binding, and refuses `comparison-unavailable` when it has neither, so a page is never called current with nothing to compare it against.
- `_require_same_leaf` refuses `revision-foreign` and `comparison-foreign`, so one leaf's page is never measured against another leaf's comparison.
- `staleness_read` reads the grade store and reconstructs the revision's recorded proof fingerprints when the caller supplies none, and answers one record that the page, the trusted view and the regeneration message all read.
- `gone_grade_references` names only the stored references the target no longer holds, so a stale grade whose block still exists is never pruned.
- `reconcile_grades` remaps a grade onto the block the target holds and carries the grades of merged hunks onto the hunk that now holds their lines, writing the store only when something was pruned or re-anchored.

## Evidence

- A read with neither an on-screen comparison nor an environment binding is refused, never answered as current [1]
- A revision or a comparison belonging to another leaf is refused by name [2]
- One answer carries the stale parts, the grade states, the trusted lines and the regeneration message [3]
- Only references the target no longer holds become the prune's `gone` tuple [4]
- Grades are remapped and merged hunks carried, and the store is written only for what changed [5]
