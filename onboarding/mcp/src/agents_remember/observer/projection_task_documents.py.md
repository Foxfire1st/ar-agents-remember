# mcp/src/agents_remember/observer/projection_task_documents.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Define the closed served task-document, series, graph and closeout reader DTOs without acquiring files or authoring task/lifecycle truth.

## Code Commentary

Task content nodes preserve steps/substeps, intentional-skip disposition, note/outcome previews and truncation flags; review whole-round counts are independent of a bounded findings preview. Decisions carry the product_record classification rather than changing the stored decision shape. The facade reexports these definitions; consumers need not move their public import path.

TaskDocNode adds optional nonGoals, acceptance, completedAt, waitsFor and both resolved dependency directions. TaskDependencyNode retains an optional docPath for gone/unaddressable facts. These DTOs do not validate same-master membership or derive order. Raw execution graph/waves remain sprint fields; the shared render-ready view is also supplied for ordinary-master Order by its producer. Legacy bare graph references are explicitly lifted.

Optional/defaulted fields keep omitted older reader content distinguishable from present collections. Direct grants are projected evidence, not authored TaskDocument fields. Folder-keyed SeriesNode remains separate from concrete task identity; its declared completed/abandoned count meanings do not turn leaf steps into master completion. Extra fields are forbidden by the DTOs, not silently made into new wire authority.

## Evidence

- Extracted closed reader DTOs retain preview/count, legacy-reference, dependency and grant boundaries without semantic derivation. [1]
