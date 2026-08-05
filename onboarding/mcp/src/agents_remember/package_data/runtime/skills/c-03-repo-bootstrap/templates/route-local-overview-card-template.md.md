# route-local-overview-card-template.md

| Field                  | Value                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                                 |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-card-template.md` |
| doc_type               | `file-level-onboarding`                                                                            |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                                 |
| lastVerifiedCommitDate |                                                                                                    2026-06-02T16:24:22+02:00|

## Purpose

This template defines the overview card used as a scoped work order before a route-local overview worker writes durable memory.

## Code Commentary

### Logic

The overview card records route metadata, why the overview exists, governed paths, what the overview must explain, required inputs, backlinks, downlinks, and open questions.

### Conventions

Overview cards are generated before overview waves. They constrain workers so route-local overview creation does not become broad repo rediscovery.

### Invariants And Boundaries

An overview card is a promotion artifact, not durable source onboarding. The durable output is the route-local `overview.md` produced from it.

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
| The overview card template records route metadata, governed paths, required explanation topics, inputs, links, and open questions. | `# Overview Card — <source route>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/route-local-overview-card-template.md:1-61 |
| `c-03-repo-bootstrap` skill Phase 4C writes overview cards for each selected governing route before route-local overview waves. | `### 4C — Route-Local Overview Cards` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:832-857 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:44:57+02:00: L6 W1-B02 curator repaired 2 source-template citations for the card structure and Phase 4C workflow.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T18:00+02:00: Created onboarding for the route-local overview card template. Verification metadata remains blank until the source file is committed.
