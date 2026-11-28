# mcp/src/agents_remember/memory_quality/style/citations/extents.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Resolve source bindings and qualified declaration spans for conversion, reference reads and the curator writer.

## Code Commentary

`Extent` records a widened source range, kind, declaration line, test-case tag, explicit `@container` chain (`containers`), and tracked `qualifier_kind`. A Lean extent also carries full-name and scope information. `definitions` adapts `grammars.bindings`, including assignments and declarators, to extents. A definition's declaration line distinguishes the actual declaration from an outward decorator or leading-wrapper range or an attached Lean prefix.

`definition_scope(language_set=None)` owns a call-local table keyed by exact path, grammar key, active provider version, and immutable source lines, binding `grammars.language_set_scope` when an explicit `language_set` is supplied. Nested operations join the existing table. A lock serializes a shared miss in copied worker contexts; results return detached dictionaries and lists. The outer scope clears the table after success or exceptions. Direct calls outside a scope perform their own extraction.

`qualified_spans` preserves every exact-name test-case occurrence, including equal spans, so same-line duplicate bare titles remain ambiguous. Ordinary exact bindings deduplicate ranges. Exact-binding providers (Lean and any provider with `uses_exact_bindings=True`) use exact keys only and return no span when a Lean key has uncertain scope. Other readers resolve qualified names through `_enclosed_qualified_spans` using the active provider's declarative `QualifierSpec` (`_qualifier_spec`), splitting on language-native separators longest-match-first (`_split_qualified`), enforcing optional `separator_kinds` filters (such as `#` vs `.` in Ruby), and matching explicit `@container` chains (`_expand_containers`, `_matches_qualifier_chain`) plus nested lexical enclosure (`_is_lexically_enclosed`). Flat languages with empty `separators` (such as C and Bash) and unresolved qualified names honestly return no span. A caller authoring a single symbol anchor requires one eligible span.

## Relationships

The curator writer, conversion, converted-reference checker, and recorded anchor reader (`read_anchors._defining_extents`) share `qualified_spans`, so they apply the same declarative qualifier, holder-containment, and binding semantics. Legacy format 1 selects its pinned reader before requesting spans. The grammar module owns parsed bindings and eligible test diagnostic trees; this module owns definition extents and call lifetime. It generates no quote, heading or occurrence ranges, FileView cache or merged ranges.

## Evidence

- The outer scope owns and releases the provider-version-keyed table while nested operations join it. [52]

- `qualified_spans` owns the qualified symbol boundary shared across writer, conversion, reference checker, and recorded anchor reads. [26]
- `Extent` records one source range and its declaration, container, and qualifier-kind metadata. [29]

- `definitions` returns names and extents with detached containers keyed by path, grammar, provider version, and source lines. [35]

- The writer, conversion, reference checker, and recorded anchor reader use the same symbol-binding rule. [36]

- Exact-name test-case spans preserve occurrence multiplicity while ordinary names deduplicate. [51]

- Whole-name lookup preserves room for unresolved Lean scope and delegates non-exact-binding qualified lookups to declarative `_enclosed_qualified_spans` (`QualifierSpec` separators, `separator_kinds`, `@container` chains, lexical enclosure, and honest refusal for flat languages). [53]
