# mcp/src/agents_remember/application/knowledge_consolidation_proposal/view.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Implements the `knowledge_read` `consolidation_proposal` view: validates selector mutual exclusion, loads the selected tree's index and history facts, writes the unbounded caller-readable JSON report, and returns a token-bounded summary response.

## Code Commentary

`proposal_view` refuses selections without a converted `memory_tree` (`snapshot_unavailable`), loads `ProposalStore` via `_store_of` (wrapping `IndexMismatchError` and `apsw.Error` as `snapshot_unavailable`), computes `(proposal, master)` via `_proposal`, and persists the complete report before constructing the bounded answer. `_proposal` enforces at most one selector among `masterId`, `recordId`, and `sourcePath` (`bad_selector`), refuses unknown/retired `recordId` (`selector_absent`), normalizes `sourcePath` by stripping whitespace, leading `./`, and slashes, and falls back to `oldest_first` with `first_written` and `last_consolidations` when no subject is named. Answer bounding applies three caps: `rows` starts at `min(max(1, request.limit), TOOL_ANSWER_LIST_MAX)`, each row truncates `attachedRules` (and `proposal.rulesInNoFamily`) to `ANSWER_RULES_MAX` (8) and shortens `title` to `ANSWER_TITLE_MAX_CHARS` (80, suffixed with `…`), and `_fitted` pops trailing rows until `count_response_tokens(answer) <= bound_for("knowledge_read") - _BOUNDARY_RESERVE`, keeping `counts.rowsReturned` and `readOn.familiesRemaining` synchronized. `_write_report` writes the full, unshortened family and rule lists via `knowledge_reports.write_report("knowledge-consolidation-proposal", ...)` and raises `ProposalRefusal("report-unwritable", ...)` on `ReportWriteError` (noting when no partial file remained).

## Relationships

Re-exported by package `__init__.py` and invoked by `mcp/tools/knowledge_views/record_views.py` (with `PROPOSAL_VIEW` registered in `mcp/tools/knowledge.py`). Orchestrates `.store`, `.history_facts`, `.first_written`, `.proposal`, `.refusal`, `application.knowledge_reports`, `memory.knowledge_index.query`, and `models.tools.tool_answer`.

## Evidence

- `proposal_view` checks for a converted `memory_tree`, builds the store and proposal, writes the full report, caps rows to `TOOL_ANSWER_LIST_MAX`, and fits the answer to the token budget. [1]
- `_proposal` refuses multiple selectors (`bad_selector`) or an absent live family (`selector_absent`), dispatches `masterId`/`recordId`/`sourcePath`, and defaults to `oldest_first`. [2]
- `_fitted` drops trailing rows while `count_response_tokens(answer)` exceeds `bound_for("knowledge_read") - _BOUNDARY_RESERVE`, updating `rowsReturned` and `familiesRemaining`. [3]
- `_write_report` writes the full unshortened proposal payload via `write_report(REPORT_STEM, ...)` and translates `ReportWriteError` into `ProposalRefusal("report-unwritable", ...)`. [4]
