# mcp/src/agents_remember/worktrees/task_retirement.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Surveys retirement readiness without deleting resources or resolving operations. It refuses actual open leaf work and current operation authority, and returns the evidence and facts left in place.

## Code Commentary

`require_master_retirement_ready` reads the master contract when present and each present leaf enclosure contract. An unreadable contract refuses because its resources and operations cannot be surveyed. `_survey_leaf_side` treats an existing leaf worktree directory and a leaf branch with commits beyond its landing line as open work.

The repository's own checkout, the master's own resources, branches reachable from their landing line and an unresolvable landing line are facts. Recorded identity differences and pending cleanup with nothing open are also facts. Available non-abandoned row-document bytes are captured without parsing or row binding; missing, unreadable or outside-folder documents are facts, and abandoned rows need none.

`_survey_operations` reads locators, current `.lifecycle` authority and sync journals. Unfinished or unreadable current operations refuse. Older-layout operation reports are facts with status and phase.

A live locator permits executable lifecycle remedies. Without one, the refusal gives the applicable manual Git removal or `mv -n` operation-record move: use an unused destination, preserve an earlier given-up record and verify the original moved before retry. A later build's adoption route replaces this manual step.

## Evidence

- Readiness accumulates actual open work and returns captured evidence and retained facts. [6]
- Operation remedies depend on live locators and current authority. [7]
- Recorded identity differences remain facts rather than today's layout requirements. [8]
- Non-abandoned document observations are facts; abandoned rows ask for no document. [9]
- A pending cleanup cell without open work permits retirement preview. [10]
