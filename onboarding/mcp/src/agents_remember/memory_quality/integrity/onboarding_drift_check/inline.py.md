# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`inline.py` extracts inline onboarding blocks embedded in source files and
classifies them by source digest. Inline onboarding reuses the same content model
as sidecars but is verified through an embedded `sourceDigest`.

## Code Commentary

### Logic

`line_bounds` and `expand_inline_bounds` grow the block to include the surrounding
comment delimiter; `extract_inline_onboarding_block` parses metadata between the
`@ar-onboarding` / `@ar-onboarding-end` markers; `compute_inline_source_digest`
hashes the source with the block removed; `classify_inline_source` compares the
recorded `sourceDigest` to the computed digest; `discover_inline_onboarding_sources`
finds inline-eligible sources via storage resolution.

### Invariants And Boundaries

- The digest is computed over the source **with the block removed**, so editing
  the block contents does not register as drift.
- Non-UTF-8 sources are reported as unsupported rather than parsed.
- Reports drift only.

## Evidence

### Repo-Internal References

- Inline source enumeration reads repo files through `git_ops.list_repo_sources`. [1]
- Inline block parsing is owned here; CLI behavior is separate and no deleted-suite pass is asserted. [2]
