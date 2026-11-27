# mcp/src/agents_remember/memory_quality/style/citations/language_catalog.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Parse, validate, and cache the shipped `language_catalog.lock.json` lockfile into immutable `LanguageCatalog` dataclasses, verifying packaged `.scm` query digests and structural invariants before any grammar is loaded.

## Code Commentary

`CATALOG_SCHEMA` pins `ar-language-catalog/v1` and `CATALOG_LOCK_PATH` locates `package_data/citations/language_catalog.lock.json`. `parse_language_catalog` validates top-level keys (`treeSitter`, `reservedSuffixes`, `ambiguousSuffixes`, `languagePack`, `languages`), enforces unique language identifiers and unambiguous suffix claims across all catalog entries, checks reserved suffixes (`.lean`) and ambiguous suffixes (`.h`, `.m`, `.v`), and validates pinned SHA-256 digests on every platform wheel and packaged `.scm` query file.

Each `CatalogLanguageSpec` models a language uniformly across three `ProviderKind` values (`providerKind` in the lockfile): `pypi_wheel` (pinned per-platform PyPI wheel URLs, SHA-256 hashes, wheel module name, and language loader), `language_pack` (pinned `tree-sitter-language-pack` wheel set plus pack language identifier), and `builtin_lean` (the built-in Lean declaration reader, which carries no tree-sitter wheel and reserves `.lean`). `_read_verified_query` reads each packaged `tags.scm` or `tests.scm` file and raises `LanguageCatalogError` if the SHA-256 digest does not match the lockfile pin.

`load_language_catalog` caches parsed catalogs per `(lock_path, package_data_root)` tuple so every consumer shares one validated view of the catalog, including `TreeSitterPin` (`version`, `abi_min`, `abi_max`) and `LanguagePackPin`.

## Relationships

`language_catalog.lock.json` is the sole shipped language table this module reads. `language_scanner.py` turns `CatalogLanguageSpec` entries into `LanguageProvider` instances and uses `catalog.ambiguous_suffixes` and `catalog.reserved_suffixes` during repository scanning. `language_cache.py` downloads and verifies wheels from `CatalogLanguageSpec.wheels` and `LanguageCatalog.language_pack`. `grammars.py` uses `load_language_catalog().tree_sitter.version` for the pinned `tree-sitter` runtime version.

## Evidence

- `CATALOG_SCHEMA` and `CATALOG_LOCK_PATH` pin the shipped catalog schema and packaged lockfile location. [1]
- Immutable catalog records represent `TreeSitterPin`, `LanguagePackPin`, `WheelArtifact`, `CatalogLanguageSpec`, and `LanguageCatalog` with uniform provider metadata. [2]
- `_read_verified_query` verifies every packaged `.scm` query file's SHA-256 digest against the lockfile pin before returning its text. [3]
- `parse_language_catalog` enforces unique language IDs, unambiguous suffix ownership, reserved `.lean` protection, and pinned wheel metadata across all catalog entries. [4]
- `load_language_catalog` caches validated catalog instances by lockfile and package-data path. [5]
