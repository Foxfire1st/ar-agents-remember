# governing-route-map-template.md

| Field                  | Value                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                          |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/governing-route-map-template.md` |
| doc_type               | `file-level-onboarding`                                                                     |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                          |
| lastVerifiedCommitDate |                                                                                             2026-06-02T16:24:22+02:00|

## Purpose

This template defines the governing route map that decides where durable route-local `overview.md` files should live, move, retire, or be removed.

## Code Commentary

### Logic

The route map records placement principles, proposed governing routes, deferred routes, moved or deleted routes, cross-cutting concept anchors, parent/child overview relationships, and developer questions.

### Conventions

The map chooses local anchors in the mirrored onboarding hierarchy, avoids creating an overview merely because a folder exists, and records stale route-memory decisions during existing-memory slice maintenance.

### Invariants And Boundaries

Route-local overviews are durable memory, but they must remain local to source traversal and must not replace file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The governing route map template defines placement principles for route-local overviews and keeps file-level onboarding separate. | `## Placement Principles`, "File-level onboarding remains separate" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/governing-route-map-template.md:7-14 |
| The template records proposed routes, deferred routes, moved/deleted routes, cross-cutting concepts, parent/child overview relationships, and developer questions. | `## Proposed Governing Routes`, `## Routes Considered But Deferred`, `## Moved Or Deleted Routes`, `## Cross-Cutting Concepts`, `## Parent / Child Overview Relationships`, `## Developer Questions` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/governing-route-map-template.md:15-52 |
| `c-03-repo-bootstrap` skill Phase 4B writes `bootstrap/governing-route-map.md` from this template before overview cards and waves, and records stale, moved, or deleted routes for existing-memory slice maintenance. | `### 4B — Governing Route Map`, "bootstrap/governing-route-map.md" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:804-831 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-03T03:01:38+02:00 — W3-B04 curator: curated 3 table citations (3 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T21:16+02:00: Refreshed for moved/deleted route decisions and existing-memory slice maintenance cleanup questions. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the governing route map template. Verification metadata remains blank until the source file is committed.
