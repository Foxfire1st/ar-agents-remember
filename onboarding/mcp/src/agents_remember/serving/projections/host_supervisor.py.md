# mcp/src/agents_remember/serving/projections/host_supervisor.py

[governing overview](overview.md)

## Purpose

Own one native host-exit subscription feeding the existing projection change pacer.

## Commentary

Prove owned process, open pidfd, then re-prove identity and immediate non-exit. Accounted drained acquisition registers one loop reader. Unsupported/failed acquisition logs unknown and leaves unarmed; cancellation/finally close unused handles. Exit closes before invalidating via the supplied pacer callback; close releases reader/fd. There is no polling loop or task-completion authority.

## Evidence

- Own one native host-exit subscription feeding the existing projection change pacer. [1]
