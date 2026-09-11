# mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Quality support overview](overview.md)

## Purpose

`post_coverage.py` owns the two fast, in-process rails that can run only after pytest has emitted
branch coverage: function-level CRAP scoring and the changed-lines/branches diagnostic report. The
split keeps the command/orchestration module below the file-size soft limit without changing the
public `check.run_crap_calculator`, `check.crap_failure_line`, or `check.run_diff_coverage` aliases.

## Code Commentary

### Logic

`run_crap_calculator` refuses missing, vacuous, or invalid coverage and renders production scores.
Functions at or above the review threshold remain visible while returning success, with simpler
code, a meaningful behavioral test, or concise justified acceptance as possible responses.
`run_diff_coverage` prints the comparison base and measured statement/arc findings without a
percentage failure. Targeted runs with no production modules are explicitly not applicable.

### Invariants And Boundaries

- Both functions consume existing coverage JSON without rerunning tests.
- Metric values are diagnostic; missing or invalid evidence still fails.
- No coverage-floor configuration or coverage-clearing prescription remains.
- The read-only `CoverageRailConfig` is satisfied by the immutable wrapper configuration.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this repository-local quality policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain contract governs these post-pytest calculations. | — | — |

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| Report integrity failures versus diagnostic high scores | `run_crap_calculator` | mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py:36-101 |
| Locate findings without required coverage percentages | `crap_failure_line` | mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py:104-113 |
| Diagnostic measured coverage and explicit nonmeasured states | `run_diff_coverage` | mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py:116-162 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| Both rails read only the current repository and the wrapper-produced artifact. | — | — |

## Update History

- 2026-09-06T21:35:26+00:00 — Reconciled the d3610903 test-policy reduction against the current source, preserved integrity/ownership boundaries, and replaced stale forcing-suite citations with current owner evidence. Existing verification hash/date retained; source comparison is not final acceptance.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T07:30+02:00 — Created when the unchanged post-pytest rail behavior was extracted
  from `check.py` during retry-pipeline implementation. Verification metadata remains blank until
  closeout stamps the code commit.
