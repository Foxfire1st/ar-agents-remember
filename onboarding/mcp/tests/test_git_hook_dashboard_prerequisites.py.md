# mcp/tests/test_git_hook_dashboard_prerequisites.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests that `.githooks/_gate.sh` reports missing dashboard dependencies before its long checks, by running the real hook script in a small Git tree.

## Code Commentary

`hook_tree` builds a temporary Git repository with `dashboard/package.json`, one tracked Python file, the product's `scripts/python-runtime-contract.env` and a stand-in `mcp/.venv/bin/python` that prints its arguments and exits 0. `PATH` holds only `git`, `uname` and `xargs`, so `npm` is missing unless a test adds a stand-in. `_run_hook` runs `/bin/sh .githooks/_gate.sh <tier>` in that tree with output and errors merged.

- `test_missing_dependencies_fail_before_ruff` runs the fast and the targeted tier without `dashboard/node_modules`: each exits 1 with the `npm ci` instruction, ends on its tier's failure line and never starts Ruff.
- `test_missing_npm_fails_before_ruff` keeps the folder and leaves out `npm`: the fast tier stops with the npm message before Ruff.
- `test_present_dependencies_keep_the_check_order` adds a stand-in `npm` and compares the whole list of result lines: the three generated-copy checks, Ruff, the format check, Pyright, the evidence catalog, the dashboard's codegen, lint and typecheck, then the fast tier's pass line.
- `test_missing_dashboard_keeps_the_skip` removes `dashboard/package.json`: the fast tier passes, prints the skip line and runs Ruff.

The stand-in tools make every step pass, so the tests check the order of the steps and the early stops, not lint or type results.

## Relationships

The module is declared in the `integration` lane. It proves the hook's early dependency look; the [hook script's card](../../.githooks/_gate.sh.md) explains the tiers.

## Evidence

- The fixture tree and its restricted search path. [1]
- Both tiers stop at a missing dependency folder before Ruff. [2]
- A missing npm stops the fast tier before Ruff. [3]
- With the dependencies present the step order is unchanged. [4]
- A tree without the dashboard package keeps the skip. [5]
