# mcp/src/agents_remember/models/task_doc.py

## Governing Overview

[models/overview.md](overview.md)

## Purpose

The STRICT response model for the `task_doc` tool: it echoes the document's identity,
progress, dry-run preview, and optional master-row sync outcome after an operation.
L11 adds `TaskReopenResponse` here — the task-domain home for the `task_reopen`
envelope; it subclasses `WorktreeCommandResponse` because the payload legitimately
carries the enclosure contract state.

## Code Commentary

### Logic

`TaskDocResponse` extends `ToolResponse` (so it inherits `ok`/`operation`/token
metadata and `extra="forbid"`) and adds `taskId`, `slug`, `kind`, `status`, optional
`lifecycleId`, `docPath`, `renderedPath`, and `stepsDone`/`stepsTotal`. The R5 **dry-run**
fields — `dryRun`, `rendered`, `diff`, `wouldLose` — are additive optional defaults, set only on a
`dry_run=true` preview (a real op leaves them at their defaults, so its response is unchanged).
`TaskDocMasterSync` is the optional nested leaf-to-master result: status, master doc path,
rendered path, subtask number, and preview-only rendered/diff/wouldLose fields. It is omitted when a
write has no same-root master impact. The **`remove_subtask` outcome** fields — `removedSubtask`
(the dropped row number), `deletedFiles` (the real op: the leaf json+md paths unlinked, or `[]` under
`keep_file`), and `wouldDeleteFiles` (the dry-run preview) — are additive optional defaults declared
so the destructive success VALIDATES against `extra="forbid"` (260703-L18 finding 1, closing friction
F-N): the application entry point emits them, and without the declaration the envelope rejected the payload,
surfacing a tool error after the removal already happened (a caller could retry an already-done op).
Every non-`remove_subtask` operation leaves them `None` (excluded by `exclude_none`). It is the
registered model for the `task_doc` row in `PUBLIC_TOOL_RESPONSE_MODELS`. The
persisted task document itself (`tasks.TaskDocument`) is deliberately not returned.

`read_steps` has the same defect class once more, and its declaration is the fix. The operation had
always emitted a focused checklist payload (`result["steps"] = task_doc_steps.step_payloads(doc.steps)`
in `application/task_docs/task_doc_tools.py`) while `TaskDocResponse` never declared `steps`, so under
`extra="forbid"` the payload was **rejected after a successful read**: `steps: Extra inputs are not
permitted`. The model now declares `steps: list[TaskDocStepRead] | None` plus the two shapes the
handler actually emits — `TaskDocStepRead` (`id`, `title`, `status`, `note`, `substeps`) and
`TaskDocSubStepRead` (`id`, `title`, `status`, `note`) — so the operation is usable on every
document. The handler was not changed: the model declares the field the handler always produced.
`steps` is present only on `read_steps`; every other operation leaves it `None` (excluded by
`exclude_none`), and the declaration is a **narrowing, not a relaxation** — an undeclared key still
fails validation, which is what keeps the envelope strict rather than merely permissive.

Since the master full-gate repair (260815-DAG, commit e5cb139f) `TaskDocResponse` also declares the
**special-op wire fields** for the sprint-linkage and execution-graph authoring surfaces
(`attach_master`, `detach_master`, `retire_master`, `linkage_report`, `author_execution_graph`): `subtaskNumber`,
`state`, `sprintTaskDocumentRef`, `masterRef`, `graphNode`, `executionNatureAsserted`, `documents`,
`removedOrchestrates`, `removedGraphNodes`, `masterResolved`, `linkageFacts`, `bootstrapped`,
`retirementRow`, `retirementProof`, `retirementResumed`, `removedEdges`, `taskArchive` (the `retire_master` answer:
the plain row kept on a sprint, the proof of a master retired on its own, whether the call resumed a recorded
retirement, the edges removed, and the archive state with the hook report),
`appliedMutations`, `executionWaves`, `leafPlacementFacts`, `numberingHints`. These ops publish
inside their own functions and return raw operation payloads; without the declaration the
`extra="forbid"` envelope REJECTED the real payloads after their writes — exactly the
`remove_subtask` bug class. They are present only on those ops; every other operation leaves them
`None` (excluded by `exclude_none`). The application entry point now merges the standard
`task_doc` identity in via `_sprint_doc_identity` in `application/task_docs/task_doc_tools.py`.

### Invariants And Boundaries

- STRICT AR-owned shape (`extra="forbid"`); register STRICT, not flexible.
- `lifecycleId` is optional-null so it survives `exclude_none=True` when absent.
- `masterSync` is optional because light docs, master docs, cross-series refs, and unchanged parent rows
  should not grow response data unnecessarily.
- Every special-op wire field is optional and op-scoped: a real special op validates against the
  declared shape, and every other operation stays byte-unchanged.
- `steps` is op-scoped to `read_steps` for the same reason, and its declaration is a narrowing:
  the response model must declare every key the handler emits, but it must not be relaxed to
  `extra="allow"` to make a mismatch disappear.

## Evidence

### Repo-Internal References

- The registry row that maps `task_doc` to this model. [1]
- The strict `ToolResponse` envelope base. [2]
- The persisted task-document model this response describes (not returns), whose class body now ends at its integration-branch normaliser. [3]
- The application entry point builds the optional `masterSync` payload for real and dry-run leaf writes. [4]

- The special-op identity merge that pairs with the declared wire fields. [5]

- The response model declares optional retirement record, state, readiness, preview and archive-result fields for retire_master. [6]

## 260815-DAG Master Full-Gate Repair

`TaskDocResponse` gained the ~16 optional special-op wire fields so the sprint-linkage and
execution-graph authoring results validate against the strict `extra="forbid"` envelope after their
writes (the same defect class as the L18 `remove_subtask` fix), and the application entry point
merges the standard task-doc identity into those raw operation payloads via
`_sprint_doc_identity` (mcp/src/agents_remember/application/task_docs/task_doc_tools.py:424-446). The former wire-shape suite
was retired; these model and application owners remain the current contract authority.

## 260821-CLIVE Discard And Projection-Effect Response Models

`TaskDocResponse` now carries bounded `projectionEffects` for every accepted task mutation. Its
discard-unstarted branch distinguishes preview, applied, already-discarded, started refusal, and
ambiguous refusal; it returns the typed parent audit, exact source-state proof, centralized
unstarted-evidence fingerprint/facts, deleted-or-would-delete paths, and executable next action.
Planning discard is therefore observable without treating queue state as task history or silently
turning a started leaf into completion.

## 260918-TSIP-L4 — `steps` Declared (`T7`)

`TaskDocResponse` now declares `steps: list[dict[str, Any]] | None = None` (**`:134`**),
which moved every line at or below the old `:127` down by `+8` (file **196 → 204 lines**;
`stepsTotal`, previously `:126`, now follows the declaration at `:135`).

`_read_steps` sets `result["steps"]` from `task_doc_steps.step_payloads`
(`application/task_docs/task_doc_tools.py:420`), so the payload was produced on every
`operation="read_steps"` call and then **rejected by this envelope's `extra=forbid`** — the one
operation the tool publishes as *the* way to read a checklist could never return it. The
declaration is present only on `read_steps`; every other operation leaves it `None` and
`exclude_none` keeps it off the wire. Same class as `removedSubtask` above and `documents`
below it in this class. Pinned by
`mcp/tests/test_tool_response_conformance.py::test_task_doc_read_steps_validates_and_returns_the_checklist`.
