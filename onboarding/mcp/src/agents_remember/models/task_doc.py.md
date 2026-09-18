# mcp/src/agents_remember/models/task_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/task_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview      | `overview.md`                              |

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
(`attach_master`, `detach_master`, `linkage_report`, `author_execution_graph`): `subtaskNumber`,
`state`, `sprintTaskDocumentRef`, `masterRef`, `graphNode`, `executionNatureAsserted`, `documents`,
`removedOrchestrates`, `removedGraphNodes`, `masterResolved`, `linkageFacts`, `bootstrapped`,
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry row that maps `task_doc` to this model. | `task_reopen` | mcp/src/agents_remember/models/tools/tool_registry.py:210-210 |
| The strict `ToolResponse` envelope base. | `ToolResponse` | mcp/src/agents_remember/models/base.py:91-94 |
| The persisted task document this response describes (not returns). | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:642-816 |
| The application entry point builds the optional `masterSync` payload for real and dry-run leaf writes. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:218-278 |
| The special-op identity merge that pairs with the declared wire fields. | `_sprint_doc_identity` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:424-446 |

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

## Update History
- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **corrected the Logic section, which said the `task_doc` response model was complete for every operation it serves.** The change set declares the `read_steps` payload the handler always emitted and the model never declared — `steps: list[TaskDocStepRead] | None` plus the `TaskDocStepRead` / `TaskDocSubStepRead` shapes — because under `extra="forbid"` the real payload was rejected *after* a successful read (`steps: Extra inputs are not permitted`), making the operation unusable on every document. This is the third instance of the class the card already records twice (`remove_subtask`, then the sprint-linkage and execution-graph fields), so the new paragraph names it as such rather than as a new topic. Added the op-scoped invariant, including the point that the declaration **narrows** (`extra="allow"` would have "fixed" the symptom by removing the strictness). The append is additive — `TaskDocResponse` moved from `115` to `138` and `TaskReopenResponse` now ends the file at `223-226` — so no other claim in this card was affected. Repairing the two ranges the new declaration did **not** cause: the `_sprint_doc_identity` merge is cited in the body prose below as `396-418` while the function spans `424-446` (the table row already carried `424-446`), and the `task_doc_tool` row cited `191-284` while the entry point spans `218-278`; both were re-read at their current position and re-pointed. Every other existing table row was left untouched for the citation pass.
- 2026-09-18T13:36:47+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:203-203. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `_sprint_doc_identity` repointed to mcp/src/agents_remember/application/task_docs/task_doc_tools.py:424-446. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:44:56+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:192-192. No content impact: mechanical anchor-range projection bound to citation source snapshot fc36bf81fd36002f552f72a34a44e9713fa47fc86ced6632de3215e5011793d3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `TaskDocument` repointed to mcp/src/agents_remember/tasks/document.py:642-816. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `task_reopen` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-anchored the unchanged persisted
  `TaskDocument` model dependency. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; task-doc response and discard evidence shapes are unchanged.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged typed discard-unstarted evidence/audit and projection effects into the response model card. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: `TaskDocResponse` declared the
  optional special-op wire fields (sprint-linkage + execution-graph authoring results) so they
  validate against `extra="forbid"` after their writes, pairing with the `_sprint_doc_identity`
  merge in `application/task_docs/task_doc_tools.py`. Verified at code commit e5cb139f.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T04:52+02:00 — 260815-DAG-L14 curator: re-read the `TaskDocument` claim — the
  persisted model gained sprint `seats` and typed `masterRef` rows; wording retained, citation
  regenerated to the current class lines, stamp advanced to code commit 2f494982.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-03T02:58:43+02:00 — W3-B05 curator: resolved 3 Tier-2 table findings with exact source paths; fixer generated all final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 1 / friction F-N): declared the
  `remove_subtask` outcome fields `removedSubtask` / `deletedFiles` / `wouldDeleteFiles` on
  `TaskDocResponse` so the destructive success validates against `extra="forbid"` — no more false
  tool error after a real removal. Regression test validates the response on both the delete-with-files
  and `keep_file` paths (and the dry-run preview). Verification metadata pinned until closeout stamps
  the L18 commit.
- 2026-07-03T00:30+02:00 — L11 adds `TaskReopenResponse` (task_reopen envelope; WorktreeCommandResponse shape, task-domain home).
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: added `TaskDocMasterSync` and optional
  `TaskDocResponse.masterSync` so leaf writes can report same-root master-row changes and dry-run master
  previews. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23+02:00 — Slice 3c reopened (R5, dry-run/preview): added the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields (set only on a `dry_run=true` preview; real-op responses unchanged). Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-13T22:34+02:00 — Created for slice 3c commit 1: the `task_doc` STRICT response model. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
