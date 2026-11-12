# mcp/tests/test_reference_note_revision.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_note_revision.py` protects MIK-R198 rule 6a: a reference's note is revised in place and nothing else moves. It also holds the fails-before case that justifies the rule — the installed table-row re-authoring route re-resolves a reference's targets when the source has moved, where a note-only revision must not.

## Code Commentary

Each case converts a scratch pair with the real `convert_memory` and freezes the Git environment so bytes are stable. The fails-before case moves the source, shows that authoring a citation row naming `[4]` changes the recorded anchor, then restores the pair and revises only the note: every target stays identical, the note changes, no number is minted, and the answer reports the reference, the author, `changed`, a non-dry run and the digest after. Refusals carry a named code and leave the sidecar byte-identical — `reference-missing`, `stale-input` against a base digest, `note-empty`, `card-absent`, `sidecar-absent`, `author-absent` — and scope admission confines the card operand, so `..`, absolute and symlinked cards are each refused as `card-escapes-memory` while a real sibling tree's bytes stay unchanged. The application route is driven with the contract's leaf as author and returns `legacy-format` on unconverted memory; the last case shows `citation_fix_tool` moving an anchor while leaving its note exactly as it was.

## Evidence

- A note revision keeps the recorded anchor the installed table-row route would have moved [1]
- Every other reference and the card are untouched and no number is minted [2]
- A missing key, a stale base digest and an empty note are refused by name with the sidecar unchanged [3]
- A card operand cannot leave the admitted memory tree [4]
- The tool revises one note and records the contract's leaf as author [5]
- A mechanical re-point changes the anchor and not the note [6]
