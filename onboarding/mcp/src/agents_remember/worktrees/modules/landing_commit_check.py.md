# mcp/src/agents_remember/worktrees/modules/landing_commit_check.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Run the repository-owned pre-commit check against the exact tree a landing will publish.

## Code Commentary

Resolve core.hooksPath or Git's hook directory; do not reproduce named hook steps in the product. A present unrunnable hook, missing or unborrowable dashboard dependencies for a repository carrying `dashboard/package.json`, a failed check, timeout, or mutation of the judged tracked/index tree refuses publication. Tracked byte identity matters even where status labels are unchanged. The shared `commit_check_process` module owns the process session, the 900-second default and the 30-second grace, the retained log and the escaped-holder cleanup; this module delegates the hook run to it. Full actual output is streamed to bounded/reclaimed on-disk logs with elapsed time and terminal pointers. Optional isolation preserves and restores pre-existing work; a hook that rewrites judged state is not silently accepted. The positive timeout is reread from landing settings per operation, with default 900 seconds. Commit-Check-Pass carries tree and hook identity in the commit; integration may use a matching fact or check the candidate in a detached worktree. Before spawning a runnable hook in a linked or temporary checkout that carries `dashboard/package.json` without `dashboard/node_modules`, `_run_checked` calls `_borrow_dashboard_node_modules` to symlink the primary checkout's `dashboard/node_modules` only when primary `dashboard/node_modules` exists, candidate and primary `dashboard/package-lock.json` are byte-identical, and `dashboard/node_modules/` is gitignored in the candidate, unlinking the symlink in `finally`; otherwise it refuses pre-spawn as `unrunnable` with no `npm install` and no leftover symlink. The runner is not task acceptance, independent review or the full affected-closure gate.

## Evidence

- The shared owner runs the process in its own session, stops it after the bound and keeps the log. [11]

- resolve_commit_check_hook: qualified source contract. [1]
- run_landing_commit_check: qualified source contract. [2]
- run_landing_commit_check_on_index: qualified source contract. [3]
- commit_check_trailer: qualified source contract. [5]
- commit_check_fact: qualified source contract. [6]
- check_published_tree: qualified source contract. [7]

- commit_check_timeout_seconds: qualified source contract. [4]
- `_run_checked` prepares and cleans up lockfile-matched `dashboard/node_modules` borrowing pre-spawn, delegates the hook run to `commit_check_process`, and keeps landing pass and refusal verdicts. [10]
- `_common_checkout_root`, `_lockfile_borrow_refusal`, and `_borrow_dashboard_node_modules` gate linked-checkout `dashboard/node_modules` symlinking on primary directory presence, byte-identical `dashboard/package-lock.json`, and gitignore status, refusing pre-spawn otherwise. [12]
