# mcp/tests/test_l6_diff_coverage_nw2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_nw2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for diff-coverage batch NW2. Covers the remaining changed lines and branches in citation source-index storage, citation provenance, terminal preflight validation, harness dispatch, finding serialization, and operator-inbox consume.

## Code Commentary

- `TestDatabaseOpen` covers sqlite errors, corrupt databases, and quick-check branches.
- `TestQuoteQueries` covers empty quotes, candidate streams, and quote-file iteration.
- `TestTerminalValidationBranches` covers absent-local preflights and provider-blocker iteration.
- `TestHarnessDispatch` covers launch-selection error refusal.
- `TestOperatorInboxConsume` covers consume without an expectation row.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestDatabaseOpen` (lines 93-122). | `TestDatabaseOpen` | mcp/tests/test_l6_diff_coverage_nw2.py:93-122 |
| Defines the class `TestQuoteQueries` (lines 168-202). | `TestQuoteQueries` | mcp/tests/test_l6_diff_coverage_nw2.py:168-202 |
| Defines the class `TestTerminalValidationBranches` (lines 228-276). | `TestTerminalValidationBranches` | mcp/tests/test_l6_diff_coverage_nw2.py:228-276 |
| Defines the class `TestHarnessDispatch` (lines 279-316). | `TestHarnessDispatch` | mcp/tests/test_l6_diff_coverage_nw2.py:279-316 |
| Defines the class `TestOperatorInboxConsume` (lines 333-348). | `TestOperatorInboxConsume` | mcp/tests/test_l6_diff_coverage_nw2.py:333-348 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
