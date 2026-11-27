# mcp/tests/test_language_set_and_tags_engine.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Unit regression suite verifying the `LanguageSet`/`LanguageProvider` seam, `.lean` suffix reservation, extractor-version derivation and cache-key isolation, declarative `tags.scm` engine policies, explicit `model.anchors_in` scoping, and shared `read_anchors`/`extents` qualified holder containment.

## Code Commentary

`_functions_only_python_set` constructs an alternate `LanguageSet` whose Python provider uses a custom `tags.scm` query capturing only functions (with upstream `@doc` capture) so cache isolation tests can contrast default and scoped extraction on the same source bytes.

Six source test functions cover the L10 seam contracts (source assertions, not a fresh execution claim):
- `test_lean_suffix_is_permanently_reserved_from_tree_sitter_providers` asserts that constructing a `LanguageSet` binding `.lean` to a `TreeSitterLanguageProvider` raises `AgentsRememberError`, while the default set resolves `Proof.lean` to `LeanLanguageProvider` (`is_tree_sitter=False`, `uses_exact_bindings=True`).
- `test_language_set_derives_extractor_version_and_isolates_caches` verifies `tree-sitter=0.26.1` in `extractor_version`, `observe.EXTRACTOR_VERSION` agreement, and cross-`LanguageSet` isolation across `extents.definitions`, `observe.observation_key`, `CodeSnapshot.resolve`, `CodeObjects.qualified_spans`, and `read_anchors.observe_anchor` while cleaning `BLOB_DEFINITIONS` and `SYMBOL_SPANS`.
- `test_tags_engine_handles_wrappers_destructuring_errors_and_exclusions` checks Python and TSX decorator/export widening, declaration-line preservation, chained/tuple/object/array destructuring, `has_error` skipping, and exclusion of imports, object keys, defaults, and attribute/subscript targets.
- `test_model_anchors_in_accepts_explicit_language_set` verifies `model.anchors_in(..., language_set=...)` threads an explicit `LanguageSet` into TypeScript spelling resolution.
- `test_read_anchors_and_extents_share_holder_containment_for_qualified_names` verifies that `read_anchors.observe_anchor` and `extents.qualified_spans` resolve `First.run` vs `Second.run` to the same enclosing-holder span.
- `test_tags_engine_ignores_doc_and_local_captures_and_preserves_document_order` checks that upstream `@doc` and `@local.definition` captures are tolerated without producing bindings and that `merge_entries` preserves document order.

## Relationships

Registered once in `mcp/tests/test-evidence-lanes.toml` under `unit-regression` and declared as an exact consumer of `_user_settings_guard.py`, portable Node `package-lock.json`, and `knowledge_conversion_test_support.py` in `mcp/tests/evidence-lifecycle.toml`. Complements `mcp/tests/test_memory_citation_grammars.py` (`PinnedDependencyTests`, `TestCaseDefinitionTests`, `PythonExtentTests`, `ScriptDefinitionTests`).

## Evidence

- Asserts `.lean` cannot be bound to a tree-sitter provider and resolves to `LeanLanguageProvider` in the default set. [1]
- Asserts `LanguageSet.extractor_version` derivation and cache-key isolation across `extents`, `observe`, `CodeSnapshot`, `CodeObjects`, and `read_anchors`. [2]
- Asserts declarative `tags.scm` wrapper widening, destructuring, `has_error` skipping, and import/key/default/attribute exclusions on Python and TSX. [3]
- Asserts `model.anchors_in` accepts an explicit `language_set` scope. [4]
- Asserts `read_anchors.observe_anchor` shares `extents.qualified_spans` holder-containment semantics for qualified names. [5]
- Asserts upstream `@doc` and `@local.definition` captures are ignored and `merge_entries` preserves document order. [6]
