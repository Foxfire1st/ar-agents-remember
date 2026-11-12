# mcp/tests/test_paseo_single_path.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the repository-wide scan that keeps one path to Paseo: only the bridge script and the runtime
commands may reach it (PNT-R02 item 1). The scan reads code, manifests and suffix-less scripts of a
checkout and trips a rule for each second path, against an allowance table per rule and file kind.

## Code Commentary

### Logic

`paseo_allowance_table` supplies the admitted uses; `may_be_scanned()`, `is_scanned()` and `rule_hits()`
decide which files the scan reads and how often each rule applies to a file's kind; `second_paths_to_paseo()`
reports the rules a file trips more often than it is allowed to. `git()` runs Git on the repository at a
given root and no other, whatever the caller's environment, and `scan_tree()` walks every tracked or
untracked, not ignored file of a checkout.

- **The tree today.** `test_only_the_bridge_and_the_runtime_commands_reach_paseo` requires the real tree
  to trip no rule, and `test_the_tree_scan_reports_exactly_the_planted_files` requires the scan to report
  exactly the files a case planted and nothing else.
- **The rules have teeth.** `test_the_scan_catches_each_kind_of_second_path` plants one second path per
  kind — an import, a shell call, a manifest dependency, a suffix-less script — and each trips the rules
  named for it, while AR's own uses trip none.
- **New admissions are held to the same bar.**
  `test_new_support_admissions_still_reject_an_extra_use_and_a_second_path` proves an added allowance
  still refuses an extra use and a second path.

### Conventions

`CODE_SUFFIXES`, `SHELL_SUFFIXES`, `MANIFEST_NAMES` and `SHELL_INTERPRETER` define what counts as code, a
script and a manifest; `TEST_PATHS` names the test paths excluded from the scan.

### Invariants And Boundaries

- The scan is repository-wide: a new file that reaches Paseo is caught wherever it sits.
- Only the bridge and the runtime commands are admitted; an admission is a count of uses, not a blanket.

## Evidence


- The bridge and runtime commands as the only admitted path, and the exactness of the tree scan. [1]


- The single-path cases as they apply to the host modules. [2]


- The dev-only fake host holds two admitted pinned-server comments, not a second host path. [3]


- One helper's allowance is two address reads: the recorded settings block and the build's resolution under the server environment. [4]
