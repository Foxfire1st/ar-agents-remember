# skills/l-01-agent-lifecycles/reference/tasks/document-authoring.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The prose conventions and template pointers for authoring a task document or requirement packet that a developer can review on its own, read by Architects and other planning roles.

## Code Commentary

Before introducing another task for the same request, the author compares it with the selected active task and requirement and reuses work that already owns the scope. The plan's problem, outcome, reasons, design and decisions are connected prose that stands without a browser or the planning conversation; the leaf, master and requirement-packet templates guide authoring, while the task schema and tool own the stored structure. The collaboration method precedes the design, the planning operation keeps approval, ownership and scope changes, and a leaf created through `task_doc` records retained-evidence maintenance per `core/acceptance.md`.

Fields carry their own prose through `task_doc`: outcome and reason in `objective`, approach in `design`, exclusions in `nonGoals`, completion in `acceptance`, packets linked in `requirements`; extra narrative goes into `freeform` sections, a master uses `subTasks` and `sharedDecisions`, and no top-level field is copied into a section. Code work shows the planned structure (paths and skeletons with one-line contracts) before code is written; a leaf uses `codeExamples` or explains their absence in `codeExamplesNote`, never both, and a master puts examples or their absence in a `freeform` section. Earlier decisions stay visible with new ones appended, and an approved packet stays at its version-addressed path when superseded, with the requirement-change rule of `core/loop.md` governing promise changes.

The Architect, Manager and Worker roles point here before authoring or editing task documents, and the Orchestrator links the decision section before `append_decision`; the leaf, master and requirement-packet templates link the field and proposed-change sections.

## Evidence

- Reuse the owning work, explain the plan as prose, and use the templates, the collaboration method and the planning operation. [1]
- Task fields carry their own prose, with `freeform` sections for further narrative. [2]
- Code work shows structure and skeletons first, with leaf and master example rules. [3]
- Decisions are appended and superseded packets keep their version-addressed path. [4]
- The Architect role points here before authoring a task document or requirement packet. [5]
