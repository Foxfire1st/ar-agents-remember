# mcp/tests/test_language_catalog_and_lazy_cache.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

End-to-end verification suite for the uniform language catalog, dependency purity, lazy external grammar cache, `tree-sitter-language-pack` provider support, corrupt-hash/download failure asymmetry, repository language scanning and overrides, custom local language (`bend2`) loading and production-consumer wiring, `languages.json` security boundaries, and the `agents-remember languages` CLI.

## Code Commentary

`test_dependency_purity_pyproject_uv_lock_and_zero_hardcoded_language_lists` parses `mcp/pyproject.toml`, `mcp/uv.lock`, and every product module under `mcp/src/agents_remember` via AST (`_find_hardcoded_language_violations`) to assert zero `tree-sitter-*` grammar dependencies and zero hardcoded language tables or suffix-to-grammar maps outside the catalog.

`test_lazy_pinned_download_and_warm_cache_reuse_without_mutating_venv`, `test_language_pack_provider_lazy_install_and_hash_verification`, and `test_corrupt_hash_and_download_failure_preserve_read_write_asymmetry` verify that pinned wheels install lazily into `AR_LANGUAGE_CACHE` without mutating the MCP venv, reuse warm cached receipts without re-downloading, verify SHA-256 digests for both standalone wheels and `tree-sitter-language-pack`, and preserve read-vs-write error asymmetry on corrupt hashes or download failures without leaving partial cache state.

`test_repo_auto_scan_ambiguous_suffixes_overrides_shebangs_and_lean_reservation`, `test_languages_json_security_boundary_rejects_remote_urls`, and `test_unknown_enable_disable_ids_and_catalog_shadowing_are_refused` verify repository scanning (including shebangs, ambiguous `.h`/`.m`/`.v`, and `.lean` reservation), rejection of remote URLs and forbidden keys in repository-root `languages.json`, and refusal of unknown IDs or catalog shadowing.

`test_custom_local_language_bend2_end_to_end_and_abi_check` and `test_repository_languages_json_and_custom_bend2_wire_through_production_consumers` compile/wrap a local custom shared library (`bend2`), verify ABI bounds checking, and prove that repository-root `languages.json` and custom languages wire end-to-end through `repository_language_set_scope` and production consumers (`read_anchors`, `code_anchors`, `observe`, `reference_state`, `runs`, `review_tree_knowledge`, `memory_initialization`, etc.). `test_cli_languages_scan_warm_and_ci_bootstrap_contracts` exercises `agents-remember languages scan`/`warm` and validates the bootstrap and Dagger pre-warm hooks.

## Relationships

Tests `language_catalog.py`, `language_cache.py`, `language_config.py`, `language_scanner.py`, `cli/languages.py`, `grammars.py`, `language_set.py`, `mcp/pyproject.toml`, `mcp/uv.lock`, `scripts/bootstrap-mcp-venv.sh`, and `.dagger/src/agents_remember_quality/main.py`.

## Evidence

- AST and lockfile checks enforce zero `tree-sitter-*` grammar dependencies in `pyproject.toml`/`uv.lock` and zero hardcoded language tables in product source. [1]
- Lazy wheel installation, `tree-sitter-language-pack` support, warm-cache reuse without venv mutation, and corrupt-hash/download failure asymmetry are verified end to end. [2]
- Repository scanning, ambiguous suffix reporting, shebang detection, `.lean` reservation, remote-URL rejection, and unknown-ID/shadowing refusals are tested. [3]
- Custom local language loading (`bend2`), ABI verification, CLI `languages scan`/`warm`, and full production-consumer wiring through `.agents-remember/languages.json` are verified. [4]
