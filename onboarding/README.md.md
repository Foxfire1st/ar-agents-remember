# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T02:20                           |
| lastVerifiedCommitHash | `6f439b24b0c2cb0420352c0a9a889fef91e4f29c` |
| lastVerifiedCommitDate | 2026-05-10T02:45:03+02:00                  |

## Purpose

`README.md` is the public-facing explanation of Agents Remember. It explains one-to-one onboarding, setup, storage modes, shared roots, resolver and drift-check roles, and the repository's skill layout.

## Code Commentary

### Logic

The README introduces the memory model first, then explains setup, storage decisions, shared workspace behavior, worktree support, and the available skill families. Its early "What This Looks Like" section now shows both the default repo-local onboarding sidecar and the working shared-memory repo example, linking to the public code repo and inspectable memory repo. It teaches `ar-memory/` for durable internal memory, `ar-management/` for local coordination, and lists C-10 as the adoption path that turns existing shared-memory onboarding into the first ledgered `memory.md` baseline after drift review.

### Conventions

The README distinguishes source files, onboarding files, generated maintenance artifacts, task workflow artifacts, shared memory repos, and the `memory.md` ledger. It treats C-08 as the resolver and C-02 as the drift classifier.

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
| One-to-one onboarding means source files have matching onboarding files. | L91-L93 | [README.md](agents-remember-md/README.md) |
| The working shared-memory example links to the code repo, the inspectable memory repo, the memory repo layout, and the `memory.md` code-to-memory ledger concept. | L43-L77 | [README.md](agents-remember-md/README.md) |
| C-00 creates memory and coordination scaffolds, while C-03 owns initial repo onboarding. | L130-L160 | [README.md](agents-remember-md/README.md) |
| Storage mode and path rules are separate concepts. | L151-L164 | [README.md](agents-remember-md/README.md) |
| Inline storage reuses the same file-level onboarding model, and agents are wired through W-02/W-01 escalation. | L187-L199 | [README.md](agents-remember-md/README.md) |
| C-08 resolves the active context and C-02 classifies stale onboarding. | L453-L459 | [README.md](agents-remember-md/README.md) |
| The repository contains core skills, workflows, roadmap material, and system examples. | L463-L473 | [README.md](agents-remember-md/README.md) |
| The README lists C-10 as the helper for converting existing shared-memory onboarding into the first ledgered baseline after drift review. | L478-L483 | [README.md](agents-remember-md/README.md) |

## Cross-Repo References

The README explains shared workspace use, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Shared memory uses one memory repo per selected code repo while the coordinator owns tasks, notes, memory-repo checkouts, and worktrees. | L344-L436 | [README.md](agents-remember-md/README.md) |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
- 2026-05-09T21:59: Updated for ar-memory/ar-management split, C-09, and resolver contract changes.
- 2026-05-10T02:20: Updated after the README added a working shared-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
