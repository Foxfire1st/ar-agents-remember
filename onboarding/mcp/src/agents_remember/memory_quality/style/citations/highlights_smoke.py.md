# mcp/src/agents_remember/memory_quality/style/citations/highlights_smoke.py

## Governing Overview

[memory_quality/ overview](../../overview.md)

## Purpose

Runs as a short-lived child process (`python -m agents_remember.memory_quality.style.citations.highlights_smoke`) to smoke-compile catalog or custom tree-sitter highlight query bundles before the serving process ever compiles them in-process.

## Code Commentary

`main()` reads a single JSON object from stdin, invokes `_smoke_compile(payload)`, writes any exception message to stderr, and returns exit code `0` on success, `1` on compile/load error, or `2` on non-dict stdin. `_smoke_compile` rejects empty query lists and dispatches on `payload["kind"]`: `"catalog"` loads `language_catalog.load_language_catalog` and `language_cache.ensure_catalog_language` via `catalog.get_highlight_spec(languageId)`, while `"custom"` loads the local shared library via `language_cache.load_custom_library_language` with the supplied ABI bounds. It then compiles every query text with `Query(lang, text)` and verifies the compiled count matches.

Running compilation in a child process isolates the MCP/dashboard server from malformed query syntax, missing symbols, or native C crashes (such as `SIGSEGV` inside a mismatched grammar binding).

## Relationships

Spawned by `highlights_service._run_smoke_compile` with a 15-second timeout and JSON payload on stdin; delegates grammar resolution to `language_catalog.py` and `language_cache.py`.

## Evidence

- Compiles catalog or custom highlight query bundles against their exact tree-sitter `Language` and verifies query count. [1]
- Provides the stdin/exit-code subprocess entry point used to isolate malformed queries and native crashes from the host process. [2]
