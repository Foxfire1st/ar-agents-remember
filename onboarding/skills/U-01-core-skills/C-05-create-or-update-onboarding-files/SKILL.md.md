# C-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `6b6b80fc358a8717f1a9d6e0f9d16e64fc93820c` |
| lastVerifiedCommitDate | 2026-05-08T19:14                           |

## Purpose

This skill defines C-05, the onboarding creation and maintenance skill. It routes file-level onboarding, repo entity catalogs, and repo bootstrap updates to the appropriate workflow.

## Code Commentary

### Logic

C-05 tells agents to classify the onboarding target, use C-08 for roots, use sources as discovery aids rather than citation targets, preserve useful existing content, and append update history entries when onboarding changes.

### Conventions

File-level onboarding mirrors one source file. Repo-entity catalogs describe recurring real entities. Sources and tools files are registries, not proof for onboarding claims.

### Invariants And Boundaries

C-05 updates onboarding content, but it should not turn task plans into current-state documentation. It must keep references verifiable and avoid overwriting unresolved warnings without evidence.

### Todos

Review this skill after worktree support changes root naming or storage behavior.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

C-05 is the content-update counterpart to C-02's detection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Routing sends file-level, entity catalog, and repo overview work to different workflows. | L21-L33 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Quick rules require precise claims, useful update history, and preservation of important existing notes. | L51-L64 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Source discovery must start from C-08-resolved registries but cite actual evidence, not `sources.md`. | L66-L78 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Reference and lifecycle rules require verified links and correct handling of obsolete statements. | L78-L107 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

C-05 can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for current skill semantics. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for C-05 skill documentation.
