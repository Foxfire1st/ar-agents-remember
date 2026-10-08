# mcp/src/agents_remember/application/review_attribution.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Attributes source paths to the selected subject from the exact resolved before and after knowledge indexes.

## Code Commentary

`_read_side` opens the selected derived index and reads its registered mappings; an incomplete or unreadable side remains uninspected. Negative attribution needs complete inspection of both sides, whereas an empty converted index can be fully inspected and confirm absence. Positive attribution records the exact invariant/family/proof relationship that supplied the path. The retired first-generation origin and damaged-half helpers do not establish historical completeness. The source inventory denominator remains separate from a bounded record selection.

## Evidence

### Repo-Internal References

- `review_attribution` owns the current boundary described above. [12]
- `_read_side` owns the current boundary described above. [13]
- `_inspection_state` owns the current boundary described above. [14]
