# mcp/tests/test_judged_history_closing_restore.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Pins the boolean return contract and non-short-circuiting restore semantics of `direct_landing._JudgedHistoryClosing.restore` and verifies polymorphic callers such as `closeout_external._restore_preparations` observe the exact `bool` outcome.

## Code Commentary

`_make_closing` seeds a temporary `history.json` and `.gitignore` with `written` bytes and constructs `_JudgedHistoryClosing` wrapping a nested `HistoryClosing` in `ignore_before` alongside a synthetic `GitMutationSnapshot` (`_snapshot`).

- `test_restore_returns_true_when_both_preparations_succeed` verifies `restore()` returns `True`, restores `history.json` to its previous bytes, and removes `.gitignore` when its `previous` was `None`.
- `test_restore_runs_ignore_restore_without_short_circuit_when_history_changed` mutates `history.json` concurrently and verifies `restore()` returns `False`, preserves the concurrent history edit, and still restores `.gitignore` to its prior bytes (no short-circuit).
- `test_restore_returns_false_and_restores_history_when_ignore_changed` mutates `.gitignore` concurrently and verifies `restore()` returns `False`, restores `history.json`, and preserves the concurrent `.gitignore` edit.
- `test_restore_returns_false_when_both_files_changed` mutates both files concurrently and verifies `restore()` returns `False` while preserving both concurrent edits.
- `test_restore_preparations_sees_bool_outcome_on_judged_closing` passes `_JudgedHistoryClosing` into `closeout_external._restore_preparations` across clean, dirty-history, and dirty-ignore cases, confirming `[]` is returned when both files restore and `[history.as_posix()]` is reported as skipped whenever either file fails to restore while the untouched companion file is still rolled back.

## Relationships

Tests [`direct_landing.py`](../src/agents_remember/worktrees/direct_landing.py.md) (`_JudgedHistoryClosing`), [`knowledge_gate.py`](../src/agents_remember/worktrees/knowledge_gate.py.md) (`HistoryClosing`), and [`closeout_external.py`](../src/agents_remember/worktrees/modules/closeout_external.py.md) (`_restore_preparations`). Declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md) and named in [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`.

## Evidence

- `_JudgedHistoryClosing.restore()` returns `True` and restores both `history.json` and `.gitignore` (unlinking when `previous` was `None`) when neither file changed concurrently. [1]
- When `history.json` changed concurrently, `restore()` returns `False`, preserves the concurrent history bytes, and still restores `.gitignore` without short-circuiting. [2]
- When `.gitignore` changed concurrently, `restore()` returns `False`, restores `history.json`, and preserves the concurrent `.gitignore` edit. [3]
- When both files changed concurrently, `restore()` returns `False` and leaves both concurrent edits intact. [4]
- `closeout_external._restore_preparations` interprets `_JudgedHistoryClosing.restore()`'s `bool` return correctly across clean (`[]`), dirty-history (`[history_path]`), and dirty-ignore (`[history_path]`) scenarios. [5]
