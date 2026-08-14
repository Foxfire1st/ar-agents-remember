# mcp/src/agents_remember/code_quality/post_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/post_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-10T07:30+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`post_coverage.py` owns the two fast, in-process rails that can run only after pytest has emitted
branch coverage: function-level CRAP scoring and the changed-lines/branches coverage floor. The
split keeps the command/orchestration module below the file-size soft limit without changing the
public `check.run_crap_calculator`, `check.crap_failure_line`, or `check.run_diff_coverage` aliases.

## Code Commentary

### Logic

`run_crap_calculator` refuses missing/vacuous/non-branch coverage, renders the bounded score table,
and then names every threshold offender with the coverage needed to clear it. `run_diff_coverage`
resolves and prints the base, scores statements and branch arcs on the diff, names uncovered units,
and fails a measured result below the configured floor. Targeted runs with no production modules
are explicitly not applicable rather than vacuous.

### Invariants And Boundaries

- These functions consume pytest's JSON; they never run or re-measure tests.
- CRAP and diff coverage remain enforcing rails with no baseline, allowlist, or exemption.
- Missing or invalid coverage fails closed.
- The `CoverageRailConfig` protocol is read-only so the frozen wrapper config satisfies it.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this repository-local quality policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain contract governs these post-pytest calculations. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper calls both rails after pytest and repeats them only after a conservative delta requires a full fallback. | `run_coverage_rails`; `complete_coverage_rails` | mcp/src/agents_remember/code_quality/check.py:517-559; mcp/src/agents_remember/code_quality/check.py:632-656 |
| CRAP calculation uses Coverage.py branch units and Radon complexity. | `calculate_scores` | mcp/src/agents_remember/code_quality/crap_calculator.py:294-305 |
| Diff measurement intersects coverage units with the resolved Git diff. | `measure` | mcp/src/agents_remember/code_quality/diff_coverage.py:289-317 |
| Existing suites continue to exercise the aliases exposed by `check.py`. | `TestCheckRails`; `WrapperIntegrationTests` | mcp/tests/test_diff_coverage.py:554-675; mcp/tests/test_l6_diff_coverage_code_quality.py:174-339 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| Both rails read only the current repository and the wrapper-produced artifact. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T07:30+02:00 — Created when the unchanged post-pytest rail behavior was extracted
  from `check.py` during retry-pipeline implementation. Verification metadata remains blank until
  closeout stamps the code commit.
