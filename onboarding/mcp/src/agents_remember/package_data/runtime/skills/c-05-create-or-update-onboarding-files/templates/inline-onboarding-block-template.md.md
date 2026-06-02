# inline-onboarding-block-template.md

| Field                  | Value                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                                             |
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

No external domain documentation is needed for this repository-local template. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this template is repository source.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found after checking live sources. | n/a       | n/a         |

## Repo-Internal References

Inline onboarding is the storage adapter for `c-05-create-or-update-onboarding-files` skill's common file-level content model.

| Finding                                                                                                                    | Citations | Source Path                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The inline template reuses the sidecar content model and differs only in storage, syntax, placement, metadata, and digesting. | L1-L6     | [inline-onboarding-block-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |
| The inline block includes `governingOverview` metadata and a governing overview section before the normal semantic sections. | L7-L42    | [inline-onboarding-block-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |
| Docs reference placeholder text now records no relevant documentation only after live-source checks or a retrieval blocker. | L34-L35   | [inline-onboarding-block-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |
| Guidelines require stable markers, host-language comment adaptation, high placement, and digest recomputation with the block removed. | L46-L51   | [inline-onboarding-block-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T13:32+02:00: Updated after inline docs-reference absence wording was aligned with live-source checks from the sidecar model. Verification metadata remains pinned until closeout commits the template change.
- 2026-05-14T18:00+02:00: Created onboarding for the inline onboarding block template and governing overview inline metadata. Verification metadata remains blank until the source file is committed.
