# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`inline.py` extracts old inline onboarding blocks from supplied source text for retained conversion and missing-block reads. It does not enumerate sources, compute source digests or classify drift.

## Code Commentary

### Logic

`line_bounds` locates the enclosing line. `expand_inline_bounds` includes an immediately preceding recognized comment opener and matching following closer, plus the final newline when present. `extract_inline_onboarding_block` returns `None` for absent/reversed markers; otherwise it retains the exact expanded raw text and parses colon-separated metadata while skipping blank, marker and comment-delimiter lines through kernel scalar cleaning.

### Invariants And Boundaries

- Parsing operates on text and performs no source-digest/currentness verdict.
- Non-UTF-8 source handling belongs to filesystem callers such as missing-onboarding; this module does not read or decode files.
- Inline raw block bytes, marker order and delimiter expansion remain the extraction contract.

## Evidence

### Repo-Internal References


- Inline block parsing is owned here; CLI behavior is separate and no deleted-suite pass is asserted. [2]
