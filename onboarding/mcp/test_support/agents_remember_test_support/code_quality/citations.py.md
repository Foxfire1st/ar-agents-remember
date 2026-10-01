# mcp/test_support/agents_remember_test_support/code_quality/citations.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Resolve repository path citations in package comments and docstrings.

## Code Commentary

### Logic

Module-level surface:

- `Citation` (class, lines 80-95) — One prose reference to a path, with the line anchor it carried.
- `anchors` (function, lines 98-108) — Directory names a citation may start with, derived from the tree.
- `prose_spans` (function, lines 111-125) — ``(line, text)`` for every comment and docstring -- prose, never a string operand.
- `_docstrings` (function, lines 128-139)
- `citations_in_source` (function, lines 142-162) — Every in-grammar citation in one module's prose.
- `resolve` (function, lines 165-171) — The file a citation names, or ``None`` when no declared root holds it.
- `_anchor_offender` (function, lines 174-187) — A citation whose line anchor points past the end of the file it resolved to.
- `module_citation_offenders` (function, lines 190-210) — Every citation in one module that does not resolve, or overruns its target.
- `unresolved_citations` (function, lines 213-223) — Every prose citation in the package that names a path this repository lacks.
- `all_citations` (function, lines 226-234) — Every in-grammar citation in the package -- what the check is actually watching.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Citation` (lines 80-95) — One prose reference to a path, with the line anchor it carried.. [1]
- Defines the function `anchors` (lines 98-108) — Directory names a citation may start with, derived from the tree.. [2]
- Defines the function `prose_spans` (lines 111-125) — ``(line, text)`` for every comment and docstring -- prose, never a string operand.. [3]
- Defines the function `_docstrings` (lines 128-139). [4]
- Defines the function `citations_in_source` (lines 142-162) — Every in-grammar citation in one module's prose.. [5]
- Defines the function `resolve` (lines 165-171) — The file a citation names, or ``None`` when no declared root holds it.. [6]
- Defines the function `_anchor_offender` (lines 174-187) — A citation whose line anchor points past the end of the file it resolved to.. [7]
- Defines the function `module_citation_offenders` (lines 190-210) — Every citation in one module that does not resolve, or overruns its target.. [8]
- Defines the function `unresolved_citations` (lines 213-223) — Every prose citation in the package that names a path this repository lacks.. [9]
- Defines the function `all_citations` (lines 226-234) — Every in-grammar citation in the package -- what the check is actually watching.. [10]
