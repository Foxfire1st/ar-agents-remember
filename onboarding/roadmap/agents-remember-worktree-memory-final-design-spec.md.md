# agents-remember-worktree-memory-final-design-spec.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `roadmap/agents-remember-worktree-memory-final-design-spec.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `f096fe5879262be3d8b3362e41c1b89720a0d7ac` |
| lastVerifiedCommitDate | 2026-05-08T02:26                           |

## Purpose

This roadmap spec is the active design reference for splitting durable memory from local coordination and adding worktree-backed task support.

## Code Commentary

### Logic

The spec describes the target `ar-memory` and `ar-management` split, shared memory ledgers, task contracts, C-08 and C-09 responsibilities, lifecycle closeout, and implementation order.

### Conventions

It is design guidance, not implemented behavior. Onboarding should cite it for current design intent and planned entities, while helper scripts remain the source of truth for behavior already implemented.

### Invariants And Boundaries

`ar-memory` is planned to own durable memory. `ar-management` is planned to own local coordination state. Task contracts are local operational state and must not be confused with onboarding files or W-02 task plans.

### Todos

Convert relevant design statements into implementation onboarding only after the corresponding source files exist.

### Docs References

No external domain documentation is needed for this repository-local design spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This spec is a design input for the worktree-support program.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The spec introduces the `ar-memory` and `ar-management` split. | L14-L18 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| The shared memory ledger is summarized as a compatibility layer between code commits and memory commits. | L30-L34 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| Tasks and contracts are planned under the local coordinator rather than memory repos. | L115-L128 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| Ledger format and invariants define newest-first commit mapping metadata. | L451-L557 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| Task contract location, purpose, and example fields define future runtime coordination state. | L692-L783 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| C-08 remains facts-only while C-09 owns worktree and lifecycle mutation. | L787-L904 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| Lifecycle and closeout steps describe how worktree-backed tasks complete. | L995-L1098 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| Safety invariants and implementation order frame the active task stack. | L1358-L1434 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

The spec is about shared memory and code repositories, but no sibling repository file is required to prove the current design text.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for this file-level onboarding pass. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the worktree memory design spec.
