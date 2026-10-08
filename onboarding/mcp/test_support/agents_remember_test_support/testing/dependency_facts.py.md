# mcp/test_support/agents_remember_test_support/testing/dependency_facts.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the declaration-free repository import, pytest-plugin, and literal-consumer fact graph shared
by lifecycle validation, selection, retry, and causal reporting. The graph has no host-runner
responsibility. A disposable content-derived store reuses individual file facts while every build
reconstructs the current repository population and relations.

## Code Commentary

### Logic

`RepositoryDependencyFacts.build` inventories tracked and non-ignored untracked Python files,
resolves import identities, parses literal `pytest_plugins` assignments in every module, and derives
reverse import and exact literal-reader consumers. Dynamic plugin declarations and parse ambiguity
make the graph incomplete.

Every Python source is read once per build. The per-file cache key combines its bytes, the facts
implementation digest, Python version, resolved module identity and package status. Reuse avoids
AST parsing; it does not reuse stale inventory, test roots or graph edges. The default store is a
UID-owned private directory. Reads reject symlinks, foreign ownership and nonregular files;
unreadable, corrupt or wrong-shaped entries trigger derivation from source. JSON recursion failures
are disposable-store failures too. Invalid source remains a reported parse error on every build.

Writes use a temporary file and atomic replacement, always attempting to remove the temporary file.
The raw stored population count survives bad-entry filtering so compaction still triggers when the
store exceeds four times the current Python population; compaction retains only current entries.
Store failure never turns valid-source analysis into a failure or invalid-source analysis into success.

### Conventions

Lifecycle metadata may be compared with these facts; it never supplies missing facts.

### Invariants And Boundaries

- Recursive plugin declarations are imports regardless of filename.
- Consumer chains are real reverse edges, not name-only declarations.
- Parse or module ambiguity is retained as a refusal reason.
- Cache correctness is established by equal derived facts and parse/read counts, never an elapsed-time budget.
- An implementation, source, Python-version, module or package-identity change invalidates reuse.

### Todos

None.

## Evidence

### Docs References

No external documentation owns this repository graph.

### Repo-Internal References

`dependency_ownership.py` consumes the graph; `test_dependency_ownership_ast_helpers.py` forces
recursive and dynamic plugin behavior.

- The current source population and content identities govern reuse and bounded compaction. [1]
- Wrong-shaped or unreadable cached data is discarded without suppressing source errors. [2]
- Private atomic writes reclaim their temporary files. [3]

### Cross-Repo References

No cross-repository boundary applies.
