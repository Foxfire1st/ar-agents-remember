# mcp/src/agents_remember/kernel/onboarding_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/onboarding_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:50+02:00                     |
| lastVerifiedCommitHash | `4c24fa63b9d1aa23ae8a8500b4ea4be3eb75e9a4`                                  |
| lastVerifiedCommitDate | 2026-06-10T05:56:31+02:00|
| governingOverview      | `../../../overview.md`                     |

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
- This module is kernel-level: it must not import worktree, controller, or
  provider modules.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The closeout sidecar/overview gates consume these helpers and re-export the moved names. | [onboarding.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/onboarding.py) |
| Helper unit tests cover body stripping, history extraction, and marker detection. | [test_onboarding_doc.py](agents-remember-md/mcp/tests/test_onboarding_doc.py) |

## Update History

- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3: added `discover_route_overviews` (doc_type-verified route discovery) for carryover overview candidates.
- 2026-06-10T04:47+02:00 — Created: extracted shared metadata/route helpers from `worktrees/modules/onboarding.py` and added the body/history classification helpers (`meaningful_body`, `meaningful_body_changed`, `update_history_section`, `new_history_lines`, `has_no_impact_marker`) for the issue #56 memory-integrity gates.
