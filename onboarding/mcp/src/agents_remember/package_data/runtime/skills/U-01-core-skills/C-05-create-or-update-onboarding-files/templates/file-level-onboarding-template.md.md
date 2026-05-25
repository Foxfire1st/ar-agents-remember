# file-level-onboarding-template.md

| Field                  | Value                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| repository             | agents-remember-md                                                                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md` |
| doc_type               | `file-level-onboarding`                                                                                      |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90`                                                                   |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

`file-level-onboarding-template.md` is the canonical Markdown template for external file-level onboarding units. C-05 uses it to keep sidecar onboarding structurally consistent across source files, including governing-overview metadata, a `## Governing Overview` backlink section, and documentation-reference wording that treats live registry-named sources as canonical while keeping local mirrors as orientation caches.

## Code Commentary

### Logic

The template defines the required metadata table, governing overview backlink, semantic commentary sections, top-level reference sections, and append-only update-history convention for one concrete source file. It tells maintainers to use the resolved C-08 `system/sources.md` only as a discovery aid for documentation evidence, to cite actual proving sources, to treat local documentation mirrors as orientation caches, to link docs rows to canonical live references, and to keep reference sections explanation-first rather than citation-only.

### Conventions

The template uses placeholder text in angle brackets and keeps the generated artifact in plain Markdown. Reference tables are preserved even when no relevant external, same-repository, or cross-repo evidence exists, because the absence of evidence is itself useful context for future maintenance. For docs references, the placeholder now asks maintainers to record that no relevant documentation was found after live-source checks rather than after only reading local files. The governing overview section links to the nearest route-local overview when one exists, otherwise an ancestor or root overview.

### Invariants And Boundaries

This file defines structure and wording for generated onboarding; it does not decide which source paths are eligible, resolve storage roots, or perform drift classification. It must stay provider-neutral and avoid naming a single documentation system in the package template. `Docs References` is a `##` top-level reference section, parallel to `Repo-Internal References` and `Cross-Repo References`, not a `###` subsection under `Code Commentary`. C-08 owns context resolution, C-02 owns drift classification, and C-05 workflows own when this template is applied.

### Todos

After this working-tree update lands, refresh verification metadata to the committed template revision.

### Docs References

No external domain documentation is needed for this repository-local template. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this template is repository source.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found after checking live sources. | n/a       | n/a         |

## Repo-Internal References

The template is governed by C-05's onboarding-maintenance contract and is consumed when creating file-level sidecars.

| Finding                                                                                                                      | Citations | Source Path                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-05 routes file-level onboarding creation to this template and requires strict one-to-one mirroring with source files and route-local governing overview links. | L19-L51 | [C-05 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) |
| The template defines metadata including `governingOverview`, the governing overview section, purpose, code commentary, top-level reference sections, and append-only update-history guidance. | L1-L68 | [file-level-onboarding-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md) |
| Docs reference placeholder text requires actual online, intranet, library, or product documentation, treats local mirrors as orientation caches, links canonical live references, and records no relevant docs only after live-source checks. | L41-L49 | [file-level-onboarding-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T13:32+02:00: Updated after docs-reference placeholder wording was tightened around canonical live references, local mirrors as orientation caches, and no-docs records after live-source checks. Verification metadata remains pinned until closeout commits the template change.
- 2026-05-18T08:49+02:00: Updated after `Docs References` became a top-level `##` section in the canonical file-level onboarding template. Verification metadata remains pinned until closeout commits the template change.
- 2026-05-14T18:00+02:00: Refreshed for governing overview metadata and backlink guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T11:30: Created onboarding for the file-level onboarding template after its update-history wording was clarified.
