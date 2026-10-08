# mcp/tests/test_review_intent_summary.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins changed-intent summary counts and typed answer states over two selected test datasets.

## Code Commentary

The six test functions distinguish added/revised/removed statements and guarantees from realization-only and membership-only changes. A revised member shared by two families counts once on each side. Status-only invariant or version-only family successors count as revisions; a same-guarantee member change remains membership-only. Divergent heads make the summary partial; absent knowledge carries an unavailable refusal and no counts. The route returns typed answers with 200 and an unwired process with 503.

`_shared_base` and `_extend` populate/copy index-shaped datasets through test-only RowStore, family, membership and realization constructors imported from knowledge_rows_test_support. The actual intent_summary_of and route readers are exercised by the assertions; no shipped canonical writer, write lock or admission guarantee is measured by those fixture constructors.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_counts_statement_and_guarantee_heads_and_keeps_other_changes_apart` supplies the current fixture or assertion described above. [9]
- `test_a_record_only_successor_counts_once_on_each_side` supplies the current fixture or assertion described above. [10]
- `test_an_identity_without_one_head_makes_the_summary_partial` supplies the current fixture or assertion described above. [11]
- `test_missing_knowledge_is_unavailable_with_its_refusal_never_zero` supplies the current fixture or assertion described above. [12]
- `test_the_route_answers_every_typed_state_in_the_body` supplies the current fixture or assertion described above. [13]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [14]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [15]
