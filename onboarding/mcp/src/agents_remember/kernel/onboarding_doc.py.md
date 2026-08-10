# mcp/src/agents_remember/kernel/onboarding_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/onboarding_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-04T03:03+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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
- This module is kernel-level: it must not import worktree, application entry point, or
  provider modules.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The kernel module defines metadata-row rewriting plus Update History extraction and delta helpers. | `onboarding_metadata_row`; `update_history_section`; `new_history_lines` | mcp/src/agents_remember/kernel/onboarding_doc.py:24-30; mcp/src/agents_remember/kernel/onboarding_doc.py:115-126; mcp/src/agents_remember/kernel/onboarding_doc.py:129-132 |
| The closeout onboarding module imports the body/history classifiers and metadata-row helper from this kernel module. | "from agents_remember.kernel.onboarding_doc import (" | mcp/src/agents_remember/worktrees/modules/onboarding.py:10-10 |
| Route-overview and sidecar classification gates consume the meaningful-body, new-history, and no-impact-marker helpers. | `_overview_revision`; `_governing_overview_bucket`; `_route_overview_bucket`; `classify_sidecar_updates` | mcp/src/agents_remember/worktrees/modules/onboarding.py:218-239; mcp/src/agents_remember/worktrees/modules/onboarding.py:242-250; mcp/src/agents_remember/worktrees/modules/onboarding.py:253-278; mcp/src/agents_remember/worktrees/modules/onboarding.py:592-646 |
| Route-overview and sidecar metadata refresh paths consume `onboarding_metadata_row`. | `refresh_route_overview_metadata_for_context`; `refresh_onboarding_metadata_for_context` | mcp/src/agents_remember/worktrees/modules/onboarding.py:358-389; mcp/src/agents_remember/worktrees/modules/onboarding.py:751-783 |
| The public worktree-manager facade imports and re-exports `onboarding_metadata_row`. | "from agents_remember.worktrees.modules.onboarding import (" | mcp/src/agents_remember/worktrees/git_worktree_manager.py:76-84 |
| Helper unit tests cover body stripping, history extraction, and marker detection. | `test_strips_metadata_rows_and_update_history`; `test_extracts_history_lines_without_heading`; `test_detects_content_marker` | mcp/tests/test_onboarding_doc.py:43-50; mcp/tests/test_onboarding_doc.py:76-78; mcp/tests/test_onboarding_doc.py:99-102 |

## Update History

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the three split consumer ranges (3 repairs, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: split the
  underbound import-only record into explicit import, classification-consumer, and metadata-refresh
  claims with complete owning symbols. All three changed bindings are provisional `:1-1` inputs
  for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated the
  kernel helper definitions from closeout consumption and the public facade re-export. Preserved
  all three generated definition ranges and added only honest `:1-1` consumer/re-export bindings;
  no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the helper and focused-test citation rows after resolving exact-anchor ambiguity; final exact frozen-snapshot check is clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3: added `discover_route_overviews` (doc_type-verified route discovery) for carryover overview candidates.
- 2026-06-10T04:47+02:00 — Created: extracted shared metadata/route helpers from `worktrees/modules/onboarding.py` and added the body/history classification helpers (`meaningful_body`, `meaningful_body_changed`, `update_history_section`, `new_history_lines`, `has_no_impact_marker`) for the issue #56 memory-integrity gates.
