# mcp/src/agents_remember/memory_quality/style/citations/extents.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Resolve source bindings and qualified declaration spans for conversion, reference reads and the curator writer.

## Code Commentary

`Extent` records a widened source range, kind, declaration line and test-case tag. A Lean extent also carries full-name and scope information. `definitions` adapts `grammars.bindings`, including assignments and declarators, to extents. A definition's declaration line distinguishes the actual declaration from an outward decorator range or an attached Lean prefix.

`definition_scope` owns a call-local table keyed by exact path, grammar and immutable source lines. Nested operations join the existing table. A lock serializes a shared miss in copied worker contexts; results return detached dictionaries and lists. The outer scope clears the table after success or exceptions. Direct calls outside a scope perform their own extraction.

`qualified_spans` preserves every exact-name test-case occurrence, including equal spans, so same-line duplicate bare titles remain ambiguous. Ordinary exact bindings deduplicate ranges. Lean lookup uses exact keys and returns no span when the selected key has uncertain scope. Other readers can use dotted containment after an exact-key miss. For example, `Holder.method` selects a method declared inside that holder. A caller authoring a single symbol anchor requires one eligible span.

## Relationships

The curator writer, conversion and converted-reference checker share `qualified_spans`, so they apply the same binding semantics. Legacy format 1 selects its pinned reader before requesting spans. The grammar module owns parsed bindings and eligible test diagnostic trees; this module owns definition extents and call lifetime. It generates no quote, heading or occurrence ranges, FileView cache or merged ranges.

## Evidence


- The outer scope owns and releases the table while nested operations join it. [52]

- `qualified_spans` owns the qualified symbol boundary. [26]
- `Extent` records one source range and its declaration metadata. [29]
- `definitions` returns names and extents with detached containers. [35]
- The writer, conversion and reference checker use the same symbol-binding rule. [36]
- Exact-name test-case spans preserve occurrence multiplicity while ordinary names deduplicate. [51]

- Whole-name lookup preserves room for unresolved Lean scope and applies dotted containment only to other readers. [53]
