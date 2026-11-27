# mcp/src/agents_remember/memory_quality/style/citations/language_cache.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Manage the external pinned tree-sitter grammar cache outside the MCP virtual environment, handling platform wheel selection, SHA-256 verification, atomic extraction with cross-process locking, ABI verification, and isolated module or local shared-library loading.

## Code Commentary

`resolve_language_cache_root` resolves the grammar cache directory from `AR_LANGUAGE_CACHE` when set, falling back to `${XDG_STATE_HOME:-~/.local/state}/agents-remember/grammars` (never writing into the MCP venv `site-packages`). `select_platform_wheel` picks the matching pinned wheel for the running Python/ABI/platform via `packaging.tags.sys_tags()`.

`warm_catalog_language` and `ensure_catalog_language` install pinned `pypi_wheel` and `language_pack` (`tree-sitter-language-pack`) wheels into versioned cache directories keyed by provider identity and digest. `_install_pinned_wheel` acquires an `fcntl.flock` lock (`_cache_entry_lock`), re-checks the installed `.ar-grammar-receipt.json` (`_receipt_matches`), downloads the wheel bytes to a temporary file via `default_wheel_downloader` (or an injected downloader), verifies the exact SHA-256 digest before extracting, rejects path-traversal zip members in `_safe_extract_zip`, and swaps the extracted directory into place atomically (`_extract_wheel_atomically`). Any hash mismatch or download failure leaves no partial directory or corrupt receipt behind and raises `GrammarUnavailableError`.

`_load_language_from_cache` imports compiled extension modules from the isolated cache directory via `_import_isolated_module` without mutating `sys.path` or installing into the venv, calls the language loader, and runs `_construct_and_verify_abi` against the catalog's `abi_min`..`abi_max` range. `load_custom_library_language` loads user-supplied local shared libraries via `ctypes.CDLL`, retains the DLL handle in `_CUSTOM_DLL_HANDLES` so the C symbol stays mapped for the process lifetime, wraps the returned pointer in a `tree_sitter.Language` PyCapsule (`_wrap_language_capsule`), and enforces the same ABI bounds.

## Relationships

`language_catalog.py` supplies `CatalogLanguageSpec`, `LanguagePackPin`, `WheelArtifact`, and `TreeSitterPin` ABI bounds. `language_scanner.py` binds lazy loader closures around `ensure_catalog_language` and `load_custom_library_language` when building `TreeSitterLanguageProvider` instances and invokes `warm_catalog_language` from `warm_repository_languages`. `errors.py` defines `GrammarUnavailableError`.

## Evidence

- `resolve_language_cache_root` and `select_platform_wheel` resolve the external cache location (`AR_LANGUAGE_CACHE` or `${XDG_STATE_HOME:-~/.local/state}/agents-remember/grammars`) and match pinned wheels to the running platform tags. [1]
- `warm_catalog_language` and `ensure_catalog_language` install pinned wheels on demand and cache loaded `tree_sitter.Language` objects in memory. [2]
- `load_custom_library_language` and `_construct_and_verify_abi` load local shared libraries via `ctypes.CDLL`, wrap the pointer in a PyCapsule, retain the DLL handle, and enforce catalog ABI bounds. [3]
- `_install_pinned_wheel`, `_extract_wheel_atomically`, and `_safe_extract_zip` serialize installs with `flock`, verify SHA-256 digests before extraction, block zip path traversal, and publish receipts atomically. [4]
- `_load_language_from_cache` and `_import_isolated_module` load cached grammar wheels without mutating `sys.path` or the MCP venv. [5]
