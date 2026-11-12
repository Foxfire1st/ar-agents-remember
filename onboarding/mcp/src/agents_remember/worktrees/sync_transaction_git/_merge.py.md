# mcp/src/agents_remember/worktrees/sync_transaction_git/_merge.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Carry code and validated memory content through resumable Git merge steps.

## Code Commentary

Converted memory is structurally planned before Git mutation: converted sides merge directly, crossings convert legacy sides, and only all-unconverted input takes plain Git. Reports retain conflicts, conversion and reference-alignment diagnostics, even for a clean merge when alignment matters. A converted staged memory merge is validated against both parents and settled paired code before commit; refusal leaves its staged tree and MERGE_HEAD. Incoming converted fast-forwards validate before refs move and require source-line repair, not blessing a destination tree. Real content conflicts remain agent-owned. Hook failure after content merge is a retained commit stop with the actual repository-check reason. Rollback strips only disposable memory cache before abort; it does not establish authority over owner work.

The report gate selects real conflicts, a converted side, nonzero renumbered references, kept evidence lines or skipped cards; aligned-card count alone does not select a report. Staged continuation threads the settled paired-code commit into `_finish_staged_memory_merge`, closes crossing history, stages the cache ignore rule and validates the exact written index tree against both pinned parents before ordinary `git commit --no-edit`. A refusal leaves HEAD, MERGE_HEAD and the staged merge intact. The result must still prove the exact two-parent ordering.

## Evidence


- validate_memory_fast_forward: qualified source contract. [1]

- _knowledge_merge: qualified source contract. [2]
- _apply_knowledge_merge: qualified source contract. [3]
- _finish_staged_memory_merge: qualified source contract. [4]
- commit_check_report: qualified source contract. [5]
- rollback_side: qualified source contract. [6]
