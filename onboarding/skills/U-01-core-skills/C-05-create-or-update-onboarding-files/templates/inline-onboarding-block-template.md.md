# inline-onboarding-block-template.md

| Field                  | Value                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                                             |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md` |
| doc_type               | `file-level-onboarding`                                                                                        |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                                         |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`                                                                                                             |
| lastVerifiedCommitDate |                                                                                                                2026-05-14T18:37:02+02:00|

## Purpose

`inline-onboarding-block-template.md` is the canonical inline-storage companion for file-level onboarding. It serializes the same content model as the Markdown sidecar template into an `@ar-onboarding` source comment block.

## Code Commentary

### Logic

The template defines stable inline metadata keys, including `sourceDigest`, `verifiedAt`, `scope`, and `governingOverview`, then lists the semantic sections that mirror sidecar file-level onboarding: governing overview, purpose, logic, conventions, invariants, todos, docs references, repo-internal references, and cross-repo references.

### Conventions

The template keeps host-language comment delimiters abstract while preserving stable `@ar-onboarding` markers. Inline storage adapts only the outer comment syntax; the semantic content model stays aligned with external file-level onboarding.

### Invariants And Boundaries

Inline onboarding must not invent a separate documentation model. It must recompute `sourceDigest` from the source body with the onboarding block removed, and it must preserve marker and metadata key stability so tooling can parse it.

### Todos

After this working-tree update lands, refresh verification metadata to the committed template revision.

### Docs References

No external domain documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

Inline onboarding is the storage adapter for C-05's shared file-level content model.

| Finding                                                                                                                    | Citations | Source Path                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The inline template reuses the sidecar content model and differs only in storage, syntax, placement, metadata, and digesting. | L1-L6     | [inline-onboarding-block-template.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |
| The inline block includes `governingOverview` metadata and a governing overview section before the normal semantic sections. | L7-L42    | [inline-onboarding-block-template.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |
| Guidelines require stable markers, host-language comment adaptation, high placement, and digest recomputation with the block removed. | L46-L51   | [inline-onboarding-block-template.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the inline onboarding block template and governing overview inline metadata. Verification metadata remains blank until the source file is committed.
