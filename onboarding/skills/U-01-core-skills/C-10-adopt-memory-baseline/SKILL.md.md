# C-10-adopt-memory-baseline/SKILL.md

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember-md                                            |
| path                   | `skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md` |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-05-12T18:51+02:00                                        |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                    |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This skill documents the ergonomic adoption path for existing external-memory onboarding that predates `memory.md`. It tells agents how to inspect that onboarding, surface drift, and create the first ledgered baseline only after the developer has accepted the trust decision.

## Code Commentary

### Logic

The skill routes users through `status` before `adopt`. The workflow resolves the code repository with C-08 using `--code-repository-name` or `--code-repository-root`, runs C-02 drift classification with the reusable report under C-08's resolved temp root by default, checks for an existing ledger, blocks actionable drift unless `--accept-drift` is present, and then delegates the actual external-memory bootstrap and `memory.md` creation to C-09.

### Conventions

The output is state-oriented: `ready`, `blocked-drift`, `already-ledgered`, `adopted`, and `would-adopt` are the reviewable states. `--accept-drift` is not an automatic refresh; it records the developer's assertion that the current onboarding is factual enough to become the memory baseline.

### Invariants And Boundaries

C-10 may create the initial ledgered external-memory baseline through C-09, but it must not overwrite an existing `memory.md` and must not update onboarding content. C-05 remains the refresh path for stale or incomplete onboarding.

### Todos

No current todo is recorded for the skill description itself. Future work should stay in the script and tests unless the user-facing workflow changes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The skill is the human-facing contract for the adoption script and its trust boundary.

| Finding                                                                                                                                                                                     | Citations                | Source Path                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| The skill defines the adoption use case, uses `--code-repository-name`/`--code-repository-root` command examples, and makes C-02 drift plus explicit acceptance the central trust boundary. | L8-L19; L23-L30; L40-L45 | [C-10 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md)                                    |
| The adoption script implements the documented states and delegates baseline creation to C-09.                                                                                               | L103-L123; L135-L176     | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| C-10's drift run delegates report path resolution to C-02 with the resolved `coordination_root` and `temp_root`.                                                                            | L53-L67                  | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-10-adopt-memory-baseline` name.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` after confirming the C-10 coordination-rename contract remains current.
- 2026-05-11T18:34: Updated after C-10 command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T00:36: Refreshed verification metadata after C-10's temp-root report wording landed on main.
- 2026-05-09T23:22: Updated after C-10 documented temp-root drift report placement.
- 2026-05-09T22:46: Created onboarding for the C-10 adoption skill.
