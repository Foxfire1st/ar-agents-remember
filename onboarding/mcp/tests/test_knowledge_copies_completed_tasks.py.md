# mcp/tests/test_knowledge_copies_completed_tasks.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Copies under the notes of a finished task are deleted; an open task's are not.

## Code Commentary

MIK-R82 rule 2: the copies command gains one rule over MIK-R26 rule 6. The legacy-copy fixture is built under a working SQLite filename, copied to the retired-name target, then stripped of derived `ix_*` tables so it represents a logical leftover rather than the current derived index. This construction respects the retired-name write guard; it is not a disabled-memory fixture or a return to canonical database storage. Review refs and retained-code refs of a completed task stay until its archive; comparison snapshots release through their generation owner.

## Evidence


- The completed-task copies rule deletes finished-task copies and keeps open-task copies. [1]


- Legacy-copy fixtures build under a working filename and remove derived index tables. [2]
