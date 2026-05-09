# agents-remember-cross-repo-mode-design-spec.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `roadmap/agents-remember-cross-repo-mode-design-spec.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `f096fe5879262be3d8b3362e41c1b89720a0d7ac` |
| lastVerifiedCommitDate | 2026-05-08T02:26                           |

## Purpose

This roadmap spec is the active design reference for cross-repo mode v2, especially branch-gated inclusion of external repository code and memory.

## Code Commentary

### Logic

The spec replaces permissive string allow entries with structured `crossRepo.allow` objects that include repo, expected branch, and inclusion flags. It defines result states, read-only external repo behavior, and interactions with worktree context and memory ledgers.

### Conventions

The file is design guidance, not implemented behavior. It should be used to understand intended cross-repo semantics while current resolver code remains the implementation source of truth.

### Invariants And Boundaries

External repository context must be branch-gated, explicit, and read-only. Cross-repo inclusion should fail closed when expected branch or memory-ledger checks do not pass.

### Todos

Create implementation onboarding for resolver changes when cross-repo v2 is coded.

### Docs References

No external domain documentation is needed for this repository-local design spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This spec is a design input for resolver and worktree changes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Executive summary defines branch-gated `crossRepo.allow` as the core v2 change. | L14-L34 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |
| Structured allow entries include `expectedBranch`, `includeCode`, and `includeMemory`. | L185-L217 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |
| External repositories are read-only context sources. | L257-L261 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |
| Result states define how branch and memory checks succeed or fail. | L604-L648 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |
| Worktree interaction is explicitly part of cross-repo resolution. | L700-L715 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |
| Final design sentence frames cross-repo mode as explicit, branch-gated, read-only, and ledger-aware. | L904-L907 | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) |

## Cross-Repo References

The spec discusses external repository inclusion, but this onboarding unit cites only the local design spec because no implementation target exists yet.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for this file-level onboarding pass. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the cross-repo mode design spec.
