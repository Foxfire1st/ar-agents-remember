# mcp/src/agents_remember/kernel/onboarding_doc.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Kernel-level onboarding-document helpers: markdown metadata-table parsing,
route normalization, and the section-aware body/history change classification
that closeout gates and carryover planning share.

## Code Commentary

### Logic

The metadata helpers (`onboarding_metadata_row`, `markdown_table_cells`,
`table_metadata`, `normalize_route`, `route_contains_changed_path`,
`ROUTE_OVERVIEW_DOC_TYPES`) moved here verbatim from
`worktrees/modules/onboarding.py`, which keeps re-exporting them as a facade.
`discover_route_overviews(onboarding_root)` returns (normalized route,
onboarding-root-relative path) pairs for doc_type-verified route overviews —
the shared discovery used by carryover overview candidates.

The change-classification helpers define what counts as an honest onboarding
update. `meaningful_body(text)` is the document minus the three verification
metadata rows (`lastUpdated`, `lastVerifiedCommitHash`,
`lastVerifiedCommitDate`) and the entire `## Update History` section;
`meaningful_body_changed(old, new)` compares those normalized bodies and treats
`old=None` (new document) as changed. `update_history_section(text)` returns the
stripped non-empty history lines, `new_history_lines(old, new)` returns history
lines present only in the new text, and `has_no_impact_marker(lines)` matches
the in-band attestation convention: an Update History entry containing
`No content impact:` (file sidecars) or `No route impact:` (route overviews),
case-insensitive, colon required.

### Invariants And Boundaries

- Metadata stamps and history appendices never count as content updates; only
  text outside the metadata rows and Update History section is "body".
- The no-impact marker is the explicit reviewed-no-impact attestation; gate
  errors teach it, and closeout payloads surface every attested document so
  marker use stays visible at the commit-approval gate.
- Any `## ` heading ends the Update History section; a marker outside the
  history section never attests anything.
- This module is kernel-level: it must not import worktree, application entry point, or
  provider modules.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The kernel module defines metadata-row rewriting plus Update History extraction and delta helpers. [1]
- The closeout onboarding module imports the body/history classifiers and metadata-row helper from this kernel module. [2]
- Route-overview and sidecar classification gates consume the meaningful-body, new-history, and no-impact-marker helpers. [3]
- On an unconverted memory tree the route-overview and sidecar metadata refresh paths consume `onboarding_metadata_row`; on a converted tree both return before it (MIK-R30 rule 5). [4]
- The public worktree-manager facade imports and re-exports `onboarding_metadata_row`. [5]
- Meaningful-body normalization strips verification fields and history. [6]
- History extraction is section-aware. [7]
- A recognized no-impact marker requires its explicit colon form. [8]
