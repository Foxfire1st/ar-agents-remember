# mcp/src/agents_remember/serving/conversation/library/normalize_common.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/normalize_common.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal primitives module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

All three resolvers consume these primitives; the ports suite exercises them through the
normalized grammar on fake native payloads.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Codex parser builds its blocks and provenance on these primitives. | L19-L24 | [codex_normalize.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex_normalize.py) |
| The Claude and Pi ports cap text, extract content, and require fields through this module. | L29-L39; L28-L36 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/claude.py), [pi.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/pi.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local primitives module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the shared normalization primitives
  sidecar. Verification is blank until closeout commits and stamps the new source.
