# mcp/test_support/agents_remember_test_support/code_quality/crap_calculator.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/test_support/agents_remember_test_support/code_quality/crap_calculator.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`crap_calculator.py` implements CRAP-Calculator: it combines Radon cyclomatic complexity
with the **branch** coverage Coverage.py emits and reports a per-function CRAP score. It is
an enforcing step of the quality wrapper, and `diff_coverage.py` reuses its coverage reader.

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
was changed to remove. Turning `[tool.coverage.run] branch` off therefore breaks the gate
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

### The Threshold: 30.0 → 20.0, Chosen On Reach

`DEFAULT_CRAP_THRESHOLD = 20.0`. There is no baseline, allowlist or exemption file beside
it: a function at or above the score fails the gate and is cleared by covering its branches
or by being split.

The number that decided this was not the failure count but **reach** — how much of the tree
a threshold is capable of failing at all. A function's ceiling is `cc**2 + cc` at zero
coverage, but no function reaches zero coverage, because its own `def` line runs at import;
the observed floor across all 4,672 scored functions is 3.03%. Reach therefore moves in
steps:

| Threshold band | Lowest complexity that can ever fail | Unreachable functions |
| --- | --- | --- |
| 28–30 | cc >= 6 | 3,821 of 4,672 (81.8%) |
| 19–27 | cc >= 5 | 3,436 of 4,672 (73.5%) |
| <= 18 | cc >= 4 | 2,832 of 4,672 (60.6%) |

Every value from 28 to 30 has identical reach, so nudging inside that range changes which
functions are named and nothing about what the gate can see. 30 failed **0** functions on
statement coverage and 3 once branch coverage arrived: the same weak gate either way.

**20 is the anchor at the bottom of the middle band, and it is a statement about code rather
than about this tree**: `crap(4, 0) = 20` is the lowest score an entirely unexercised
four-path function can have, so the threshold is exactly the rule *"four independent paths
that no test ever enters is a finding"*. Nothing between 21 and 27 buys any reach over it,
so within that band the strictest value is the honest one. Concretely it demands branch
coverage above 53.6% at C901's ceiling of cc = 10, above 71.9% at cc = 15, and cannot be met
at all at cc >= 20 — which is not a second complexity gate, because `C901` already rejects
anything past 10.

**One measured caveat that decides which failures are honest.** The two terms are measured
by tools that disagree about what a branch is: Radon counts `and`/`or` short-circuits as
decisions, Coverage.py emits no arc for them. 69 of the 102 functions at cc >= 11 had fewer
branch arcs than their Radon complexity. The extreme case was
`observer/reducer.py::project_workspace` — Radon cc 25, **zero** branch arcs, 100% covered,
CRAP exactly 25.00, its complexity entirely ~20 `x or []` keyword defaults. No test could
move it; normalising those defaults took it to cc 5. So a threshold in this band is a claim
about complexity as well as about testing, which is why it belongs at a number defensible
without reference to which functions sit above it today.

**Cost when it was armed, all of it paid rather than recorded:** 46 of 4,469 functions. 41
were undertested and got real behavioural tests; 5 could not be cleared by any test
(`crap(cc, 1.0) = cc`) and were split — `project_workspace` 25 → 5, `_engine_process`
22 → 6, `_map_task_lifecycle` 22 → 3, `_map_collab_tool_call` 25 → 4, `parse_runner_config`
20 → 5. The tree now tops out at **19.83**
(`serving/claude_stream_state.py::ClaudeStreamState._complete_pending_on_disconnect`, cc 10
at 53.8%), so the margin is 0.17 and the next regression is a failure.

### Radon Is Load-Bearing Here, And Only Here

`radon cc` and `radon mi` are relabelled *reports* in the quality wrapper because they exit
0 whatever they find. That is a statement about the **gate steps**, not about the library.
`complexity_blocks` imports `radon.complexity` and calls `cc_visit` for the complexity term
of every CRAP score, raising a clear "install the development requirements first" error when
it is absent. Removing Radon from the dependency set would remove CRAP. Radon is the report;
Radon is also CRAP's complexity engine.

### Shared With The Diff Coverage Gate

`load_coverage_by_path`, `FileCoverage` and `coverage_keys` are imported by
`diff_coverage.py`, which re-keys the result on repo-relative posix paths. Two consequences
worth knowing: the branch-data refusal above applies to the changed-lines floor as well, and
both rails count the same units (statements plus branch arcs) from the same report.

### Inversion Used By The Wrapper's Failure Lines

`coverage_clearing(complexity, threshold)` solves the formula for `c` so the gate can say
what it is asking for. It returns `None` when the complexity term alone already reaches the
threshold — the case no amount of testing can fix — and `check.py` prints "split it" rather
than an impossible percentage.

## Invariants And Boundaries

- CRAP-Calculator consumes coverage data; it does not run pytest or coverage itself.
- **A report without `meta.branch_coverage == true` is refused, not degraded.**
- Radon is a report in the gate and the complexity engine here. Both are true at once.
- `DEFAULT_CRAP_THRESHOLD` is **20.0** and it binds: the worst function in the tree scores
  19.83. There is no CRAP baseline, allowlist or exemption file, and none may be added.
- Scores are function/method level. File rollups are summaries over function scores, not
  replacements for the function-level risk list.
- Malformed branch arcs raise; they are never dropped.
- An unmeasured file scores as wholly uncovered; a `# pragma: no cover` span scores as
  covered. These are different states and must not be collapsed.
- Radon and coverage are development dependencies; this helper should not be imported by MCP
  runtime paths.
- The user-facing helper name is `CRAP-Calculator`; the Python module remains import-safe as
  `crap_calculator`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Unit tests cover the CRAP formula, function-span coverage intersection, branch-arc parsing, and missing coverage data behavior. | `CrapCalculatorTests` | mcp/tests/test_crap_calculator.py:17-235 |
| The wrapper feeds pytest coverage into the CRAP rail and declares its two non-enforcing Radon report steps. | `run_coverage_rails`; `_radon_report_steps` | mcp/test_support/agents_remember_test_support/code_quality/check.py:368-392; mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:221-244 |
| The changed-lines coverage floor reuses this module's coverage reader and inherits its branch-data refusal. | "class DiffCoverage" | mcp/test_support/agents_remember_test_support/code_quality/diff_coverage.py:58-58 |
| `[tool.coverage.run] branch = true` is set here, with the measured effect on the aggregate recorded beside it. | "[tool.coverage.run]" | pyproject.toml:68-68 |
| Development tool guidance documents the source quality wrapper and CRAP-Calculator command flow. | `# Coding Tools & Repo Notes` | system/tools.md:1-296 |

## Update History
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired every claim that this reader
  consumes statement coverage and that the threshold stays at 30.0 with a named follow-up
  owner.** `load_coverage_by_path` now reads `executed_branches`/`missing_branches` and
  refuses a report whose `meta.branch_coverage` is not true; the threshold is 20.0, chosen on
  reach (`crap(4,0) = 20`) rather than on the failure count, with all 46 offenders cleared —
  41 by behavioural tests, 5 by splitting — leaving a 0.17 margin. Also removed the reference
  to the deleted `quality/complexity-baseline.txt`, and recorded that `diff_coverage.py`
  reuses this coverage reader. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf): recorded that Radon stays
  CRAP's complexity engine even though its two wrapper steps are labelled reports.

- 2026-05-24T06:30+02:00: Updated after the source quality wrapper started running CRAP-Calculator as part of the remembered suite.
- 2026-05-24T06:05+02:00: Created CRAP-Calculator for function-level complexity plus coverage risk reporting.
