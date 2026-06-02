# mcp/src/agents_remember/kernel/memory_ledger.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/memory_ledger.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_ledger.py` parses, validates, writes, and updates the external-memory
`memory.md` ledger that maps code commits to memory-content commits.

## Code Commentary

### Logic

The module reads a fenced JSON metadata block plus the first `Code commit |
Memory commit` table, validates that the newest table row matches the metadata,
serializes the canonical ledger format, prepends new mappings, finds existing
mappings, and creates an initial ledger.

### Conventions

The parser deliberately uses the standard library and a small markdown/table
grammar rather than pulling in a general markdown or YAML dependency.

### Invariants And Boundaries

- `sortOrder` must remain `newest-first`.
- The first table row must match `lastVerifiedCodeCommit` and
  `lastMemoryContentCommit`.
- `prepend_mapping()` requires both commits and updates metadata and rows
  together.

### Todos

- `parse_ledger_rows()` is a Phase 06 complexity hotspot candidate.

## Docs References

No external documentation is needed for this repository-local ledger format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local ledger parser. | n/a | n/a |

## Repo-Internal References

Same-repository source is the direct evidence for the external-memory ledger
format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines the canonical ledger schema, row and ledger dataclasses, and validation error type (a subclass of `AgentsRememberError`). | L17-L41 | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| `parse_ledger_text()` requires the fenced JSON metadata block, required metadata fields, supported schema, and a valid mapping table. | L51-L104 | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| `validate_ledger()`, `ledger_to_text()`, and `prepend_mapping()` keep metadata and newest-first rows synchronized. | L142-L179; L193-L204 | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Cross-Repo References

The ledger records code and memory commits across the source repository and its
external memory repository, but the implementation contract is local to this
file and the `c-09-git-worktree-manager` skill worktree manager.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-09-git-worktree-manager` skill imports ledger helpers for closeout, integration, and direct closeout mapping updates. | L18-L24; L923-L929; L1071-L1078 | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed `find_ledger_anchor_commit()` (and its `subprocess` use) from Logic and references; `LedgerError` now subclasses `AgentsRememberError` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted `_ledger_rows_from` (inner row loop) from `parse_ledger_rows` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
