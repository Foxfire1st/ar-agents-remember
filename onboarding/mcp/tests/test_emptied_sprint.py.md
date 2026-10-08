# mcp/tests/test_emptied_sprint.py

## Governing Overview

[tests overview](overview.md)

## Purpose

A sprint that lost its last master to a retirement stays a sprint, for every tool: the altitude, the role check, the scheduling mode, the topology validation, the closeout queue, the linkage report, `task_doc get` and the dashboard's queue listing. No answer names a next action that cannot work, and a master can be attached to it again.

## Code Commentary

`_read_as_a_sprint` reads the emptied sprint through every listed tool and `_task_doc` drives operations; `test_a_sprint_that_lost_its_last_master_is_read_as_a_sprint_by_every_tool` and `test_an_emptied_sprint_is_edited_and_commands_a_master_again` carry the rule.

## Evidence

- A sprint that lost its last master to a retirement is read as a sprint by every tool, with no next action that cannot work. [1]
- An emptied sprint can be edited and commands a master again. [2]
