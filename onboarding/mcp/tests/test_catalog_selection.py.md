# mcp/tests/test_catalog_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_catalog_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `8133b6a9de2f787cb6c4527621a70123357aff31` |
| lastVerifiedCommitDate | 2026-09-08T13:24:49+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that test-evidence catalog consumer metadata selects both removed and added consumers while ignoring comments, order-only changes, and non-consumer policy changes. It also proves global population files remain global inputs.

## Code Commentary

### Logic

`_catalog` builds a compact catalog fixture. The tests distinguish consumer-set changes from comment/order changes, policy/version/path changes, and global configuration ownership.

### Invariants And Boundaries

- Removed and added consumers both remain affected.
- Consumer ordering and comments do not create a selection delta.
- Global test inputs are distinguished from catalog consumer metadata.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Consumer-selection behavior is defined by the retained tests. | `test_removed_and_added_consumers_both_remain_affected`; `test_non_consumer_policy_changes_keep_global_selection` | mcp/tests/test_catalog_selection.py:19-22; mcp/tests/test_catalog_selection.py:39-44 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture emits the catalog shape consumed by the selection helper. | `_catalog` | mcp/tests/test_catalog_selection.py:10-16 |
| Consumer differences select both sides while comments/order and policy-only changes do not. | `test_removed_and_added_consumers_both_remain_affected`; `test_comment_and_consumer_order_changes_do_not_select_tests`; `test_non_consumer_policy_changes_keep_global_selection` | mcp/tests/test_catalog_selection.py:19-44 |
| Global input ownership is asserted separately from consumer metadata. | `test_population_configuration_is_global_but_consumer_metadata_is_not` | mcp/tests/test_catalog_selection.py:47-50 |

## Cross-Repo References

None; these are local selection contracts.

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent test sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `90b637e74dd462cdc9fa72603b27d87821988ae67ba24502c02d318eea66c00b`). No test execution or future candidate verification stamp is claimed.
