# mcp/src/agents_remember/memory/knowledge_index/__init__.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The package door of the derived knowledge index (MIK-R23).** Knowledge is text in Git (D18), and each relationship is written once, from its owner's side (D19). This package answers the reverse directions no file records — invariant to its code, test to invariant, route to families, record to what links to it, subject to its history rows — from an SQLite file derived from one memory tree and nothing else. The module docstring is the package map; the module body only re-exports.

## Code Commentary

### Logic

- The package map names `tree`, `build`, `projection`, `query` and `cache`. `with_prose_companions` is public: nonexcluded onboarding Markdown and Markdown beside indexed record JSON ride as unparsed bytes for card/record comparison, never parsed JSON. The index remains derived-only and is never a write authority.

- The cache groups files by loaded build and memory-tree key; `open_cached_index` exposes read-only reuse of an existing matching file.

- `__all__` re-exports the public names of those modules, so callers (`application/published_intent.py`, `mcp/tools/knowledge.py`, `cli/knowledge_index.py`) import from the package.

### Conventions

- Imports are absolute (`agents_remember.memory.knowledge_index.<module>`), and `__all__` is sorted.

### Invariants And Boundaries

- No knowledge writer writes the index, and the index is never merged: it is rebuilt from the tree.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The package statement and its exports.






### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.

- The package map and the rule that no writer writes the index and it is never merged. [1]
- The re-exported public surface. [2]
- Public index surface includes prose companions without making prose an indexed model. [3]
