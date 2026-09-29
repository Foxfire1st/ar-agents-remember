# mcp/src/agents_remember/application/knowledge_paging/scope_pages.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/scope_pages.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Pages of the selective scope read, the selection behind the published-intent block (MIK-R02).** The same functions build page 1 for `read_ar_files` and every later page for `knowledge_read`, so the pages of one walk are cut from one selection by one rule.

## Code Commentary

### Logic

- `SCOPE_POLICY`/`SCOPE_POLICY_VERSION` come from `KNOWLEDGE_READ_POLICY_VERSION` (`recorded-family-frontier`/`v1`). `_RESUMING_VIEW` maps a seed kind to the `knowledge_read` view that resumes it (a path is `source_context`).
- `scope_rows(items)`: each scope item is one row; a `family_revision` item heads the memberships of that revision with a `family_header_reference`; `advertised_family` items are rows without a header reference.
- `prepare_scope(request)`: selects the whole scope through `knowledge_read.select_knowledge_scope`, binds tree, policy, manifest and the context's code tree, and checks a resumed position (`position_refusal`). For a collapsed walk it also selects the first queued seed's manifest (`_next_manifest`), which the move on to it binds.
- `PreparedScope.render`, `.deferred()` (counts plus a position-0 continuation) and `.collapsed(queued)` (one entry listing `seeds`, `counts` of `total` and `returned`).
- `_page`: the block keeps `items`, `counts` (with `primary_items_returned`/`remaining` restated), `hasMore`, `enumerationComplete` (never true on a partial index), `continuation`, and adds `page`, `indexState`, `continuationOperation: "knowledge_read"`, `continuationView`, and `continuationSeed` when a finished seed's continuation moves on to the next queued seed.
- `scope_page(request)`: `prepare_scope` plus `cut_page`, the single-response path.

### Conventions

- The seed is spelled as the minting surface spelled it (`_seed_json`), so a resuming call need not repeat it.

### Invariants And Boundaries

- **What is selected does not change:** the rows are `select_recorded_scope`'s items; the reviewer found every real walk's union equal to `select_knowledge_scope`.
- In a collapsed walk a seed's last page states `enumerationComplete: true` while `continuation` moves on to the next seed; consumers follow `continuation` (R2-2, documented in c-04).

### Todos

- R2-2: the collapsed entry's `counts` has no `remaining` (accepted, ruling 21:32:34).

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
| The module statement: one rule for page 1 and later pages. | "Pages of the selective scope read" | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:1-14 |
| The resuming view by seed kind. | `_RESUMING_VIEW` | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:67-73 |
| Items as rows; a family revision heads its memberships. | `scope_rows` | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:106-124 |
| A prepared seed, deferred or collapsed. | `PreparedScope`; `collapsed` | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:127-183 |
| Selecting and checking a resumed position. | `prepare_scope`; `_next_manifest` | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:186-235 |
| The next token, or the move on to a queued seed. | `_continuation`; `continuationSeed` | mcp/src/agents_remember/application/knowledge_paging/scope_pages.py:257-305 |

## Cross-Repo References

No meaningful cross-repo references found: the scope is one memory tree's recorded neighbourhood.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q1 deferred seeds; Q6 page 1's code tree is bound), 20:40:40 (F2 the collapsed tail) and 21:32:34 (R2-2 accepted). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
