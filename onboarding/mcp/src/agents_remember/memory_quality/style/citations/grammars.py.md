# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse citation definitions and extents with tree-sitter.

## Code Commentary

### Logic

Module-level surface:

- `Binding` (class) — One name a construct binds: its extent, and the line the declaration itself begins on. The two differ for a decorated Python definition, whose extent is widened through `decorated_definition` to cover the decorator while the declaration begins on the `def`/`class` line below it.
- `CallLiteral` (class, lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.
- `grammar_of` (function, lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.
- `parsed` (function, lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.
- `typescript_anchor_identifier` (function, lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.
- `call_argument_literals` (function, lines 188-213) — Every direct string argument and the call it belongs to, in document order.
- `language` (function, lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.
- `definitions` (function, lines 231-256) — Every name ``path`` binds, and the WIDENED line span of the construct that binds it, so a decorated definition's extent covers its decorator. A caller needing the declaration's own first line as well reads `bindings`.
- `bindings` (function) — Every name ``path`` binds, with both its widened extent and its declaration line, from ONE walk. The declaration line is the first line of the unwidened construct: the ``def``/``class`` line for a decorated definition, and the extent's start for every other construct — including an exported TypeScript declaration, whose ``export`` keyword shares the declaration's own first line.
- `_walk` (function, lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.
- `_widened` (function, lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.
- `_span` (function, lines 282-286) — The one-based line range ``node`` occupies.
- `_text` (function, lines 289-290)
- `_python_names` (function, lines 293-299) — The names one Python construct binds.
- `_python_targets` (function, lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.
- `_script_names` (function, lines 317-323) — The names one JavaScript or TypeScript construct binds.
- `_script_targets` (function, lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `CallLiteral` (lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.. [1]
- Defines the function `grammar_of` (lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.. [2]
- Defines the function `parsed` (lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.. [3]
- Defines the function `typescript_anchor_identifier` (lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.. [4]
- Defines the function `call_argument_literals` (lines 188-213) — Every direct string argument and the call it belongs to, in document order.. [5]
- Defines the function `language` (lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.. [6]
- Defines the function `definitions` (lines 231-256) — Every name ``path`` binds, and the line span of the construct that binds it.. [7]
- Defines the function `_walk` (lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.. [8]
- Defines the function `_widened` (lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.. [9]
- Defines the function `_span` (lines 282-286) — The one-based line range ``node`` occupies.. [10]
- Defines the function `_text` (lines 289-290). [11]
- Defines the function `_python_names` (lines 293-299) — The names one Python construct binds.. [12]
- Defines the function `_python_targets` (lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.. [13]
- Defines the function `_script_names` (lines 317-323) — The names one JavaScript or TypeScript construct binds.. [14]
- Defines the function `_script_targets` (lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.. [15]
