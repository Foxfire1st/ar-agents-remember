# mcp/test_support/agents_remember_test_support/testing/dependency_facts.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the declaration-free repository import, pytest-plugin, and literal-consumer fact graph shared
by lifecycle validation, selection, retry, and causal reporting. Candidate A's direct diagnostic
consumer was removed; the graph has no retained host-runner responsibility.

## Code Commentary

### Logic

`RepositoryDependencyFacts.build` inventories tracked and non-ignored untracked Python files,
resolves import identities, parses literal `pytest_plugins` assignments in every module, and derives
reverse import and exact literal-reader consumers. Dynamic plugin declarations and parse ambiguity
make the graph incomplete.

### Conventions

Lifecycle metadata may be compared with these facts; it never supplies missing facts.

### Invariants And Boundaries

- Recursive plugin declarations are imports regardless of filename.
- Consumer chains are real reverse edges, not name-only declarations.
- Parse or module ambiguity is retained as a refusal reason.

### Todos

None.

## Evidence

### Docs References

No external documentation owns this repository graph.

### Repo-Internal References

`dependency_ownership.py` consumes the graph; `test_dependency_ownership_ast_helpers.py` forces
recursive and dynamic plugin behavior.

### Cross-Repo References

No cross-repository boundary applies.
