# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/agents-md-files/system/AGENTS.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T00:38+02:00                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This file is the package-owned template for installed
`ar-coordination/system/AGENTS.md`. It defines the hard onboarding maintenance
gate and the read/update discipline agents must follow around memory-backed
onboarding.

## Code Commentary

### Logic

The template requires C-08 context resolution and C-02 drift detection before
agents rely on repository onboarding for any task, including read-only
analysis. It defines the developer decision point when drift exists, the C-05
maintenance route for approved refreshes, and the second C-02 check after
maintenance. It also preserves the planning rule that agents read the repo
overview and verified file-level onboarding alongside source, then update or
create onboarding when implementation changes current-state knowledge.

### Conventions

The system template is strict because it protects trust in durable memory. It
uses numbered gates for the startup workflow and separates the post-gate
planning and implementation expectations from the initial trust check.

### Invariants And Boundaries

C-08 and C-02 are mandatory before trusting onboarding. C-02 detects drift but
does not update onboarding; C-05 owns approved onboarding maintenance. The drift
report is temporary coordination state and should be deleted after the gate is
complete.

### Todos

Refresh verification metadata after the current `AGENTS.md` source reshuffle is
committed.

### Docs References

No external domain documentation is needed for this repository-local runtime
template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                                     | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The hard gate requires C-08 context resolution, C-02 drift detection, developer review of drift, approved C-05 refresh, a second C-02 check, and drift report deletion. | L1-L30 | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |
| Cross-repo drift handling runs the first three gates for every allowed repo before asking about onboarding refresh.          | L32-L38   | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |
| Post-gate planning reads overview and source-paired onboarding, and implementation updates onboarding through C-05.          | L40-L68   | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this runtime template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T00:38+02:00: Created onboarding after the former root `system/AGENTS.md` guidance moved to the installable system template path. Verification metadata remains pinned to the last committed source until closeout.
