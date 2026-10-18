# dashboard/src/panels/review/ReviewHeader.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Task identity and reviewer controls.

## Code Commentary

Render Back, leaf identity, grouped task/subject identifiers, caller refresh and ReviewKeys beside it. Recorded history is labelled Historical task comparison. A task-context fallback suppresses a selected-subject label. The wrapping header is independent of subject acquisition and writes no judgment.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Task identity and reviewer controls: `ReviewHeader` owns the described branch. [1]
- Task identity and reviewer controls: `subjectLabel` owns the described branch. [2]

