# mcp/tests/test_code_quality_check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_code_quality_check.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-12T00:08+02:00               |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_code_quality_check.py` verifies the fixed source quality suite wrapper.

## Code Commentary

### Logic

The tests import `agents_remember.code_quality.check` from `mcp/src` and use a
fake command runner to avoid launching Ruff, Pyright, Radon, or pytest subprocesses
during unit tests. The fake runner records command composition and writes a
synthetic coverage JSON report for the pytest step so the real
CRAP-Calculator path still executes. The runner now also receives the subprocess
environment, and one test asserts the wrapper puts this checkout's source import
root first on `PYTHONPATH` while preserving any pre-existing `PYTHONPATH` entry.
The command-composition test also asserts Pyright receives `--pythonpath` with
the active interpreter, which lets linked worktrees reuse the primary checkout
virtualenv without losing third-party import resolution.
L22 adds direct regressions that targeted configuration preserves the repository file-size arm and
that both development dependency entry points carry the same exact Ruff version.

### L23 Enclosure Progress-Report Configuration

The targeted-configuration regression now also defines every report-related CLI seam explicitly,
sets `AR_QUALITY_PROGRESS_REPORT`, and proves `config_from_args` derives the enclosure-owned
`progress_report` path while retaining the repository file-size arm. This pins the environment
fallback branch that clean and local quality executors share: a caller may omit the CLI report
argument, but the configured enclosure report must still reach the resulting quality configuration.
The same regression then supplies an explicit `args.progress_report` while the environment remains
set and proves that explicit path wins. Together the two calls pin both sides of the precedence
boundary—CLI selection first, environment only when the CLI seam is absent—without adding a second
configuration owner.

### Repository-Gate Parity After The Hook Split (260731-EFA-L1)

Two tests hold the local gates to the wrapper, and the split between them matters.

`test_repository_gates_use_default_strict_wrapper` scans the files that must literally contain
`agents_remember.code_quality.check` and must not contain `fail-on-crap-threshold`. That list is
now `.githooks/_gate.sh` and `.github/workflows/quality-checks.yml` — **not** the two hook files.
The hooks no longer inline the wrapper command; both `exec` the shared tiered body, and the full
tier is where the wrapper runs. The fix was to follow the indirection, not to drop the assertion.

`test_git_hooks_delegate_to_the_shared_tiered_gate` closes the hole that indirection would
otherwise open: `.githooks/pre-commit` must contain `exec "$hook_dir/_gate.sh" fast` and
`.githooks/pre-push` must contain `exec "$hook_dir/_gate.sh" full`. Together the two tests still
prove every repository gate reaches the wrapper with no threshold opt-out, while pinning the tier
each hook is wired to — so a pre-commit silently promoted to the full tier (the cost that trained
the `--no-verify` habit) or a pre-push silently demoted to the fast tier both fail here.

### Radon Is A Report, Not A Gate (260731-EFA-L2)

`RadonIsAReportNotAGateTests` is the class that holds the leaf's central claim in place.

- `test_radon_steps_are_declared_reports_and_the_rest_enforce` — exactly `radon-cc` and
  `radon-mi` carry a `report_note`; every other step is enforcing.
- `test_report_section_header_says_it_cannot_fail` — the printed section header for a
  report step contains the note, so the wrapper's own output never presents a Radon run
  as something that passed.
- `test_help_text_does_not_present_radon_as_enforcement` — the CLI description lists the
  enforcing steps and says Radon cannot fail the gate.
- `test_a_report_step_that_breaks_still_fails_the_gate` — a non-zero exit from a report
  step **does** fail the wrapper, reported as the tool breaking rather than as a finding.
  A tool that exits 0 on every finding can only exit non-zero when it is broken.

### Every Enforcing Step Can Fail (260731-EFA-L2)

`EveryEnforcingStepCanFailTests` holds the two steps this leaf added, and the complexity
rules **at full strength**. Both were configured-but-unenforced before the leaf: the
formatter ran in no gate at all, and `max-complexity = 10` was set while `C901` was
unselected. Arming them produced 67 complexity offenders, which were first parked behind a
shrink-only baseline and then — on the developer's correction — refactored outright.

- `test_the_ruff_step_routes_no_rule_away_from_itself` — the `ruff` step passes **no**
  `--extend-ignore` and no `--select`; it lints exactly what `pyproject.toml` selects.
- `test_the_complexity_rules_are_selected_and_nothing_ignores_them` — `C901`, `PLR0911`,
  `PLR0912`, `PLR0915` are selected and unignored.
- `test_ruff_rejects_an_over_complex_function_at_this_repository_configuration` — a real
  Ruff run, at this repository's real `--config`, rejects a function that trips all four
  rules at once (60 branches, 61 returns, 121 statements, cyclomatic complexity 61).
- `test_no_suppression_directive_in_the_tree_holds_a_complexity_rule_down` — no
  `noqa`/per-file-ignore anywhere in the tree may hold one of those codes down.
- `test_ruff_format_is_checked_over_the_whole_derived_scope`.
- `test_the_complexity_baseline_and_its_gate_step_are_gone` — **the ratchet is forbidden,
  not merely absent.** `quality/complexity-baseline.txt`, the
  `code_quality/complexity_baseline.py` module, its test module and its wrapper step were
  all built during this leaf and then deleted when the developer ruled that ratchets,
  baselines, grandfather lists and burn-down schedules are all forbidden. This test is what
  stops them coming back.

### PLR0913's One Exemption (260731-EFA-L2)

`ToolSignatureExemptionTests`. `PLR0913` is armed, and 163 parameter objects were
introduced so 274 of 293 long signatures could be fixed by extraction. The 19 that remain
are `@server.tool()` declarations under `mcp/src/agents_remember/mcp/registration/`, where
FastMCP derives the tool's **published JSON input schema** from the Python signature —
collapsing the parameter list into an object is a breaking wire change, not a refactor.

The per-file-ignore covers only that directory, and this class is what holds it shut:

- `test_plr0913_is_armed_and_nothing_globally_ignores_it`.
- `test_the_registration_modules_are_the_only_path_exempt_from_plr0913` — a second exempt
  path fails.
- `test_every_function_in_the_exempted_path_is_a_published_tool_declaration` — an **AST**
  walk over every file the pattern really resolves to (read from `pyproject.toml`, not
  from a path written in the test, so a widened pattern drags its new files into the walk
  instead of escaping it). Only `@server.tool()` declarations and the thin
  `register_*_tools(server, config)` registrars are allowed; the decorator is matched on
  the syntax tree, not on its spelling.
- `test_no_suppression_directive_in_the_tree_holds_an_argument_count_finding_down`.
- `test_ruff_rejects_a_seven_parameter_function_at_this_repository_configuration`.

### CRAP Has A Threshold, Not An Exemption List (260731-EFA-L2)

`CrapThresholdEnforcementTests`:

- `test_a_failing_gate_names_every_offender_not_only_the_reported_top`.
- `test_an_offender_is_told_the_branch_coverage_that_would_clear_it` and
  `test_the_clearing_coverage_inverts_the_crap_formula` — `crap = cc**2 * (1-cov)**3 + cc`
  inverts exactly, so the gate reports the coverage that would clear a function rather
  than only its score.
- `test_an_offender_that_no_test_can_clear_is_told_to_split_instead` — above a certain
  complexity, 100% coverage still fails; the gate says "split" rather than "test harder".
- `test_no_repository_gate_carries_a_crap_exemption_file`.

### Scope Is Derived, Not Written Down (260731-EFA-L2)

`GateScopeDerivationTests`:

- `test_module_declares_no_hand_written_scope_constant` — the retired
  `DEFAULT_SOURCE_PATHS` / `DEFAULT_TEST_PATHS` shape cannot come back.
- `test_scope_derived_from_this_checkout_reaches_the_whole_tree`.
- `test_a_script_outside_every_package_reaches_ruff_and_pyright` — the specific hole the
  leaf closed: a file that is in no importable package still reaches both rails.
- `test_scope_is_the_index_so_an_unadded_file_is_not_yet_part_of_the_tree` — `git ls-files`
  reads the index, which is exactly the content the pre-commit tier certifies.
- `test_top_level_packages_ignores_nested_packages`.
- `test_missing_testpaths_is_an_error_rather_than_a_default`,
  `test_a_project_with_no_pyproject_at_all_cannot_derive_where_the_suite_lives`,
  `test_a_pytest_table_that_is_not_a_table_reads_as_absent_rather_than_crashing`,
  `test_a_repository_tracking_no_python_is_refused_instead_of_scoped_to_nothing`,
  `test_python_that_belongs_to_no_package_leaves_coverage_nothing_to_measure` and
  `test_scope_failure_exits_non_zero_with_an_explanation` — a gate that cannot work out
  its scope refuses rather than certifying nothing.
- `test_a_derivable_scope_runs_the_gate_and_main_reports_its_verdict` — `main` owns no
  verdict of its own: it derives scope from the project root on the command line, then
  hands back whatever the gate decided, carrying the threshold and diff base through.

The sample projects these tests build are **real git repositories**, deliberately: every
rail of the wrapper reads the tree through git (`derive_scope` from `git ls-files`, the
changed-lines coverage floor from `git diff` against the merge base), so a sample project
that is not a repository would exercise nothing.

### Pytest Configuration Is Asserted, Not Assumed (260731-EFA-L2)

`PytestConfigurationTests` reads the real `[tool.pytest.ini_options]` and pins the
strictness switches, `python_classes` covering the `*Tests` house convention, and
`filterwarnings` erroring by default. Two of its tests are ratchets rather than checks:

- `test_the_warning_ignore_list_is_capped` asserts an **exact count of 5** ignores, not a
  ceiling. Paying one off forces the number down in the same commit, and adding one is a
  visible edit to a test.
- `test_registered_markers_and_the_suite_environment_gates_agree` scans the suite for
  `AR_*` / `AGENTS_REMEMBER_*` environment gates and reconciles them against the
  registered markers **in both directions**, so neither list can drift ahead of the other.

### Invariants And Boundaries

- Tests verify command order and fixed module selection without shelling out,
  including that Pyright receives the derived scope and the active interpreter path.
- Fixed check failures make the wrapper return nonzero.
- Missing coverage JSON makes the CRAP step fail.
- CRAP threshold hits fail the default wrapper, and the parser exposes no
  report-only or strict opt-in mode — and now no path arguments either.
- Repository-gate fixtures prove the shared tiered hook body and CI both invoke
  the same default wrapper command, and separately that each hook is wired to
  its intended tier (`pre-commit` → `fast`, `pre-push` → `full`). The wrapper
  itself runs in the full tier and in CI; the fast tier runs the generated-copy
  checks (skills, runtime assets, **harness trees**) plus Ruff,
  `ruff format --check`, and Pyright. The full tier is the only one that carries
  pytest, CRAP and the changed-lines coverage floor, because the floor needs a diff base.
- The wrapper threads an environment to the runner whose `PYTHONPATH` leads with
  this checkout's source import root, so the gate measures the current checkout.
- **Exactly two steps are reports** and both are Radon; every other step enforces.
- The `ruff` step routes **no** rule away from itself. There is no second complexity step
  and no baseline for one to hold against.
- **No ratchet, baseline, grandfather list or burn-down schedule may be reintroduced.**
  `test_the_complexity_baseline_and_its_gate_step_are_gone` enforces this.
- The only exemption anywhere in the gate is the `PLR0913` per-file-ignore over the MCP
  registration directory, and an AST test proves every function it reaches is a published
  `@server.tool()` declaration or its registrar.
- Scope assertions read the real repository through `derive_scope`; there is no fixture
  that could let a narrowed scope pass.
- The warning-ignore cap is an exact count, so the list can only shrink.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The source quality wrapper: enforcing steps, two declared Radon reports, and scope derived from `git ls-files` plus pytest `testpaths`. | `quality_steps`, `testpaths` | mcp/src/agents_remember/code_quality/check.py:320-366; mcp/src/agents_remember/code_quality/scope.py:111-111 |
| The changed-lines coverage floor the full tier carries, and its own behavioural suite. | "DEFAULT_DIFF_COVERAGE_FLOOR = 100.0"; "Score the changed lines, or report why there is nothing to score."; "def test_a_diff_below_the_floor_fails_the_wrapper(self) -> None:"; "def test_the_floor_runs_inside_the_wrapper_rather_than_beside_it(self) -> None:" | mcp/src/agents_remember/code_quality/diff_coverage.py:30-30; mcp/src/agents_remember/code_quality/diff_coverage.py:289-317; mcp/tests/test_diff_coverage.py:570-585; mcp/tests/test_diff_coverage.py:629-659 |
| CRAP-Calculator owns the function scoring used by the wrapper, and keeps Radon load-bearing. | `complexity_blocks`, `calculate_scores` | mcp/src/agents_remember/code_quality/crap_calculator.py:232-239; mcp/src/agents_remember/code_quality/crap_calculator.py:294-305 |
| The `@server.tool()` declarations the one `PLR0913` per-file-ignore covers, walked by AST. | `register_core_tools`, `test_every_function_in_the_exempted_path_is_a_published_tool_declaration` | mcp/src/agents_remember/mcp/registration/core.py:21-25; mcp/tests/test_code_quality_check.py:540-553; pyproject.toml:34-38 |
| The complexity-selection and branch-coverage settings this suite reads. | "\"C901\", # Enforce [tool.ruff.lint.mccabe] max-complexity."; "branch = true" | pyproject.toml:17-17; pyproject.toml:67-70 |
| The pytest configuration this suite reads. | `testpaths` | pyproject.toml:119-119 |
| An independent recomputation that the wrapper's real argument vectors reach every tracked file. | `test_every_tracked_python_file_is_linted_and_type_checked`, `test_python_coverage_and_test_rails_reach_their_trees` | mcp/tests/test_gate_scope.py:152-173; mcp/tests/test_gate_scope.py:175-194 |
| The shared tiered hook body scanned by the parity test; the full tier invokes the wrapper. | "dashboard_checks() {" | .githooks/_gate.sh:120-291 |
| CI defines a workflow for pull requests. | "pull_request" | .github/workflows/quality-checks.yml:3-58 |
| The targeted configuration regression pins both environment fallback and explicit-argument precedence for the enclosure progress report. | `test_targeted_config_keeps_the_repository_file_size_arm`, "self.assertEqual(explicit_config.progress_report, explicit_progress_report)" | mcp/tests/test_code_quality_check.py:110-163 |

### 260731-EFA-L17 — The Pre-Push Tier Is Targeted

`test_repository_gates_use_default_strict_wrapper` still walks every gate file
for a wrapper reach and no CRAP opt-out, but the hook tier assertions now expect
`{"pre-commit": "fast", "pre-push": "targeted"}`
(`test_git_hooks_delegate_to_the_shared_tiered_gate`), and
`test_the_pre_push_tier_runs_the_targeted_contract` (lines 156-166) asserts
`_gate.sh` delegates to `code_quality.check --targeted` while `full` remains a
manual tier only.

## L23 Native Temp Regression

The CLI boundary tests now assert both ordinary and memory-capped runs pass the
constant short native scratch root to environment sanitization, independently
of durable progress-report placement.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented `/tmp/arq` ownership at the quality CLI boundary; verification remains closeout-owned.

- 2026-08-12T17:27+02:00 — 260731-EFA-L23 final Dagger diff-coverage repair: expanded the existing
  targeted-configuration test with the complementary explicit-progress-report call, proving the CLI
  path wins even while `AR_QUALITY_PROGRESS_REPORT` is set. Focused pytest is 1/1; verification
  provenance remains closeout-owned.

- 2026-08-12T16:28+02:00 — 260731-EFA-L23 final diff-coverage repair: extended the existing
  targeted-configuration regression to prove environment-derived progress-report ownership and
  to define the optional coverage/progress/pytest-report arguments explicitly. Focused test proof
  belongs to the code change; verification provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded the targeted file-size-arm and exact
  Ruff-pin regressions; refreshed shifted ranges after inserting them.

- 2026-08-12T00:08+02:00 — No content impact: the repository-gate subtest reports each gate path
  as a serializable POSIX string for xdist; the gate reachability and no-opt-out assertions are
  unchanged. Verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the pre-push
  targeted-tier assertions and the full-tier manual/master-gate posture.
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-03T03:59:59+02:00 — Curated 19 citation findings (9 table rows, 10 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator, **correcting the mid-leaf card below**.
  The complexity baseline it described no longer exists: `complexity_baseline.py`,
  `quality/complexity-baseline.txt`, `test_complexity_baseline.py` and the wrapper's
  baseline step were deleted when the developer ruled ratchets/baselines/grandfather
  lists/burn-down schedules forbidden, and all 67 offenders were fixed by extraction.
  `EveryEnforcingStepCanFailTests` was rewritten accordingly and now ends with
  `test_the_complexity_baseline_and_its_gate_step_are_gone`. Added the two classes that
  did not exist when that card was written — `ToolSignatureExemptionTests` (the single
  `PLR0913` exemption over the MCP registration directory, held shut by an AST test) and
  `CrapThresholdEnforcementTests` (every offender named, the clearing coverage inverted
  from the CRAP formula, split-instead-of-test, no exemption file) — plus the expanded
  `GateScopeDerivationTests` refusal arms and `main`'s verdict pass-through. Corrected the
  fast-tier description (no baseline step) and dropped the baseline reference row.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf, superseded above).
  Recorded the four new test classes:
  `RadonIsAReportNotAGateTests` (exactly the two Radon steps are reports; the header and
  help text say so; a broken report step still fails), `EveryEnforcingStepCanFailTests`
  (the routed complexity rules match the baseline's exactly; format and baseline steps
  are enforcing over the derived scope; the ratchet must name an owner and a burn-down),
  `GateScopeDerivationTests` (no hand-written scope constant; the index is the scope; a
  script outside every package reaches both rails; a underivable scope refuses), and
  `PytestConfigurationTests` (strictness switches, `python_classes`, the exact-count
  warning cap, and two-way marker/environment-gate reconciliation). Corrected the fast
  tier description to include the formatter, the baseline, and the harness generated-copy
  check. Verification metadata is pinned to the leaf's reformat commit until closeout
  stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 split the hooks into a fast staged-content tier and a full
  pre-push tier over a shared `.githooks/_gate.sh`. `test_repository_gates_use_default_strict_wrapper`
  now scans `_gate.sh` and the CI workflow instead of the two hook files, which no longer inline the
  wrapper command; the new `test_git_hooks_delegate_to_the_shared_tiered_gate` pins each hook to its
  tier so neither can be silently promoted or demoted. Corrected this card's claim that pre-commit
  invokes the wrapper. Verification metadata pinned to the pre-leaf source authority until closeout
  stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: documented mandatory default
  threshold failure, removal of the strict opt-in surface, and repository-gate command parity;
  verification remains pinned until the code commit.

- 2026-06-08T12:06+02:00: Added coverage that the Pyright command includes
  `--pythonpath` and the active interpreter path, matching the linked-worktree
  quality gate fix. Verification metadata stays pinned until closeout.
  task/runtime-asset-canonical-sync branch.
- 2026-06-02T10:35+02:00: Added a test that the wrapper threads this checkout's source import root first onto `PYTHONPATH` (preserving any pre-existing value); the fake runners now take the `env` argument. Verification metadata stays pinned until closeout. fix/quality-gate-worktree-local branch.
- 2026-05-28T19:52+02:00: Updated after source quality wrapper tests began asserting Pyright command wiring.
- 2026-05-24T06:30+02:00: Created unit coverage for the source quality suite wrapper.
