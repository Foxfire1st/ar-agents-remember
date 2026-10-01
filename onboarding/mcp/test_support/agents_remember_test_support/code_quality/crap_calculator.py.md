# mcp/test_support/agents_remember_test_support/code_quality/crap_calculator.py

## Governing Overview

[Quality support overview](overview.md)

## Purpose

`crap_calculator.py` implements CRAP-Calculator: it combines Radon cyclomatic complexity
with the **branch** coverage Coverage.py emits and reports a per-function CRAP score. It is
a diagnostic step of the quality wrapper, and `diff_coverage.py` reuses its coverage reader.

```text
CRAP = complexity**2 * (1 - branch_coverage)**3 + complexity
```

## Code Commentary

### Coverage Is Branch Coverage, And A Statement-Only Report Is Refused

The formula is defined over *branch* coverage, and the coverage term is the only thing a
test can move. `load_coverage_by_path` reads `executed_branches` and `missing_branches`
alongside `executed_lines`/`missing_lines`, and `require_branch_measurement` **raises**
when `meta.branch_coverage` is not `true`.

That refusal is the point. `executed_branches`/`missing_branches` are simply *absent* from
a statement-only report, so without the check every function would read as having no
branches, every ratio would silently collapse back to the statement ratio, and CRAP would
go on being computed over a metric it is not defined against — the exact defect this reader
was changed to remove. Turning `[tool.coverage.run] branch` off therefore fails report integrity
loudly instead of softening it.

`parse_branch_arcs` raises on a malformed entry rather than dropping it, for the same
reason: a silently skipped arc is a branch that reads as taken, which moves a score in the
forgiving direction.

Arcs are attributed to a function by their **source** line — the branching statement —
because a destination is frequently outside the span (a `return` arc leaves the function,
and Coverage.py writes the exit destination as a negative number).

### One Ratio, No Metric Switching

`coverage_ratio_for_function` divides `covered_lines + taken_arcs` by
`executable_lines + taken_arcs + untaken_arcs` — the same ratio Coverage.py reports as
`percent_covered` under `branch = true`. A function containing no branch at all is not a
special case: its arc terms are both zero and the same division applies. That degeneration
is arithmetic, not a fallback, so two functions' scores are always the same measurement and
the threshold means one thing everywhere.

Two edge cases are distinguished deliberately:

- a span that is entirely excluded (`# pragma: no cover`) has a zero denominator and scores
  as **covered** — a deliberate opt-out;
- a file the report never mentions is carried by `has_data=False` and scores as **wholly
  uncovered**, so unmeasured complex code stays visible as risk.

### Production Review Threshold

`DEFAULT_CRAP_THRESHOLD = 20.0` identifies production functions worth examining. Scores at or
above it do not fail delivery. The wrapper requests simpler code, a meaningful behavioral test,
or a concise justified acceptance; no coverage percentage, baseline, or exception registry is
required. Tests and verification-support packages are outside the wrapper's production scoring
roots. A standalone calculator still scores the paths its caller supplies.

Complexity and Coverage.py arcs describe different aspects of control flow: short-circuit
expressions can add Radon decisions without producing corresponding arcs. Inspect the actual
function before choosing a remedy; a score alone does not demonstrate a missing behavior.

### Radon Is Load-Bearing Here, And Only Here

`radon cc` and `radon mi` are relabelled *reports* in the quality wrapper because they exit
0 whatever they find. That is a statement about the **gate steps**, not about the library.
`complexity_blocks` imports `radon.complexity` and calls `cc_visit` for the complexity term
of every CRAP score, raising a clear "install the development requirements first" error when
it is absent. Removing Radon from the dependency set would remove CRAP. Radon is the report;
Radon is also CRAP's complexity engine.

### Shared With The Diff Coverage Report

`load_coverage_by_path`, `FileCoverage` and `coverage_keys` are imported by
`diff_coverage.py`, which re-keys the result on repo-relative posix paths. Two consequences
worth knowing: the branch-data refusal above applies to the changed-lines report as well, and
both rails count the same units (statements plus branch arcs) from the same report.

### Reporting Without A Coverage Prescription

The calculator renders function scores and file rollups. The removed `coverage_clearing` helper
has no replacement: the wrapper identifies review findings without prescribing tests to reach a
percentage. Invalid input remains an error even though a high score is diagnostic.

## Invariants And Boundaries

- CRAP-Calculator consumes coverage data; it does not run pytest or coverage itself.
- **A report without `meta.branch_coverage == true` is refused, not degraded.**
- Radon is a report in the gate and the complexity engine here. Both are true at once.
- `DEFAULT_CRAP_THRESHOLD` is **20.0**, a diagnostic review trigger without a score exception registry.
- Scores are function/method level. File rollups are summaries over function scores, not
  replacements for the function-level risk list.
- Malformed branch arcs raise; they are never dropped.
- An unmeasured file scores as wholly uncovered; a `# pragma: no cover` span scores as
  covered. These are different states and must not be collapsed.
- Radon and coverage are development dependencies; this helper should not be imported by MCP
  runtime paths.
- The user-facing helper name is `CRAP-Calculator`; the Python module remains import-safe as
  `crap_calculator`.

## Evidence

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Bounded coverage term and CRAP formula [1]
- Coverage reader and branch-data requirement [2]
- Statement-plus-arc ratio and excluded-span behavior [3]
- Diagnostic review label, function and file summaries [4]
- Render scores without score-based failure [5]
