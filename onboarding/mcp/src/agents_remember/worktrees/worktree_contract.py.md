# mcp/src/agents_remember/worktrees/worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T22:37+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`worktree_contract.py` reads, writes, validates, and renders the C-09
`contract.md` file that records worktree-backed task state.

## Code Commentary

### Logic

The module defines the contract schema, supported memory modes, the
`WorktreeContract` dataclass, deterministic task/worktree folder naming helpers,
default contract construction, markdown front-matter serialization, validation,
limited YAML-like parsing, and conversion from parsed front matter back into a
typed contract object.

### Conventions

The contract parser intentionally supports only the subset written by the
workflow: scalar top-level fields and one-level nested sections. This keeps
contract files human-readable without introducing a general YAML dependency.

### Invariants And Boundaries

- External-memory contracts must include memory repo, memory worktree, and
  ledger paths.
- Contract serialization must preserve closeout and integration state.
- Task and worktree folders use slugified names with legacy `-ar` support only
  where the resolver needs to find existing work.

### Todos

- `contract_to_text()` is a Phase 06 candidate for splitting into smaller
  rendering helpers.

## Docs References

No external documentation is needed for this local contract format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local worktree contract parser. | n/a | n/a |

## Repo-Internal References

Same-repository source defines the contract format and C-09 uses it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines the contract schema, valid memory modes, error type, and full `WorktreeContract` state record. | L14-L58 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Folder naming and default contract helpers derive task roots, worktree groups, and external-memory ledger paths. | L61-L151 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Load/write/render helpers parse front matter, validate contracts, and render closeout/integration state back to markdown. | L154-L270 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Validation and limited YAML parsing enforce required fields and external-memory path requirements. | L273-L368 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The C-09 worktree manager imports contract helpers and records closeout/integration commit state through these contract objects. | L25-L35; L934-L951; L1367-L1383 | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here; the contract points at
external memory paths, but the parser and renderer are same-repository code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
