# file-level-onboarding-template.md

## Purpose

`file-level-onboarding-template.md` is the canonical Markdown template for external file-level onboarding units. `c-05-create-or-update-onboarding-files` skill uses it to keep sidecar onboarding structurally consistent across source files, including governing-overview metadata, a `## Governing Overview` backlink section, and documentation-reference wording that treats live registry-named sources as canonical while keeping local mirrors as orientation caches.

## Code Commentary

### Logic

The template defines the required metadata table, governing overview backlink, semantic commentary sections, top-level reference sections, and prepend-only update-history convention (newest entry at the top, earlier entries preserved) for one concrete source file. It tells maintainers to use the resolved `c-08-ar-coordination-context-resolver` skill `system/sources.md` only as a discovery aid for documentation evidence, to cite actual proving sources, to treat local documentation mirrors as orientation caches, to link docs rows to canonical live references, and to keep reference sections explanation-first rather than citation-only.

### Conventions

The template uses placeholder text in angle brackets and keeps the generated artifact in plain Markdown. Reference tables are preserved even when no relevant external, same-repository, or cross-repo evidence exists, because the absence of evidence is itself useful context for future maintenance. For docs references, the placeholder now asks maintainers to record that no relevant documentation was found after live-source checks rather than after only reading local files. The governing overview section links to the nearest route-local overview when one exists, otherwise an ancestor or root overview.

### Invariants And Boundaries

This file defines structure and wording for generated onboarding; it does not decide which source paths are eligible, resolve storage roots, or perform drift classification. It must stay provider-neutral and avoid naming a single documentation system in the package template. `Docs References` is a `##` top-level reference section, parallel to `Repo-Internal References` and `Cross-Repo References`, not a `###` subsection under `Code Commentary`. `c-08-ar-coordination-context-resolver` skill owns context resolution, `c-02-memory-quality-control` skill owns drift classification, and `c-05-create-or-update-onboarding-files` skill workflows own when this template is applied.

### Todos

None; verification metadata is current as of committed template revision df07057.

### Docs References

No external domain documentation is needed for this repository-local template. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this template is repository source.

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

The template is governed by `c-05-create-or-update-onboarding-files` skill's onboarding-maintenance contract and is consumed when creating file-level sidecars.

- `c-05-create-or-update-onboarding-files` skill routes file-level onboarding creation to this template and requires strict one-to-one mirroring with source files and route-local governing overview links. [1]
- The template defines metadata including `governingOverview`, the governing overview section, purpose, code commentary, top-level reference sections, and append-only update-history guidance. [2]
- Docs reference placeholder text requires actual online, intranet, library, or product documentation, treats local mirrors as orientation caches, links canonical live references, and records no relevant docs only after live-source checks. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
