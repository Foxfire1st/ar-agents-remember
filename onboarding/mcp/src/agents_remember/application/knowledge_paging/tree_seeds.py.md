# mcp/src/agents_remember/application/knowledge_paging/tree_seeds.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A read seed a converted memory tree does not hold is refused, never answered as an empty complete view (L37
ruling, P2 task 4).** A read of a converted tree addresses invariant and family revisions by the UUIDs the derived
index projects for `<ID>@<revision>`. At the cutover every remembered database-era revision ID names nothing, and so
does a bare `INV-…`. An empty, complete answer to such a seed would look like "the tree holds nothing about this".
This module decides whether a seed is held and words the `selector_absent` reason.

## Code Commentary

### Logic

- `absent_seed(index, name, named)` asks the index for the text ID behind `named` (`index.text_id`). The seed is
  held when that text starts with the parameter's prefix (`INV-` for `invariantRevisionId`, `FAM-` for
  `familyRevisionId`) and holds an `@`. Otherwise it returns the reason, which ends with `SEED_SOURCES`: take a seed
  from the knowledge section of `read_ar_files` or from a `source_context` row.
- **A bare held ID is told its seed.** When `named` is itself a record ID the tree holds (not retired, with a
  revision), the reason adds "`<ID>` is held here at revision `<n>`, whose seed is `<uuid>`"
  (`text_uuid("revision", "<ID>@<revision>")`).
- `tree_seed_refusal(database_path, tree_key, *, invariant_revision_id, family_revision_id)` opens the index of the
  tree (`KnowledgeIndex(..., expected_key=tree_key)`) only when a seed is named, and returns the reason of the first
  seed that is absent, or `None`.

### Conventions

- Callers: `knowledge_paging/tree_read._fresh_seed_absent` (a fresh `knowledge_read` page) and
  `mcp/tools/knowledge._tree_seeds_absent` (the view seeds of `knowledge_project`). Both refuse with
  `selector_absent`.

### Invariants And Boundaries

- **A database read is not touched.** Only a selection that carries a converted memory tree reaches this module;
  an unconverted dataset keeps its own answers, including an empty complete view for an unknown seed.
- The module reads the index and writes nothing.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the L37 ruling of 2026-10-01T02:28:10 in `37_cutover-to-text-storage.json` (task `260928_maintained-invariant-knowledge`), with `MIK-R23@v1` rule 6; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: why an unheld seed is refused and that a database read is untouched. [1]
- Why a named seed names no revision the tree holds; a bare held ID is told its seed. [2]
- The reason for the first seed the tree does not hold. [3]
- Where current seeds come from, as every refusal says. [4]
- A converted tree refuses a database-era UUID, a bare ID and an unheld family; a database read with an unknown seed is still a complete view. [5]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one derived index.

No cross-repo boundary is crossed by this file.
