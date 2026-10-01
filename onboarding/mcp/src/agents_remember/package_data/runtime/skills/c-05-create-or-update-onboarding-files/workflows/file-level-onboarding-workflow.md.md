# file-level-onboarding-workflow.md

## Purpose

This workflow defines how `c-05-create-or-update-onboarding-files` skill creates and maintains onboarding for one concrete source file, including the governing-overview backlink that connects file-level onboarding to route-local overview context, the routing boundary for structural slice changes, preservation-first handling for moved/split/merged/deleted behavior, and the provider-neutral source-discovery rules for documentation evidence.

## Code Commentary

### Logic

The workflow selects sidecar or inline storage, stores sidecar onboarding under the resolved onboarding root, enforces metadata and required sections, discovers the nearest governing route-local overview, reads source and existing onboarding, verifies references, writes concise commentary, and updates verification metadata. Its source-discovery rules start from the `c-08-ar-coordination-context-resolver` skill resolved `system/sources.md` `Domain Documentation` category, treat live documentation sources named there as authoritative, use local mirrors only as orientation caches, and require live retrieval through the registry's named tool or MCP before saying no relevant documentation exists. `Docs References` is a required top-level `##` reference section, not a `###` subsection under `Code Commentary`. Before file-level create/delete/move work, it checks whether the change is actually a route-level slice case that belongs in `c-03-repo-bootstrap` skill. For moved, split, merged, relocated, or deleted code, the workflow reads old onboarding before deletion and reuses accurate durable knowledge in current targets whenever behavior moved.

**Converted memory (L37 fix round P1b).** The workflow now opens with a pointer: when the memory tree holds
`knowledge/layout.json`, use `converted-card-workflow.md` instead. A converted card has no metadata table, no
Update History and no citation tables, and its sidecar references are authored by `citation_fix`. The metadata,
Update History and citation rules of this workflow are for unconverted memory.

### Conventions

Sidecar onboarding mirrors the repo-relative source path under the resolved onboarding root and appends `.md`. The required sections include metadata with `governingOverview`, `## Governing Overview`, purpose, code commentary, docs references, repo-internal references, cross-repo references, and update history. When the resolved source registry has local and live documentation variants, onboarding output links to the canonical live document rather than local mirror paths.

### Invariants And Boundaries

File-level onboarding must describe current source-file behavior and remain useful when opened directly. It should not absorb active task plans, should not cite registries where actual evidence files are available, should update the governing overview link when the nearest route-local overview changes, should record live-source checks or blockers when no documentation evidence is found, should preserve reusable onboarding across behavior-preserving refactors, and should route whole-slice create/move/delete work to `c-03-repo-bootstrap` skill.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this workflow is repository source.

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

This workflow is the primary schema source for mirrored file-level onboarding.

- Scope and placement rules require one onboarding unit per source file, store sidecar onboarding under the resolved onboarding root, and route structural slice changes to `c-03-repo-bootstrap` skill. [1]
- Source discovery rules require the resolved `Domain Documentation` category, authoritative live documentation retrieval when the registry names it, local mirrors as orientation only, and actual evidence citations instead of source registries. [2]
- Section rules require metadata with `governingOverview`, a governing overview section, code commentary, top-level docs references, repo-internal references, cross-repo references, and update history. [3]
- Creation steps now confirm the target is one concrete file, route route-local slice cases to `c-03-repo-bootstrap` skill, identify/read the nearest governing overview, and cross-check all reference sections. [4]
- Maintenance steps require re-reading source and onboarding, refreshing changed sections and citations, applying inline syntax rules, appending update history, classifying moves/splits/merges/relocations/deletions, preserving accurate old onboarding in current targets, and routing whole-route moves or deletions to `c-03-repo-bootstrap` skill. [5]

- The workflow sends converted memory to the converted-card workflow. [6]

### Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

No meaningful cross-repo references found.
