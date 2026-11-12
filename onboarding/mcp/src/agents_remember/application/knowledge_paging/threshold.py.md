# mcp/src/agents_remember/application/knowledge_paging/threshold.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The one token threshold every bounded knowledge read of a memory tree is cut to (MIK-R02 rule 1).** 8,000 `tiktoken:o200k_base` tokens, declared once. Under MIK-R108 the threshold guarantee belongs to the whole result the producer computed (read back from the answer's detail file): answers no longer carry the stamped count — the log line does — so a page is cut to the threshold less the reserve below and the received answer stays within it.

## Code Commentary

The threshold header uses the light TOKENIZER_NAME string; measuring a response loads the existing models.tokens counter at first measurement, retaining the same 8000-token threshold and tokenizer name.

### Logic

- `KNOWLEDGE_PAGE_THRESHOLD_TOKENS = 8000` and `KNOWLEDGE_PAGE_TOKENIZER` (the default counter's name). Every surface that pages a memory tree reads this constant, every page states it, and a continuation binds it, so a resumed read uses the same bound on whichever surface it resumes.
- `ENVELOPE_RESERVE_TOKENS = 64`: what the mounted response choke point adds after a page is cut (`ok` and, under MIK-R108, `next`/`log` instead of the envelope). A page is cut to the threshold less this reserve, so the answer a caller receives — not only the body this module measured — stays within the threshold.
- `response_tokens(value)` is `count_response_tokens`; `threshold_block()` is the `{tokens, tokenizer}` object every page, block and refusal states.
- **The threshold, not `limit`, bounds a converted read (ruling Q4, 19:56:40).** `limit` still bounds database reads.

### Conventions

- One constant, never a per-surface value.

### Invariants And Boundaries

- **Every response states the threshold**, refusals included (ruling F8, 20:40:40); database refusals do not, which is preserved.
- `PUBLISHED_INTENT_MAX_UTF8_BYTES` is retired from the public API and from every converted read; the database page keeps a private byte budget until MIK-R26 (L26) retires that route (ruling Q2, 19:56:40).

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The module statement: one measurement for the cut and the stamped tokens. [1]

- The declared threshold and its tokenizer. [2]
- The envelope reserve the choke point adds. [3]
- The measurement and the stated threshold. [4]

### Cross-Repo References

No meaningful cross-repo references found: the constant is read by the package's own modules and the two read surfaces.

No cross-repo boundary is crossed by this file.

- The threshold header uses the light TOKENIZER_NAME string; measuring a response loads the existing models.tokens counter at first measurement, retaining the same 8000-token threshold and tokenizer name. [5]
