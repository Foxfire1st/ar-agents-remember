# mcp/src/agents_remember/memory_quality/style/citations/extents.py

## Governing Overview


[overview](../../overview.md)

## Purpose

Resolve source symbol bindings and qualified declaration spans shared by conversion, reference reads and the curator writer.

## Code Commentary

`Extent` retains widened construct range, kind and declaration line; `definitions` adapts `grammars.bindings`, including assignments/declarators, to definition extents. `qualified_spans` filters nested names by containment and deduplicates ranges; one symbol is bound only when a single distinct span remains. Quote/heading/occurrence range generation, FileView caching and range merging are absent.

### Logic

`Extent.test_case` is carried from grammar bindings. An exact-name lookup in `qualified_spans` keeps every test-case occurrence, even equal line spans, so same-line duplicate bare titles remain ambiguous. Ordinary exact bindings still deduplicate; only a name without an exact key uses dotted containment. `definitions` accepts `Sequence[str]`. This current mechanism qualifies the older unconditional distinct-span description below; quote, heading and unsupported-title behavior are not broadened, and no execution result is claimed.

Module-level surface:

- `Extent` (class, lines 16-27) — One range an anchor occupies in a file, and how it was found. A `DEFINITION` extent also carries `declaration`: the line the declaration itself begins on, which differs from `start` for a decorated Python definition because the extent is widened to cover its decorator (it is `None` for every other kind, where the two coincide).





- `definitions` (function, lines 30-52) — Every name this file binds at any depth, and the extent of the construct binding it, filled from `grammars.bindings` so each `DEFINITION` extent also records the line its declaration begins on.
- `qualified_spans` (function, lines 55-74; MIK-R24) — The distinct extents binding `name` in one file's `definitions`. `Holder.method` is the `method` defined inside a `Holder` definition, so a same-named method of another class does not make the name ambiguous. A symbol anchor names one construct only when exactly one span comes back. It is the one symbol-binding rule: the curator writer (`application/knowledge_writer/code_anchors._bound_spans`, MIK-R12), the conversion (`memory/conversion/code_objects.CodeObjects.symbol_span`, MIK-R24) and the converted-tree reference check (`memory_quality/reference_state`) all call it, so a symbol binds the same way wherever it is resolved. The conversion-format version pins its behaviour (MIK-R24 rule 6).















### Conventions

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

### Todos

None.

## Evidence

- Definition extents carry the test-case tag, and exact-name test-case spans preserve occurrence multiplicity while ordinary names retain deduplication. [51]



### Repo-Internal References



- `qualified_spans` owns the current boundary described above. [26]





This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.


- Defines the class `Extent` — one range an anchor occupies in a file, and how it was found. [29]








- Defines the function `definitions` — every name this file binds at any depth, and the extent of the construct binding it. [35]



- The one symbol-binding rule, shared by the curator writer, the conversion and the reference check. [36]
