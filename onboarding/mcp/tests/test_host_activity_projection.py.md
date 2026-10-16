# mcp/tests/test_host_activity_projection.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin startup reconciliation and notification-only host activity intake, separate from supervisor lease heartbeat.

## Code Commentary

A configured bridge snapshot must acknowledge the current publication boot before activity is known. Only registered role facts join to task identity; unrelated agents count as ignored. A new boot/dashboard requires reconciliation, failed acknowledgement stays unknown and retries only after changed publication. Idle heartbeat, periodic full-heal and degraded wakes retain known activity without rereading host publications or role records. Tests patch bridge/publication boundaries; they do not run a live hosted agent.

## Evidence

- Watch roots admit the activity directory, not the supervisor lease or broad host home. [1]
- Composition binds host-activity-snapshot to the existing bridge. [2]
- Reconciliation replaces stale startup activity and joins only registered roles. [3]
- New boot requires matching acknowledgement and failed bridge reads remain unknown. [4]
- Idle heartbeat passes neither read publications nor relaunch the bridge snapshot. [5]
- Periodic healing/degraded wakes do not poll host activity or role records. [6]
- A failed boot attempt retries only after new publication bytes. [7]
