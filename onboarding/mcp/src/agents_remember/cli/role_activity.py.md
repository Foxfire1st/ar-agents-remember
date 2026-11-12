# mcp/src/agents_remember/cli/role_activity.py

[governing overview](../../../overview.md)

## Purpose

Publish receipt-bound role identity before native start or resume can emit its first event.

## Commentary

`publish_receipt_role_agent` validates stored selection and agent/report identity, then publishes role, qualified task/master/sprint key (or Projects) and reportPath. Missing runtime/report or config/filesystem failure is best effort; malformed selection validation can still raise. `resume_role_agent` publishes before native resume. Neither boundary proves plugin consumption or task acceptance.

## Evidence

- Publish receipt-bound role identity before native start or resume can emit its first event. [1]
