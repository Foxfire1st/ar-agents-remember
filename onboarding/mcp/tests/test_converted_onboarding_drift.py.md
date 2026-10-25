# mcp/tests/test_converted_onboarding_drift.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

One case per rule of converted onboarding drift (MIK-R44@v2): a converted tree takes the converted branch
instead of legacy discovery, the result names every measured field, empty, unreadable and unbuildable trees
report truthfully, and every consumer of the measurement returns the same answer. The baseline cases cover
blocking, adoption and the refusal paths either side of the commit.

## Code Commentary

### Logic

`bound_validation()` supplies the validator binding the baseline cases need, and the cases drive
`context_packet`, `memory_quality.converted_check`, the validator trees and the worktree services.

- **The branch.** `test_converted_trees_take_the_converted_branch_and_skip_legacy_discovery` requires the
  converted basis, its count and actionable count, the measured states, and an actionable sample with no
  legacy classification key.
- **The result.** `test_converted_result_names_every_measured_field` requires every converted field present
  with anchors and bounded samples only.
- **Truthful absence.** `test_empty_missing_and_unbuildable_base_trees` keeps zero means empty, unread means
  error and an unbuildable base one refusal.
- **Carried anchors.** `test_carried_anchor_is_refused_as_carried_stale_never_as_new` requires a carried
  deleted anchor to refuse as `R22.6-carried-stale`, never as a new anchor.
- **One measurement.** `test_three_consumers_return_one_answer` and
  `test_report_and_snapshot_come_from_the_same_result` keep the drift check, context drift and both baseline
  tools on one summary, and the Markdown report and observer snapshot on one measurement.
  `test_complete_drift_fingerprint_changes_beyond_equal_counts_and_sample` proves the fingerprint is taken
  over the full findings, not the limited sample.
- **Baseline states.** `test_baseline_states_for_converted_trees` reports `ready`, `blocked-drift` and
  `blocked-invalid` distinctly; `test_accept_drift_never_clears_a_validator_violation` keeps validator refusal independent of drift acceptance.
  The former stale-anchor-adopts case moved to `test_converted_onboarding_baseline.py`, where drift acceptance still refuses the stale reference and only a repaired pair adopts;
  `test_first_baseline_commits_exactly_the_validated_tree` requires the commit to record the staged tree
  validation passed.
- **Nothing on refusal.** `test_dry_run_and_refusal_change_nothing` keeps the index, the refs and every file
  untouched, and `test_adoption_refuses_where_the_validator_is_not_bound` refuses rather than commits.
- **Command line.** `test_baseline_command_line_validates` keeps the module command line validating like the
  tool.

### Conventions

Adoption-path fixtures now use `card=True` current anchors. This preserves the validated-tree, dry-run and CLI assertions while letting them reach their intended transaction behavior under the anchor validator.

The measurement is taken once and read by every consumer in a case, so two consumers disagreeing is the
failure the case looks for.

### Invariants And Boundaries

- A missing or unreadable tree is never reported as a checked zero.
- Adoption commits exactly the tree validation passed, and a refusal changes nothing.

## Evidence


- Converted trees are measured on the converted basis, with the expected count, actionable count and states, and no legacy classification key in the actionable sample. [1]


- The converted result names every measured field. [2]
- Empty, missing and unbuildable-base trees report truthfully, never as checked zero. [3]



- The carried deleted-path test refuses R22.6-carried-stale rather than new-anchor-path; the moved helper constructs anchors, the separate descriptions case checks current-row doctrine, and the split context/summary case asserts three matching violations. [4]




- The consumers return the same summary; the carried deleted-path test and split context/summary fixture retain matching carried-stale observations and three violations. The moved descriptions assertion is separate current-row doctrine, not additional carried-stale proof. [5]


- Report and snapshot come from the same measured result. [6]
- Converted baseline states block on violations first, then on unaccepted drift. [7]
- Accepting drift never clears a validator violation. [8]

- The first baseline commits exactly the validated tree. [9]

- Full findings, not the limited sample, own the fingerprint identity; incomplete input yields null. [16]



- A successful would-adopt dry-run preview and a separate blocked-invalid live refusal preserve HEAD/unborn, write-tree-stdout, porcelain-status and non-.git path/byte fingerprints. [10]





- Surviving descriptions state measurement/currentness/advisory wording. Canonical and sole packaged c-05 copies include their moved memory-quality-control workflow when checking current-row/no-counted-card-edit-alone doctrine; both c-10 copies must state that drift acceptance lifts only the stale-anchor gate and still refuses invalid paired anchors as R198.1-reference-anchor and blocked-invalid. [11]

- The context-packet leaf route binds the leaf base. [12]





- Injected RuntimeError("boom") for both dry-run values preserves HEAD/unborn, write-tree-stdout, porcelain-status, non-.git path/byte fingerprints and ls-files --stage; intent-to-add, unstaged symlink target and staged file text remain asserted. Source caption: `test_interval_failure_leaves_everything_untouched` `_fingerprint` [13]






- Static description assertions inspect surviving descriptions and canonical/package copies, retain c-05 current-row doctrine, and reject restoration of the removed drift tool. [14]






- Carried deleted-path refusal and context/summary parity remain asserted at their current owners; current-row doctrine is a separate static text check, not executed acceptance. Source caption: `test_context_packet_agrees_with_the_summary_on_carried_anchors` `test_descriptions_say_what_the_check_is` [15]
