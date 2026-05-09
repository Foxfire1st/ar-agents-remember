# C-10-adopt-memory-baseline/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:46                           |
| lastVerifiedCommitHash | `82d7bbbb2cb222f168efd16d894aba260d7dfe75` |
| lastVerifiedCommitDate | 2026-05-09T22:42                           |

## Purpose

This skill documents the ergonomic adoption path for existing shared-memory onboarding that predates `memory.md`. It tells agents how to inspect that onboarding, surface drift, and create the first ledgered baseline only after the developer has accepted the trust decision.

## Code Commentary

### Logic

The skill routes users through `status` before `adopt`. The workflow resolves the repository with C-08, runs C-02 drift classification, checks for an existing ledger, blocks actionable drift unless `--accept-drift` is present, and then delegates the actual shared-memory bootstrap and `memory.md` creation to C-09.

### Conventions

The output is state-oriented: `ready`, `blocked-drift`, `already-ledgered`, `adopted`, and `would-adopt` are the reviewable states. `--accept-drift` is not an automatic refresh; it records the developer's assertion that the current onboarding is factual enough to become the memory baseline.

### Invariants And Boundaries

C-10 may create the initial ledgered shared-memory baseline through C-09, but it must not overwrite an existing `memory.md` and must not update onboarding content. C-05 remains the refresh path for stale or incomplete onboarding.

### Todos

No current todo is recorded for the skill description itself. Future work should stay in the script and tests unless the user-facing workflow changes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The skill is the human-facing contract for the adoption script and its trust boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill defines the adoption use case and makes C-02 drift plus explicit acceptance the central trust boundary. | L8-L10; L21-L28; L38-L43 | [C-10 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md) |
| The adoption script implements the documented states and delegates baseline creation to C-09. | L106-L123; L138-L176 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T22:46: Created onboarding for the C-10 adoption skill.
