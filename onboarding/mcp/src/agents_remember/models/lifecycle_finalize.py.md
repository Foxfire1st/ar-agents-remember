# mcp/src/agents_remember/models/lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/lifecycle_finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines the strict public response contract for `lifecycle_finalize_task`.

## Code Commentary

`LifecycleFinalizeTaskResponse` inherits from `ToolResponse`, so it uses the
strict Agents Remember response-envelope convention. It declares the finalizer
operation name plus identity fields (`taskId`, `taskName`, `lifecycleId`), the
current finalizer `state`, `dryRun`, contract path, optional landed commit and
target branch, blocker list, cleanup detail, task-update detail, and summary.

The model intentionally does not accept the full `worktree_status` payload. The
finalizer response is a separate terminal contract: it reports only the edge
proof, cleanup result, task-document reconciliation, and blockers relevant to
finalization.

**260707-HFX2-L11** replaces the former completion-edge retirement field with
`autoLandedSeats: list[str] = Field(default_factory=list)` — the session ids marked `landed` at this
master→super finalize completion edge (config-gated via
`config.retirement.auto_land_on_finalize`, default ON, `mcp/config.py`). Empty when the gate is
off, when nothing matched the finalizing master's own qualified leaf key
(`repo/master/master-doc-id`), or when the call was a dry run. The
landing sweep is best-effort and never fails this finalize call itself — any failure in the landing
body (contract load or catalog I/O) is swallowed and reported as an empty list
(`application/worktree_tools.py::_auto_land_completed_seats`), so this field can legitimately be
empty even when spent seats existed, never a signal that finalization itself failed.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict tool response base class is defined here. | "class StrictResponseModel" | mcp/src/agents_remember/models/base.py:10-10 |
| Public response registry maps `lifecycle_finalize_task` to this model. | `lifecycle_finalize_task` | mcp/src/agents_remember/models/tool_registry.py:168-168 |
| Conformance tests validate representative finalizer payloads against this model. | `ToolResponseConformanceTests` | mcp/tests/test_tool_response_conformance.py:538-616 |
| `lifecycle_finalize_task_tool` populates `autoLandedSeats` from `_auto_land_completed_seats`, gated by `config.retirement.auto_land_on_finalize`. | "def worktree_start_tool" | mcp/src/agents_remember/application/worktree_tools.py:83-83 |
| `RetirementSettings.auto_land_on_finalize` is the config gate this field's population depends on. | "class McpRuntimeConfig" | mcp/src/agents_remember/mcp/config.py:114-114 |

## Series-Contract Notes

`LifecycleFinalizeTaskResponse` carries both the leaf `enclosurePath` and the root-level `taskArchive` result so finalization can report contract cleanup and root archival separately.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-08-02T01:05+02:00 — No content impact: repaired this document's `Repo-Internal References` table shape. Rows carrying a citation cell were rendering short: the header declared two columns while those rows held three, and GFM TRUNCATES the extra cell, so the citation was in the source but invisible in the rendered table (`memory_quality/style/document_shape/tables.py`, `table_row_cell_count_mismatch`). Widened the header and its delimiter row to `| Finding | Citations | Source Path |` — the shape 1,941 rows in this tree already use — and padded the two-cell rows with `n/a`, which is this tree's own no-citation value (489 uses; zero empty citation cells exist). No finding text and no citation was changed by the widening. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: finalizer response onboarding now
  names `autoLandedSeats` and the `auto_land_on_finalize` gate; completion-edge cleanup marks seats
  `landed` for archive inspection rather than retiring them. Verification metadata pinned until
  closeout stamps the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state):
  added `autoRetiredSeats: list[str]` (default empty) — session ids auto-retired at the
  master→super finalize edge, config-gated (`auto_retire_on_finalize`, default ON), best-effort and
  never a signal of finalize failure. Verification metadata pinned until closeout stamps the HFX-L8
  commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: finalization responses now expose `enclosurePath` and `taskArchive` so callers can report the leaf contract path and root-task archive action. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Created the strict `LifecycleFinalizeTaskResponse` model for the lifecycle finalizer tool. Verification metadata is pending until closeout stamps the source commit.
