# mcp/src/agents_remember/application/task_docs/task_retirement_answers.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

What the retire operation answers: the result of a request, and what a dry run would change. `RetirementPlan` holds the observed state, the remaining steps and the files a run writes; the answers name the remaining work, the cleanup state by the operation's own state table, and the exact files a real run would write.

## Code Commentary

`preview_answer` builds the dry-run answer from a plan: the pending steps (`_pending_steps`) and the pending files (`_pending_files`) — the sprint's document pair and the master folder move. `_archived_state` reports the operation's own state (`retired-with-hook-failures` after a partial cleanup), and `first_answer` builds the result of a request. A dry run lists every file a real run writes, also after a death inside the sprint edit.

## Evidence

- A dry run of a retirement lists every file a real run writes, also after a death inside the sprint edit. [1]
- A dry run names a cleanup that failed hook-failed by the operation's own state table. [2]
- The answer names the remaining steps and files for a repeated request, so a resumed request does only what remains. [3]
