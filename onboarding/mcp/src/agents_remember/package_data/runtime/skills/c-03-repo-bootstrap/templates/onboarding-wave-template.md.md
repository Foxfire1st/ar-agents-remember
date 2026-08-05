# onboarding-wave-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                      |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/onboarding-wave-template.md` |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-06-02T16:24:22+02:00|

## Purpose

This template defines route-overview and file-onboarding wave manifests.

## Code Commentary

### Logic

The wave manifest records wave metadata, goal, included cards, excluded/deferred paths, evidence requirements, worker instructions, assignments, done criteria, and developer review questions.

### Conventions

Waves are small, bounded units. Workers read assigned cards first, read only listed evidence, keep planning notes out of durable onboarding, preserve strict one-to-one file mapping, and return changed paths plus unresolved questions.

### Invariants And Boundaries

The wave manifest coordinates workers; it is not durable source behavior documentation. Every included target needs onboarding output or an explicit blocker plus curator review.

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
| The onboarding wave template records wave metadata, cards, deferred targets, evidence needs, worker instructions, assignments, done criteria, and review questions. | `## Goal`; `## Included Cards`; `## Excluded Or Deferred`; `## Evidence Required`; `## Worker Instructions`; `## Worker Assignments`; `## Done When`; `## Developer Review Questions` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/onboarding-wave-template.md:11-65 |
| `c-03-repo-bootstrap` Phase 4H writes onboarding wave manifests. | `### 4H — File-Level Onboarding Waves` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:985-1020 |
| The onboarding-file worker instructions are governed by the c-05 skill routing section. | `## Routing` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:40-54 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T18:00+02:00: Created onboarding for the onboarding wave template. Verification metadata remains blank until the source file is committed.
