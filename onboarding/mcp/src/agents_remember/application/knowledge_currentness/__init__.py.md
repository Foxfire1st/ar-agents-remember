# mcp/src/agents_remember/application/knowledge_currentness/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_currentness/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083`|
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Stale invariants flagged at read time (MIK-R03@v2): the package's front door.** Every read that returns
an invariant from a converted memory tree also returns its currentness at the requested code tree:
`stale`, `unverifiable`, `unrealized` or `current`. A stale invariant stays visible and names each
differing entry; reads never write, re-anchor or judge. The package docstring maps the rules to the three
modules, and this file re-exports their public names.

## Code Commentary

### Logic

- `observe` holds rules 1 and 5: one entry's state at one code tree, and the observation cache
  (`OBSERVATIONS`, `observation_key`, `EXTRACTOR_VERSION`).
- `state` holds rules 2 to 4: `invariant_currentness`, the one function of (code tree, memory tree), which
  the reviewer (MIK-R25) will call per side and the path-based reader (MIK-R29) at its selected commit.
- `surface` holds the `currentness` block that `knowledge_read` and the published-intent block of
  `read_ar_files` attach (`read_currentness`, `requested_code_tree`, `returned_records`).

### Conventions

- Callers import from the package (`knowledge_currentness import CodeTree, read_currentness`), not from the
  submodules. The tests reach into `observe` and `surface` only to patch.

### Invariants And Boundaries

- **Inert before MIK-R37.** Both surfaces attach the block only when the selection is a converted memory
  tree, so an unconverted tree (today's installed runtime) reads byte-identically, with no `currentness`
  key (worker and reviewer real-data comparisons).

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package statement and its map of rules to modules. | "Stale invariants flagged at read time" | mcp/src/agents_remember/application/knowledge_currentness/__init__.py:1-14 |
| The re-exported names. | `invariant_currentness`; `read_currentness` | mcp/src/agents_remember/application/knowledge_currentness/__init__.py:26-39 |
| The two consumers import through the package. | "from agents_remember.application.knowledge_currentness import" | mcp/src/agents_remember/application/published_intent.py:91-91; mcp/src/agents_remember/mcp/tools/knowledge.py:41-44 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's index and one code
repository's object store, both named by its caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new package MIK-R03 adds. No `knowledge_currentness/overview.md` was created, following the `knowledge_worklist/` precedent; the application route overview governs it. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
