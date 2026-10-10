# mcp/tests/test_knowledge_review_attribution_precedence.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Checks that attribution precedence never turns an unread knowledge half into a negative conclusion.

## Code Commentary
A readable side can positively attribute its linked path while the remaining population stays unknown. Empty converted knowledge is completely inspected and can confirm absence; a damaged or unreadable half cannot. The fixture uses exact tree indexes, not a fabricated first canonical generation or repaired origin record. These assertions delimit the read's knowledge state and make no run claim.

### Conventions

Marked `pytest.mark.evidence_unit`. Every case is function-scoped over `tmp_path` and states the
property it protects in its docstring.

### Todos
None.

## Evidence

### Repo-Internal References

- The empty-base case: a real empty converted Git base counts as completely inspected for absence; no canonical origin record invents its emptiness. [15]

- `test_one_unreadable_knowledge_half_leaves_the_readable_side_attributed_and_the_rest_unknown` owns the current boundary described above. [9]
- `test_an_empty_converted_base_counts_as_completely_inspected_for_absence` owns the current boundary described above. [10]
- `test_a_damaged_knowledge_half_cannot_support_a_negative_attribution_conclusion` owns the current boundary described above. [11]

- **The precedence cases: one unreadable half leaves the readable side attributed and the rest unknown; the same pair read completely confirms absence where the lost half could not; a damaged half cannot support a negative conclusion.** [12]
- The unit-regression lane row, beside its sibling's. [14]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs in-process against a temporary coordination root.

No meaningful cross-repo references found.
