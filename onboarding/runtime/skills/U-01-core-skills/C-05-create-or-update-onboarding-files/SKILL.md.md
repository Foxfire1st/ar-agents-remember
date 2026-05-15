# C-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                                                     |
| ---------------------- | ------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                        |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                                                   |
| lastUpdated            | 2026-05-15T11:46+02:00                                                    |
| lastVerifiedCommitHash | `947b0e52ef06b1160819bd83ac90b5cefa7db811`                                |
| lastVerifiedCommitDate | 2026-05-15T12:19:03+02:00|

## Purpose

This skill defines C-05, the onboarding creation and maintenance skill. It routes file-level onboarding and repo-level entity catalogs to the appropriate workflow, points file-level onboarding at inline adapter additions when storage-specific syntax is needed, records the nearest governing route-local overview for file-level onboarding, maintains deterministic entity fingerprints, and routes structural source-slice maintenance to C-03.

## Code Commentary

### Logic

C-05 tells agents to classify the onboarding target and the shape of the source change, use C-08 for the active coordination context and resolved roots, use sources as discovery aids rather than citation targets, preserve useful existing content, append update history entries when onboarding changes, and keep file-level onboarding self-sufficient while linking it back to the nearest governing overview. It handles single-file work directly, routes package/module/source-route creation, refresh, move, or deletion cleanup to C-03 `existing-memory-slice-maintenance`, and owns the curation/refresh of `git-blob-set-v1` entity evidence paths that C-02 checks deterministically.

### Conventions

File-level onboarding mirrors one source file directly under the resolved onboarding root. Route-local overview files may exist beside mirrored source folders as governing context, but they do not replace file-level onboarding. Repo-entity catalogs describe recurring real entities and carry deterministic fingerprints over the smallest practical set of load-bearing evidence files. Sources and tools files are registries, not proof for onboarding claims.

### Invariants And Boundaries

C-05 updates onboarding content, but it should not turn task plans into current-state documentation or flatten structural route changes into unrelated file-level edits. It must keep references verifiable, avoid overwriting unresolved warnings without evidence, and keep same-repository, docs, and cross-repo evidence in the correct buckets.

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
| Routing sends file-level onboarding, repo-level entity catalog work, and route/slice maintenance to different workflows or C-03 modes. | L21-L34 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| C-05 handles simple file/entity updates directly but routes package/module/source-route creation, refresh, move, or deletion cleanup to C-03 `existing-memory-slice-maintenance`. | L36-L56 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Sidecar placement rules now use the resolved onboarding root directly, include route-local `overview.md` files under mirrored source folders, and require file-level onboarding to record `governingOverview` when available. | L58-L74 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Quick rules require file-level onboarding to stay self-sufficient, link to the nearest governing overview, preserve reference explanations, maintain deterministic entity fingerprints, check reference health, keep update history append-only, and route structural changes to C-03. | L76-L92 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Reference and lifecycle rules require verified links, correct bucket selection, metadata refresh, mirrored handling for simple file moves, and C-03 routing for package/module/source-route moves or deletions. | L105-L135 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

C-05 can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current skill semantics. | n/a       | n/a         |

## Update History

- 2026-05-15T11:46+02:00: Refreshed after C-05 took ownership of curating and refreshing repo entity `git-blob-set-v1` evidence paths for deterministic C-02 checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:38+02:00: Refreshed after the skill frontmatter was tightened to expose file-level/entity maintenance plus C-03 routing for package/module/source-slice changes. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement and C-03 routing of structural source-slice create, refresh, move, and deletion cleanup cases. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for route-local governing overview support, self-sufficient file-level onboarding, and reference-bucket requirements. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-05-create-or-update-onboarding-files` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale C-05 routing wording after coordination rename verification.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-05 skill documentation.
