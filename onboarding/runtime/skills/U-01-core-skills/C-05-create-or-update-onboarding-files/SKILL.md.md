# C-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                                                     |
| ---------------------- | ------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                        |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                                                   |
| lastUpdated            | 2026-05-22T16:39+02:00                                                    |
| lastVerifiedCommitHash | `7d45d37e091fab28d25aa993a922e2e9eb71ccb7`                                |
| lastVerifiedCommitDate | 2026-05-22T16:56:53+02:00|

## Purpose

This skill defines C-05, the onboarding creation and maintenance skill. It routes file-level onboarding and repo-level entity catalogs to the appropriate workflow, points file-level onboarding at inline adapter additions when storage-specific syntax is needed, records the nearest governing route-local overview for file-level onboarding, maintains deterministic entity fingerprints, keeps entity inventory entries matched to fingerprint rows, routes structural source-slice maintenance to C-03, preserves useful onboarding across refactors before deletion, and requires documentation discovery to follow the target repository's resolved `Domain Documentation` sources without hard-coding a provider.

## Code Commentary

### Logic

C-05 tells agents to classify the onboarding target and the shape of the source change, use C-08 for the active coordination context and resolved roots, use sources as discovery aids rather than citation targets, preserve useful existing content, append update history entries when onboarding changes, and keep file-level onboarding self-sufficient while linking it back to the nearest governing overview. Its source-discovery rule makes the resolved memory layer's `Domain Documentation` category the required discovery plan: live sources named by that registry are authoritative, local mirrors/caches are only orientation aids, and missing/stale local docs trigger live retrieval through the registry's named tool or MCP before an agent records that no domain documentation exists. It handles single-file work directly, routes package/module/source-route creation, refresh, move, or deletion cleanup to C-03 `existing-memory-slice-maintenance`, keeps route overview `## Hot Path Summary` sections current, refreshes generated route indexes after onboarding changes, and owns the curation/refresh of `git-blob-set-v1` entity evidence paths that C-02 checks deterministically. Its preservation rule makes behavior-preserving moves update the mirrored onboarding path, makes splits/merges/behavior relocation reuse still-accurate old onboarding in new targets, and allows deletion or retirement only after proving the documented behavior is gone. When C-02 reports missing or orphaned entity fingerprint rows, C-05 reviews whether the entity was removed, renamed, moved, or simply lacks verification.

### Conventions

File-level onboarding mirrors one source file directly under the resolved onboarding root. Route-local overview files may exist beside mirrored source folders as governing context, but they do not replace file-level onboarding. Generated route indexes carry coverage, sidecar absence inference, and `hotPath` summary/hints; they are refreshed from overview/sidecar state rather than hand-edited. Repo-entity catalogs describe recurring real entities and carry deterministic fingerprints over the smallest practical set of load-bearing evidence files. Every inventory entry should have exactly one fingerprint row. Sources and tools files are registries, not proof for onboarding claims. Provider-specific documentation systems belong in resolved memory-layer source registries, not in this package's generic C-05 source.

### Invariants And Boundaries

C-05 updates onboarding content, but it should not turn task plans into current-state documentation, flatten structural route changes into unrelated file-level edits, or discard old onboarding before checking whether its documented behavior moved. It must keep references verifiable, avoid overwriting unresolved warnings without evidence, and keep same-repository, docs, and cross-repo evidence in the correct buckets. It must not treat local documentation caches as authoritative when the resolved source registry names a live retrieval path, and it must record live-source checks or blockers when no relevant documentation is found.

### Todos

After this working-tree update lands, refresh verification metadata to the committed C-05 source revision.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this package behavior is repository source.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found after checking live sources. | n/a       | n/a         |

## Repo-Internal References

C-05 is the content-update counterpart to C-02's detection.

| Finding                                                                                                  | Citations | Source Path                                                                                                 |
| -------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| Routing sends file-level onboarding, repo-level entity catalog work, and route/slice maintenance to different workflows or C-03 modes. | L21-L34 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| C-05 handles simple file/entity updates directly, requires proof before treating deleted files as cleanup-only, and routes package/module/source-route creation, refresh, move, split, merge, relocation, or deletion cleanup to C-03 when file-by-file work would lose structure. | L36-L56 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| The onboarding preservation rule treats existing onboarding as durable memory, moves one-to-one behavior-preserving sidecars, reuses accurate old content after splits/merges/relocation, and deletes or retires only when no safe current target remains. | L58-L65 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Sidecar placement rules now use the resolved onboarding root directly, include route-local `overview.md` files under mirrored source folders, and record generated route indexes with hot-path summary/hints. | L67-L86 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Quick rules require file-level onboarding to stay self-sufficient, link to the nearest governing overview, preserve reference explanations, maintain deterministic entity fingerprints, refresh route indexes, keep `Hot Path Summary` current, and avoid deleting onboarding before checking whether behavior moved. | L88-L107 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Route index refresh derives coverage, scope, copied `hotPath.summary`, candidate hints, anchor hints, and indexed sidecar absence from current onboarding/source state. | L109-L135 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Source discovery requires the resolved `Domain Documentation` category, treats live registry-named documentation sources as authoritative, uses local mirrors only as orientation caches, and triggers live retrieval before reporting no domain docs. | L137-L148 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| Reference and lifecycle rules require verified links, correct bucket selection, metadata refresh, preservation-first handling for moves/splits/merges/relocation/deletion, entity cleanup review for removed/renamed/moved cases, and C-03 routing for package/module/source-route moves or deletions. | L150-L184 | [C-05 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

C-05 can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current skill semantics. | n/a       | n/a         |

## Update History

- 2026-05-22T16:39+02:00: Updated after C-05 gained explicit preservation-first handling for renamed, moved, split, merged, relocated, or deleted source behavior. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-22T13:32+02:00: Updated after C-05 source discovery became provider-neutral while treating live documentation sources named by the resolved registry as authoritative over local caches. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T02:45+02:00: Updated for generated route-index `hotPath` fields and the requirement to keep route overview `## Hot Path Summary` sections current before refreshing indexes.
- 2026-05-15T12:57+02:00: Clarified that C-05 owns entity inventory-to-fingerprint coverage and must verify removed, renamed, or moved entities before deleting stale rows or evidence paths. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after C-05 took ownership of curating and refreshing repo entity `git-blob-set-v1` evidence paths for deterministic C-02 checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:38+02:00: Refreshed after the skill frontmatter was tightened to expose file-level/entity maintenance plus C-03 routing for package/module/source-slice changes. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement and C-03 routing of structural source-slice create, refresh, move, and deletion cleanup cases. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for route-local governing overview support, self-sufficient file-level onboarding, and reference-bucket requirements. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-05-create-or-update-onboarding-files` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale C-05 routing wording after coordination rename verification.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-05 skill documentation.
