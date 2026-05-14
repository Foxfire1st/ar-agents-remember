# file-level-onboarding-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T21:16+02:00                     |
| lastVerifiedCommitHash | `4a7c82ddab26013f0cad740227b6896f9bc41aed` |
| lastVerifiedCommitDate | 2026-05-14T21:53:38+02:00|

## Purpose

This workflow defines how C-05 creates and maintains onboarding for one concrete source file, including the governing-overview backlink that connects file-level onboarding to route-local overview context and the routing boundary for structural slice changes.

## Code Commentary

### Logic

The workflow selects sidecar or inline storage, stores sidecar onboarding under the resolved onboarding root, enforces metadata and required sections, discovers the nearest governing route-local overview, reads source and existing onboarding, verifies references, writes concise commentary, and updates verification metadata. Before file-level create/delete/move work, it checks whether the change is actually a route-level slice case that belongs in C-03.

### Conventions

Sidecar onboarding mirrors the repo-relative source path under the resolved onboarding root and appends `.md`. The required sections include metadata with `governingOverview`, `## Governing Overview`, purpose, code commentary, repo-internal references, cross-repo references, and update history, with docs references under code commentary.

### Invariants And Boundaries

File-level onboarding must describe current source-file behavior and remain useful when opened directly. It should not absorb active task plans, should not cite registries where actual evidence files are available, should update the governing overview link when the nearest route-local overview changes, and should route whole-slice create/move/delete work to C-03.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This workflow is the primary schema source for mirrored file-level onboarding.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Scope and placement rules require one onboarding unit per source file, store sidecar onboarding under the resolved onboarding root, and route structural slice changes to C-03. | L1-L44 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Section rules require metadata with `governingOverview`, a governing overview section, code commentary, repo-internal references, cross-repo references, and update history. | L46-L85 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Creation steps now confirm the target is one concrete file, route route-local slice cases to C-03, identify/read the nearest governing overview, and cross-check all reference sections. | L87-L100 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |
| Maintenance steps require re-reading source and onboarding, refreshing changed sections and citations, applying inline syntax rules, appending update history, and routing whole-route moves or deletions to C-03. | L102-L117 | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement and C-03 routing of route-level slice create, refresh, move, and delete cases. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for governing overview metadata, route-local overview discovery, canonical reference sections, and self-sufficient file-level onboarding. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 file-level workflow.
