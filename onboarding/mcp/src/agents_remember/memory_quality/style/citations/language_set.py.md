# mcp/src/agents_remember/memory_quality/style/citations/language_set.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Defines the `LanguageProvider` protocol, built-in `TreeSitterLanguageProvider` and `LeanLanguageProvider` implementations, immutable `LanguageSet` suffix/key registry, and `ContextVar`-backed `language_set_scope` seam.

## Code Commentary

Language resolution is a pure function of `(LanguageSet, path)` rather than a process-global suffix map. `LanguageSet` indexes its providers by key (`by_key`) and lowercase dot-prefixed suffix (`by_suffix`) as immutable `MappingProxyType` views, refusing duplicate keys, non-lowercase or dot-less suffixes, duplicate suffix claims, and any attempt to bind a reserved suffix in `RESERVED_SUFFIXES` (`.lean`) to a tree-sitter or non-`lean` provider.

Each `TreeSitterLanguageProvider` builds its `version` string from `grammar_version` plus 16-hex-character SHA-256 digests of its `tags.scm` query text and optional `tests.scm` query text (`tags_engine.query_digest`). `LanguageSet.extractor_version` deterministically joins `tree-sitter=<version>` with sorted `<key>[<suffixes>]=<provider.version>` entries (`_build_extractor_version`), and `LanguageSet.language_identity(path)` returns `<key>@<version>` so every downstream parse, definition, anchor, and observation cache key separates distinct provider sets. `without(*keys)` and `with_providers(...)` produce derived immutable `LanguageSet` instances without mutating the default set.

`LeanLanguageProvider` adapts `lean_declarations.declarations` behind the same `LanguageProvider` protocol (`is_tree_sitter=False`, `uses_exact_bindings=True`, `has_test_cases=False`, `version="builtin-lean/1"`). `extract_bindings` emits exact full-name keys, possible full-name keys with `scope_uncertain=True` when scope is uncertain, and written-name aliases, layering `written` then `possible` then `full` so established full names take precedence over possible names and written aliases.

`current_language_set(default)`, `has_language_set_override(default)`, and `language_set_scope(language_set)` manage the module's `_active_language_set` `ContextVar` and always reset the context token on scope exit.

## Relationships

`language_scanner.py` constructs `TreeSitterLanguageProvider` and `LeanLanguageProvider` instances from `language_catalog.py` and `language_config.py` (including optional glob selectors and lazy `language_cache` loaders). `grammars.py` builds the default `LanguageSet` via `language_scanner.build_language_set()`, re-exports the seam helpers alongside `repository_language_set_scope`, and dispatches `bindings`, `test_case_refusal`, and `test_case_range` through the active provider. `tags_engine.py` supplies `Binding`, `DestructuringSpec`, query compilation/digests, and declarative tag/test extraction for `TreeSitterLanguageProvider`. `lean_declarations.py` supplies the Lean declaration scanner wrapped by `LeanLanguageProvider`.

## Evidence

- `LanguageProvider` declares the uniform key, suffix, version, tree-sitter/exact-binding, and test-case interface. [1]

- `TreeSitterLanguageProvider` hashes `tags.scm` and optional `tests.scm` queries into its version and delegates extraction to `tags_engine`. [2]

- `LeanLanguageProvider.extract_bindings` preserves full-name precedence over possible and written aliases while marking uncertain scope. [3]

- `LanguageSet` owns immutable key/suffix maps, derived set builders, and deterministic `extractor_version` and `language_identity`. [4]

- `_register_suffix` enforces normalized dot-prefixed suffixes, rejects duplicate claims, and permanently reserves `.lean` for the built-in Lean scanner. [5]

- `_build_extractor_version` combines `tree-sitter` and sorted provider versions and suffixes into one deterministic version string. [6]

- `current_language_set`, `has_language_set_override`, and `language_set_scope` bind and restore the active `LanguageSet` `ContextVar`. [7]
