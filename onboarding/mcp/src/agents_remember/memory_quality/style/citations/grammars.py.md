# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

## Governing Overview

[overview](../../overview.md)

## Current source account — Named JavaScript and TypeScript test-case bindings

Binding adds a test_case flag. bindings accepts a Sequence of lines and still emits widened extents and unwidened declaration lines in one deterministic walk. For recognized non-Python test files it also binds statically recognized named test cases; no name is invented when the parser reports none. test_case_refusal supplies a specialized diagnostic only for TypeScript, TSX or JavaScript test files; other files retain ordinary symbol diagnostics.

This source-bound correction covers the described L54 seams only. Unrelated inherited prose and references below are preserved, not recertified; no installed behavior, test execution, permission, landing or MEMORY acceptance is inferred.

## Current evidence

- Bindings add recognized named non-Python test cases while retaining normal declaration semantics.



- Specialized unresolved-case diagnostics are restricted to script test files. [17]



## Inherited source-epoch account (non-operative)

The following complete predecessor retains useful explanations, old observations and provenance. Its superseded claims on the updated seams are historical, not a parallel current contract; its numbered groups keep their original meanings.

> ## Governing Overview
>
> [overview](../../overview.md)
>
> ## Purpose
>
> Parse citation definitions and extents with tree-sitter.
>
> ## Code Commentary
>
> ### Logic
>
> Module-level surface:
>
> - `Binding` (class) — One name a construct binds: its extent, and the line the declaration itself begins on. The two differ for a decorated Python definition, whose extent is widened through `decorated_definition` to cover the decorator while the declaration begins on the `def`/`class` line below it.
> - `Binding` (class, lines 124-133) — One name a construct binds: its extent and the line its declaration itself begins on, which differ for a decorated definition because the extent grows outward through the decorator while the declaration starts at the def or class line.
> - `grammar_of` (function, lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.
> - `parsed` (function, lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.
> - `typescript_anchor_identifier` (function, lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.
> - `call_argument_literals` (function, lines 188-213) — Every direct string argument and the call it belongs to, in document order.
> - `language` (function, lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.
> - `definitions` (function, lines 231-256) — Every name ``path`` binds, and the WIDENED line span of the construct that binds it, so a decorated definition's extent covers its decorator. A caller needing the declaration's own first line as well reads `bindings`.
> - `bindings` (function) — Every name ``path`` binds, with both its widened extent and its declaration line, from ONE walk. The declaration line is the first line of the unwidened construct: the ``def``/``class`` line for a decorated definition, and the extent's start for every other construct — including an exported TypeScript declaration, whose ``export`` keyword shares the declaration's own first line.
> - `_walk` (function, lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.
> - `_widened` (function, lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.
> - `_span` (function, lines 282-286) — The one-based line range ``node`` occupies.
> - `_text` (function, lines 289-290)
> - `_python_names` (function, lines 293-299) — The names one Python construct binds.
> - `_python_targets` (function, lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.
> - `_script_names` (function, lines 317-323) — The names one JavaScript or TypeScript construct binds.
> - `_script_targets` (function, lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.
>
> ### Conventions
>
> Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.
>
> ### Invariants And Boundaries
>
> - The card mirrors the source file one-to-one at `mcp/src/...` path.
>
> ### Todos
>
> None.
>
> ## Evidence
>
> ### Repo-Internal References
>
> This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.
>
> - Defines the function `grammar_of` (lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.. [2]
> - Defines the function `parsed` (lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.. [3]
> - Defines the function `typescript_anchor_identifier` (lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.. [4]
> - Defines the function `language` (lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.. [6]
> - Defines the function `definitions` (lines 231-256) — Every name ``path`` binds, and the line span of the construct that binds it.. [7]
> - Defines the function `_walk` (lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.. [8]
> - Defines the function `_widened` (lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.. [9]
> - Defines the function `_span` (lines 282-286) — The one-based line range ``node`` occupies.. [10]
> - Defines the function `_text` (lines 289-290). [11]
> - Defines the function `_python_names` (lines 293-299) — The names one Python construct binds.. [12]
> - Defines the function `_python_targets` (lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.. [13]
> - Defines the function `_script_names` (lines 317-323) — The names one JavaScript or TypeScript construct binds.. [14]
> - Defines the function `_script_targets` (lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.. [15]

## Current account — the case-extent entry

`test_case_range(path, lines, start, end, reaches)` is the grammar's one new entry beside `test_case_refusal`: it parses the candidate bytes and answers the one case a range is, or the refusal naming why the lines are no case. The caller passes its own resolver, so a range is admitted only where no name really reaches the case. `_span` now delegates to `test_cases.span_of`, so every extent in this module is measured by one rule, and `test_case_refusal` passes the path through.

- The one new grammar entry answers the case a range is or why the lines are none, using the caller's name resolver. [18]
- Every extent in this module is measured by the case module's one rule. [19]


- Defines the function `grammar_of` — The grammar that reads ``path``, or ``None`` when nothing does.. [2]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `grammar_of` (lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.. [2]



- Defines the function `parsed` — Whether a definition in ``path`` is distinguishable from a mention of it.. [3]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `parsed` (lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.. [3]




- Defines the function `typescript_anchor_identifier` — The direct identifier rooted by a complete TS call or generic type spelling..

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory_quality/style/citations/grammars.py:1-357 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060. Retired means the anchor no longer stands, not that the cited subject was deleted [4]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `typescript_anchor_identifier` (lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.. [4]




- Defines the function `language` — The loaded grammar, built once. A failure to load is fatal, never a fallback.. [6]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `language` (lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.. [6]






- `definitions` is not defined in this module any more: the walk lives in `memory_quality/style/citations/extents.py`, returning every name a file binds at any depth with the extent of the construct that binds it. Source caption: `definitions`







- Defines the function `_walk` — Every node in the tree, at any depth, in DOCUMENT ORDER.. [8]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_walk` (lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.. [8]



- Defines the function `_widened` — ``node`` grown outwards through the syntax that decorates or exports it.. [9]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_widened` (lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.. [9]




- Defines the function `_span` — The one-based line range ``node`` occupies..



> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_span` (lines 282-286) — The one-based line range ``node`` occupies.. [10]




- Defines the function `_text`. [11]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_text` (lines 289-290). [11]



- Defines the function `_python_names` — The names one Python construct binds.. [12]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_python_names` (lines 293-299) — The names one Python construct binds.. [12]



- Defines the function `_python_targets` — The plain names an assignment target binds, unpacking nested tuples and lists.. [13]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_python_targets` (lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.. [13]



- Defines the function `_script_names` — The names one JavaScript or TypeScript construct binds.. [14]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_script_names` (lines 317-323) — The names one JavaScript or TypeScript construct binds.. [14]



- Defines the function `_script_targets` — The names a declarator binds, unpacking destructuring one alternative at a time.. [15]


> Retained earlier card wording; superseded by the current account above:
> - Defines the function `_script_targets` (lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.. [15]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory_quality/style/citations/grammars.py:209-243 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 0b30d9358b6ef00be9af1bdeb6c22eb802bf8d1e. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory_quality/style/citations/grammars.py:1-357 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060. Retired means the anchor no longer stands, not that the cited subject was deleted.
