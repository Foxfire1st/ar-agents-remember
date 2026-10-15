# skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This source is the inline-storage companion template for the c-05 file-level content model. It illustrates how the same semantic sections are serialized into a host-language `@ar-onboarding` comment block. This converted card documents that adapter source; it does not install an inline block or authorize legacy memory authoring.

## Code Commentary

### Logic

The sample block retains `format`, `sourceDigest`, `verifiedAt`, `scope` and `governingOverview`, a governing-overview link before purpose, and the same logic, conventions, invariants/boundaries, todos and three reference buckets as the external template. Its documentation placeholder distinguishes no relevant documentation after live-source checks from merely absent local material and includes retrieval blockers.

### Conventions

Host-language comment delimiters remain abstract. The adapter description changes storage, comment syntax, placement, verification metadata and digesting, not the semantic content model. Stable `@ar-onboarding` and `@ar-onboarding-end` markers and metadata keys, outer-delimiter-only adaptation, and placement as high as leading syntax/tooling permit are explicit source guidelines. Provider-neutral live-source wording stays aligned with the file-level template.

### Invariants And Boundaries

Within the documented inline adapter, `sourceDigest` is recomputed from the source body with the onboarding block removed; stable markers and keys support parsing rather than defining a separate documentation model. The governing-overview placeholder asks for a Markdown link consistent with its adapter field. These are properties of the inline source example, not metadata requirements for a converted Markdown/companion card. The current c-05 Converted Memory section and converted workflow govern this card instead.

This card describes a template as source; it is not an instance of that template. Converted onboarding uses mirrored Markdown and a companion authored by the supported writers: no metadata table or in-card Update History, and no hand-authored companion JSON. Citation tables are authoring input for the fixer, not the final evidence representation. Describing an older template format does not authorize new legacy-format memory writes.

The converted workflow’s moved-source section documents entries first through the writer, then moving/re-authoring the card and retiring the old companion. That ordering belongs to the workflow, not to this inline template. The absence of typed entries does not grant permission to hand-edit a companion or execute a move.

### Todos

The inherited todo asked to refresh verification metadata after a working-tree update landed. Retain that as historical adapter-maintenance context only; it is not an outstanding converted-card field update, and establishes no current landing or metadata refresh.

## Evidence

### Docs References

The inherited documentation notes described no external domain-document need, no configured `Domain Documentation` registry entries and no relevant external documentation after live-source checks. Those registry and live-retrieval observations are inherited, not independently repeated here.

### Repo-Internal References

The inline sample proves markers, semantic-section alignment, overview placement and digest guidance. The current c-05 skill confirms that inline is a storage-specific adapter, while the converted workflow separately owns current card format and move sequencing.

- The inline adapter source reuses the file-level semantic model and describes storage, syntax, placement, metadata and digest differences. [1]
- The sample places governingOverview and the governing-overview link before purpose and the remaining semantic sections. [2]
- The docs placeholder ties no-evidence wording to live-source checks and explicitly allows recording a retrieval blocker. [3]
- The inline source guidelines preserve markers/keys, adapt outer delimiters, respect leading syntax and recompute the digest with the block removed. [4]
- The current c-05 package treats inline as an adapter to the shared file-level semantic content model. [5]
- The c-05 converted-memory branch selects the converted workflow rather than legacy metadata and history rules. [6]
- The converted workflow, not the inline template, documents writer entry movement before card relocation and reference re-authoring. [7]
- Converted cards have no legacy metadata table or in-card Update History and do not hand-author sidecars. [8]

### Cross-Repo References

The inherited explanation needed no sibling-repository evidence and recorded no meaningful cross-repository references. The source-template description establishes no external boundary.
