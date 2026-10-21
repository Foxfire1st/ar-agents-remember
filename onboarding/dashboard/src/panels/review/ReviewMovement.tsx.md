# dashboard/src/panels/review/ReviewMovement.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Preserve the supplied synchronization, external Git movement and staleness facts for the review’s Technical details record.

## Code Commentary

`movementRecord` returns a plain record. With no payload it names both movement channels `not read`; with a payload it retains each complete supplied owner object, uses `not measured` for a missing owner, and includes the payload’s staleness value.

The function performs no measurement, classification, filtering of owner fields or rendering. The Technical details owner incorporates the record, while the top-line status model presents measured state words.

## Invariants And Boundaries

The caller must pass the payload appropriate to the selected read. This function accepts no pending/unavailable status and cannot independently guard a previous subject’s payload. Missing owner evidence stays explicit; it does not become an empty object or a fabricated measurement.

## Evidence

- Complete owner records survive while absent payloads and absent owners receive different labels. [5]
