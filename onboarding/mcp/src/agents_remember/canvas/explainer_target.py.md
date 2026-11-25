# mcp/src/agents_remember/canvas/explainer_target.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The target comparison's own answers, read from the bytes its bound trees hold and from the task's records, so a staleness read can ask whether a basis still resolves there.

## Code Commentary

Symbol basis resolution supplies the selected path grammar to qualified-span lookup. One span is required, and Lean keys are resolved whole.

For a complete blob, the reader directs Git into a private temporary file. It memoizes the bytes after a successful exit and the unavailable result after a nonzero exit. The temporary file closes on both return and exception.

- An unreadable or malformed basis returns an unavailable result where the method's return type allows it. A readable history listing without the named file yields an empty row set.
- `content_identity` hashes a range or a whole blob at one tree, and refuses a range that falls outside the blob rather than hashing what happens to be there.
- `mapped_lines` maps a recorded range into the target's tree through the zero-context hunks of the two blobs, and answers `None` when the range cannot be mapped or the blobs cannot be read.
- `memory_revision` reads a record's revision from the file the basis names at that side's tree, and answers `None` when the file is absent, does not parse, or holds another record.
- `proof_entry` resolves an entry's anchor in the code candidate and answers its fingerprint and execution state, or no fingerprint at all when the anchor no longer resolves.
- `block_fingerprint` dispatches by block kind — record, non-text file, hunk, invariant location — so each kind is fingerprinted by what identifies it, and `registered_version` answers only a strictly later version from the requirements manifest.

## Evidence

- A range or whole blob is hashed at its own tree, and a range outside the blob answers nothing rather than a wrong hash [1]
- A recorded range is mapped into the target's tree through the two blobs' hunks, and an unmappable range answers nothing [2]
- A record's revision is read at the side the claim names, and an absent or foreign record answers nothing [3]
- A proof entry's fingerprint and execution state are answered from its re-resolved anchor, or its fingerprint is withheld [4]
- Each block kind is fingerprinted by the identity that kind carries [5]
- Only a strictly later version the requirements manifest registers is reported [6]
