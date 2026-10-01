# mcp/src/agents_remember/application/knowledge_currentness/__init__.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The package statement and its map of rules to modules. [1]
- The re-exported names. [2]
- The two consumers import through the package. [3]

### Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's index and one code
repository's object store, both named by its caller.

No cross-repo boundary is crossed by this file.
