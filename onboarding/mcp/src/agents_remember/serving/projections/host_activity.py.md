# mcp/src/agents_remember/serving/projections/host_activity.py

[governing overview](overview.md)

## Purpose

Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity.

## Commentary

Intake runs only at startup/HOST_ACTIVITY invalidation. Known requires armed supervisor, complete readable publication and bridge acknowledgement of that boot. First/new-boot generations reconcile; missing/incomplete/failed/unacknowledged evidence stays unknown. Registrations bind agents to task keys; unmatched agents plus ignoredEvents are counted. No host polling timer or second status store exists.

## Turn-end and second-view reads

`turn_ended_agents` selects idle, closed or ended observations for held delivery. It deduplicates both stamped and unstamped observations per reader in `seen` using the published `eventAt` stamp or a boot-scoped `unstamped:<boot_id>` key from `_ParsedPublication.boot_id` without fabricating `eventAt` in `host-activity.json`, and the held-delivery tick passes its selected IDs to the explainer callback where wired. The same tick shares its parsed publication with `new_stamped_ends`, which requires a changed stamped idle observation and a registered role-agent identity for usage. `agent_in_turn` independently checks whether a complete publication shows the recipient in a turn. Task projection still qualifies its activity on startup or host invalidation.

`usage_read_batch` combines one tick's new stamped ends with the report ids due for a five-minute recheck. A due report names only the mapped agents still in the role record and not ended in the same publication; the batch shares the tick's stat-bound publication and role-record parse rather than reading either again. A due report with no eligible mapped seat is left to `provider_limit_hold` to log once per period.

## Evidence



- Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity. [1]



## Shared held-delivery publication parse

The three-second `_held_delivery_loop` in `serving/_app_lifespan.py` shares `_parsed_publication` between its separate ending and stamped-idle lists; `_ParsedPublication` also retains `boot_id` and `ended` alongside `endings` and `idle`. The parser caches a complete publication by path and reuses it when inode, size, nanosecond mtime and nanosecond ctime match, with at most four paths. Missing, unreadable or incomplete publication evicts the cached value.

**L184 — INV-VDWN33.** This input is where an answer is accepted, so the ordering rule is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
