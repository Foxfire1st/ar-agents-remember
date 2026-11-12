# skills/l-01-agent-lifecycles/templates/master-task.md

## Governing Overview

[overview](../overview.md)

## Purpose

The scaffold planning roles use for a master task's shared outcome and reasoning.

## Code Commentary

Field and section meanings come from `reference/tasks/document-authoring.md#put-prose-in-the-fields-that-render-it`. Sections are Objective, Non-goals, Requirements (approved identifiers, versions and packet paths, relating the promises without restating them), Design (the shared approach and why its division into leaves is coherent; leaf reasoning stays in the leaf), Acceptance (including evidence at the seams between leaves), Sub-tasks as an ordered `subTasks` section for the generated child list, Shared Decisions as a `sharedDecisions` section, and Open Questions and References as `freeform` sections.

## Evidence

- Masters are authored through `task_doc` fields and ordered sections. [1]
- Sub-tasks and Shared Decisions use the `subTasks` and `sharedDecisions` section kinds; Open Questions and References are freeform. [2]
- The Architect reads the master template before authoring a master. [3]
