# mcp/src/agents_remember/tasks/sprint_rows.py

## Governing Overview

[tasks overview](overview.md)

## Purpose

How a master and the sprint that commands it find each other, and which sprint row is the master's. A sprint commands a master through `orchestrates`; its row for that master is either typed (`masterRef`) or, on sprints older than typed linkage, a seat row whose `file` is the seat document that names the master. A sprint may also hold no row for a commanded master.

## Code Commentary

`master_rows` correlates the master's row from the sprint's rows (`correlate_seat_row`, `MasterRows`) and reports the shape as a fact. `sprint_census` walks the repository's task tree for the sprints that command a master (`SprintCensus`, `_closed_task_folders`). `_raw_membership` parses `orchestrates`/`subTasks` and classifies a list field that is not a list as unreadable, so retirement fails closed and names the file; `membership_removal_action` names the edit that works on the sprint that took the master.

## Evidence

- A task.json whose orchestrates or subTasks is not a list is unreadable, so retirement fails closed and names the file. [1]
- The linkage report states a typed row, a correlated legacy seat row, and a commanded master with no row as facts. [2]
- A refusal on the retire and finalize routes names task_doc.detach_master only where a typed row links the master to the sprint. [3]
