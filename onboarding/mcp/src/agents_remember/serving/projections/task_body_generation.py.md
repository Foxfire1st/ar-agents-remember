# mcp/src/agents_remember/serving/projections/task_body_generation.py

[governing overview](overview.md)

## Purpose

Capture native input generations for a task body and recheck them before cache reuse/304.

## Commentary

Capture lstat/target identities: missing is (), unreadable None. Context-local capture restores prior binding in finally; it is not rollback. body_input records before/after and inconsistent rereads. current rejects unreadable/inconsistent/changed dependencies, enabling cache validation but not an atomic filesystem snapshot, whole-corpus currentness or permission cache.

## Evidence

- Capture native input generations for a task body and recheck them before cache reuse/304. [1]
