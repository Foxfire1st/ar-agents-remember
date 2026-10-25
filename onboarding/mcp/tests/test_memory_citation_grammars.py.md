# mcp/tests/test_memory_citation_grammars.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Language-aware declaration resolution for citation repair.

## Code Commentary

### Logic

`TestCaseDefinitionTests` adds plain test/spec title extraction across the supported JavaScript-family extensions. Nested describe titles bind qualified names and unique bare case names; a non-test filename does not acquire those case definitions. Plain-string escapes decode, UTF-16 pairs agree with scalar titles, lone units remain represented, and duplicate occurrences remain ambiguous even on one line. Comment extras do not replace the semantic first argument: computed/nonstring first arguments do not borrow a later string. Unsupported forms refuse with a reason: skip, todo, skipIf, runIf and fails cases get no range offer, while each, for and computed-title forms are offered a `line_range`. These added source cases do not claim a parser run or support for the refused forms.

Current tests derive named declaration spans from grammars.bindings. Python decorator/class/member and TypeScript/TSX/JavaScript binding cases remain. Removed pure-move repair, URL quote matching and pooled-interface repair fixtures are historical, not current runtime-repair guarantees.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A parser-supported declaration is stronger evidence than textual similarity. Missing grammar support cannot silently justify a confident move. The retired recorded-stamp relocation fixtures do not provide a current repair route.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence


- The new test-title cases cover qualified/bare names, escapes, UTF-16/lone-unit handling, ambiguity, semantic-first arguments and explicit unsupported-form refusals. [11]



### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- A decorated definition is stamped from its first decorator. [4]
- A class and its methods and attributes all bind. [5]
- Each declaration form binds its name over its own lines. [6]
- A tsx component is read by the tsx dialect. [7]
- A javascript module is read by the javascript grammar. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

## Current account — the range-refusal pins

The supported-case pins now assert the changed texts: the symbol refusal offers the exact `line_range`, the modifiers are read by name, and a form that runs and that no name reaches is offered its extent while a form that does not run is offered none.

- The unsupported-form cases assert the reason and that the offered remedy is a line range only where a range reaches the case. [12]
