# mcp/tests/test_knowledge_index.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rules 1–5 and the Failure rule: sources, key, answers, partial state, cache and the `knowledge-index` command.** Every case builds a real memory tree in a real Git repository (`write_review_tree`) and indexes it through the public cache, so the key, the capture and the Git-object reads are the production ones. Registered in the `unit-regression` lane; 22 collected cases (the index-flag case is parametrized over both flags; MIK-R04 added the root-route case).

## Code Commentary

### Logic

- **Sources and key:** a working tree and its Git tree index to the same key and answers; a historical tree is read through objects without a checkout (HEAD and status unchanged); the key equals `HEAD^{tree}` when clean, `git stash create`'s tree when edited, is restored by reverting, is equal for an identical copy, and ignores an ignored `overview.index.json`; capturing writes nothing (index bytes, object set and status unchanged); a plain directory has no key.
- **Answers:** path lookups, the invariant answer (code, tests, families, links, history), family members and routes with routes answering their families, a family routed at the root route `.` governing both a root-level file and a deep file (MIK-R04, added by leaf 260928-MIK-L04 for review R3-1), incoming links, and history rows by subject and by leaf (the index query moved here from MIK-R07).
- **Freshness and failure:** an edited working tree is never answered from the previous content; a file failing its schema marks the index `partial` and is named; an unconverted tree indexes empty and says so.
- **Cache:** reuse, rebuild and loss-free deletion; eviction by age and size; a cache inside a Git working tree is refused with no directory left behind; an `assume-unchanged` or `skip-worktree` flag never hides an edit; the file declares its format and key.
- **Command and filter:** `knowledge-index` reports JSON and exits 0/1/2 by state; the index reads the files the validator reads (knowledge record, hidden directory, route cache, census, Markdown).

### Conventions

- The `memory` fixture writes the review tree and commits it; the `cache` fixture places the cache under `tmp_path`, outside the repository.

### Invariants And Boundaries

- Each packet obligation has a case that drives real Git state, not a stub.

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

The cases.

- The fixtures: a committed review tree and a cache outside it. [1]
- Sources and key. [2]
- Answers. [3]
- A family routed at the root governs every path. [4]
- Freshness, partial state and an unconverted tree. [5]
- Cache, flags and format. [6]
- The command and the shared file filter. [7]
- The lane row. [8]

### Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

No cross-repo boundary is crossed by this file.
