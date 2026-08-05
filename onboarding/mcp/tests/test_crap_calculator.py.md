# mcp/tests/test_crap_calculator.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_crap_calculator.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Unit coverage for `agents_remember.code_quality.crap_calculator`: the CRAP formula, the
join of Radon function complexity with Coverage.py data, file rollups, and table/JSON CLI
rendering.

## CRAP Consumes Branch Coverage (260731-EFA-L2)

The reader was changed to consume **branch** coverage, not statement coverage.
`crap = cc**2 * (1 - coverage)**3 + cc` is defined over branch coverage, and the coverage
term is the only thing a test can move. The calculator reads the `executed_branches` /
`missing_branches` fields Coverage.py emits under `[tool.coverage.run] branch = true`, and
**refuses** a report produced without them. Arcs are `[source_line, destination_line]`
pairs attributed to a function by their *source* line.

The tests that pin this:

- `test_a_partially_taken_branch_lowers_the_score_a_statement_reader_calls_perfect` — the
  defect the change removes, in one function. Every statement of `branchy` runs, so a
  statement-only reader scores it 1.0 and reports the bare complexity; the untaken false
  arm is invisible to it.
- `test_a_function_without_branches_is_scored_by_the_same_division` — the zero-branch case
  takes no special path, no metric switch, and no division by zero.
- `test_a_report_without_branch_measurement_is_refused` — **no silent fallback.**
  Statement-only input fails loudly rather than scoring low. This is the property that
  makes the whole gate honest: a coverage run misconfigured without `branch = true` cannot
  produce flattering CRAP numbers.
- `test_a_malformed_branch_arc_raises_rather_than_being_dropped`.
- `test_well_formed_arcs_survive_including_the_negative_exit_endpoint` — Coverage.py encodes
  "this branch leaves the function" as a negative destination line; it is a real arc, not
  a parse error.

`branch_report()` is the module's fixture helper: a Coverage.py JSON report that declares
branch measurement, as the reader requires.

## Threshold

`DEFAULT_CRAP_THRESHOLD` is **20.0** (was 30.0). The value was chosen against the measured
branch-coverage distribution of `mcp/src/agents_remember` on 2026-07-31 under the full
suite; the reasoning, including why 30.0 was a weak gate under either metric and the
Radon-vs-Coverage.py disagreement about what a branch is, is recorded in the module header
of `crap_calculator.py`. All 46 offenders under the new threshold were cleared — 41 by
being tested, 5 by being split. There is no exemption file beside the threshold;
`test_code_quality_check.py::CrapThresholdEnforcementTests` asserts that.

`coverage_clearing(complexity, threshold)` inverts the formula so the gate can tell an
offender the branch coverage that would clear it, and returns `None` when no coverage can
— the "split this instead" case.

## Invariants And Boundaries

- These tests do not run pytest-cov; they feed synthetic coverage JSON directly into the
  calculator.
- The fixture stays temporary and does not require repository-wide coverage data.
- A report without branch fields is an error, never zero-coverage and never full coverage.
- Function-level scoring is the primary contract; file rollups and rendering are covered as
  derived behaviour.
- Missing coverage *file* (as opposed to missing branch measurement) still counts as zero
  coverage.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CRAP-Calculator owns the formula, branch-arc attribution, Radon integration, the clearing-coverage inversion, and both renderings. | "class FunctionScore" | mcp/src/agents_remember/code_quality/crap_calculator.py:63-63 |
| The wrapper side: threshold enforcement, per-offender failure lines, and the no-exemption-file assertion. | `CodeQualityCheckTests` | mcp/tests/test_code_quality_check.py:38-165 |
| `[tool.coverage.run] branch = true` — without it the reader refuses. | "[tool.ruff]" | pyproject.toml:1-1 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: rewritten. The previous card described a
  statement-coverage reader; CRAP now consumes branch coverage and refuses a report without
  it. Recorded the five branch-arc tests, the 30.0 → 20.0 threshold change and where its
  justification lives, and `coverage_clearing`'s split-instead-of-test answer. Verification
  metadata is pinned to the leaf's reformat commit until closeout stamps the code commit.
- 2026-05-24T06:12+02:00: Updated after tests added rollup and CLI rendering coverage.
- 2026-05-24T06:05+02:00: Created unit coverage for CRAP-Calculator.
