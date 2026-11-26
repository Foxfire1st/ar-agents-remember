# mcp/src/agents_remember/cli/role_handover_projection.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Defines the hand-over projection a first message carries — which fields, in what order, and what the rest of the object is left to — and measures it, so the field list and its budget have one home.

## Code Commentary

`PROJECTION_FIELDS`, `WORKSPACE_FIELDS`, `AR_MCP_CONTEXT_FIELDS`, and `HOST_FIELDS` are the single definitions of the projected top-level and nested fields; tests derive from them and never repeat them, so a field change in code is seen by every check. `project_handover(..., omit_handover_file_field=True)` builds the deduplicated inline wire view while leaving `.handover.json` complete on disk: it drops absent or `null` keys (including `null` keys inside `selection`), flattens the bound `documents[0]` entry to `{id, kind, repo_id, task_name, slug, renderedReadPath, jsonPath, contentDigest}` (adding `taskDocumentRef` only when it differs from `selection.taskDocumentRef`), projects `taskDocumentFiles` with only non-default fields (`extraCopies`, non-empty `missingCopies`, non-default `paths` or `state`, omitting the section when empty), subsets `workspace` to `WORKSPACE_FIELDS` (`path`, `codeRoot`, `memoryRoot`, `scratchRoot`, `outsideScratchRoot`, `contractPath`), collapses identical `arMcpContext.readerArguments` for `context_packet` and `read_ar_files` into `{"readerArguments": {"shared": <args>}}`, projects `host` (`parent` with selection-identical refs omitted from `parent` and `parent.returnAddress`, plus `developerQuestionRoute`), projects `leafSeats` to `{"roles": [...]}` alone, and omits inline `handoverFile` by default because the trailing `AR handover artifacts:` line carries its path and SHA-256. `FILE_ONLY_FIELDS` (including `assignment` and `canonicalTaskReportPath`) and `FILE_ONLY_NESTED` (including `host.ownerRelation`, `host.developerQuestions`, `documents[0].canonicalTaskPath`, `documents[0].taskDocReadArgs`, `documents[0].documentIdentity`, `workspace.taskReportRoot`, `workspace.taskReportAccessRoot`, and `leafSeats.roleMessageArguments`) name the fields kept exclusively in `.handover.json`. `projection_text` renders the compact JSON exactly as the message carries it, `first_read_paragraph(first_read, *, rendered_read_path=None)` replaces a repeated `rendered_read_path` lead with `documents[0].renderedReadPath` and points readers to the complete JSON named on the trailing `AR handover artifacts:` line, and `projection_tokens` counts with the vendored vocabulary. The module writes nothing: it publishes no hand-over file and keeps no state, and its one reach outward is the token count's own vocabulary lookup through the packaged cache.

## Evidence

- The projection is counted with the vendored vocabulary as it stands in the message. [4]

- `PROJECTION_FIELDS`, `WORKSPACE_FIELDS`, `HOST_FIELDS`, `FILE_ONLY_FIELDS`, and `FILE_ONLY_NESTED` define the slim deduplicated wire projection and list all fields kept exclusively in `.handover.json` (including `leafSeats.roleMessageArguments`, `workspace.taskReportRoot`, `workspace.taskReportAccessRoot`, and `documents[0]` duplicates). [1]
- `project_handover` omits `handoverFile` by default, flattens `documents[0]`, emits only non-default `taskDocumentFiles`, collapses identical `readerArguments` to `shared`, deduplicates `host.parent` refs against `selection`, and projects `leafSeats` to `roles` only. [2]
- `first_read_paragraph` compacts a repeated `renderedReadPath` lead to `documents[0].renderedReadPath`, states `Each contentDigest is launch snapshot; turn != acceptance.`, and directs readers to the full JSON on the trailing `AR handover artifacts:` line (`1 field/step`). [3]
