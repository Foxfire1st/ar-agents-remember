# repo-overview-template.md

| Field                  | Value                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                    |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/repo-overview-template.md`      |
| doc_type               | `file-level-onboarding`                                                               |
| lastUpdated            | 2026-05-15T11:46+02:00                                                                |
| lastVerifiedCommitHash | `947b0e52ef06b1160819bd83ac90b5cefa7db811`                                                                                    |
| lastVerifiedCommitDate |                                                                                       2026-05-15T12:19:03+02:00|

## Purpose

This template defines the root repo overview created or refreshed by C-03 bootstrap.

## Code Commentary

### Logic

The template records repo metadata, route-based verification fields, purpose, architecture, code structure with local-overview status, functional areas, cross-repo references, build/dev commands, invariants, glossary terms, docs references, next exploration targets, needs verification, and update history.

### Conventions

The root overview is the minimum successful bootstrap output and should stay high-signal. Detailed local routing moves into route-local overviews once they exist. Its `sourceRoute` is `<repo-root>`, and `lastVerifiedCommitHash` plus `lastVerifiedCommitDate` describe the source commit C-02 should compare against for repo-wide overview drift.

### Invariants And Boundaries

The root overview gives repo-wide context. It should not become a catch-all area deep dive or replace route-local/file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                       | Citations | Source Path                                                                            |
| --------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------- |
| The repo overview template defines metadata, route-based verification fields, repo purpose, architecture, code structure, functional areas, cross-repo references, build/dev commands, invariants, glossary, docs references, next work, verification needs, and update history. | L1-L79    | [repo-overview-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/repo-overview-template.md) |
| C-03 treats the root repo overview as the minimum successful bootstrap output. | L8-L14 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| C-03 Phase 3 synthesizes the root repo overview from state, input ledger, scout report, area briefs, and existing overview when present. | L604-L651 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T11:46+02:00: Updated after the template added `lastVerifiedCommitDate` for deterministic route-based overview drift checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T18:00+02:00: Created onboarding for the repo overview template and route-local overview-aware code-structure model. Verification metadata remains blank until the source file is committed.
