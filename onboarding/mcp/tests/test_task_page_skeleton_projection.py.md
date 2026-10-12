# mcp/tests/test_task_page_skeleton_projection.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin task-document form, bounded display fields, review aggregates and full-body recovery at the real projection producer.

## Code Commentary

Tests validate and write real TaskDocument inputs, then call summary and body producers. They distinguish sprint/master/task forms, status/header/step fields and absent review state; newly displayed-field mutations change bodyRevision. Two collection sizes preserve full totals while bounding preview arrays/text. The on-demand body restores whole strings and clears tested truncation flags. Temporary coordination fixtures do not establish dashboard browser behavior.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
