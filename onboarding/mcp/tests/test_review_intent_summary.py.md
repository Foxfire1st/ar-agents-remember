# mcp/tests/test_review_intent_summary.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins changed-intent summary counts and typed answer states over two selected test datasets.

## Code Commentary

The six test functions distinguish added/revised/removed statements and guarantees from realization-only and membership-only changes. A revised member shared by two families counts once on each side. Status-only invariant or version-only family successors count as revisions; a same-guarantee member change remains membership-only. Divergent heads make the summary partial; absent knowledge carries an unavailable refusal and no counts. The route returns typed answers with 200 and an unwired process with 503.

`_shared_base` and `_extend` populate/copy index-shaped datasets through test-only RowStore, family, membership and realization constructors imported from knowledge_rows_test_support. The actual intent_summary_of and route readers are exercised by the assertions; no shipped canonical writer, write lock or admission guarantee is measured by those fixture constructors.

### Logic

- `_shared_base` authors a common ancestor (`A` shared by two families, `B`, `D` realized once,
  families `F1 {A, B}` and `F2 {A, D}`); `_extend` copies it to an after side; `_resolution` builds the
  `ReviewCandidateResolution` the summary reads.
- **Counts:** added, revised and removed statements and guarantees are `+`/`−`; realization-only and
  membership-only changes are typed apart (+3 −4, realization_only 1, membership_only 1). A revised
  member shared by two families counts once on each side.
- **Record-only successors (L47-R1-F3):** a status-only invariant successor and a version-only family
  successor each count (1, 1); a same-guarantee successor with a new member stays `membership_only`.
- **States:** divergent successors make the answer `partial`; an absent candidate dataset is
  `unavailable` with its refusal and no counts; the route answers every typed state with 200 and an
  unwired process with 503.

### Conventions

Registered in the `unit-regression` lane of `test-evidence-lanes.toml` (an unregistered test file is
refused by the lane gate). It uses local constants rather than the exact-consumer
`read_scope_test_support` module, which would have made it a consumer of that support (worker event
E2). The module docstring states the route's status idiom (review F6).

### Invariants And Boundaries

A revert of the F3 rule
(`review_intent_summary.py` at A1) fails the record-only case (`assert (0, 0) == (1, 1)`, review R2).

### Todos

None.

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

### Docs References

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

- The shared ancestor the count cases extend. [16]
- Added/revised/removed as +/−, relationship-only as typed counts. [17]
- A shared revised member counts once per side. [18]
- Record-only successors count; a same-guarantee member change stays typed. [19]
- Divergent heads are `partial`. [20]
- Absent knowledge is `unavailable`, never zero. [21]
- 200 for every typed state, 503 unwired. [22]
- The lane registration. [23]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
