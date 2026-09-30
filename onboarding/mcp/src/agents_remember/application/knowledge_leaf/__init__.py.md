# mcp/src/agents_remember/application/knowledge_leaf/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_leaf/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T02:10:00+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The family-complete leaf read of a converted memory tree (MIK-R01@v2): the package's front door.** A read seeded with one source path returns, from the tree's derived index (MIK-R23), the path's own invariants, every family containing them with its guarantee and routes, every member's statement, conditions and entries, and the advertised frontier. It is returned in one response when it fits the shared threshold, and otherwise as pages that `knowledge_read` continues (MIK-R02). The package re-exports the policy name and version, the view name, the request and prepared types, `prepare_leaf`, `select_leaf` and `family_names`.

## Code Commentary

### Logic

- **Module map.**
  - `selection`: what a seed path selects, in which order, and the rows at a code tree.
  - `pages`: the paged response both surfaces emit (the `read_ar_files` block and `knowledge_read`'s `source_context` view), through L02's `knowledge_paging` seam.
  - `currentness`: the page's `currentness` block, cut from what each prepared leaf already computed. It is imported by its module path, not re-exported.
- **The leaf read is one more paged response.** Nothing in the paging seam is duplicated: `PreparedLeaf` has the same shape as L02's `PreparedScope` (rows, binding, `render`, `deferred`, `collapsed`), and its continuation carries the response kind `leaf` and resumes on view `source_context`.
- **Where it is reached.** On a converted tree, a path seed of `read_ar_files` and a fresh `knowledge_read` `source_context` read with `sourcePath` are the leaf read. An identity seed keeps the scope read (L01 ruling N2, 2026-09-30 00:08:39).

### Conventions

- The docstring is the package's design statement; each module's docstring carries its rule's detail.

### Invariants And Boundaries

- **Unconverted reads do not reach this package.** A read of an unconverted database keeps the recorded-scope read; the worker and both review rounds measured unconverted reads byte-identical to base.
- **Inert before MIK-R37.** Only a converted memory tree (the layout marker present) reaches this code, and the installed runtime reads no converted tree today.
- **Reads only.** The package opens the index read-only and writes nothing (MIK-R01 Exclusions: no ranking and no writes).

### Todos

- **MIK-R05.** Route-chain families for a path with no entries belong to MIK-R05 (L01 ruling Q6, 2026-09-29 23:21:57). Today such a path is `registration_absent`; route-chain rows would be appended after the advertised frontier.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R01@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`01_family-complete-leaf-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package statement: one seed path, the whole family neighbourhood, paged by the shared threshold. | "The family-complete leaf read of a converted memory tree" | mcp/src/agents_remember/application/knowledge_leaf/__init__.py:1-13 |
| The re-exported surface. | `prepare_leaf`; `select_leaf`; `family_names` | mcp/src/agents_remember/application/knowledge_leaf/__init__.py:17-39 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's derived index.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): created this card for the new package MIK-R01 adds. It records the architect rulings of 2026-09-29 23:21:57 (Q6: route-chain families are MIK-R05's) and 2026-09-30 00:08:39 (N2: identity seeds keep the scope read). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
