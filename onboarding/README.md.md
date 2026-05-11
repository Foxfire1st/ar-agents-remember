# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-11T19:42                           |
| lastVerifiedCommitHash | `aa85d3862bf21fed791e3170e6957f9288c319e8` |
| lastVerifiedCommitDate | 2026-05-11T19:32                           |

## Purpose

`README.md` is the public-facing explanation of Agents Remember. It explains one-to-one onboarding, setup, storage modes, shared roots, resolver and drift-check roles, and the repository's skill layout.

## Code Commentary

### Logic

The README introduces the memory model first, then explains setup, storage decisions, shared workspace behavior, active coordination context resolution, chat/worktree closeout behavior, and the available skill families. Its early "What This Looks Like" section shows both the default repo-local onboarding sidecar and the working shared-memory repo example, using clickable Markdown links to the public code repo and inspectable memory repo. It teaches `ar-memory/` for durable internal memory, `ar-coordination/` for local coordination, names C-09 `direct-closeout` as the approved current-checkout commit sequence for small shared-memory chat-mode edits, and lists C-10 as the adoption path that turns existing shared-memory onboarding into the first ledgered `memory.md` baseline after drift review.

### Conventions

The README distinguishes source files, onboarding files, generated maintenance artifacts, task workflow artifacts, shared memory repos, and the `memory.md` ledger. It treats C-08 as the resolver, uses `code_repository_name`/`code_repository_root` for resolver inputs, and treats C-02 as the drift classifier.

### Invariants And Boundaries

The README is explanatory, not an implementation source. When it disagrees with helper scripts, current script behavior should be verified before changing operational assumptions.

### Todos

Second-wave documentation should add richer walkthroughs for real C-09 start/closeout usage after the first production worktree task is run.

### Docs References

No external domain documentation is needed for this repository-level README.

| Finding                                                                                                               | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No relevant external documentation found; repository files are the source of truth for this README's behavior claims. | n/a       | n/a         |

## Repo-Internal References

The README establishes the conceptual map future tasks will repeatedly cite.

| Finding                                                                                                                                                                                                                                            | Citations | Source Path                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| One-to-one onboarding means source files have matching onboarding files.                                                                                                                                                                           | L89       | [README.md](agents-remember-md/README.md) |
| The working shared-memory example links to the code repo, the inspectable memory repo, the memory repo layout, and the `memory.md` code-to-memory ledger concept.                                                                                  | L43-L73   | [README.md](agents-remember-md/README.md) |
| C-00 creates memory and coordination scaffolds, while C-03 owns initial repo onboarding.                                                                                                                                                           | L137-L163 | [README.md](agents-remember-md/README.md) |
| Storage mode and path rules are separate concepts.                                                                                                                                                                                                 | L171-L180 | [README.md](agents-remember-md/README.md) |
| Inline storage reuses the same file-level onboarding model, and agents are wired through W-02/W-01 escalation.                                                                                                                                     | L203-L217 | [README.md](agents-remember-md/README.md) |
| The three modes section now notes that small chat-mode shared-memory edits can use C-09 `direct-closeout` for code-first onboarding metadata refresh and ledger sequencing, while larger or parallel work should use C-09 worktrees.               | L319      | [README.md](agents-remember-md/README.md) |
| C-08 resolves the active context from `code_repository_name` or `code_repository_root`, returns `coordination_root` and `memory_root`, and C-02 classifies stale onboarding.                                                                       | L468-L472 | [README.md](agents-remember-md/README.md) |
| The repository contains core skills, workflows, roadmap material, and system examples.                                                                                                                                                             | L476-L489 | [README.md](agents-remember-md/README.md) |
| The README lists C-09 as the helper for worktree-backed tasks and direct closeout of approved current-checkout edits, and C-10 as the helper for converting existing shared-memory onboarding into the first ledgered baseline after drift review. | L487-L488 | [README.md](agents-remember-md/README.md) |

## Cross-Repo References

The README explains shared workspace use, but this file-level onboarding does not rely on sibling repository internals.

| Finding                                                                                                                                  | Citations | Source Path                               |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Shared memory uses one memory repo per selected code repo while the coordinator owns tasks, notes, memory-repo checkouts, and worktrees. | L376-L462 | [README.md](agents-remember-md/README.md) |

## Update History

- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the resolver overview adopted `code_repository_name`, `code_repository_root`, and `coordination_root` terminology.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, C-09, and resolver contract changes.
- 2026-05-10T03:01: Updated after the README added C-09 direct-closeout as the lightweight current-checkout path for approved shared-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working shared-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
