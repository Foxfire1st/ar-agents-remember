# mcp/src/agents_remember/worktrees/modules/landing_commit_check.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Run the repository-owned pre-commit check against the exact tree a landing will publish.

## Code Commentary

Resolve core.hooksPath or Git's hook directory; do not reproduce named hook steps in the product. A present unrunnable hook, a failed check, timeout, or mutation of the judged tracked/index tree refuses publication. Tracked byte identity matters even where status labels are unchanged. Timeout handling owns descendants and retained pipe holders, not only the direct Git PID. Full actual output is streamed to bounded/reclaimed on-disk logs with elapsed time and terminal pointers. Optional isolation preserves and restores pre-existing work; a hook that rewrites judged state is not silently accepted. The positive timeout is reread from landing settings per operation, with default 900 seconds. Commit-Check-Pass carries tree and hook identity in the commit; integration may use a matching fact or check the candidate in a detached worktree. The runner is not task acceptance, independent review or the full affected-closure gate.

## Evidence

- resolve_commit_check_hook: qualified source contract. [1]
- run_landing_commit_check: qualified source contract. [2]
- run_landing_commit_check_on_index: qualified source contract. [3]
- commit_check_timeout_seconds: qualified source contract. [4]
- commit_check_trailer: qualified source contract. [5]
- commit_check_fact: qualified source contract. [6]
- check_published_tree: qualified source contract. [7]
- _run_hook_to_log: qualified source contract. [8]
- _stop_escaped_pipe_holders: qualified source contract. [9]
