# mcp/tests/test_knowledge_diff_attribution.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pins changed-path attribution accounting and the limits of what an inspected mapping can establish.

## Code Commentary

The comparison partitions the measured changed-path population into disjoint attributed, confirmed-unregistered and unknown-attribution buckets. Unchanged mapped paths contribute no changed count, repeated claims contribute one path, and selected-subject links are distinguished from completely established outside-selection links. Family scope comes from exact membership revisions.

Unresolved or stale locators do not establish attribution. An unread snapshot prevents a negative conclusion and qualifies outside-selection membership; a known-empty inspected side can support absence. An unavailable observation carries null totals, while a partial denominator names omitted uncarriable paths.

The two-tree fixture and extra realization rows use test-only knowledge_rows_test_support constructors. `_author_candidate_claim` is a fixture helper despite its historical write-plane docstring. Surviving production anchor readers, source measurement and partition/comparison code supply the asserted output; this suite does not prove canonical write admission.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_measured_changes_are_partitioned_once_and_the_buckets_are_disjoint_and_exhaustive` supplies the current fixture or assertion described above. [14]
- `test_a_registered_mapping_that_did_not_resolve_does_not_establish_attribution` supplies the current fixture or assertion described above. [15]
- `test_one_uninspected_snapshot_turns_every_unmapped_change_into_undetermined_attribution` supplies the current fixture or assertion described above. [16]
- `test_an_unavailable_partition_states_no_total_and_never_a_measured_zero` supplies the current fixture or assertion described above. [17]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [18]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [19]
