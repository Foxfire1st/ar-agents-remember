# mcp/tests/test_memory_case_ranges.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — the case extents a line range may prove

`grammars.test_case_range` is asked which case a given line span is. It answers either a `CaseExtent` carrying `start`, `end`, `kind`, `test_case` and the titles the evidence may use, or the refusal text opening `lines {start}-{end} of {path} are not a case a line range proves: `. The admitted set is every running form no name reaches: `.only`, `.concurrent`, `.sequential`, an `it.for` table, a computed title, a plain case inside a parameterised `describe.each`, and a title bound twice, where the two extents make neither a definition. A parameterised case is admitted only by its whole extent, and the inner `it.each([...])` that holds the parameters rather than the title and body is no case; it is refused with the failing span `1-3`.

Refusals read the modifier by name on the case and on every enclosing suite: `.skip` and `.todo` do not run, `.skipIf` and `.runIf` run only when the condition holds, `.fails` passes only when its body fails, a uniquely named case is a definition to be named `path::suite > plain`, lines inside a case name the extents they overlap (or say that none overlaps), and a file that is not a `.test.`/`.spec.` JavaScript or TypeScript file is refused by name. `test.describe`, `test.step` and `test.setTimeout` members are no case, while the inner `test` of a `test.describe` stays a definition. The symbol route's refusal offers the exact `"start"/"end"` lines for `.each` and offers no `line_range` for `.skip` or `.skipIf`.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Every running form that no name reaches is admitted by its whole extent, and a twice-bound title resolves to two extents that are no definition [1]

- Each blocking modifier is refused with its own name and text, on the case and on an enclosing suite [2]
