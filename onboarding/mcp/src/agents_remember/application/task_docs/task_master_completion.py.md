# mcp/src/agents_remember/application/task_docs/task_master_completion.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

Completing an organizational master through the task tool. An atomic master's completion is proved by its closeout, which walks the landing chain; an organizational master has no closeout, so the edit that sets its status to `Completed` is the place where completion is decided. The rule that a label never removes a landed leaf is kept here, and the one contradiction of an abandoned row that records a completed integration is refused by name.

## Code Commentary

`require_master_completion` runs before a status edit completes an organizational master. It refuses a task that is executed organizationally (`_executes_organizationally`) when an abandoned row's enclosure records a completed integration, naming the row; an abandoned row without a landing blocks nothing and is asked for no enclosure. A row in any other unfinished state is refused by the ordinary completion blockers, not here.

## Evidence

- An organizational master's completion refuses an abandoned row whose enclosure records a completed integration and names the row. [1]
- Completion of an organizational master is decided at the status edit; an atomic master's is proved by its closeout. [2]
- An abandoned row without a completed landing blocks nothing and needs no enclosure. [3]
