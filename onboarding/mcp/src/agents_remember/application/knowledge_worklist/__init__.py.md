# mcp/src/agents_remember/application/knowledge_worklist/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The package front of the change-to-knowledge worklist (MIK-R08@v2).** For a leaf, the worklist is the
complete list of knowledge items its change requires a disposition for, computed from the exact code and
memory trees of the leaf's base and candidate (B, K_B, C, K_C; MIK-R07 rule 0) and persisted as
`knowledge-worklist/v1` in the leaf's enclosure. This module holds the package overview and re-exports the
public names of its submodules; it contains no logic of its own.

## Code Commentary

### Logic

- The docstring maps the package: `code` (hunks, line-range mapping, anchor ranges, content identities),
  `knowledge` (K_B and K_C through the derived index's parser), `classify` (entry classes and knowledge-side
  changes), `registry` (item kinds and stable item IDs), `compute` (one run), `leaf` (a leaf's sides, run and
  persisted file) and `surface` (what `knowledge_integrity_check` returns). `base_cache` (the converted-base
  cache, review R1 F6) is imported by `leaf` and is not re-exported.
- `__all__` re-exports the run (`compute_worklist`, `incomplete_worklist`, `WorklistInputs`, `Item`,
  `Incomplete`, `WORKLIST_SCHEMA`), the leaf surface (`leaf_worklist`, `recompute_leaf_worklist`,
  `LeafWorklistRecompute`, `worklist_for_sides`, `ExplicitSides`, `persist_worklist`, `read_leaf_worklist`,
  `worklist_path`, `WORKLIST_FILE_NAME`) and the registry (`ITEM_KINDS`, `ItemKind`, `item_id`,
  `register_item_kind`, `satisfying_row`).

### Conventions

- Consumers outside the package import from here, except `mcp/tools/knowledge.py`, which imports
  `surface.leaf_worklist_fields` directly, and the tests, which reach into `code`, `leaf` and `registry`.

### Invariants And Boundaries

- **An entry is raised in exactly three cases** (changed lines intersect its own range, it moved or
  disappeared, or it changed outside the managed flow); a change elsewhere in the same file raises nothing.
- **No verdict.** What an open item means is the closeout gate's (MIK-R09); the worklist carries no
  severity or causal explanation (MIK-R08 Exclusions).
- **Inert until the cutover.** A leaf whose two memory sides are both unconverted gets no worklist, which
  is every production leaf before MIK-R37; the installed runtime's behaviour is unchanged.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map and the three raising cases. | "a change elsewhere in the same file raises nothing" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:1-18 |
| The re-exported public names. | `__all__` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:49-70 |
| The run entry point it re-exports. | `compute_worklist` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:136-146 |
| The one recompute entry point it re-exports. | `recompute_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:403-434 |

## Cross-Repo References

No meaningful cross-repo references found: the module only re-exports its own package.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
