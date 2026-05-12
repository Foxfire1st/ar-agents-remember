# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/AGENTS.md`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-12T11:36                           |
| lastVerifiedCommitHash | `3274222c6f818f2241073eecd351cc6f6cb43e07` |
| lastVerifiedCommitDate | 2026-05-12T11:38:46+02:00|

## Purpose

`skills/U-01-core-skills/AGENTS.md` is the local routing guide for the core C-\* skills. It helps agents choose the correct support skill before editing memory, onboarding, task contracts, worktrees, ledgers, or carryover state.

## Code Commentary

### Logic

The file is a numbered question-to-skill map. It routes context resolution to C-08, missing scaffolds to C-00, stale onboarding to C-02, durable finding placement to C-01, bootstrap onboarding to C-03, unfamiliar-surface discovery to C-04, onboarding artifact maintenance to C-05, lifecycle and ledger operations to C-09, baseline adoption to C-10, and branch memory carryover to C-11.

### Conventions

Each route is written as a developer-facing question followed by the canonical skill identifier. The file intentionally stays compact so it can be read quickly when an agent is already inside the core-skills folder.

### Invariants And Boundaries

This file is routing context only. It should point to the owning skill rather than duplicating that skill's full workflow contract, approval gates, or command syntax.

### Todos

No standalone TODO is recorded for this routing file.

### Docs References

No external domain documentation is needed for this repository-local routing guide.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The local routing guide is governed by the broader skills-folder doctrine, but the route list itself is the primary implementation evidence.

| Finding                                                                                                             | Citations | Source Path                                                                   |
| ------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------- |
| Core-skill routing maps common memory, onboarding, discovery, lifecycle, baseline, and carryover needs to C-\* IDs. | L1-L33    | [Core Skills AGENTS.md](agents-remember-md/skills/U-01-core-skills/AGENTS.md) |
| The parent skills instruction explains that agents should reframe non-trivial task requests and expose assumptions. | L20-L91   | [skills AGENTS.md](agents-remember-md/skills/AGENTS.md)                       |

## Cross-Repo References

No sibling repository evidence is needed for this routing guide.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T11:36: Created onboarding for the core-skills routing guide while preparing direct closeout.
