# file-card-template.md

| Field                  | Value                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                  |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/file-card-template.md` |
| doc_type               | `file-level-onboarding`                                                             |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                  |
| lastVerifiedCommitDate |                                                                                     2026-06-02T16:24:22+02:00|

## Purpose

This template defines the file-card work order that constrains a future file-level onboarding worker.

## Code Commentary

### Logic

The file card records source and onboarding targets, classification, governing context, why the file matters, what the worker must explain, required inputs, allowed and disallowed reads, required onboarding sections, reference expectations, traps, open questions, and done criteria.

### Conventions

File cards are created before assigning file-level onboarding work except for tiny repositories. They keep file workers scoped and prevent broad rediscovery.

### Invariants And Boundaries

A file card does not replace `c-05-create-or-update-onboarding-files` skill. It prepares bounded instructions for `c-05-create-or-update-onboarding-files` skill file-level onboarding and must keep task planning out of durable onboarding.

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
| The file card template records classification, governing context, worker inputs, allowed/disallowed reads, required sections, reference expectations, traps, questions, and done criteria. | `# File Card — <source path>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/file-card-template.md:1-100 |
| `c-03-repo-bootstrap` skill Phase 4G writes file cards for priority source files and requires them before file-level onboarding unless the repo is tiny. | `### 4G — File Card Generation` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:960-984 |
| `c-03-repo-bootstrap` skill Phase 4H says each file worker receives one file card and follows `c-05-create-or-update-onboarding-files` skill for file-level onboarding. | `### 4H — File-Level Onboarding Waves` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:985-1020 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 3 repo-internal citation rows and preserved verification metadata.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T18:00+02:00: Created onboarding for the file card template. Verification metadata remains blank until the source file is committed.
