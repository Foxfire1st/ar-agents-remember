# mcp/src/agents_remember/memory_quality/style/update_history/history_order.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`history_order.py` validates that onboarding `## Update History` sections use
timestamped bullets ordered newest-first.

## Code Commentary

### Logic

The checker scans Markdown files under an onboarding root, locates level-two
`Update History` sections, parses bullet timestamps, and emits structured
warnings for missing timestamps, invalid timestamps, and entries inserted below
older entries. Timezone-aware values are normalized before comparison.

### Invariants And Boundaries

- This checker reports style findings only; it does not rewrite onboarding.
- Continuation lines are ignored for ordering and belong to the preceding
  bullet by convention.
- The checker intentionally runs during closeout quality control, not at task
  start.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The memory quality runner registers this checker as `style.update_history.history_order`. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py) |
| Regression tests cover newest-first, out-of-order, and missing timestamp cases. | [test_memory_quality.py](agents-remember-md/mcp/tests/test_memory_quality.py) |

## Update History

- 2026-05-24T02:47+02:00: Created for the update-history ordering style check.
