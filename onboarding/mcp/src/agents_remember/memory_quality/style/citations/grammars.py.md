# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Extract source bindings and test-case diagnostics with tree-sitter.

## Code Commentary

A scoped call reuses each exact TypeScript anchor input, including an unresolved spelling, until its request owner clears. Calls outside that scope use a separate process memo. Loaded grammars and parsed test-file trees keep their own owners.

`Binding` records a construct's widened extent, its declaration line and whether it is a test case. A decorated Python definition includes its decorators in the extent while retaining the actual `def` or `class` declaration line. An exported script declaration includes its export syntax.

`grammar_of` chooses a grammar by path; `parsed` tells whether the file supports parsed definitions. `typescript_anchor_identifier` recognizes a direct identifier rooted by a complete TypeScript call or generic spelling. `language` loads each grammar once; grammar-load failures propagate.

`bindings` walks the parsed tree in document order and emits declarations, assignment targets and recognized named script test cases. Python tuple/list assignments and script destructuring unpack their plain names. No case name is invented for an unsupported computed title. `_walk`, `_widened`, `_span` and `_text` own traversal, outward decoration/export ranges, shared one-based spans and source text extraction.

Within a definition scope, eligible JavaScript, TypeScript and TSX test inputs retain one parsed tree shared by bindings, refusal diagnostics and exact-case range lookup. The key includes path, contents and grammar. Ordinary source trees are not retained in this diagnostic table. Nested parsing scopes join the call; the outer scope clears it on every exit.

`test_case_refusal` supplies specialized diagnostics only for recognized script test files. `test_case_range(path, lines, start, end, reaches)` answers an exact case extent or a refusal. Its caller supplies name reachability, so a range is accepted only where no name reaches the case. `_span` delegates to `test_cases.span_of`.

## Relationships

`extents.definitions` adapts these bindings to definition extents and owns call-scoped definition reuse. The case modules own title/modifier analysis and exact-case reachability. Ordinary symbol diagnostics remain with callers outside recognized script test files.

## Evidence


- A call retains eligible parsed test inputs and clears them at the outer exit. [20]
- Bindings retain widened extents, declaration lines and recognized named test cases. [21]

- `grammar_of` selects the grammar for a path. [2]
- `parsed` identifies files whose definitions can be parsed. [3]

- `typescript_anchor_identifier` recognizes a complete direct TypeScript anchor spelling. A native request reuses the exact input’s answer until the request memo clears. [4]

- `language` loads the chosen grammar and propagates load failures. [6]
- `_walk` traverses every node in document order. [8]
- `_widened` includes decoration or export syntax. [9]
- `_span` uses the shared case-span rule. [10]
- `_text` extracts a node's source bytes. [11]
- `_python_names` extracts names bound by Python constructs. [12]
- `_python_targets` unpacks Python assignment targets. [13]
- `_script_names` extracts script declaration names. [14]
- `_script_targets` unpacks script destructuring targets. [15]
- Specialized unresolved-case diagnostics are restricted to script test files. [17]
- Exact range lookup returns a case or its refusal using the caller's name resolver. [18]
- Every extent uses the case module's span rule. [19]
