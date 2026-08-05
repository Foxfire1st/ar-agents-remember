# route-local-overview-template.md

| Field                  | Value                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-template.md` |
| doc_type               | `file-level-onboarding`                                                                       |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                            |
| lastVerifiedCommitDate |                                                                                               2026-06-02T16:24:22+02:00|

## Purpose

This template defines durable route-local overview files that live in the mirrored onboarding hierarchy and act as construction pillars for nearby file-level onboarding.

## Code Commentary

### Logic

The template records route metadata, route-based verification fields, parent overview, area explanation, hot-path summary, scope boundaries, structures, operating model, flows, load-bearing files, local invariants, canonical reference sections, file-level onboarding map, child overviews, usage guidance, verification needs, and update history.

### Conventions

Route-local overviews use canonical `Repo-Internal References`, `Cross-Repo References`, and `Docs References` buckets. Their `## Hot Path Summary` stays short because it is copied into generated route indexes for `c-04-retrieval-strategy-router` skill discovery. Links from nested route-local overviews to root `bootstrap/` evidence packs must be calculated relative to the overview's depth. Their `sourceRoute`, `lastVerifiedCommitHash`, and `lastVerifiedCommitDate` fields give `c-02-memory-quality-control` skill the deterministic route scope to compare later.

### Invariants And Boundaries

Route-local overviews are durable memory, but they are not replacements for file-level onboarding. They provide local area context and must keep file-specific facts in file-level onboarding.

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
| The route-local overview template defines route metadata, route verification fields, hot-path summary, scope, structures, flows, load-bearing files, local invariants, and traps. | `# <Area Or Route Name> Overview` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-template.md:1-112 |
| The template uses canonical repo-internal, cross-repo, and docs reference sections, with depth-aware evidence-pack link placeholders. | `## Repo-Internal References` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-template.md:61-68 |
| The template maps file-level onboarding, child overviews, usage order, needs verification, and update history. | `## File-Level Onboarding Map` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-template.md:85-90 |
| `c-03-repo-bootstrap` skill Phase 4D writes route-local overviews in mirrored source folders using this template. | "Overview workers write durable route-local overviews:" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:877-877 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 4 citation entries (8 findings); no Tier-3 findings.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-19T02:45+02:00: Added `## Hot Path Summary` to the route-local overview template so generated route indexes can expose compact route summaries and source anchors.
- 2026-05-15T11:46+02:00: Updated after the template added `lastVerifiedCommitDate` for deterministic route-local overview drift checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T18:00+02:00: Created onboarding for the route-local overview template and canonical reference-section/depth-aware evidence-link guidance. Verification metadata remains blank until the source file is committed.
