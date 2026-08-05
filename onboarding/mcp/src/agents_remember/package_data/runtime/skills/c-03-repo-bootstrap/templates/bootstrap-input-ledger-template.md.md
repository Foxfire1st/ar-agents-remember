# bootstrap-input-ledger-template.md

| Field                  | Value                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| repository             | agents-remember                                                                               |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-input-ledger-template.md` |
| doc_type               | `file-level-onboarding`                                                                          |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                               |
| lastVerifiedCommitDate |                                                                                                  2026-06-02T16:24:22+02:00|

## Purpose

This template defines the source-intake ledger used before bootstrap agents ask for additional sources or proceed into research, including source deltas for existing-memory slice maintenance.

## Code Commentary

### Logic

The template captures target repo, control mode, bootstrap mode, memory root, onboarding root, topology, branch, source inventory gate status, presented source inventory, excluded sources, weak categories, user-added sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and operator decision.

### Conventions

The ledger is the durable record of what sources were presented and accepted or rejected. It should be written after the source inventory review, before scout and deeper bootstrap work or automated execution.

### Invariants And Boundaries

The source inventory must be shown before asking for additions, and the ledger should not cite source registries as proof. It is an intake decision artifact, not evidence for durable behavior claims.

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
| The input ledger records run metadata, onboarding root, source inventory gate status, and the presented source inventory with status, planned use, and user decision. | `# Bootstrap Input Ledger — <repo>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-input-ledger-template.md:1-100 |
| The template captures excluded sources, weak source categories, additional user sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and proceed/no-proceed decision. | `# Bootstrap Input Ledger — <repo>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/bootstrap-input-ledger-template.md:1-100 |
| `c-03-repo-bootstrap` skill requires source inventory review to be written to `bootstrap/input-ledger.md` using this template before automated execution starts. | `### 0.3 Present source inventory before asking for additions` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:533-565 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 3 citation entries (6 findings); no Tier-3 findings.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T21:38+02:00: Refreshed after the default-exclude section became a settings path-rule review checklist instead of an independent bootstrap filter. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for onboarding-root/source-inventory gate fields, existing-memory source deltas, and default bootstrap candidate excludes. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the bootstrap input ledger template. Verification metadata remains blank until the source file is committed.
