# coverage-plan-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                      |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md` |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-06-02T16:24:22+02:00|

## Purpose

This template defines the coverage-planning artifact that turns scout and area research into prioritized route, file, evidence, and slice cleanup work.

## Code Commentary

### Logic

The coverage plan records strategy, area coverage goals, route classifications, file classifications, evidence pack needs, deferred routes/files, slice cleanup decisions, developer review questions, and decisions.

### Conventions

Coverage planning happens before governing route maps and waves. It should classify work by risk and value, and in existing-memory slice maintenance it should decide whether stale route memory is refreshed, moved, removed, retired, or preserved.

### Invariants And Boundaries

The plan is scheduling and prioritization input. It should not become durable file behavior documentation or promote low-confidence findings into fact.

### Todos

Fill verification metadata after the source file is committed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The coverage plan template captures strategy, area goals, route classification, file classification, and evidence pack queues. | "Strategy"; "Area Coverage Summary"; "root + route overview + top files"; "Route Classification Queue"; "core-logic / cross-repo-boundary"; "File Classification Queue"; "landmine / boundary / core-logic / routine-support"; "Evidence Pack Queue"; "Boundary Pack Needed?"; "<route>" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:10-10; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:14-14; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:18-18; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:20-20; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:24-24; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:26-26; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:30-30; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:32-32; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:34-34; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:36-36 |
| The template records deferred routes/files, slice cleanup decisions, developer review questions, and decisions for later waves. | "Deferred Routes And Files"; "simple DTO / generated / routine helper"; "Slice Cleanup Queue"; "route overview / child file onboarding"; "Developer Review Questions"; "Are these the right routes to document first?"; "Decision Log"; "<decision>" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:38-38; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:42-42; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:44-44; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:50-50; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:52-52; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:54-54; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:61-61; mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/coverage-plan-template.md:65-65 |

## Update History

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended both template inventory claims through their table bodies and regenerated the final ranges with the scoped fixer.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T21:16+02:00: Refreshed for route cleanup classifications, slice cleanup queue, and stale-route review questions. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the coverage plan template. Verification metadata remains blank until the source file is committed.
