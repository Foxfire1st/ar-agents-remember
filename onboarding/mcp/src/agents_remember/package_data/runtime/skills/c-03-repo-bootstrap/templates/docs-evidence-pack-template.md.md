# docs-evidence-pack-template.md

| Field                  | Value                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                          |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/docs-evidence-pack-template.md` |
| doc_type               | `file-level-onboarding`                                                                     |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                                                                                          |
| lastVerifiedCommitDate |                                                                                             2026-08-05T12:41:24+02:00|

## Purpose

This template defines the documentation evidence pack used when bootstrap needs domain, protocol, vendor, library, or business-rule evidence.

## Code Commentary

### Logic

The docs pack records scope, checked documentation sources, confirmed findings with evidence, documentation constraints, terms, files likely affected, explicit no-evidence records, and open questions.

### Conventions

The pack may use `system/sources.md` only as a routing index. It must cite actual documentation or a local mirror with canonical links in downstream onboarding.

### Invariants And Boundaries

Docs packs prove documentation-sensitive claims; they do not replace repo-internal source evidence or cross-repo boundary packs.

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
| The docs pack template records scope, source checks, confirmed documentation findings, constraints, terms, affected files, no-evidence records, and open questions. | "Docs Evidence Pack — <area-or-route>" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/docs-evidence-pack-template.md:1-1 |
| `c-03-repo-bootstrap` skill Phase 4E writes docs evidence packs for priority routes where documentation affects behavior. | `# Repo Bootstrap` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:6-1265 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 2 citation items; scoped citation check now passes.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T18:00+02:00: Created onboarding for the docs evidence pack template. Verification metadata remains blank until the source file is committed.
