# file-level-onboarding-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|

## Purpose

This workflow defines how `c-05-create-or-update-onboarding-files` skill creates and maintains onboarding for one concrete source file, including the governing-overview backlink that connects file-level onboarding to route-local overview context, the routing boundary for structural slice changes, preservation-first handling for moved/split/merged/deleted behavior, and the provider-neutral source-discovery rules for documentation evidence.

## Code Commentary

### Logic

The workflow selects sidecar or inline storage, stores sidecar onboarding under the resolved onboarding root, enforces metadata and required sections, discovers the nearest governing route-local overview, reads source and existing onboarding, verifies references, writes concise commentary, and updates verification metadata. Its source-discovery rules start from the `c-08-ar-coordination-context-resolver` skill resolved `system/sources.md` `Domain Documentation` category, treat live documentation sources named there as authoritative, use local mirrors only as orientation caches, and require live retrieval through the registry's named tool or MCP before saying no relevant documentation exists. `Docs References` is a required top-level `##` reference section, not a `###` subsection under `Code Commentary`. Before file-level create/delete/move work, it checks whether the change is actually a route-level slice case that belongs in `c-03-repo-bootstrap` skill. For moved, split, merged, relocated, or deleted code, the workflow reads old onboarding before deletion and reuses accurate durable knowledge in current targets whenever behavior moved.

### Conventions

Sidecar onboarding mirrors the repo-relative source path under the resolved onboarding root and appends `.md`. The required sections include metadata with `governingOverview`, `## Governing Overview`, purpose, code commentary, docs references, repo-internal references, cross-repo references, and update history. When the resolved source registry has local and live documentation variants, onboarding output links to the canonical live document rather than local mirror paths.

### Invariants And Boundaries

File-level onboarding must describe current source-file behavior and remain useful when opened directly. It should not absorb active task plans, should not cite registries where actual evidence files are available, should update the governing overview link when the nearest route-local overview changes, should record live-source checks or blockers when no documentation evidence is found, should preserve reusable onboarding across behavior-preserving refactors, and should route whole-slice create/move/delete work to `c-03-repo-bootstrap` skill.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this workflow is repository source.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

This workflow is the primary schema source for mirrored file-level onboarding.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Scope and placement rules require one onboarding unit per source file, store sidecar onboarding under the resolved onboarding root, and route structural slice changes to `c-03-repo-bootstrap` skill. | L1-L44 | [file-level workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Source discovery rules require the resolved `Domain Documentation` category, authoritative live documentation retrieval when the registry names it, local mirrors as orientation only, and actual evidence citations instead of source registries. | L20-L29 | [file-level workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Section rules require metadata with `governingOverview`, a governing overview section, code commentary, top-level docs references, repo-internal references, cross-repo references, and update history. | L47-L86 | [file-level workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Creation steps now confirm the target is one concrete file, route route-local slice cases to `c-03-repo-bootstrap` skill, identify/read the nearest governing overview, and cross-check all reference sections. | L87-L100 | [file-level workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Maintenance steps require re-reading source and onboarding, refreshing changed sections and citations, applying inline syntax rules, appending update history, classifying moves/splits/merges/relocations/deletions, preserving accurate old onboarding in current targets, and routing whole-route moves or deletions to `c-03-repo-bootstrap` skill. | L103-L121 | [file-level workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T16:39+02:00: Updated after the workflow gained explicit preservation-first handling for moved, split, merged, relocated, or deleted source behavior. Verification metadata remains pinned until closeout commits the workflow change.
- 2026-05-22T13:32+02:00: Updated after source discovery rules made live registry-named documentation authoritative and local mirrors orientation-only for file-level onboarding. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-18T08:49+02:00: Updated after the workflow was aligned with the template's top-level `## Docs References` section. Verification metadata remains pinned until closeout commits the workflow change.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement and `c-03-repo-bootstrap` skill routing of route-level slice create, refresh, move, and delete cases. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for governing overview metadata, route-local overview discovery, canonical reference sections, and self-sufficient file-level onboarding. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the `c-05-create-or-update-onboarding-files` skill file-level workflow.
