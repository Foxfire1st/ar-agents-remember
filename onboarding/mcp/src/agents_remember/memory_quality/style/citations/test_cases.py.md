# mcp/src/agents_remember/memory_quality/style/citations/test_cases.py

## Governing Overview

[Area overview](../../overview.md)

## Purpose

Extracts plain-string JavaScript/TypeScript test titles for citation definitions and explains unsupported proof targets.

## Code Commentary

Only literal it/test calls with valid plain-string first arguments are cases. Leading comment nodes are skipped. Escape decoding combines valid UTF-16 pairs while preserving lone surrogate units; enclosing literal describe titles form a qualified name alongside the bare title. Computed suite titles prevent qualification. refusal names the blocking modifier for skip, todo, skipIf, runIf and fails, offers line_range for a case that runs and that no name reaches, and offers none for a case that does not run.

## Invariants And Boundaries

Filename eligibility is the separate .test./.spec. predicate. Ambiguous or unsupported titles are not silently repaired into unique symbol proofs; source extraction is not test execution.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence


- Extracts plain-string JavaScript/TypeScript test titles for citation definitions and explains unsupported proof targets. Filename eligibility is the separate .test./.spec. predicate. Ambiguous or unsupported titles are not silently repaired into unique symbol proofs, a case that does not run is refused with no range offer, and source extraction is not test execution. [5]


## Current account — the case extent, the modifiers and the range remedy

The module now supplies the pieces a line-range proof needs. `span_of` is the one extent rule for a syntax node, shared with the grammar module; `title_of` reads the semantic first argument and decodes escapes and UTF-16 pairs; `is_case_call` recognizes an `it`/`test` callee and its modifiers by name (`each`, `for`, `only`, `concurrent`, `sequential`, `skip`, `todo`, `skipIf`, `runIf`, `fails`); `blocking_reason` reports the modifier that stops a case from running, read on the case and every enclosing `describe`; `pairing_titles` gives the titles a proof's evidence pairs with. `refusal` now names the real modifier rather than reporting `.skipIf` as `.skip`, and offers the case's exact `line_range` only where a modifier or a computed title explains the miss — `_offer_lines` builds that text — while a case that does not run gets no offer and a title that no call explains is reported as ambiguous with an `S`/`E` placeholder range for the curator to fill.

- One extent rule serves every citation here, so a case's lines are measured as every other extent is. [2]
- Modifiers are read by name on the case and on every enclosing suite, so `.skipIf` and `.runIf` are reported as themselves. [3]

- The refusal offers the exact lines where a modifier or a computed title explains the miss, and otherwise names the ambiguity with an `S`/`E` placeholder range for the curator to fill; a case that does not run gets no offer. [6]
