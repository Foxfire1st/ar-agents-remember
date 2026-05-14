# C-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                                                     |
| ---------------------- | ------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                        |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                                                   |
| lastUpdated            | 2026-05-14T18:00+02:00                                                    |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                                |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This skill defines C-05, the onboarding creation and maintenance skill. It routes file-level onboarding and repo-level entity catalogs to the appropriate workflow, points file-level onboarding at inline adapter additions when storage-specific syntax is needed, and now records the nearest governing route-local overview for file-level onboarding when one exists.

## Code Commentary

### Logic

C-05 tells agents to classify the onboarding target, use C-08 for the active coordination context and resolved roots, use sources as discovery aids rather than citation targets, preserve useful existing content, append update history entries when onboarding changes, and keep file-level onboarding self-sufficient while linking it back to the nearest governing overview.

### Conventions

File-level onboarding mirrors one source file. Route-local overview files may exist beside mirrored source folders as governing context, but they do not replace file-level onboarding. Repo-entity catalogs describe recurring real entities. Sources and tools files are registries, not proof for onboarding claims.

### Invariants And Boundaries

C-05 updates onboarding content, but it should not turn task plans into current-state documentation. It must keep references verifiable, avoid overwriting unresolved warnings without evidence, and keep same-repository, docs, and cross-repo evidence in the correct buckets.

### Todos

After this working-tree update lands, refresh verification metadata to the committed C-05 source revision.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

C-05 is the content-update counterpart to C-02's detection.

| Finding                                                                                                  | Citations | Source Path                                                                                                 |
| -------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| Routing sends file-level onboarding and repo-level entity catalog work to different workflows, with inline adapter additions for file-level onboarding. | L19-L31 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Sidecar placement rules now include route-local `overview.md` files under mirrored source folders and require file-level onboarding to record `governingOverview` when available. | L33-L51 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Quick rules require file-level onboarding to stay self-sufficient, link to the nearest governing overview, preserve reference explanations, check reference health, and keep update history append-only. | L53-L67 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Source discovery must start from C-08-resolved registries but cite actual evidence, not `sources.md`, and route same-repo facts to `Repo-Internal References`. | L69-L79 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Reference and lifecycle rules require verified links, correct bucket selection, metadata refresh, and mirrored handling when code moves. | L81-L110 | [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

C-05 can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current skill semantics. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Refreshed for route-local governing overview support, self-sufficient file-level onboarding, and reference-bucket requirements. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-05-create-or-update-onboarding-files` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale C-05 routing wording after coordination rename verification.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-05 skill documentation.
