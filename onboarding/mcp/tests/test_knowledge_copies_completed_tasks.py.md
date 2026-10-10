# mcp/tests/test_knowledge_copies_completed_tasks.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Copies under the notes of a finished task are deleted; an open task's are not.

## Code Commentary

MIK-R82 rule 2: the copies command gains one rule over MIK-R26 rule 6. Review refs and retained-code refs of a completed task stay until its archive; comparison snapshots release through their generation owner.

## Evidence

- The completed-task copies rule deletes finished-task copies and keeps open-task copies. [1]
