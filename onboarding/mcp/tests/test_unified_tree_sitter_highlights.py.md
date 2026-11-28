# mcp/tests/test_unified_tree_sitter_highlights.py

## Governing Overview

[tests/ overview](overview.md)

## Purpose

Unit and live-grammar regression suite proving the unified server-side tree-sitter syntax highlighting pipeline across query composition, capture precedence, UTF-16 offset accuracy, custom local language configuration, cache/size/span ceilings, and all seven code-serving surfaces.

## Code Commentary

Split into two `unittest.TestCase` classes registered in the `unit-regression` lane (`mcp/tests/test-evidence-lanes.toml`) and governed in `mcp/tests/evidence-lifecycle.toml`:
- `HighlightEngineUnitTests` runs without warmed grammars to verify `; inherits:` parsing and cycle protection, catalog-driven `scope.language_for` with `_LANG_BY_EXT` absent, `TreeSitterLanguageProvider.highlight_version` independence from `EXTRACTOR_VERSION`, remote-URL rejection on custom `highlightsQueryPath`, empty/oversized `HIGHLIGHT_MAX_BYTES` degradation to `None`, and `ReviewSourceSide` rejecting highlights on `binary`/`absent` states.
- `LiveGrammarHighlightTests` (gated by `@unittest.skipUnless(_warm_cache_available(), ...)`) verifies 17 languages including TS/TSX/C++ composition, Python/JSON key suppression/Markdown `@none` precedence, UTF-16 offsets across BOM/astral emoji/combining marks/CRLF/lone CR without mutating caller text, custom `bend2` language routing and safe smoke-compile degradation, LRU cache hit accounting and compact wire overhead, `HIGHLIGHT_MAX_SPANS` ceiling behavior (19,600 spans vs 20,400 -> `None` under `HIGHLIGHT_MAX_BYTES`), Surfaces 1/2/4/5/6/7 contracts with binary/media `null`, and Surface 3 (`GET /api/knowledge/reader/code`) over a temp git code + converted memory repo for present text, SVG media, and binary NUL files.

## Relationships

Directly proves the backend invariants in `models/highlights.py`, `highlights_engine.py`, `highlights_smoke.py`, `highlights_service.py`, `language_catalog.py`, `language_config.py`, `language_set.py`, `serving/scope.py`, `serving/files.py`, `serving/diff_side.py`, `serving/notes.py`, `application/knowledge_reader/truth.py`, `application/review_source_content.py`, `application/review_tree_entries.py`, and `cli/role_report.py`. Paired on the frontend with `dashboard/src/panels/file-viewer/serverHighlights.test.tsx`.

## Evidence

- Tests `; inherits:` cycle guard, catalog `language_for`, `highlight_version` vs `EXTRACTOR_VERSION` independence, remote URL rejection, byte cap, and `ReviewSourceSide` guards. [1]
- Tests live grammar composition/precedence, UTF-16 CRLF/astral/BOM offsets, custom Bend2 routing, LRU cache overhead, and `HIGHLIGHT_MAX_SPANS` ceiling. [2]
- Tests all seven code-serving surfaces including the production `/api/knowledge/reader/code` route contract for present text, media, and binary files. [3]
