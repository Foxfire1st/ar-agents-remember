# mcp/src/agents_remember/memory_quality/style/citations/highlights_service.py

## Governing Overview

[memory_quality/ overview](../../overview.md)

## Purpose

Owns catalog- and custom-language display resolution, out-of-process smoke-compile verification, bounded generation-keyed LRU caching, and graceful `None` degradation for server-side syntax highlighting across all dashboard code-serving surfaces.

## Code Commentary

`resolve_display_language` resolves a file path first through the active or repository-scoped `LanguageSet` (`grammar_of`), then falls back to `LanguageCatalog.display_language_for` (covering display-only `highlightLanguages` and `displaySuffixes` such as `.pyi -> python`), and finally returns `"text"`.

`highlight_text` enforces `HIGHLIGHT_MAX_BYTES` immediately, resolves a `_HighlightTarget` (preferring custom local providers from `languages.json` with `highlights_query_texts` before catalog specs, and skipping unwarmed catalog grammars unless `allow_download=True`), and keys the bounded LRU `_HIGHLIGHT_CACHE` on `(HIGHLIGHT_VERSION, language_id, version_tag, sha256(text)[:24])` where `version_tag` combines `grammar_version` and the 16-hex composed query bundle digest.

Before compiling any bundle in-process, `_verify_bundle` runs `highlights_smoke` in a subprocess with `_SMOKE_TIMEOUT_SECONDS = 15` and caches the boolean outcome in `_VERIFIED_BUNDLES` (cap 256). Verified bundles are compiled once into `_COMPILED_BUNDLES` (cap 128). `_HIGHLIGHT_CACHE` enforces both entry (`_RESULT_CACHE_MAX_ENTRIES = 512`) and estimated-byte (`_RESULT_CACHE_MAX_BYTES = 16 MiB`) LRU limits under `_CACHE_LOCK`, tracking counters in `_HIGHLIGHT_CACHE_STATS` exposed via `highlight_cache_stats()`. All four mutable state objects (`_VERIFIED_BUNDLES`, `_COMPILED_BUNDLES`, `_HIGHLIGHT_CACHE`, `_HIGHLIGHT_CACHE_STATS`) are registered in `PROCESS_MUTABLE_STATES` (`global_state.py`) for per-test isolation. Any missing grammar, unwarmed cache, smoke-compile failure, or `QueryError` degrades cleanly to `None` without raising.

## Relationships

Called by `serving/scope.py` (`language_for`), `serving/files.py`, `serving/diff_side.py`, `serving/notes.py`, `application/knowledge_reader/truth.py`, `application/review_source_content.py`, `application/review_tree_entries.py`, and `cli/role_report.py`. Delegates pure sweeping/UTF-16 encoding to `highlights_engine.py` and child-process verification to `highlights_smoke.py`.

## Evidence

- Declares thread-safe bounded caches `_VERIFIED_BUNDLES`, `_COMPILED_BUNDLES`, `_HIGHLIGHT_CACHE`, and `_HIGHLIGHT_CACHE_STATS`. [1]
- Resolves display language via active/repo `LanguageSet` then catalog `display_language_for` with `"text"` fallback. [2]
- Runs out-of-process smoke compilation via `highlights_smoke` before compiling query bundles in-process. [3]
- Coordinates target resolution, generation-keyed LRU caching, and graceful `None` degradation in `highlight_text`. [4]
