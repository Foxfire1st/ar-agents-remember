# mcp/src/agents_remember/application/knowledge_paging/scope_pages.py

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

- The module statement: one rule for page 1 and later pages. [1]
- The resuming view by seed kind. [2]
- Items as rows; a family revision heads its memberships. [3]
- A prepared seed, deferred or collapsed. [4]
- Selecting and checking a resumed position. [5]
- The next token, or the move on to a queued seed. [6]

### Cross-Repo References

No meaningful cross-repo references found: the scope is one memory tree's recorded neighbourhood.

No cross-repo boundary is crossed by this file.
