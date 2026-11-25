# mcp/tests/knowledge_rows_test_support.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Knowledge-row test support.

## Code Commentary

Test helpers that build valid and deliberately invalid row documents across the row kinds —
as text trees (invariant/family records and file sidecars with entries), never by inserting rows.
Caller-side identities are projected to the tree's own; provenance is carried, not projected.

The text fixture includes history documents in the same canonical output as records and sidecars. The fixture drafts carry authored revision fields. A closed review fact in a fixture history supplies the separate evidence for derived standing.

## Evidence



- The fixture tree renders and preserves test-owned histories. [2]

- The file realizes its current contract at the corrected candidate. [1]
