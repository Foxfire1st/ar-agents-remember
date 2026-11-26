# mcp/tests/test_host_activity_projection.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin startup reconciliation and notification-only host activity intake, separate from supervisor lease heartbeat.

## Code Commentary

A configured bridge snapshot must acknowledge the current publication boot before activity is known. Only registered role facts join to task identity; unrelated agents count as ignored. A new boot/dashboard requires reconciliation, failed acknowledgement stays unknown and retries only after changed publication. Idle heartbeat, periodic full-heal and degraded wakes retain known activity without rereading host publications or role records. Unstamped closed/ended/idle turn-end entries trigger `turn_ended_agents` once per plugin boot (`unstamped:<bootId>`), fire again on a real `eventAt` or a new `bootId`, leave `host-activity.json` bytes unchanged, and never trigger `new_stamped_ends` (`:85–120`). Tests patch bridge/publication boundaries; they do not run a live hosted agent.


**L184 — INV-VDWN33.** This is the consumer's own test, the one that fails on the old comparison. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

The dashboard composition fixture supplies empty registry history and checks that the registry read precedes the activity snapshot (:53–73). Receipt-backed restoration is exercised in test_role_revival_registration.py. The stale-reply case rejects the earlier reconciliation ID after accepting a newer reply for the same boot-a (:172–189). [2]

## Evidence

- Watch roots admit the activity directory, not the supervisor lease or broad host home. [1]


- The composition fixture reads empty registry history before the snapshot. A separate case rejects a stale reconciliation ID for the same boot. [2]

- Reconciliation replaces stale startup activity and joins only registered roles. [3]
- New boot requires matching acknowledgement and failed bridge reads remain unknown. [4]


- Idle heartbeat passes neither read publications nor relaunch the bridge snapshot. [5]
- Periodic healing/degraded wakes do not poll host activity or role records. [6]


- A failed boot attempt retries only after new publication bytes. [7]
