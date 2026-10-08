# mcp/tests/test_knowledge_review_attribution_precedence.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Checks that attribution precedence never turns an unread knowledge half into a negative conclusion.

## Code Commentary

A readable side can positively attribute its linked path while the remaining population stays unknown. Empty converted knowledge is completely inspected and can confirm absence; a damaged or unreadable half cannot. The fixture uses exact tree indexes, not a fabricated first canonical generation or repaired origin record. These assertions delimit the read's knowledge state and make no run claim.

## Evidence

### Repo-Internal References

- `test_one_unreadable_knowledge_half_leaves_the_readable_side_attributed_and_the_rest_unknown` owns the current boundary described above. [9]
- `test_an_empty_converted_base_counts_as_completely_inspected_for_absence` owns the current boundary described above. [10]
- `test_a_damaged_knowledge_half_cannot_support_a_negative_attribution_conclusion` owns the current boundary described above. [11]
