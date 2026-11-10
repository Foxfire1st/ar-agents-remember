# skills/l-01-agent-lifecycles/templates/leaf-task.md

## Governing Overview

[overview](../overview.md)

## Purpose

The scaffold planning roles use to author one leaf task through `task_doc`.

## Code Commentary

The Markdown is an authoring example, not another stored task document; field meanings come from `reference/tasks/document-authoring.md#put-prose-in-the-fields-that-render-it`. Sections are Objective, Non-goals, Requirements (approved stable identifier and version with the exact packet path, naming the implemented promise and the adjacent constraints), Design, Acceptance, Implementation Steps (one heading per step identifier and reviewable outcome; progress lives in step records), Proposed Code Examples (placement paths and body-less skeleton contracts, after reading `#show-the-proposed-changes`), Decision Log, Open Questions and References. The Architect role and core invariants point to it before a leaf is authored; small code work uses it.

## Evidence

- The scaffold is an authoring example for `task_doc` fields, not a stored task document. [1]
- Requirements name the approved identifier, version and packet path, and the promise this leaf implements. [2]
- Implementation steps are reviewable outcomes; proposed code examples give placement and body-less skeletons. [3]
- The Architect reads the leaf template before authoring a leaf. [4]
