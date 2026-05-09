# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:46                           |
| lastVerifiedCommitHash | `9ab2d2ceddc5dd0b83e14b64b44f5087e4d1935e` |
| lastVerifiedCommitDate | 2026-05-09T22:43                           |

## Purpose

`README.md` is the public-facing explanation of Agents Remember. It explains one-to-one onboarding, setup, storage modes, shared roots, resolver and drift-check roles, and the repository's skill layout.

## Code Commentary

### Logic

The README introduces the memory model first, then explains setup, storage decisions, shared workspace behavior, worktree support, and the available skill families. It teaches `ar-memory/` for durable internal memory, `ar-management/` for local coordination, and lists C-10 as the adoption path that turns existing shared-memory onboarding into the first ledgered `memory.md` baseline after drift review.

### Conventions

The README distinguishes source files, onboarding files, generated maintenance artifacts, and task workflow artifacts. It treats C-08 as the resolver and C-02 as the drift classifier.

### Invariants And Boundaries

The README is explanatory, not an implementation source. When it disagrees with helper scripts, current script behavior should be verified before changing operational assumptions.

### Todos

Second-wave documentation should add richer walkthroughs for real C-09 start/closeout usage after the first production worktree task is run.

### Docs References

No external domain documentation is needed for this repository-level README.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found; repository files are the source of truth for this README's behavior claims. | n/a | n/a |

## Repo-Internal References

The README establishes the conceptual map future tasks will repeatedly cite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| One-to-one onboarding means source files have matching onboarding files. | L57-L61 | [README.md](agents-remember-md/README.md) |
| C-00 creates memory and coordination scaffolds, while C-03 owns initial repo onboarding. | L101-L131 | [README.md](agents-remember-md/README.md) |
| Storage mode and path rules are separate concepts. | L122-L135 | [README.md](agents-remember-md/README.md) |
| Inline storage reuses the same file-level onboarding model, and agents are wired through W-02/W-01 escalation. | L158-L170 | [README.md](agents-remember-md/README.md) |
| C-08 resolves the active context and C-02 classifies stale onboarding. | L424-L430 | [README.md](agents-remember-md/README.md) |
| The repository contains core skills, workflows, roadmap material, and system examples. | L434-L444 | [README.md](agents-remember-md/README.md) |
| The README lists C-10 as the helper for converting existing shared-memory onboarding into the first ledgered baseline after drift review. | L449-L454 | [README.md](agents-remember-md/README.md) |

## Cross-Repo References

The README explains shared workspace use, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Shared memory uses one memory repo per selected code repo while the coordinator owns tasks, notes, memory-repo checkouts, and worktrees. | L344-L436 | [README.md](agents-remember-md/README.md) |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
- 2026-05-09T21:59: Updated for ar-memory/ar-management split, C-09, and resolver contract changes.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
