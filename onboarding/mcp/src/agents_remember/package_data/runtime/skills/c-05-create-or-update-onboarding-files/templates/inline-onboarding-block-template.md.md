# inline-onboarding-block-template.md

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

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

Inline onboarding is the storage adapter for `c-05-create-or-update-onboarding-files` skill's common file-level content model.

- The inline template reuses the sidecar content model and differs only in storage, syntax, placement, metadata, and digesting. [1]
- The inline block includes `governingOverview` metadata and a governing overview section before the normal semantic sections. [2]
- Docs reference placeholder text now records no relevant documentation only after live-source checks or a retrieval blocker. [3]
- Guidelines require stable markers, host-language comment adaptation, high placement, and digest recomputation with the block removed. [4]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
