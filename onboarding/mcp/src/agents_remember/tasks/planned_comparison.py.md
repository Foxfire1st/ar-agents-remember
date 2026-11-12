# mcp/src/agents_remember/tasks/planned_comparison.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Pure task-document, series-contract and frame-manifest helpers for planned comparisons and page rows — the vocabulary both serving and application read without either importing the other.

## Code Commentary

- It lives in the `tasks` tier so `serving` and `application` can both read a master's contract branches and build the planned record while `serving` still imports nothing from `application`.
- `planned_comparison` binds number 0 with each side's base equal to its candidate: a planning leaf's page compares the master line against nothing but itself.
- `agreed_revision_number` answers a number only through the canonical agreement resolver and only when its recorded digest verifies. A loose key, an unretained revision or a manifest satisfying neither exact-byte nor declared-artifact digest mode pins nothing.
- `contract_branch_lines` reads `source_branch` and `work_branch` per side from the contract text, orders them by the master's execution nature, de-duplicates them and falls back to `HEAD` only when the contract names neither.
- `resolve_line_commit` follows the first ref that resolves and answers `None` rather than substituting the repository's HEAD; `master_is_organizational` accepts `executionNature: organizational`, then either legacy organizational marker even when another executionNature value is present; absent all three markers it returns false.

## Evidence

- A planned comparison records number 0 with every base equal to its candidate [1]
- Only a resolved, digest-verified agreement pins a revision number [2]
- Each side's lines are read from the contract in the order the master's nature implies [3]
- An unresolvable line answers nothing instead of the repository's HEAD [4]

- A master with none of the three organizational markers reads as atomic [5]
