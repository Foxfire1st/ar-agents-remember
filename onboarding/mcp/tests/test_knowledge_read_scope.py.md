# mcp/tests/test_knowledge_read_scope.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Pins exact scope stopping, retained-revision grouping, deterministic paging and read-only refusals.

## Code Commentary

Path and exact revision seeds close over the appropriate directly containing families, siblings and recorded locations; an advertised family is reached only by selecting it. Identity seeds group retained revisions separately, while an exact revision excludes its siblings in history. Claim identities, repeated membership edges and distinct source locations are counted separately.

The ordered page stream keeps one snapshot/manifest across continuation, names truncation and registration/selector absence, and refuses budgets or selection bounds that cannot hold the next result. Refused reads preserve every table and the logical digest; selection remains in the requested namespace.

The dataset is populated by read_scope_test_support and test-only knowledge_rows_test_support RowStore. Direct fixture inserts and production-shaped constructor names do not enforce the retired production write-admission rules. The current scope selection/page owners are the behavior under test.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_an_exact_family_revision_seed_stops_after_its_own_members` supplies the current fixture or assertion described above. [19]
- `test_an_identity_seed_returns_every_retained_revision_as_its_own_group` supplies the current fixture or assertion described above. [20]
- `test_every_page_declares_the_same_snapshot_and_manifest_and_the_union_equals_the_selection` supplies the current fixture or assertion described above. [21]
- `test_a_refused_read_leaves_every_table_and_the_logical_digest_unchanged` supplies the current fixture or assertion described above. [22]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [23]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [24]
