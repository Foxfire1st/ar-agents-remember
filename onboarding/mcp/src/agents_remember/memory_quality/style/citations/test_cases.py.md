# mcp/src/agents_remember/memory_quality/style/citations/test_cases.py

## Governing Overview

[Area overview](../../overview.md)

## Purpose

Extracts plain-string JavaScript/TypeScript test titles for citation definitions and explains unsupported proof targets.

## Code Commentary

Only literal it/test calls with valid plain-string first arguments are cases. Leading comment nodes are skipped. Escape decoding combines valid UTF-16 pairs while preserving lone surrogate units; enclosing literal describe titles form a qualified name alongside the bare title. Computed suite titles prevent qualification. refusal distinguishes skip/todo/each and computed titles and directs callers to line_range.

## Invariants And Boundaries

Filename eligibility is the separate .test./.spec. predicate. Ambiguous or unsupported titles are not silently repaired into unique symbol proofs; source extraction is not test execution.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Extracts plain-string JavaScript/TypeScript test titles for citation definitions and explains unsupported proof targets. Filename eligibility is the separate .test./.spec. predicate. Ambiguous or unsupported titles are not silently repaired into unique symbol proofs; source extraction is not test execution. [1]
