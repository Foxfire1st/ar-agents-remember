# mcp/src/agents_remember/package_data/citations/language_catalog.lock.json

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

Shipped lockfile (`ar-language-catalog/v1`) pinning the `tree-sitter` runtime version and ABI range, reserved and ambiguous file suffixes, pinned `tree-sitter-language-pack` wheels, and the uniform catalog of language specifications with per-platform wheel SHA-256 digests and packaged `.scm` query digests.

## Code Commentary

This lockfile is the single source of truth for shipped citation language support. Top-level fields pin `schema` (`ar-language-catalog/v1`), `treeSitter` (`version: "0.26.1"`, `abiMin: 13`, `abiMax: 15`), `reservedSuffixes` (`[".lean"]`), `ambiguousSuffixes` (`[".h", ".m", ".v"]`), and `languagePack` (pinned `tree-sitter-language-pack` wheel artifacts for Linux/macOS/Windows).

Under `languages`, each language entry (`python`, `typescript`, `tsx`, `javascript`, `lean`) declares its `providerKind` (`pypi_wheel`, `language_pack`, or `builtin_lean`), claimed `suffixes`, optional `shebangs`, `wrappers`, `destructuring`, `hasTestCases`, packaged `tagsQuery` / `testsQuery` paths with SHA-256 digests, and per-platform pinned wheel URLs and SHA-256 digests (for `pypi_wheel` entries). No `tree-sitter-*` grammar wheel is declared in `mcp/pyproject.toml`; every grammar loads lazily from this lockfile into the external language cache.

## Relationships

Parsed and verified by `language_catalog.py`. Consumed by `language_cache.py` for platform wheel selection, SHA-256 verification, and ABI validation, and by `language_scanner.py` for repository language detection and `LanguageSet` construction. Verified against `mcp/pyproject.toml` and `mcp/uv.lock` by `test_memory_citation_grammars.py` and `test_language_catalog_and_lazy_cache.py`.

## Evidence

- The lockfile pins `schema` (`ar-language-catalog/v1`), `treeSitter` version `0.26.1` (`abiMin: 13`, `abiMax: 15`), reserved `.lean`, ambiguous `.h`/`.m`/`.v`, and `languagePack` wheels alongside uniform `languages` entries (`python`, `typescript`, `tsx`, `javascript`, `lean`). [1]
