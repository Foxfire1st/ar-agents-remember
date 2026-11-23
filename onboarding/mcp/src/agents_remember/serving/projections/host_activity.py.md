# mcp/src/agents_remember/serving/projections/host_activity.py

[governing overview](overview.md)

## Purpose

Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity.

## Commentary

Intake runs only at startup/HOST_ACTIVITY invalidation. Known requires armed supervisor, complete readable publication and bridge acknowledgement of that boot. First/new-boot generations reconcile; missing/incomplete/failed/unacknowledged evidence stays unknown. Registrations bind agents to task keys; unmatched agents plus ignoredEvents are counted. No host polling timer or second status store exists.

## Turn-end and second-view reads

`turn_ended_agents` selects idle, closed or ended observations for held delivery. The held-delivery tick deduplicates available event stamps and also passes its selected IDs to the explainer callback where wired. The same tick shares its parsed publication with `new_stamped_ends`, which requires a changed stamped idle observation and a registered role-agent identity for usage. `agent_in_turn` independently checks whether a complete publication shows the recipient in a turn. Task projection still qualifies its activity on startup or host invalidation.

## Evidence



- Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity. [1]



## Shared held-delivery publication parse

The three-second `_held_delivery_loop` in `serving/_app_lifespan.py` shares `_parsed_publication` between its separate ending and stamped-idle lists. The parser caches a complete publication by path and reuses it when inode, size, nanosecond mtime and nanosecond ctime match, with at most four paths. Missing, unreadable or incomplete publication evicts the cached value.

**L184 — INV-VDWN33.** This input is where an answer is accepted, so the ordering rule is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
