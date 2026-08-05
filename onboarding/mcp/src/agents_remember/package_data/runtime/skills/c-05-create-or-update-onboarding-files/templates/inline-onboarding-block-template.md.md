# inline-onboarding-block-template.md

| Field                  | Value                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                                             |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md` |
| doc_type               | `file-level-onboarding`                                                                                        |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                                             |
| lastVerifiedCommitDate |                                                                                                                2026-06-02T16:24:22+02:00|

## Purpose

`inline-onboarding-block-template.md` is the canonical inline-storage companion for file-level onboarding. It serializes the same content model as the Markdown sidecar template into an `@ar-onboarding` source comment block, including the same no-docs wording for cases where live documentation sources were checked but yielded no relevant evidence.

## Code Commentary

### Logic

The template defines stable inline metadata keys, including `sourceDigest`, `verifiedAt`, `scope`, and `governingOverview`, then lists the semantic sections that mirror sidecar file-level onboarding: governing overview, purpose, logic, conventions, invariants, todos, docs references, repo-internal references, and cross-repo references. The docs-reference placeholder now distinguishes "no relevant documentation found after checking live sources" from merely missing local documentation.

### Conventions

The template keeps host-language comment delimiters abstract while preserving stable `@ar-onboarding` markers. Inline storage adapts only the outer comment syntax; the semantic content model stays aligned with external file-level onboarding, including provider-neutral live-source documentation discovery wording.

### Invariants And Boundaries

Inline onboarding must not invent a separate documentation model. It must recompute `sourceDigest` from the source body with the onboarding block removed, preserve marker and metadata key stability so tooling can parse it, and keep docs-reference absence wording aligned with the sidecar template.

### Todos

After this working-tree update lands, refresh verification metadata to the committed template revision.

### Docs References

No external domain documentation is needed for this repository-local template. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this template is repository source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

Inline onboarding is the storage adapter for `c-05-create-or-update-onboarding-files` skill's common file-level content model.

| Finding | Anchor | Source |
| --- | --- | --- |
| The inline template reuses the sidecar content model and differs only in storage, syntax, placement, metadata, and digesting. | "It reuses the same semantic content model" | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md:5-5 |
| The inline block includes `governingOverview` metadata and a governing overview section before the normal semantic sections. | "governingOverview:" | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md:14-14 |
| Docs reference placeholder text now records no relevant documentation only after live-source checks or a retrieval blocker. | "No relevant documentation found after checking live sources." | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md:35-35 |
| Guidelines require stable markers, host-language comment adaptation, high placement, and digest recomputation with the block removed. | "Place the block as high in the file as possible" | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md:50-50 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact template anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T13:32+02:00: Updated after inline docs-reference absence wording was aligned with live-source checks from the sidecar model. Verification metadata remains pinned until closeout commits the template change.
- 2026-05-14T18:00+02:00: Created onboarding for the inline onboarding block template and governing overview inline metadata. Verification metadata remains blank until the source file is committed.
