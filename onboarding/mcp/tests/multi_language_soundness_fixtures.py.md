# mcp/tests/multi_language_soundness_fixtures.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Table-driven positive-binding, negative-soundness, qualifier-policy, and pure-move test fixture catalog covering all 15 core pilot languages (`c`, `cpp`, `rust`, `zig`, `go`, `java`, `csharp`, `kotlin`, `swift`, `ruby`, `php`, `bash`, `elixir`, `sql`, `hcl`) and all 56 `tree-sitter-language-pack` long-tail languages.

## Code Commentary

`PilotFixture` defines one core pilot case (`language`, `path`, `source`, `expected_spans`, `forbidden_names`, `qualified_cases`, `move_symbol`, `shift_prefix`), asserting exact `(start, end)` line spans for every construct class captured by the language's `tags.scm` query (including attributes, decorators, and leading wrappers), forbidden false-definition traps (imports, calls, comments, strings, literal keys, field accesses), per-language qualifier queries (or `None` for honest refusal), and a pure-move anchor symbol.

`LongTailFixture` defines one long-tail language-pack case (`language`, `path`, `source`, `expected_symbol`, `forbidden_names`, `shift_prefix`). `CORE_PILOT_IDS`, `PILOT_FIXTURES`, and `LONG_TAIL_FIXTURES` expose the immutable fixture tables consumed by `test_multi_language_catalog_soundness.py`.

## Relationships

Registered as a permanent `shared-support` artifact in `mcp/tests/evidence-lifecycle.toml` (`owner = "multi-language-catalog-soundness"`, replacement node `mcp/tests/test_multi_language_catalog_soundness.py::test_15_core_pilots_positive_binding_wrappers_and_negative_soundness`, exact consumer `mcp/tests/test_multi_language_catalog_soundness.py`). This module holds static fixture data only and asserts nothing on its own.

## Evidence

- `PilotFixture`, `LongTailFixture`, `CORE_PILOT_IDS`, `PILOT_FIXTURES`, and `LONG_TAIL_FIXTURES` supply the static soundness, qualifier, and pure-move fixture tables for all 15 core pilots and 56 language-pack entries. [1]
- `mcp/tests/evidence-lifecycle.toml` registers `multi_language_soundness_fixtures.py` as a permanent `shared-support` artifact with `test_multi_language_catalog_soundness.py` as its exact consumer and replacement node. [2]
