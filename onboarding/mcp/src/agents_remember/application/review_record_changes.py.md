# mcp/src/agents_remember/application/review_record_changes.py

## Governing Overview

[application overview](overview.md)

## Purpose

`review_record_changes` holds the index-only recorded-meaning facts shared by the review outline and the detail badges: one `RecordChanges` per read decides guarantee, intent and membership from the two memory indexes, each record and membership list read once. There is exactly one definition of change.

## Code Commentary

`RecordSide` abstracts what a decision needs (index, read state, problems) with no source read; `Known` is one side's answer about one record (live, absent, retired, or unknown with reason). `Fact` accumulates established, unknown and unresolvable-entry reasons with `change` and `membership` outcomes. `RecordChanges.record` caches per-side records and same-kind parse-problem lists. A found record returns its live/retired state first; for an absent record, only problem basenames starting with the requested ID followed by `-` or `.` make it unknown. Its bounded reason names that ID and at most three matching paths; unrelated failures leave it absent; `guarantee` compares family guarantee text (added/removed/changed/unchanged/unknown); `intent` compares invariant revision then authored wording (`statement`, `applicability`, `conditions`, `exclusions`), marking `text_differs` when the revision is kept but the text differs; `membership` compares family roster listing; `presence` settles the one-sided added/removed/retired cases.

## Evidence

- Family change comes from guarantee text and liveness [2]
- Invariant change comes from revision, then authored wording [3]
- One-sided records settle as added, removed or retired [5]

- RecordChanges caches records by side and record ID, problem lists by side and kind, and membership sets by side and family. Found records return live/retired state before parse-problem handling. For absent records, only same-kind problem basenames beginning with record_id plus '-' or '.' yield unknown; the bounded diagnostic includes at most three matching paths. [1]
- membership reads each side's family through record, returns unknown when that read is unknown, caches the live family's members or an empty set, and establishes joined/left only when the invariant's listing differs between sides. [4]
