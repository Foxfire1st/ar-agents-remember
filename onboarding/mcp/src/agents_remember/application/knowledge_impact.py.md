# mcp/src/agents_remember/application/knowledge_impact.py

## Governing Overview

[application](overview.md)

## Purpose

Implements `knowledge_read(view="impact")` to return a deduplicated, family-grouped impact summary for one or more files and/or a folder, including family guarantees, one-line out-of-scope `familySiblings`, open weaknesses, compact standing dependents, and token-bounded pagination.

## Code Commentary

- `impact_view` refuses (`refusalCode="invalid-input"`) when neither `files` nor a non-blank `folder` is supplied, and refuses (`refusalCode="bad_continuation"`) on malformed, mismatched, or out-of-range cursors.
- Deduplicates live invariants across all realizations and proofs in scope (skipping retired invariants), assigns each invariant to one primary live family (recording secondary families in `otherFamilies`), and orders families and rules deterministically by scope overlap, staleness, and ID.
- In non-compact mode, every out-of-scope live family member is emitted as a paginatable `_RuleUnit(is_sibling=True)` formatted as `<id>: <title> [paths]` (up to `_SIBLING_FILE_CAP = 3` files), avoiding inline truncation across large families while keeping each page's `familySiblings` a plain list within `_MAX_ITEMS_PER_PAGE = 20`.
- Paginates inside `DEFAULT_IMPACT_BUDGET_TOKENS = 3150` (staying under the 3,500-token envelope target), reports `counts.totalPages` and a `compact=true` hint on multi-page non-compact views, and attaches open weaknesses and compact dependents on page 0.
- Non-compact mode trims statements at 80 words; `compact=True` emits one line per rule and omits family `guarantee` and `familySiblings`.

## Relationships

- Called by `mcp/src/agents_remember/mcp/tools/knowledge_queries.py` (`ImpactQuery`, `impact_view`); tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Depends on `application/knowledge_query_formatting.py`, `application/file_briefs/titles.py::rule_title`, `application/knowledge_reader/marks.py`, `application/knowledge_reader/marks_compact.py::compact_dependent_rows`, `application/knowledge_reader/paths.py::states_at`, and `application/knowledge_reader/selection.py::ReaderSelection`.

## Evidence

- `impact_view` validates scope and cursor, loads live invariants/families/currentness, and paginates within `DEFAULT_IMPACT_BUDGET_TOKENS` (`3150`). [1]
- `_render_impact_page` separates rule and sibling counts, attaches page-0 weaknesses/dependents, and emits multi-page `compact=true` hints. [2]
- `_build_rule_units` orders families/rules deterministically and appends out-of-scope family siblings as paginatable units. [3]
- `_scope_dependents` gathers file-matched and invariant-standing dependents and projects them via `compact_dependent_rows`. [4]
