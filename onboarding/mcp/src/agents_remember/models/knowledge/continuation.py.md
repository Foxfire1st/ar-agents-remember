# mcp/src/agents_remember/models/knowledge/continuation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/continuation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one continuation every bounded read of a memory tree mints and `knowledge_read` accepts (MIK-R02 rule 3).** `KnowledgeContinuation` is self-describing, so a surface that did not mint it can resume it.

## Code Commentary

### Logic

- **What it binds:** `memory_tree_id` (the index key), `response` (`scope` or `view`), the resuming `view`, the `seed` as the minting surface spelled it (a view seed also carries its effective ordering), `selection_policy` and `policy_version`, `manifest_digest`, `position`, `threshold_tokens`, the optional `code_tree_id` page 1 resolved anchors at, and `rest`, the seeds queued behind this one in a collapsed block tail (at most 64).
- **No local path (ruling F2, 20:40:40).** Only the Git tree ID is bound; where its objects are read comes from the resuming request. The architect accepted the content-addressed tree ID plus a root check as equivalent or stronger than a repository-identity digest (ruling 21:32:34).
- `encode_continuation`: short aliases, `exclude_defaults`, canonical JSON, zlib level 9, base64url, prefix `kc2.`; a typical token is about 300 characters.
- `decode_continuation`: bounded length (16,384) and bounded decompression, then validation; any failure, or a seed value over `PATH_MAX_LENGTH`, returns `None`.
- The prefix has no `:`, so the view-token codec reads it as "not a view token", and the view token and database scope cursor keep their own meanings.

### Conventions

- The model is frozen and forbids extra fields; the wire uses the aliases.

### Invariants And Boundaries

- **The token is the whole state of a walk:** no cursor state is kept on the server.

### Todos

- **R2-1 (carried to L01):** a block of more than 64 queued seeds cannot be minted (`rest` `max_length`); unreachable through `read_ar_files`. The architect fixed R2-3's over-long docstring line.

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
| The module statement: every binding the token carries. | "The one continuation every bounded read of a memory tree mints" | mcp/src/agents_remember/models/knowledge/continuation.py:1-28 |
| The format, prefix and bounds. | `CONTINUATION_PREFIX`; `_MAX_QUEUED_SEEDS` | mcp/src/agents_remember/models/knowledge/continuation.py:57-67 |
| The bound fields and their short aliases. | `KnowledgeContinuation` | mcp/src/agents_remember/models/knowledge/continuation.py:72-113 |
| Encoding and bounded decoding. | `encode_continuation`; `decode_continuation` | mcp/src/agents_remember/models/knowledge/continuation.py:116-147 |

## Cross-Repo References

No meaningful cross-repo references found: the token names one memory tree and one code tree by content-addressed ID.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q5 ordering, Q6 code tree), 20:40:40 (F2 no local path) and 21:32:34 (the tree ID binding accepted; R2-1 carried to L01; R2-3 fixed). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
