# mcp/src/agents_remember/package_data/citations/language_catalog.lock.json

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

Shipped lockfile (`ar-language-catalog/v1`) pinning the `tree-sitter` runtime version and ABI range, reserved and ambiguous file suffixes, pinned `tree-sitter-language-pack` wheels, and the uniform catalog of language specifications with per-platform wheel SHA-256 digests and packaged `.scm` query digests.

## Code Commentary

This lockfile is the single source of truth for shipped citation language support. Top-level fields pin `schema` (`ar-language-catalog/v1`), `treeSitter` (`version: "0.26.1"`, `minAbi: 13`, `maxAbi: 15`), `reservedSuffixes` (`[".lean"]`), `ambiguousSuffixes` (including `.h`, `.m`, `.v`, `.scm`, etc.), and `languagePack` (pinned `tree-sitter-language-pack==0.13.0` wheel artifacts bundling offline ABI 13–15 bindings for Linux/macOS/Windows).

Under `languages`, 76 admitted language entries — 19 `pypi_wheel` entries (`python`, `typescript`, `tsx`, `javascript`, plus the 15 core pilots `c`, `cpp`, `rust`, `zig`, `go`, `java`, `csharp`, `kotlin`, `swift`, `ruby`, `php`, `bash`, `elixir`, `sql`, `hcl`), 56 `language_pack` long-tail entries (53 `verified`, 3 `best_effort`: `nix`, `make`, `dockerfile`), and `builtin_lean` (`lean`) — declare their `providerKind`, unambiguous `suffixes`, optional `filenames`/`shebangs`, `wrappers`, `leadingWrappers`, `destructuring`, `qualifiers` (`separators`, optional `separatorKinds`), `guaranteeTier`, packaged `tagsQuery` / `testsQuery` paths with SHA-256 digests, and per-platform pinned wheel URLs and SHA-256 digests (for `pypi_wheel` entries). All 19 `pypi_wheel` entries also carry `highlightsQueries` (ordered `{path, sha256}` entries pointing to packaged `.scm` highlight queries).

Two top-level display-only sections extend dashboard syntax highlighting without broadening symbol-citation admission: `highlightLanguages` declares 9 non-anchoring display languages (8 `language_pack` entries — `json`, `css`, `scss`, `html`, `xml`, `markdown`, `toml`, `ini` — with pinned `highlightsQueries`, plus 1 `display_only` entry `yaml` without a highlight query), and `displaySuffixes` maps `.pyi` to `python`. No `tree-sitter-*` grammar wheel is declared in `mcp/pyproject.toml`; every grammar loads lazily from this lockfile into the external language cache.

## Relationships

Parsed and verified by `language_catalog.py`. Consumed by `language_cache.py` for platform wheel selection, SHA-256 verification, direct pack binding loading, and ABI validation, by `language_scanner.py` for repository language detection, full-catalog warming (`all_catalog_language_ids`), and `LanguageSet` construction, and by `highlights_service.py` for `highlightsQueries`, `highlightLanguages`, and `displaySuffixes` lookup. Verified against `mcp/pyproject.toml`, `mcp/uv.lock`, and soundness fixtures by `test_memory_citation_grammars.py`, `test_language_catalog_and_lazy_cache.py`, `test_multi_language_catalog_soundness.py`, and `test_unified_tree_sitter_highlights.py`.

## Evidence

- The lockfile pins `schema` (`ar-language-catalog/v1`), `treeSitter` version `0.26.1` (`minAbi: 13`, `maxAbi: 15`), reserved `.lean`, ambiguous suffixes (including `.h`, `.m`, `.v`, `.scm`), `tree-sitter-language-pack==0.13.0` wheels, 76 uniform `languages` entries (19 `pypi_wheel` with `highlightsQueries`, 56 `language_pack`, and `builtin_lean`), 9 `highlightLanguages` (8 `language_pack` + `yaml` `display_only`), and `displaySuffixes` (`.pyi` -> `python`). [1]
