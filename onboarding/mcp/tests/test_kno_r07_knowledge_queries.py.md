# mcp/tests/test_kno_r07_knowledge_queries.py

## Governing Overview

[tests](overview.md)

## Purpose

Focused unit test suite proving KNO-R07 rules 8–10 and Attempt 2 regressions: deterministic SQLite FTS5 `ix_fts` (`ar-knowledge-index/v8`), `knowledge_read` `impact`/`search`/`records` views, compact `dependent` projection, verbatim multi-symbol preservation in `records`, and complete multi-page `familySiblings` enumeration in `impact`.

## Code Commentary

- Verifies `INDEX_FORMAT == "ar-knowledge-index/v8"`, deterministic identical `search_fts` outputs across independent caches, exclusion of retired invariants, closed weaknesses, and default decisions, phrase matching, and `invalid-input` refusal for `kinds=("history",)`.
- Verifies `view="impact"` deduplication, family guarantees, one-line `familySiblings`, 80-word trimming, weaknesses/dependents, compact mode, and `<= 3500`-token bound; verifies `view="search"` `<= 3500`-token bound.
- Verifies `view="records"` verbatim non-trimmed statements, inline `staleAnchors`, missing IDs, `> 25`-ID refusal, `bound_for("knowledge_read") == 5000`, and `view="dependent"` with `compact=True` (`<= 1500` tokens, zero 40-char blob hashes, zero `movingCommitUnknown`).
- Verifies 15-ID `records` pagination preserves every `realizedIn` and 4-symbol `proofs` locator verbatim without `(+N)` collapse, and 30-member family `impact` paginates all 29 out-of-scope `familySiblings` across 2 pages as plain lists without truncation.

## Relationships

- Tests `memory/knowledge_index/fts.py`, `application/knowledge_impact.py`, `application/knowledge_search.py`, `application/knowledge_reader/{records_batch,marks_compact}.py`, `application/knowledge_queries.py`, and `mcp/tools/knowledge.py`.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit` lane) and `mcp/tests/evidence-lifecycle.toml`; sibling of `mcp/tests/test_kno_r07_briefs_and_pairing.py`.

## Evidence

- Verifies `INDEX_FORMAT == "ar-knowledge-index/v8"` deterministic FTS5 ranking and exclusion of retired, closed, and history records. [1]
- Verifies `impact` and `search` views within 3,500-token bound, family siblings, 80-word trimming, and `history` refusal. [2]
- Verifies `records` (verbatim statements, inline `staleAnchors`, 25-ID cap, 5,000-token bound) and compact `dependent` rows. [3]
- Verifies 15-ID `records` pagination preserves every `realizedIn` and 4-symbol `proofs` locator verbatim without collapse. [4]
- Verifies 30-member family `impact` enumerates all 29 out-of-scope `familySiblings` across 2 pages without truncation. [5]
