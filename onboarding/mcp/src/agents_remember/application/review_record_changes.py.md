# mcp/src/agents_remember/application/review_record_changes.py

## Governing Overview

[application overview](overview.md)

## Purpose

`review_record_changes` holds the index-only recorded-meaning facts shared by the review outline and the detail badges: one `RecordChanges` per read decides guarantee, intent and membership from the two memory indexes, each record and membership list read once. There is exactly one definition of change.

## Code Commentary

`RecordSide` abstracts what a decision needs (index, read state, problems) with no source read; `Known` is one side's answer about one record (live, absent, retired, or unknown with reason). `Fact` accumulates established, unknown and unresolvable-entry reasons with `change` and `membership` outcomes. `RecordChanges.record` caches per-side records and names unparseable files; `guarantee` compares family guarantee text (added/removed/changed/unchanged/unknown); `intent` compares invariant revision then authored wording (`statement`, `applicability`, `conditions`, `exclusions`), marking `text_differs` when the revision is kept but the text differs; `membership` compares family roster listing; `presence` settles the one-sided added/removed/retired cases.

## Evidence

- Each record and membership list is read once per read [1]
- Family change comes from guarantee text and liveness [2]
- Invariant change comes from revision, then authored wording [3]
- Roster change comes from listing on each side [4]
- One-sided records settle as added, removed or retired [5]
