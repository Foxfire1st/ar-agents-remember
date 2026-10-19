# mcp/src/agents_remember/serving/projections/host_activity.py

[governing overview](overview.md)

## Purpose

Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity.

## Commentary

Intake runs only at startup/HOST_ACTIVITY invalidation. Known requires armed supervisor, complete readable publication and bridge acknowledgement of that boot. First/new-boot generations reconcile; missing/incomplete/failed/unacknowledged evidence stays unknown. Registrations bind agents to task keys; unmatched agents plus ignoredEvents are counted. No host polling timer or second status store exists.

## Turn-end and second-view reads

Two readers take the publication as it is, without the projection's boot reconciliation. `turn_ended_agents` answers the agents whose published state is `idle` or `ended`, once per `eventAt` stamp (a caller keeps at most 4,096 stamps), and the held-delivery tick uses it as the turn end it waits for. `agent_in_turn` answers whether a complete publication names one agent `in-turn`, and the send decision weighs it as a second view of a running turn. Both are one read of the same publication: neither writes a status store, starts a second intake or adds a polling timer; the caller owns the cadence.

## Evidence

- Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity. [1]

## 260928-MIK-L177 The Held-Delivery Tick Parses Only New Publication Bytes

The held-delivery tick — the projection loop's `MAX_PROJECTION_REST_SECONDS = 3.0` rest in
`change_watcher.py` — used to read and parse the host's publication file on every pass.
`_no_turn_endings` now stats the file first and parses it only when its inode, size, mtime or ctime
moved, keeping the last parsed `(agent, stamp)` pairs for at most four publication files. A missing,
unreadable or incomplete publication answers nothing and keeps nothing for it.
