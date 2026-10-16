# mcp/src/agents_remember/serving/projections/host_activity.py

[governing overview](overview.md)

## Purpose

Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity.

## Commentary

Intake runs only at startup/HOST_ACTIVITY invalidation. Known requires armed supervisor, complete readable publication and bridge acknowledgement of that boot. First/new-boot generations reconcile; missing/incomplete/failed/unacknowledged evidence stays unknown. Registrations bind agents to task keys; unmatched agents plus ignoredEvents are counted. No host polling timer or second status store exists.

## Evidence

- Intake the plugin’s event-driven host publication only at startup or host invalidation, reconciling boot identity before exposing known activity. [1]
