# mcp/tests/test_cleanup_repeated_archive_ready.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Regression proof for MIK-R129: a cleanup interrupted after its terminal archive was written can be
repeated, and the repeat finishes without re-judging the accepted gate or inventing an absent
judgement record.

## Code Commentary

Three cases over temporary code and memory repositories; no real-root cleanup is performed.
`test_repeated_cleanup_with_archive_ready_finishes` publishes the enclosure and the terminal archive
exactly as the first cleanup does before its destructive outputs, then repeats `cleanup_result` as a
dry run: before the fix the repeat raised `UnboundLocalError: kept_line`, after it the repeat returns
0 with `landedTips` absent — the archive holds no kept-line record, so the repeat carries none and
invents none. `test_repeated_cleanup_real_run_reaches_cleanup_completed` drives the production path
with `approved=True`: the contract reads `cleanup == "completed"` and the terminal authority
re-reads `cleanup-completed`.
`test_repeated_cleanup_with_branches_already_gone_finishes` retires the worktrees and work branches
in tail order after the archive publication, then repeats: the repeat finishes and completes, because
replay demands no live refs the accepted first run already consumed. All cases leave the
completed-cleanup and argument-mismatch answers untouched.

## Evidence

- The dry-run repeat of an archive-ready cleanup finishes with no invented `landedTips`. [4]
- The real-run repeat completes the contract and the terminal authority re-reads `cleanup-completed`. [5]
- The branch-gone repeat finishes and completes without live refs. [6]

> Retained earlier citation wording: - The archive-ready branch binds `kept_line = None` and invents no record. [7]

- The archive-ready branch binds `kept_line = None` and invents no record.  Anchor: `cleanup_result` [7]
