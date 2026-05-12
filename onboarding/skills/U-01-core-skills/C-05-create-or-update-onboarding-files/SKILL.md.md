# C-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                                                     |
| ---------------------- | ------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                        |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                                                   |
| lastUpdated            | 2026-05-12T18:51+02:00                                                    |
| lastVerifiedCommitHash | `3eb9e862887736f0a488ec8144683fb22bb35b16`                                |
| lastVerifiedCommitDate | 2026-05-12T02:01:56+02:00                                                 |

## Purpose

This skill defines C-05, the onboarding creation and maintenance skill. It routes file-level onboarding and repo-level entity catalogs to the appropriate workflow, and points file-level onboarding at inline adapter additions when storage-specific syntax is needed.

## Code Commentary

### Logic

C-05 tells agents to classify the onboarding target, use C-08 for the active coordination context and resolved roots, use sources as discovery aids rather than citation targets, preserve useful existing content, and append update history entries when onboarding changes.

### Conventions

File-level onboarding mirrors one source file. Repo-entity catalogs describe recurring real entities. Sources and tools files are registries, not proof for onboarding claims.

### Invariants And Boundaries

C-05 updates onboarding content, but it should not turn task plans into current-state documentation. It must keep references verifiable and avoid overwriting unresolved warnings without evidence.

### Todos

Review this skill after worktree support changes root naming or storage behavior.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

C-05 is the content-update counterpart to C-02's detection.

| Finding                                                                                                  | Citations | Source Path                                                                                                 |
| -------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| Routing sends file-level onboarding and repo-level entity catalog work to different workflows, with inline adapter additions for file-level onboarding. | L19-L33   | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Quick rules require updating existing artifacts, preserving useful reference explanations, checking reference health, and append-only update history.   | L51-L64   | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Source discovery must start from C-08-resolved registries but cite actual evidence, not `sources.md`.                         | L66-L77   | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Reference and lifecycle rules require verified links, correct handling of obsolete statements, metadata refresh, and mirrored handling when code moves. | L78-L104  | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

C-05 can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current skill semantics. | n/a       | n/a         |

## Update History

- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-05-create-or-update-onboarding-files` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale C-05 routing wording after coordination rename verification.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-05 skill documentation.
