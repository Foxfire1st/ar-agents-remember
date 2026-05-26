# mcp/src/agents_remember/worktrees/worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:41+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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
typed contract object. Contract rendering is split into small section renderers
for memory, human review, closeout, integration, and body content.

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
| Load/write/render helpers parse front matter, validate contracts, and render closeout/integration state back to markdown. | L154-L289 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Validation and limited YAML parsing enforce required fields and external-memory path requirements. | L292-L387 | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The worktree lifecycle modules import contract helpers and record closeout/integration commit state through these contract objects. | n/a | [modules/overview.md](agents-remember-md/mcp/src/agents_remember/worktrees/modules/overview.md) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here; the contract points at
external memory paths, but the parser and renderer are same-repository code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-25T20:41+02:00: Updated after contract rendering was split into section helpers during worktree package refactoring.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
