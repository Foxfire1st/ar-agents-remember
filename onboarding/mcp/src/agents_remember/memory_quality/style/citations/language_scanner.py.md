# mcp/src/agents_remember/memory_quality/style/citations/language_scanner.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Construct repository-scoped `LanguageSet` instances from the shipped catalog plus user/repository overrides, scan repositories to detect active and ambiguous languages, and pre-warm required pinned wheels in the external grammar cache.

## Code Commentary

`build_provider_from_catalog` wraps each `CatalogLanguageSpec` uniformly: `builtin_lean` builds `LeanLanguageProvider`, while `pypi_wheel` and `language_pack` build `TreeSitterLanguageProvider` instances with lazy loader closures backed by `language_cache.ensure_catalog_language`, forwarding `leading_wrappers`, `qualifiers`, and `guarantee_tier`. `build_provider_from_custom` reads the custom language's local `tags.scm` (and optional `tests.scm`), hashes its shared library bytes into the provider version string, and binds a lazy loader backed by `language_cache.load_custom_library_language`.

`build_language_set` and `build_repository_language_set` merge catalog languages, custom languages, `enable`/`disable` sets, and `suffixes`/`globs` overrides, validating via `_validate_override_identities` and `_validate_override_target_ids` that custom IDs never shadow catalog IDs and that `enable`, `disable`, `suffixes`, and `globs` never reference unknown language IDs. `repository_language_set` memoizes built sets per `(repo_root, config_stat_tokens, custom_artifact_stat_tokens, catalog_path, cache_root)` in a bounded insertion-order cache (`_REPO_LANGUAGE_SETS`) so repeated repository calls avoid rebuilding while automatically invalidating whenever `<repo>/languages.json`, user settings, or custom `.so`/`.scm` files change on disk.

`scan_repository_languages` enumerates repository files (using `git ls-files` when inside a Git tree, falling back to `os.walk` skipping `_SKIP_DIRS`), classifies each file by custom/override globs, suffix claims, shebang interpreters (`_read_shebang_interpreter`), and catalog suffixes, and returns a `LanguageScanReport` separating unambiguously detected languages from unresolved `ambiguous_suffixes` (such as `.h`, `.m`, `.v`, `.scm` without a `suffixes`/`globs` override binding). `all_catalog_language_ids` returns every non-builtin catalog language ID sorted for full-catalog warming (`languages warm --all`) without hardcoding any language list. `warm_repository_languages` resolves the target language IDs (explicit `languages`, or auto-scanned repository languages), calls `language_cache.warm_catalog_language` for each tree-sitter catalog entry, and returns a `LanguageWarmReport`.

## Relationships

`language_catalog.py` supplies the validated catalog, `language_config.py` supplies merged overrides, `language_cache.py` performs lazy wheel installation and local shared-library loading, and `language_set.py` defines `LanguageSet` and its `ContextVar` seam. `grammars.py` exposes `repository_language_set_scope` over `repository_language_set`, and `cli/languages.py` exposes `scan_repository_languages`, `all_catalog_language_ids`, and `warm_repository_languages` as the `agents-remember languages` CLI.

## Evidence

- `build_provider_from_catalog` (forwarding `leading_wrappers`, `qualifiers`, and `guarantee_tier`), `build_provider_from_custom`, and `all_catalog_language_ids` construct lazy `LanguageProvider` instances and enumerate non-builtin catalog language IDs uniformly. [1]

- `build_language_set` and `repository_language_set` build and stat-keyed-cache repository `LanguageSet` instances from the catalog and merged overrides. [2]
- `scan_repository_languages` enumerates repository files, applies overrides, globs, suffixes, and shebang detection, and reports detected languages alongside unresolved ambiguous suffixes. [3]
- `warm_repository_languages` pre-warms catalog wheels for scanned or explicitly requested language IDs into the external cache. [4]
- `_validate_override_identities` and `_validate_override_target_ids` reject custom IDs shadowing catalog entries and unknown language IDs in `enable`, `disable`, or `suffix_overrides`. [5]
