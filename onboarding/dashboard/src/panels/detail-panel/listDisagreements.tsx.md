# dashboard/src/panels/detail-panel/listDisagreements.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Render the selected task entry's served list/record disagreements without rebuilding membership or interpreting task documents in the browser.

## Code Commentary

`ListDisagreements` consumes `entry.disagreements`, returning nothing for an empty collection. Each served item becomes a row under “Records and list disagree”. The `WHAT` table distinguishes a record naming another master, an attachment already owned by another list, a record not listed, and a literal master value that resolves to no task. It uses already-served task titles when available and preserves useful reference/literal fallbacks.

The React key includes kind, record reference, listed row, declared master, unresolved master literal and actual parent. This keeps distinct served disagreements distinct; it is not client-side deduplication. A record present in the shared task map gets a navigation callback through its served key; an absent record retains its reference-path label without an invented navigation target. `TaskChildrenBlock` composes this section alongside its child groups, including when disagreement is the only task content.

## Invariants And Boundaries

The server owns membership, deterministic conflict reporting and the once-per-owner disagreement population. This component displays that population; it neither repairs task JSON nor attaches an unlisted record to a parent. Its title fallback and explanatory words are presentation, never task status or authority.

## Evidence

- Render the served disagreement population, with navigation only for a present shared TaskEntry. [1]
- Distinguish disagreements by every served identity field, without recomputing or deduplicating the population. [2]
- The task-group block includes disagreements even when no child group exists and composes the section from its own entry and shared task map. [3]
- Disagreement uniqueness is server-owned, keyed by reporting master and the complete serialized disagreement; membership permits one acyclic parent. [4]
