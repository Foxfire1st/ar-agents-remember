# mcp/src/agents_remember/memory_quality/style/citations/tags_engine.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Executes standard upstream-compatible tree-sitter `tags.scm` queries and optional `tests.scm` call-site queries without per-language AST walker code.

## Code Commentary

`QUERIES_ROOT` locates packaged `.scm` query files under `mcp/src/agents_remember/package_data/citations/queries/`. `load_query_text` reads a query file as UTF-8, `query_digest` computes its 16-hex-character SHA-256 prefix for extractor versioning, and `compile_query` caches compiled `tree_sitter.Query` objects per `(language, query_text)` pair.

`Binding` records a bound name's widened one-based `(start, end)` line span, its own `declaration` line (below decorators or export wrappers), `test_case`, and Lean `full_name`/`scope_uncertain` metadata. `widened(node, wrappers)` grows a definition node outward through parent node types declared in `wrappers` while `_TagCollector.collect_match` keeps `declaration` on the captured `@definition.*` node's own start line via `test_cases.span_of`.

`extract_tag_entries` runs `QueryCursor.matches` over a `tags.scm` query, accepts `@definition.*` and `@name` captures (tolerating upstream `@doc` and `@local.*` captures), skips definition or name nodes where `has_error` is true, deduplicates `(definition_node.id, name_node.id)` pairs, and unpacks destructuring name containers through `DestructuringSpec`. `DestructuringSpec.unpack` traverses only bound-side leaves, named fields (`recurse_fields`), and child containers (`recurse_children`) in source order, avoiding object keys, default-value expressions, and attribute/subscript targets.

`extract_test_calls` collects unique `@test.*` call nodes from a `tests.scm` query in `(start_byte, -end_byte)` document order. `extract_test_case_entries` passes those captured calls into `test_cases.case_names` to produce `test_case=True` `Binding` entries with widened spans. `merge_entries` combines tag and test-case entries in `(start_byte, -end_byte, order)` pre-order document order and groups bindings by name.

## Relationships

`language_set.py`'s `TreeSitterLanguageProvider` owns per-language query text, `wrappers`, and `DestructuringSpec` data and delegates compilation and extraction here. `grammars.py` re-exports `Binding` and `DestructuringSpec` and loads the packaged Python, TypeScript, TSX, and JavaScript `.scm` files through `load_query_text`. `test_cases.py` supplies `span_of` and `case_names`. `global_state.py` registers `tags_engine.compile_query` in `PROCESS_MUTABLE_STATES` so pytest clears compiled query caches between modules.

## Evidence

- `QUERIES_ROOT` resolves the packaged `citations/queries` directory; `load_query_text`, `query_digest`, and `compile_query` load, hash, and cache `.scm` queries. [1]
- `Binding` retains a construct's widened line span, own declaration line, test-case flag, and Lean scope metadata. [2]
- `DestructuringSpec` declares bound-side leaf, child, and field unpacking rules so destructuring extracts only bound names in source order. [3]
- `widened` expands a syntax node outward through declared wrapper parent types. [4]
- `extract_tag_entries` runs `@definition.*`/`@name` captures, skips `has_error` nodes, deduplicates pairs, widens wrappers, and unpacks destructuring targets. [5]
- `extract_test_calls` collects unique `@test.*` call sites in document order and `extract_test_case_entries` delegates title extraction to `test_cases.case_names`. [6]
- `merge_entries` orders tag and test-case entries in pre-order document order and groups bindings by name. [7]
