# bootstrap-state-template.md

| Field                  | Value                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| repository             | agents-remember                                                                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-state-template.md` |
| doc_type               | `file-level-onboarding`                                                                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                         |
| lastVerifiedCommitDate |                                                                                            2026-06-02T16:24:22+02:00|

## Purpose

This template defines the persistent bootstrap state file that allows `c-03-repo-bootstrap` skill runs to pause and resume across sessions, including existing-memory slice maintenance and the closeout boundary.

## Code Commentary

### Logic

The template tracks run metadata, onboarding root, source inventory gate status, phase status, areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and the next recommended action.

### Conventions

`bootstrap/STATE.md` is read first and updated last in each bootstrap session. It is state and coordination memory for the bootstrap, not file-level onboarding, and it records whether closeout has merely been requested after handoff.

### Invariants And Boundaries

The state file must preserve decisions, blockers, and low-confidence parking-lot items rather than promoting them into durable facts.

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
| The state template records bootstrap mode, memory root, onboarding root, branch, topology, source inventory status, and phase status across the full `c-03-repo-bootstrap` skill lifecycle. | `# Bootstrap State — <repo>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-state-template.md:1-88 |
| The state template tracks areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and next action. | `## Areas`; `## Governing Routes`; `## Slice Maintenance`; `## Waves`; `## Decisions`; `## Parking Lot`; `## Blockers`; `## Deferred Files`; `## Closeout Boundary`; `## Next Recommended Action` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-state-template.md:33-88 |
| `c-03-repo-bootstrap` skill requires every bootstrap to maintain `bootstrap/STATE.md` from this template. | `## Bootstrap State File` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:428-458 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T11:40:58+02:00 — 260731-EFA-L6 S18-B08 curator: bound the template headings and packaged skill requirement to exact current anchors; non-evidentiary boundary rows were unchanged.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T21:16+02:00: Refreshed for onboarding-root/source-inventory fields, existing-memory slice maintenance state, route cleanup statuses, and the separate closeout boundary. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the bootstrap state template. Verification metadata remains blank until the source file is committed.
