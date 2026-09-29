# mcp/src/agents_remember/memory/knowledge_index/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The package door of the derived knowledge index (MIK-R23).** Knowledge is text in Git (D18), and each relationship is written once, from its owner's side (D19). This package answers the reverse directions no file records — invariant to its code, test to invariant, route to families, record to what links to it, subject to its history rows — from an SQLite file derived from one memory tree and nothing else. The module docstring is the package map; the module body only re-exports.

## Code Commentary

### Logic

- The docstring names the seven modules and their jobs: `tree` (read a tree and compute its key), `build` (parse through the MIK-R21/R07 models and write the index; a failing file marks it `partial`), `projection` (also write the index as a dataset of the store's newest schema generation), `query` (the lookups; every answer carries the index state), `adapters` (a read-only store for the registered-scope construction) and `cache` (one file per tree key under the coordination runtime, never inside a Git working tree).
- `__all__` re-exports the public names of those modules, so callers (`application/published_intent.py`, `mcp/tools/knowledge.py`, `cli/knowledge_index.py`) import from the package.

### Conventions

- Imports are absolute (`agents_remember.memory.knowledge_index.<module>`), and `__all__` is sorted.

### Invariants And Boundaries

- No knowledge writer writes the index, and the index is never merged: it is rebuilt from the tree.
- Before MIK-R37 no production memory tree holds `knowledge/layout.json`, so the installed runtime's reads never reach this package.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The package statement and its exports.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map and the rule that no writer writes the index and it is never merged. | "No knowledge writer writes the index" | mcp/src/agents_remember/memory/knowledge_index/__init__.py:1-20 |
| The re-exported public surface. | `__all__` | mcp/src/agents_remember/memory/knowledge_index/__init__.py:63-94 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
