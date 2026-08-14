# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/grammars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse citation definitions and extents with tree-sitter.

## Code Commentary

### Logic

Module-level surface:

- `CallLiteral` (class, lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.
- `grammar_of` (function, lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.
- `parsed` (function, lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.
- `typescript_anchor_identifier` (function, lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.
- `call_argument_literals` (function, lines 188-213) — Every direct string argument and the call it belongs to, in document order.
- `language` (function, lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.
- `definitions` (function, lines 231-256) — Every name ``path`` binds, and the line span of the construct that binds it.
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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `CallLiteral` (lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.. | `CallLiteral` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:123-131 |
| Defines the function `grammar_of` (lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.. | `grammar_of` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:134-136 |
| Defines the function `parsed` (lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.. | `parsed` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:139-141 |
| Defines the function `typescript_anchor_identifier` (lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.. | `typescript_anchor_identifier` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:144-185 |
| Defines the function `call_argument_literals` (lines 188-213) — Every direct string argument and the call it belongs to, in document order.. | `call_argument_literals` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:188-213 |
| Defines the function `language` (lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.. | `language` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:216-228 |
| Defines the function `definitions` (lines 231-256) — Every name ``path`` binds, and the line span of the construct that binds it.. | `definitions` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:231-256 |
| Defines the function `_walk` (lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.. | `_walk` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:259-272 |
| Defines the function `_widened` (lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.. | `_widened` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:275-279 |
| Defines the function `_span` (lines 282-286) — The one-based line range ``node`` occupies.. | `_span` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:282-286 |
| Defines the function `_text` (lines 289-290). | `_text` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:289-290 |
| Defines the function `_python_names` (lines 293-299) — The names one Python construct binds.. | `_python_names` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:293-299 |
| Defines the function `_python_targets` (lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.. | `_python_targets` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:302-314 |
| Defines the function `_script_names` (lines 317-323) — The names one JavaScript or TypeScript construct binds.. | `_script_names` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:317-323 |
| Defines the function `_script_targets` (lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.. | `_script_targets` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:326-343 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
