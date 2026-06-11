# test_resolver_parity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_resolver_parity.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `b9f1a31ccf6c826f4558e15d3feada70d2375e66` |
| lastVerifiedCommitDate | 2026-06-11T15:04:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_resolver_parity.py` protects the package resolver CLI output shape for
external, internal, and contract-backed contexts.

## Code Commentary

### Logic

The tests create temporary code, adjacent, coordination, and memory roots, write
minimal settings, and execute `agents_remember.kernel.coordination_context_resolver`
as a package module. Assertions check the complete context key set for external
memory, internal memory, and worktree contract resolution, including worktree
contract path and group fields.

### Invariants And Boundaries

The resolver must keep the `c-08-ar-coordination-context-resolver` skill JSON shape stable after moving out of the skill
tree. Tests should exercise the package route directly rather than loading a
deleted runtime skill script.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package resolver module provides the tested CLI. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Worktree contracts supply the contract-backed fixture. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after resolver parity tests stopped comparing against the deleted old script.
