# dashboard/src/panels/lifecycle-list/docProgress.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Adapt served TaskEntry major-step or child-count facts into sidebar/page numeric progress.

## Code Commentary

Task summaries read entry.stepsDone/stepsTotal and use Steps done. Parents use childProgress: completed over planned+started+completed, with aborted outside the denominator and summary.discardedCount separately defaulted to zero. No local sub-task/series recount remains.

The adapter does not recount nested work, author major-step completion or decide lifecycle readiness. Numeric progress and the sidebar’s cached step-dot payload are distinct presentation inputs.

## Evidence
