# mcp/src/agents_remember/cli/role_handover_projection.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Defines the hand-over projection a first message carries — which fields, in what order, and what the rest of the object is left to — and measures it, so the field list and its budget have one home.

## Code Commentary

`PROJECTION_FIELDS`, `WORKSPACE_FIELDS`, `AR_MCP_CONTEXT_FIELDS`, and `HOST_FIELDS` are the single definitions of the projected top-level and nested fields; tests derive from them and never repeat them, so a field change in code is seen by every check. `project_handover` drops any field the object does not carry or carries as `null`, projects the bound task document alone out of `documents`, and keeps only the workspace, reader, host, and seat parts the role needs before its first tool call: `workspace` carries `WORKSPACE_FIELDS` (including `outsideScratchRoot` immediately after `scratchRoot`), and `host` carries only `HOST_FIELDS = ("parent", "developerQuestionRoute")`. `FILE_ONLY_FIELDS` (including `assignment` and `canonicalTaskReportPath`) and `FILE_ONLY_NESTED` (including `host.ownerRelation` and `host.developerQuestions`) name the prose and duplicate fields kept exclusively in `.handover.json` so checks verify they stay out of the wire projection. `projection_text` renders the compact JSON exactly as the message carries it, `first_read_paragraph` carries the unique task-doc instructions in `## Launch Context` and explicitly names `assignment`, `host.ownerRelation`, and `host.developerQuestions` as available in `handoverFile`, and `projection_tokens` counts with the vendored vocabulary. The module writes nothing: it publishes no hand-over file and keeps no state, and its one reach outward is the token count's own vocabulary lookup through the packaged cache.

## Evidence


- The projection is counted with the vendored vocabulary as it stands in the message. [4]


- `PROJECTION_FIELDS`, `HOST_FIELDS`, `FILE_ONLY_FIELDS`, and `FILE_ONLY_NESTED` define the slim wire projection (`host.parent`, `host.developerQuestionRoute`) and keep `assignment`, `canonicalTaskReportPath`, `host.ownerRelation`, and `host.developerQuestions` exclusively in `.handover.json`. [1]
- `project_handover` subsets top-level, workspace, reader, host, and seat fields, dropping absent and `null` values and naming `handoverFile`. [2]
- `first_read_paragraph` carries the unique first-read rules and names `assignment`, `host.ownerRelation`, and `host.developerQuestions` as living in `handoverFile`. [3]
