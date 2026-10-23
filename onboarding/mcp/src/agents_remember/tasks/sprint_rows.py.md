# mcp/src/agents_remember/tasks/sprint_rows.py

## Governing Overview

[tasks overview](overview.md)

## Purpose

How a master and the sprint that commands it find each other, and which sprint row is the master's. A sprint commands a master through `orchestrates`; its row for that master is either typed (`masterRef`) or, on sprints older than typed linkage, a seat row whose `file` is the seat document that names the master. A sprint may also hold no row for a commanded master.

## Code Commentary

`master_rows` correlates the master's row from the sprint's rows (`correlate_seat_row`, `MasterRows`) and reports the shape as a fact. `sprint_census` reads exactly the direct task documents of the repository task root — `<task root>/<folder>/task.json` — for the sprints that command a master, excludes `0_archive`, `enclosures` and the master's own document, and skips a symlinked task folder; a `task.json` deeper inside a task folder is never read, counted or listed (`SprintCensus`, `_closed_task_folders`). The callers read the direct documents they cannot read differently and on purpose: finalization and the master sync stop only on one whose text names the master, while retirement and sprint archival stop on every unreadable direct document; the archive-skip fact reads only `commanding`. `_raw_membership` parses `orchestrates`/`subTasks` and classifies a list field that is not a list as unreadable, so retirement fails closed and names the file; `membership_removal_action` names the edit that works on the sprint that took the master.

## Evidence

- A direct task document whose orchestrates or subTasks is not a list is unreadable, so retirement fails closed and names the file. [1]
- The linkage report states a typed row, a correlated legacy seat row, and a commanded master with no row as facts. [2]
- A refusal on the retire and finalize routes names task_doc.detach_master only where a typed row links the master to the sprint. [3]
