# mcp/src/agents_remember/memory/carryover_records.py

## Governing Overview

[Memory area overview](overview.md)

## Purpose

Plans the transitive outgoing record dependencies of carried converted cards without authoring records or history.

## Code Commentary

### Exact dependency graph

Schema edges are realizes/proves invariant IDs, ID reference targets, record members/supersedes and non-route links. Traverse outgoing named records to closure, not invented incoming records. Entry IDs and onboarding subjects additionally select source history as reading aids only.

### Pair and identity conflicts

Record JSON is required; existing optional Markdown travels and participates in exact byte comparison. Source pairs must match indexed identity/document/path. Identical target pairs are present even under a different slug when their suffix-keyed members match. An exact interrupted subset at the same canonical source path is needed for companion completion, including an exact prose-only member with no indexed JSON yet. Differing held bytes, JSON occupied without the expected indexed ID, partial/unconverted indexes and missing/unreadable source records are conflicts, never absence proof.

### No history or overwrite payload

`record_payloads` returns complete fresh source units for missing or resumable records only. When a companion is missing, exact present members remain in the payload so the transaction checks the whole unit, skips equal writes and includes those held members in refusal-versus-HEAD reporting; differing existing bytes are refused. Apply must reopen indexes/replan to catch relocated identity conflicts. Source history has reading_aid_only=True and is never a payload or a recovery-curator row. These helpers perform no writes; the caller owns the transaction.

## Evidence

- Exact dependency graph: Schema edges are realizes/proves invariant IDs, ID reference targets, record members/supersedes and non-route links. Traverse outgoing named records to closure, not invented incoming records. Entry IDs and onboarding subjects additionally select source history as reading aids only. [1]
- Pair and identity conflicts: Record JSON is required; existing optional Markdown travels and participates in exact byte comparison. Source pairs must match indexed identity/document/path. Identical target pairs are present even under a different slug when their suffix-keyed members match. An exact interrupted subset at the same canonical source path is needed for companion completion, including an exact prose-only member with no indexed JSON yet. Differing held bytes, JSON occupied without the expected indexed ID, partial/unconverted indexes and missing/unreadable source records are conflicts, never absence proof. [2]
- No history or overwrite payload: `record_payloads` returns complete fresh source units for missing or resumable records only. When a companion is missing, exact present members remain in the payload so the transaction checks the whole unit, skips equal writes and includes those held members in refusal-versus-HEAD reporting; differing existing bytes are refused. Apply must reopen indexes/replan to catch relocated identity conflicts. Source history has reading_aid_only=True and is never a payload or a recovery-curator row. These helpers perform no writes; the caller owns the transaction. [3]
