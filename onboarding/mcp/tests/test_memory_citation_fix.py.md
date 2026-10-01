# mcp/tests/test_memory_citation_fix.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

On-disk code/memory tree and assertion helpers for citation-fixer consumers.

## Code Commentary

### Logic

Tree creates temporary source and onboarding files, invokes scoped check/fix boundaries, and now builds real Git provenance: `git` runs one command and raises `AssertionError` on a non-zero exit, `history` makes the code root a Git repository with a user config, `stamp` commits every source written so far and returns the resulting commit SHA, and `remove_source` unlinks one already-committed source so the move can be discovered. A fixture that expects a legitimate relocation must therefore create the verified tree first, because a relocation may only follow a name when the extent the claim was verified against is readable at that commit. `document` and `Tree.card` take an optional `stamp` that inserts a `| lastVerifiedCommitHash | \`<sha>\` |` row inside the metadata table — never below the citation header, where a bare row would parse as another claim — and `Tree.row` locates one citation row by finding the `CITATION_HEADER` line and stepping past header and delimiter, so card metadata can no longer shift the row index. TreeCase provides repaired/declined/clean assertions. The frozen no-discovery helper supports explicit scoped source acquisition. There are no retained repair-class or write-guard tests in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The module docstring states a PURE MOVE is applied only when continuity is proved: the anchor kept its name, changed file, and the extent the claim was verified against is readable at its stamp with the same kind. RENAME, DELETION and AMBIGUOUS remain refused. Historical pure-move/rename/deletion/ambiguity prose describes earlier tests, not current standalone protection. Helpers must not manufacture semantic similarity approval.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Frozen no discovery. [1]
- Document. [2]
- Filler. [3]
- Tree. [4]
- One Git command per root, failing loudly on a non-zero exit. [5]
- The code root is initialised, stamped by committing every source written so far, and one committed source can be removed so the move is discovered. [6]
- A citation row is located by the citation header, not by a fixed row index. [7]
- Treecase. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
