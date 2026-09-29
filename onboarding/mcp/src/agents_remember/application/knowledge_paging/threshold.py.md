# mcp/src/agents_remember/application/knowledge_paging/threshold.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/threshold.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The one token threshold every bounded knowledge read of a memory tree is cut to (MIK-R02 rule 1).** 8,000 `tiktoken:o200k_base` tokens, declared once and measured over the same canonical compact JSON the response choke point stamps as `tokens`.

## Code Commentary

### Logic

- `KNOWLEDGE_PAGE_THRESHOLD_TOKENS = 8000` and `KNOWLEDGE_PAGE_TOKENIZER` (the default counter's name). Every surface that pages a memory tree reads this constant, every page states it, and a continuation binds it, so a resumed read uses the same bound on whichever surface it resumes.
- `ENVELOPE_RESERVE_TOKENS = 64`: what the mounted choke point adds after a page is cut (`ok`, `operation` and the three token-accounting fields). A page is cut to the threshold less this reserve, so the response a caller receives stays within the threshold.
- `response_tokens(value)` is `count_response_tokens`; `threshold_block()` is the `{tokens, tokenizer}` object every page, block and refusal states.
- **The threshold, not `limit`, bounds a converted read (ruling Q4, 19:56:40).** `limit` still bounds database reads.

### Conventions

- One constant, never a per-surface value.

### Invariants And Boundaries

- **Every response states the threshold**, refusals included (ruling F8, 20:40:40); database refusals do not, which is preserved.
- `PUBLISHED_INTENT_MAX_UTF8_BYTES` is retired from the public API and from every converted read; the database page keeps a private byte budget until MIK-R26 (L26) retires that route (ruling Q2, 19:56:40).

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: one measurement for the cut and the stamped tokens. | "The one token threshold every bounded knowledge read" | mcp/src/agents_remember/application/knowledge_paging/threshold.py:1-9 |
| The declared threshold and its tokenizer. | `KNOWLEDGE_PAGE_THRESHOLD_TOKENS`; `KNOWLEDGE_PAGE_TOKENIZER` | mcp/src/agents_remember/application/knowledge_paging/threshold.py:27-28 |
| The envelope reserve the choke point adds. | `ENVELOPE_RESERVE_TOKENS` | mcp/src/agents_remember/application/knowledge_paging/threshold.py:33-33 |
| The measurement and the stated threshold. | `response_tokens`; `threshold_block` | mcp/src/agents_remember/application/knowledge_paging/threshold.py:36-45 |

## Cross-Repo References

No meaningful cross-repo references found: the constant is read by the package's own modules and the two read surfaces.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q2 the private database budget until L26; Q4 the threshold, not `limit`) and 20:40:40 (F8 refusals state the threshold). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
