# mcp/tests/test_task_page_skeleton_projection.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin task-document form, bounded display fields, review aggregates and full-body recovery at the real projection producer.

## Code Commentary

Tests validate and write real TaskDocument inputs, then call summary and body producers. They distinguish sprint/master/task forms, status/header/step fields and absent review state; newly displayed-field mutations change bodyRevision. Two collection sizes preserve full totals while bounding preview arrays/text. The on-demand body restores whole strings and clears tested truncation flags. Temporary coordination fixtures do not establish dashboard browser behavior.

The RF01 legacy-completion case writes a Completed leaf and compares both summary and on-demand body completedAt over five subcases: newest-first and oldest-first finalization arrays both choose the newer timestamp; an invalid finalization timestamp between valid records is ignored; an invalid-only finalization array yields None; and a stored explicit completedAt takes precedence. Each fixture appends a still-newer ordinary Authored decision that must not count as finalization, and compares task.json bytes after both reads. This pins latest valid exact-finalization selection instead of last-array-position selection. It does not test timezone-equivalent or naive timestamps, tied instants, all document kinds or browser sorting, and it is a source assertion account, not a test run.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module declares form/bounded-summary/whole-body assertions and RF01 completion-time subcases for array order, invalid records, non-finalization exclusion, explicit precedence and unchanged task JSON. These are fixture-scoped source assertions, not execution or browser acceptance. [1]
