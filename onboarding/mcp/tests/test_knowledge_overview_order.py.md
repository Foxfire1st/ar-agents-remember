# mcp/tests/test_knowledge_overview_order.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Behavioral regression cases for the overview heading parser and mechanical trailing citation region. Each case replaces an overview in the converted-memory fixture and calls the actual validator; assertions check the owning rule, reported path and line or heading rather than a count-only surrogate.

## Code Commentary

`_overview()` replaces only the fixture route's Markdown. `_validate()` supplies the paired code fixture and defaults `leaf_publication=True`, without changing the shared fixture helper’s default. `_only()` requires exactly one refusing rule before returning its rendered findings. The direct no-publication control bypasses this local helper and calls `validate_tree` without the flag, asserting no R80 findings for three scaffold stub forms.

Heading cases cover nested leaf/date sections, legal indentation, closing hashes, escaped/tab-indented controls and the distinction between a title and a section. Citation-region cases distinguish intro prose before the first citation from interleaved or trailing prose and subsections. Fenced code remains a control; shown escaped/code-span brackets, hidden bracket text, list presentation and marker-keyword narration never create a prose exemption inside the region.

The split-citation case additionally calls `require_valid_commit(..., leaf_publication=True)` and requires `KnowledgeValidationError` naming the citation-placement rule. This witnesses the leaf-publication validator API, not a production closeout transaction.

## Invariants And Boundaries

The inside-region escaped-example expected value is refusal, while the same line before the region remains allowed. These cases pin the mechanical whitelist rather than the semantic topic of an example. Fixture citation-number/anchor validity remains owned by the shared converted-memory support.

This module supplies executable evidence; it does not establish semantic correctness or source correspondence of the repository's real overview corpus. Purpose-first and standalone-conversion integration cases also live in the broader validator test module.

## Evidence

- A nested leaf-named subsection refuses with its heading and rule. [1]
- Closing hashes retain the fixed purpose heading rather than changing its name. [2]
- An escaped example inside the trailing region refuses. [4]
- The same escaped example before the citation region remains allowed. [5]
- Narration cannot become an allowed line by carrying a marker keyword and escaped bracket. [6]

- Split citation prose refuses the validator with leaf publication explicitly selected. [3]
- Three scaffold overview forms produce no R80 findings without leaf publication. [7]
- The local order-test helper defaults publication while retaining caller overrides. [8]
