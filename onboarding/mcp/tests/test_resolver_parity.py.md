# test_resolver_parity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_resolver_parity.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

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

## Series-Contract Notes

Resolver parity tests now pin task-name lookup over active roots, nested parent disambiguation, leaf-id selection, archive exclusion, and parity between source API and MCP wrapper arguments.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: resolver parity coverage now includes active task-name lookup, nested parent disambiguation, leaf enclosure resolution, archive exclusion, and source API/MCP wrapper parity for the new resolver arguments. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after resolver parity tests stopped comparing against the deleted old script.
