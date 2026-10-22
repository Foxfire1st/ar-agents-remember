# mcp/tests/test_held_delivery_tick_cost.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

What one held-delivery tick costs when nothing has changed.

## Code Commentary

The tick reads the host's publication and the role record for two decisions, and the finding this file guards was a second reader that parsed both files on every tick even when the host had written nothing. The cases count the reads, the stats and any bridge process for one seat and for a fleet.

**L184 — INV-1ZKP4R.** The cost bound is measured by this case, which is where a regression would show. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
