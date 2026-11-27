# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Build the default `LanguageSet` from the shipped catalog lockfile (`language_catalog.lock.json`) and lazy external grammar cache (`language_cache`), expose the active and repository-scoped `LanguageSet` seams, and dispatch source bindings and script test-case diagnostics through the selected provider.

## Code Commentary

`DEFAULT_LANGUAGE_SET` is built at import time via `language_scanner.build_language_set()` over the cached `language_catalog.load_language_catalog()` (which pins `tree-sitter` `0.26.1` and every shipped language's `.scm` query digests and per-platform wheels; the former `MEASURED_VERSIONS` dict and direct `tree_sitter_*` imports have been removed). `default_language_set`, `active_language_set`, `is_default_language_set`, `language_set_scope`, `repository_language_set_scope`, `extractor_version`, and `language_identity` expose the active `LanguageSet` `ContextVar` seam from `language_set.py` and per-repository `languages.json` resolution from `language_scanner.py`.

A scoped call reuses each exact `(provider.version, text)` TypeScript anchor input, including an unresolved spelling, until its request owner clears. Calls outside that scope use a separate process memo (`_process_typescript_anchor_identifier`) only on the default `LanguageSet`, parsing directly when a non-default `LanguageSet` is active. Loaded grammars and parsed test-file trees keep their own owners.

`Binding` (re-exported from `tags_engine.py`) records a construct's widened extent, its declaration line and whether it is a test case. A decorated Python definition includes its decorators in the extent while retaining the actual `def` or `class` declaration line. An exported script declaration includes its export syntax. A Lean binding carries a verified full name or marks unresolved scope.

`grammar_of` selects the active `LanguageSet`'s reader key by glob/suffix. `parsed` identifies paths that support structural definitions. `typescript_anchor_identifier` recognizes a direct identifier rooted by a complete TypeScript call or generic spelling. `language` resolves the registered `TreeSitterLanguageProvider` from the default or active `LanguageSet` and delegates to `provider.load_language()` (backed by `language_cache`); grammar-load failures raise `GrammarUnavailableError`.

`bindings` resolves the path's active `LanguageProvider`: `LeanLanguageProvider` runs `extract_bindings(lines)`, while `TreeSitterLanguageProvider` parses the bytes and executes declarative `tags.scm` (and `tests.scm` for eligible script test files) via `tags_engine`. The former bespoke per-language walker helpers (`_widened`, `_span`, `_text`, `_python_names`, `_python_targets`, `_script_names`, `_script_targets`, `_lean_bindings`) have been replaced by `tags_engine.py` and `language_set.py`. `_walk` remains for `typescript_anchor_identifier` syntax-tree traversal.

Within a `parsing_scope` (which optionally binds a `LanguageSet`), eligible script test inputs retain one `_ParsedSource` (tree plus declarative `tests.scm` `test_calls`) shared by `bindings`, `test_case_refusal`, and `test_case_range`. The cache key includes path, grammar key, active provider version, and source lines. Ordinary source trees are not retained in this diagnostic table. Nested parsing scopes join the call; the outer scope clears it on every exit.

`test_case_refusal` supplies specialized diagnostics only for providers where `supports_test_cases(path)` is true, feeding `source.test_calls` into `test_cases.refusal`. `test_case_range(path, lines, start, end, reaches)` feeds `source.test_calls` into `test_case_ranges.case_at` and answers an exact case extent or a refusal. Its caller supplies name reachability, so a range is accepted only where no name reaches the case.

## Relationships

`language_set.py` defines `LanguageProvider`, `TreeSitterLanguageProvider`, `LeanLanguageProvider`, `LanguageSet`, and the `ContextVar` seam. `tags_engine.py` owns declarative `tags.scm`/`tests.scm` compilation and extraction. `extents.definitions` adapts `bindings` to definition extents and owns call-scoped definition reuse. The case modules own title/modifier analysis and exact-case reachability. Ordinary symbol diagnostics remain with callers outside recognized script test files.

## Evidence

- `DEFAULT_LANGUAGE_SET` builds from the shipped catalog lockfile (`language_catalog.lock.json`) and `repository_language_set_scope` layers per-repo `languages.json` overrides. [23]

- `active_language_set`, `default_language_set`, `is_default_language_set`, and `extractor_version` expose the active `LanguageSet` and its version identity. [24]

- A call retains eligible parsed test inputs keyed by path, grammar, provider version, and lines, and clears them at the outer exit. [20]

- Bindings delegate to the active `LanguageProvider` (`LeanLanguageProvider` or `TreeSitterLanguageProvider` via `tags_engine`) and retain widened extents, declaration lines, and recognized named test cases. [21]

- `grammar_of` selects the active `LanguageSet` grammar key for a path. [2]

- `typescript_anchor_identifier` recognizes a complete direct TypeScript anchor spelling and keys request/process reuse by active TypeScript provider version. [4]

- `_walk` traverses every node in document order for TypeScript anchor spelling inspection. [8]
- Specialized unresolved-case diagnostics are restricted to providers supporting test cases on the path and pass `tests.scm` call sites to `test_cases.refusal`. [17]

- Exact range lookup returns a case or its refusal from declarative `tests.scm` call sites using the caller's name resolver. [18]

- The built-in Lean reader in `LeanLanguageProvider.extract_bindings` exposes exact written and full-name keys and retains the status of uncertain keys. [22]

- `parsed` identifies files whose definitions can be parsed. [3]

- `language` loads the chosen grammar and propagates load failures. [6]
