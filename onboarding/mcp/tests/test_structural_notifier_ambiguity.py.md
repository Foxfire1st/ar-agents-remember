# mcp/tests/test_structural_notifier_ambiguity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_notifier_ambiguity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:03+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves that malformed or ambiguous canonical routes fence only their own notifier row/finding while
unrelated retry, expiry, and heartbeat work continues.

## Code Commentary

### Logic

A focused read-only cohort first proves that rebind evaluation, state-signal holding, boundary drain,
and current-manager projection all fence an ambiguous manager seat without selecting a row. One
sweep scenario then seeds duplicate managers plus an invalid stale structural chain, then checks that the
ambiguous row is skipped, the malformed row never becomes actionable, an unrelated row redelivers,
and the heartbeat advances. A second scenario forces ambiguous architect resolution during expiry
preparation and proves only that expiry remains pending while an unrelated row expires normally.

### Conventions

The tests run a real notifier sweep over temporary catalog, inbox, expectation, event, and heartbeat
stores. They assert both the returned actions and durable post-sweep rows.

### Invariants And Boundaries

- Ambiguity never selects the first catalog row or an alternate recipient.
- One invalid structural chain cannot abort the sweep or consume unrelated budget.
- Skipped rows stay pending for a later unambiguous pass.
- The sweep heartbeat advances despite contained route failures.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is repository-local notifier forcing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Read-only rebind and state-signal evaluators fence only the ambiguous manager seat. | `test_read_only_evaluators_fence_only_the_ambiguous_seat` | mcp/tests/test_structural_notifier_ambiguity.py:36-105 |
| Ambiguous and malformed rows are contained while unrelated redelivery and heartbeat continue. | `test_ambiguous_row_is_skipped_while_unrelated_retry_and_heartbeat_continue` | mcp/tests/test_structural_notifier_ambiguity.py:108-206 |
| Ambiguous expiry preparation skips one row while an unrelated expiry and heartbeat complete. | `test_ambiguous_expiry_mailbox_skips_only_that_row_and_heartbeat_continues` | mcp/tests/test_structural_notifier_ambiguity.py:209-286 |

## Cross-Repo References

No cross-repository dependency governs this test module.

## Update History

- 2026-08-26T16:03+02:00 — Post-failure repair: added direct read-only ambiguity forcing and gave
  the unrelated expiry row a valid non-seat address, preserving per-row containment. No certifying
  test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for per-row notifier ambiguity
  containment. Verification remains closeout-owned.
