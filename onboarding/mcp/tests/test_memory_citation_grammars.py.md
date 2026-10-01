# mcp/tests/test_memory_citation_grammars.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Language-aware declaration resolution for citation repair.

## Code Commentary

### Logic

With the TypeScript grammar a moved declaration resolves uniquely instead of matching mentions; without it the same move declines as ambiguous. Python extents include decorators, classes and members. TypeScript, TSX and JavaScript constructs bind their own names, quoted URLs retain slashes and pooled interface members repair to one defining file.

The grammar fixtures now prove continuity rather than assuming it. `TypeScriptPureMoveTests.moved()` writes the cited `dashboard/src/rail.tsx` holding the `RailRow` declaration and commits it with `Tree.stamp()`, then writes the moved file, deletes the cited one with `remove_source`, and stamps the card at the commit that held the declaration. `TypeScriptInterfacePoolRepairTests.test_three_interface_members_in_another_file_repair_as_one_claim` does the same for `dashboard/src/panels/gone.ts` holding the `PanelProps` interface. The legitimate kind-preserving relocations therefore still repair because the same extent kind is provable at the recorded stamp; the grammar expectations themselves were not relaxed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A parser-supported declaration is stronger evidence than textual similarity. Missing grammar support cannot silently justify a confident move. A unique tree-wide name match is likewise not sufficient by itself: the relocation fixtures must show the same extent kind at the card's recorded stamp.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Cited declaration is written, committed and stamped, then moved and removed. [1]
- With the grammar the move is repaired onto the declaration. [2]
- Without the grammar the same move is declined. [3]
- A decorated definition is stamped from its first decorator. [4]
- A class and its methods and attributes all bind. [5]
- Each declaration form binds its name over its own lines. [6]
- A tsx component is read by the tsx dialect. [7]
- A javascript module is read by the javascript grammar. [8]
- A url does not lose its double slash during quote matching. [9]
- Three interface members in another file repair as one claim. [10]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
