# mcp/src/agents_remember/worktrees/modules/onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Worktree modules overview](overview.md)

## Purpose

Plans and applies closeout-time onboarding metadata, route overview metadata,
route index, and entity fingerprint refreshes for changed code paths.

## Code Commentary

The module finds changed source sidecars — gating each changed source on the
boolean `resolver.is_sidecar_storage(storage)` predicate (sidecar-backed storage
modes only) — validates required verification metadata, updates
`lastVerifiedCommitHash` and `lastVerifiedCommitDate`, parses
route overview metadata, updates affected route overviews, runs generated route
index refreshes, parses repo entity fingerprint tables, computes
`git-blob-set-v1` fingerprints, and updates affected entity rows after the code
commit exists. The shared metadata/route parsing helpers
(`onboarding_metadata_row`, `markdown_table_cells`, `table_metadata`,
`normalize_route`, `route_contains_changed_path`, `ROUTE_OVERVIEW_DOC_TYPES`)
live in `kernel/onboarding_doc.py` and are re-exported here as a facade.

`refresh_onboarding_metadata_for_context` also stamps the task's regenerated citation documents
(`_refresh_regenerated_documents`, 260731-EFA-L16): the citation gate clears a changed claim by
making its citation CURRENT, which the fixer achieves without the document's own source file
changing, so those documents are outside the changed-source plan — any onboarding document the
task touched in the memory worktree that carries verification metadata advances to the new code
commit here, except route overviews and entity catalogs (their own refresh passes own them).

`onboarding_refresh_plan_for_context` carries the two-tier responsibility split
(issue #83) through its keyword-only `working_paths`: paths in the working set
without onboarding land in the blocking `missing`/`unsupported` buckets exactly
as before, while committed-range paths (transported merges, pre-committed
slices) without onboarding collect in the non-blocking `unonboarded` list, so
already-onboarded artifacts gate regardless of author but never-onboarded files
are not blanket-onboarded at closeout. `working_paths=None` keeps the strict
legacy semantics. `contract_memory_verified_commit(contract)` resolves the
body-gate baseline (`ledger_commit` → `memory_content_commit` →
`memory_base_commit`), `_changed_memory_paths` widens gate membership to dirty
∪ committed-since-verified memory paths, and `_joined_sample` caps gate error
path joins at `PATH_SAMPLE_LIMIT`.

It also enforces the closeout content gate. `classify_sidecar_updates` sorts
each changed source's sidecar by meaningful body change (content outside the
verification metadata rows and Update History, vs the last verified memory
commit via `commit_text_or_none` — `memory_verified_commit`, falling back to
HEAD when empty) and new Update History lines into four cases:
body+history passes; body without history is `untraced` (traceability);
history-only passes only with a new `No content impact:` marked entry and is
collected as `attested_no_impact`; everything else (unchanged, metadata-only,
unmarked history-only) is `stale`. The verified-commit baseline means sidecar
work already committed in the memory worktree before closeout still classifies
honestly, and a new sidecar committed early passes like an untracked one
(absent at the baseline). `require_updated_sidecar_content` raises on
`stale`/`untraced` — the error teaches both the c-05 body-update path and the
explicit no-impact marker — and returns the attested source paths so closeout
payloads can surface them. The check accepts an explicit `memory_tree` (the
worktree wrapper passes the memory worktree) and safely skips sidecars that do
not resolve under that tree rather than reporting false stale findings;
`validate_onboarding_refresh_plan_for_context` wires it into the worktree
closeout path before the code commit.

Route overviews get the same body gate scoped by domain evidence.
`_nearest_governing_route` picks the longest matched route per changed path
(`.` loses to any deeper route); `classify_route_overview_updates` classifies
only those nearest-governing overviews as stale / untraced / attested (marker
`No route impact:`), while ancestor-matched overviews — including the repo-root
overview matched by happenstance — are collected as
`stamped_without_body_review` (skipped when their body was reviewed anyway) and
never gate closeout.

Since 260731-EFA-L2 that classification is three named steps, and
`classify_route_overview_updates` is just the loop that appends each returned bucket name:

- `_overview_revision(overview_path, *, memory_root, baseline_ref, changed_memory)` → `(body
  meaningfully changed, history lines added) | None`. **`None` is not a verdict** — it means the
  overview is outside the memory tree or absent from the baseline, neither of which is a stale
  signal, so those overviews drop out of the classification entirely.
- `_governing_overview_bucket(body_changed, added_history)` → the gating bucket for a
  nearest-governor overview: `None` once it is properly updated (body changed *and* history added),
  else `untraced` / `attested_no_impact` / `stale`.
- `_route_overview_bucket(overview_path, *, memory_root, baseline_ref, changed_memory,
  domain_evident)` → the bucket for one matched overview. Only a nearest governor
  (`domain_evident`) is classified like a sidecar; an ancestor match returns
  `stamped_without_body_review` when its body went unreviewed, and `None` otherwise.

`refresh_onboarding_metadata(contract, change)`,
`refresh_onboarding_metadata_for_context(context, change, *, memory_tree=None,
memory_verified_commit="")` and `refresh_route_overview_metadata_for_context(context, change, *,
memory_tree=None, memory_verified_commit="")` all take a `VerifiedChange` (from `modules.models`)
in place of the separate `changed_paths` / `verified_commit` / `verified_date` / `working_paths`
arguments, so a refresher cannot stamp one commit's hash beside another's path list. `require_updated_route_overview_content` raises on
stale/untraced and returns attested routes;
`validate_route_overview_refresh_plan_for_context` runs it (with `memory_tree`
and `memory_verified_commit` plumbed from the worktree wrapper) before the code
commit. New overview files absent from the verified baseline pass without
classification.

MX-FIX-4 keeps route-index authority attached to that same resolved context:
both preview and apply pass `context.storage` explicitly to
`build_route_indexes()`. Closeout therefore cannot generate derived memory
using a different path-rule interpretation from the refresh plan it validated.

### Conventions

This module owns closeout orchestration and classification; shared Markdown
parsing stays in `kernel/onboarding_doc.py`, deterministic source census stays
in `kernel/route_index_census.py`, and rendering stays in
`kernel/route_index.py`.

### Invariants And Boundaries

- Sidecar and nearest-governing overview body/history gates run before code
  commit; ancestor overviews are reported but do not become false blockers.
- Working-tree missing onboarding blocks, while transported committed-range
  gaps remain explicitly reported as `unonboarded`.
- Route-index preview and apply must use the exact `context.storage` authority
  resolved for the refresh plan; no builder default may replace it.
- Generated indexes and entity fingerprints are derived after their owning
  authored bodies are validated.

### Todos

None known for the MX-FIX-4 closeout caller boundary.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Drift checking verifies the same sidecar and entity fingerprint metadata maintained here. | `classify_sidecar_onboarding_units`; `classify_entity_fingerprint` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:289-342; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:222-280 |
| Route-index refresh accepts the resolved storage authority and consumes one deterministic source snapshot. | `build_route_indexes`; `route_index_source_snapshot` | mcp/src/agents_remember/kernel/route_index.py:182-230; mcp/src/agents_remember/kernel/route_index_census.py:41-63 |
| Worktree tests cover missing sidecar blocking, metadata refresh, long paths, and entity fingerprints. |"test_onboarding_refresh_plan_detects_long_sidecar_paths"; "test_closeout_refreshes_onboarding_metadata_to_new_code_commit"; "test_closeout_blocks_missing_onboarding_for_changed_source"; "test_closeout_refreshes_entity_fingerprint_after_code_commit"|mcp/tests/test_worktree_support_tests_1.py:1076-1076; mcp/tests/test_worktree_support_tests_2.py:77-77; mcp/tests/test_worktree_support_tests_2.py:120-120; mcp/tests/test_worktree_support_tests_2.py:514-514|

## Cross-Repo References

Closeout can coordinate code and external-memory worktrees, but no external
implementation governs this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded `_refresh_regenerated_documents` — the metadata refresh now also stamps onboarding documents the task touched (memory worktree diff) that carry verification metadata, so citations the fixer regenerated against the working tree do not stay pinned to a commit whose constructs no longer exist; route overviews and entity catalogs keep their own refresh passes. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T18:47+02:00 — 260731-EFA-L6 S18-B17 curator: corrected the four drifted test ranges
  in the worktree-tests row (long-sidecar 1573-1592, metadata refresh 1631-1673, missing-sidecar
  blocking 1674-1694, entity fingerprint 2041-2094) and narrowed the claim: the "explicit
  initialized-memory storage authority" sub-claim is evidenced by none of the four cited tests, so
  it was dropped rather than pointed at an unrelated route-index test.
- 2026-08-03T10:55+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 7 assigned citation findings (3 missing anchors and 4 malformed sources); final scoped check is clean.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912`/`PLR0913` armed with no
  exemptions): `classify_route_overview_updates`'s body was extracted into `_overview_revision`,
  `_governing_overview_bucket` and `_route_overview_bucket`, leaving the public function as the
  loop that appends each returned bucket; and `refresh_onboarding_metadata`,
  `refresh_onboarding_metadata_for_context` and `refresh_route_overview_metadata_for_context` were
  re-signed onto `VerifiedChange`. Classification outcomes and stamped metadata are unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: route-index preview and apply now pass the resolved
  `context.storage` authority explicitly into deterministic generation.
- 2026-06-12T19:06+02:00 — Issue #83: two-tier plan split via `working_paths` (blocking `missing`/`unsupported` scoped to working paths, committed-range gaps collected as non-blocking `unonboarded`), body gates re-baselined on `contract_memory_verified_commit` via `commit_text_or_none` with `_changed_memory_paths` membership, and `_joined_sample` capping gate error joins.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added the route-overview body gate (`_nearest_governing_route`, `classify_route_overview_updates`, `require_updated_route_overview_content` with the `No route impact:` marker) wired into `validate_route_overview_refresh_plan_for_context`; ancestor matches report as `stamped_without_body_review` instead of failing.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: moved shared metadata/route helpers to `kernel/onboarding_doc.py` (facade re-exports kept) and rebuilt the content gate as the four-case body/history classification (`classify_sidecar_updates` + `require_updated_sidecar_content` returning marker-attested paths): untraced body edits and unmarked history-only edits now fail; `No content impact:` entries pass and are surfaced.
- 2026-06-02T16:24+02:00: User-facing closeout content-gate error messages now say "Run the `c-05-create-or-update-onboarding-files` skill, then rerun closeout" (was "Run C-05 create-or-update-onboarding-files"). Reference-style normalization; behavior unchanged.
- 2026-05-31T12:50+02:00 — `onboarding_refresh_plan_for_context` now gates the sidecar-storage check on the boolean `resolver.is_sidecar_storage(storage)` predicate, replacing the label-returning `resolver.sidecar_storage_label(storage)`; behavior-preserving (truthiness unchanged). Added a Code Commentary note naming the predicate (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Gave the refresh-plan producers precise `TypedDict` return types and removed the now-redundant `isinstance` guards in `require_updated_sidecar_content`; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-29T07:36+02:00: Added `require_updated_sidecar_content` and wired it into `validate_onboarding_refresh_plan_for_context` (direct and worktree) so a changed source file with an unmodified sidecar body fails closeout instead of receiving a metadata-only verification refresh.
- 2026-05-28T15:24+02:00: Updated after closeout began refreshing route overview metadata and generated route indexes before memory quality and memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
