# mcp/src/agents_remember/memory_quality/style/citations/editing.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Byte-preserving edits shared by citation migration and steady-state repair.

## Code Commentary

### Logic

`Documents.lines` reads raw bytes, decodes UTF-8 and splits only on LF. Rejoining therefore preserves CRLF carriage returns and a trailing newline. `Site` identifies one source-list span; `spliced` retains its surrounding padding; `rewritten` applies edits right-to-left so multiple cells on one line keep their original offsets.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- UTF-8 decoding does not perform universal-newline conversion.
- Untouched text and source-cell padding survive a rewrite; right-to-left composition preserves offsets.
- This cache is the original document read. Publication freshness belongs to `documents.transaction`, which rereads the full document before replacement.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

No configured external domain source.

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Site` (lines 9-15) — The exact span of one claim's source list, in one line of one document.. [1]
- Defines the class `Documents` (lines 18-27) — The memory documents one run reads, split so that rejoining is lossless.. [2]
- Defines the function `spliced` (lines 30-34) — ``line`` with the source list replaced and the cell's own padding untouched.. [3]
- Defines the function `rewritten` (lines 37-42) — ``lines`` with each site's source list replaced, right to left so offsets hold.. [4]

### Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

No new cross-repository protocol.
