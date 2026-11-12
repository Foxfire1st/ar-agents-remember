# mcp/src/agents_remember/worktrees/abandoned_row_landing.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

A label never removes a landed leaf: the one check behind every place that completes a master. An abandoned row is a finished record of a leaf that will not run. It blocks nothing and is asked for no enclosure, unless the enclosure it does have records a completed integration: that row contradicts itself.

## Code Commentary

`require_abandoned_rows_unlanded` is called by every operation that completes a master — the task tool for an organizational master (`require_master_completion`), the closeout for an atomic one, and finalization for both — because the row's label may have been set after the operation before it looked. A contradiction is refused by the row's name.

## Evidence

- Finalizing a master decides again that an abandoned row whose enclosure records a completed integration refuses by name, for a master of either nature. [1]
- An abandoned row without a completed landing blocks nothing and is asked for no enclosure. [2]
