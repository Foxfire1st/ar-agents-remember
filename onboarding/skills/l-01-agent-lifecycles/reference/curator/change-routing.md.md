# skills/l-01-agent-lifecycles/reference/curator/change-routing.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for routing each change-set item and notes item to its file card, route overview, entity catalog or Operational-Notes home, and for deleted or renamed sources.

## Code Commentary

Changed source files get compact current contracts in their cards and sidecars, with the judgment recorded in a history row on converted memory; a mechanical consumer change with no contract impact gets a precise reviewed no-impact row. A route overview's body changes only when its meaning changed; otherwise an explicit no-impact entry is written only if the overview was reviewed. The entity catalog changes only for a real, load-bearing entity change. The level-three Operational-Notes target is the last resort, for a notes item with no file, route or entity home. Route indexes are regenerated with `route_index_refresh`, scoped to the leaf. When a leaf deletes or renames a source file, its card is retired and every reference to it is re-pointed or removed, including references the validator only reports.

## Evidence

- Every change-set and notes item is routed to its card, overview, catalog or last-resort Operational-Notes home, and route indexes are refreshed per leaf. [1]
- A deleted or renamed source retires its card and re-points or removes every reference. [2]
- The Curator role points here before routing a changed file or notes item. [3]
