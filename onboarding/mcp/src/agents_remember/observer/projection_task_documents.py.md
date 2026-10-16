# mcp/src/agents_remember/observer/projection_task_documents.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Define closed task-summary, full task-document, graph and closeout reader DTOs without acquiring files or authoring task/activity truth.

## Code Commentary

Task content nodes preserve steps/substeps, intentional-skip disposition, note/outcome previews and truncation flags; review whole-round counts are independent of a bounded findings preview. Decisions carry the product_record classification rather than changing the stored decision shape. The facade reexports these definitions; consumers need not move their public import path.

`TaskSummary` contains reader content, optional nonGoals/acceptance/completedAt/waitsFor and both dependency directions. `TaskDocNode(TaskSummary)` adds authored identity, status, path, step totals and subTasks for the full on-demand document. `TaskDependencyNode` carries ID/title plus optional qualified `reference` and explicit `gone`; it no longer copies status or docPath. These DTOs do not derive order or validate same-master membership. Raw execution graphs/waves and render-ready graph views retain their producer boundaries; legacy bare references are lifted explicitly.

Optional/defaulted fields distinguish omitted older reader content from present collections. Direct grants are projected evidence, not authored TaskDocument fields or permission. Separate SeriesNode/series-child DTOs and lifecycle links are removed: task membership and activity belong to TaskEntry production. Extra fields remain forbidden rather than becoming new wire authority.

## Evidence

- Extracted closed reader DTOs retain preview/count, legacy-reference, dependency and grant boundaries without semantic derivation. [1]
