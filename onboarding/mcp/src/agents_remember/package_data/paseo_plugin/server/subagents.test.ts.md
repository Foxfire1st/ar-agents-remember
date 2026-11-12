# mcp/src/agents_remember/package_data/paseo_plugin/server/subagents.test.ts

## Governing Overview

[plugin overview](../overview.md)

## Purpose

The subagent subscription, tracker and reconciliation under the plugin's real event and publication shapes.

## Code Commentary

The cases cover the running set and its bounds, the skip of traffic that changes nothing, the merge of the listed running subagents under later events, and the reconciliation generation that refuses an older reply. A finished child keeps no activity of its own, while a parent keeps its running subagents through its own turn end; only archiving or closing the parent drops the parent's subagents. A count beyond a bound is published as the bound.

**L184 — INV-VDWN33.** The tracker's rules are held by these cases, which is where the generation's meaning is pinned. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
