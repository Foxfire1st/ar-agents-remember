# mcp/src/agents_remember/serving/conversation/library/normalize_common.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Single source for the small normalization primitives every dormant harness resolver needs, so
the Codex, Claude, and Pi ports cannot drift apart on text capping, provenance, required-field
parsing, or vendor text-content extraction.

## Code Commentary

### Logic

`capped_text` bounds one block's text at 8192 chars with a visible `…[truncated]` marker (the
resource guard). `native_provenance` builds native-history provenance: strength is always
`native-only`, producer only when proven. `required_field` extracts a non-empty string or
raises `LibraryStoreError` naming the missing key. `first_text` returns the first non-empty
trimmed string among candidate keys. `text_content_parts` extracts the text segments of a
vendor content field, whether a plain string or a typed block list.

### Conventions

Module-level constants and pure functions only; no state and no harness-specific knowledge.
Callers import through narrow aliases (`capped_text as _capped`) to keep resolver code
readable.

### Invariants And Boundaries

- Provenance strength is never promoted beyond `native-only` in this layer.
- Truncation is always visible; silent clipping is forbidden.
- Missing required fields fail closed as typed store errors, never `None` propagation.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal primitives module.

No configured domain documentation was available.

### Repo-Internal References

All three resolvers consume these primitives; the ports suite exercises them through the
normalized grammar on fake native payloads.

- The Codex parser builds its blocks and provenance on these primitives. [1]
- The Claude and Pi ports cap text, extract content, and require fields through this module. [2]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local primitives module.

No meaningful cross-repo references found.
