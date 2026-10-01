# mcp/tests/test_knowledge_citation_bindings.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The citation-binding vocabulary's 25 collected unit cases: the generation-5 append, the closed state
vocabulary and its shipped-literal identity, the counts partition and key-form coverage, the projection
rule, and the closure's refusal and honesty properties. Every case runs against real Pydantic models
and the real registry — no store, no subprocess, no fixture invented for the occasion.

## Code Commentary

### Logic

The generation cases measure the append by **the generation it descends from**: `GENERATION_5`'s
tables begin with `GENERATION_4`'s twenty-one names and each inherited name keeps generation 4's
columns, and `test_the_generation_1_pin_still_recomputes_after_this_leaf_appends_a_generation` proves
the pinned generation-1 fingerprint is unaffected. `test_the_binding_table_has_no_content_address_digest_or_fingerprint_column`
scans the declared column set for identity-valued names — the case would fail if a digest column were
ever added. `test_the_locator_check_names_exactly_the_shipped_source_locator_union` and
`test_the_key_form_check_names_exactly_the_declared_key_forms` read the declared `CHECK` constraints as
text, so a fourth, binding-local spelling cannot be introduced silently.

`test_every_shared_fact_reports_the_identical_shipped_literal` is parametrized over the four shared
states and asserts membership of the shipped `ANCHOR_RESOLUTIONS`;
`test_the_binding_vocabulary_extends_the_shipped_one_only_in_one_direction` asserts the reverse
direction too, so the shipped vocabulary cannot acquire a citation fact. The counts cases drive
`CitationBindingCounts` from both directions (a report that dropped a declared state, and one whose
per-state counts do not partition the set), and the coverage cases refuse a record that leaves an
uncovered form uncounted.

The projection cases assert the three consequences directly, including `hasattr` checks on
`AssessmentDisplay` for a field that must not exist. The closure cases assert a genuine
`selection_incomplete` refusal with the bound reached and **no items and no counts**, that the result
has no semantic-completeness attribute, and that the enumeration returns every recorded binding with
exactly one state.

### Invariants And Boundaries

- Every case here is hermetic: in-process models, the real registry, temporary directories. There is
  no store open, no Git subprocess and no integration marker, which is why the module is registered in
  the unit lane.
- The cases assert **structure**, not literals where a literal would go stale: the generation sequence
  is checked as contiguous `1..N` with `ar-knowledge-sqlite/vN` names rather than as a hand-written
  list, so a renumber cannot leave a green case behind.
- The module-local helpers (`_projection_case`, the small model builders) are module-local test
  source. They are deliberately **not** registered in the governed test-input inventory, and must not
  be.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The append measured by the generation it descends from, by name, and the generation-1 pin recomputed after the append.** [1]
- **The case that scans the declared column set for an identity-valued name, which is how "no second identity authority" is enforced rather than promised.** [2]
- The two cases that read the declared `CHECK` constraints as text, so a binding-local locator or key-form spelling cannot appear. [3]
- **The shipped-literal identity, asserted per shared fact in both directions.** [4]
- The closed vocabulary agreeing with its facts in both directions. [5]
- **The counts partition refused in both directions, and the coverage that refuses to leave an uncovered form uncounted.** [6]
- The uncovered-form state distinct from an absent key, and the write-boundary refusal of a key without the declared mark. [7]
- **The three projection consequences measured directly.** [8]
- **The bound refusal with no items and no counts, and the absent completeness field beside the declared coverage.** [9]
- The enumeration returning every recorded binding with exactly one state, and an unresolvable key keeping its recorded key and attribution. [10]
- **The lane row this module occupies, and the lane it sits in — the unit lane, because every case here is hermetic.** [11]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No meaningful cross-repo references found.
