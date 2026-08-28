# mcp/test_support/agents_remember_test_support/testing/dependency_facts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/dependency_facts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T10:16:27+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No external documentation owns this repository graph.

## Repo-Internal References

`dependency_ownership.py` consumes the graph; `test_dependency_ownership_ast_helpers.py` forces
recursive and dynamic plugin behavior.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T10:03:40+02:00 — Removed the retired direct-diagnostic consumer from the current
  dependency-fact ownership description; selection, retry, lifecycle, and causal consumers remain.

- 2026-08-27T11:08+02:00 — Created to remove declaration-owned completeness.
