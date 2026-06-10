# mcp/src/agents_remember/worktrees/modules/onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T04:47+02:00|
| lastVerifiedCommitHash | `5397b76fc4d2bb6808c286fbf8fd780baa5139e0` |
| lastVerifiedCommitDate | 2026-06-10T05:03:05+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Plans and applies closeout-time onboarding metadata, route overview metadata,
route index, and entity fingerprint refreshes for changed code paths.

## Code Commentary

The module finds changed source sidecars — gating each changed source on the
boolean `resolver.is_sidecar_storage(storage)` predicate (sidecar-backed storage
modes only; non-sidecar modes are recorded as `unsupported`) — validates
required verification metadata, updates `lastVerifiedCommitHash` and
`lastVerifiedCommitDate`, parses
route overview metadata, updates affected route overviews, runs generated route
index refreshes, parses repo entity fingerprint tables, computes
`git-blob-set-v1` fingerprints, and updates affected entity rows after the code
commit exists. The shared metadata/route parsing helpers
(`onboarding_metadata_row`, `markdown_table_cells`, `table_metadata`,
`normalize_route`, `route_contains_changed_path`, `ROUTE_OVERVIEW_DOC_TYPES`)
live in `kernel/onboarding_doc.py` and are re-exported here as a facade.

It also enforces the closeout content gate. `classify_sidecar_updates` sorts
each changed source's sidecar by meaningful body change (content outside the
verification metadata rows and Update History, vs the memory tree's HEAD via
`head_text_or_none`) and new Update History lines into four cases:
body+history passes; body without history is `untraced` (traceability);
history-only passes only with a new `No content impact:` marked entry and is
collected as `attested_no_impact`; everything else (unchanged, metadata-only,
unmarked history-only) is `stale`. `require_updated_sidecar_content` raises on
`stale`/`untraced` — the error teaches both the c-05 body-update path and the
explicit no-impact marker — and returns the attested source paths so closeout
payloads can surface them. New sidecars absent from the memory HEAD pass
without classification. The check accepts an explicit `memory_tree` (the
worktree wrapper passes the memory worktree) and safely skips sidecars that do
not resolve under that tree rather than reporting false stale findings;
`validate_onboarding_refresh_plan_for_context` wires it into both closeout
paths before the code commit.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Drift checking verifies the same sidecar and entity fingerprint metadata maintained here. | [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |
| Route index refresh is delegated to the generated route index builder. | [route_index.py](agents-remember-md/mcp/src/agents_remember/kernel/route_index.py) |
| Worktree tests cover missing sidecar blocking, metadata refresh, long paths, and entity fingerprint refresh. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: moved shared metadata/route helpers to `kernel/onboarding_doc.py` (facade re-exports kept) and rebuilt the content gate as the four-case body/history classification (`classify_sidecar_updates` + `require_updated_sidecar_content` returning marker-attested paths): untraced body edits and unmarked history-only edits now fail; `No content impact:` entries pass and are surfaced.
- 2026-06-02T16:24+02:00: User-facing closeout content-gate error messages now say "Run the `c-05-create-or-update-onboarding-files` skill, then rerun closeout" (was "Run C-05 create-or-update-onboarding-files"). Reference-style normalization; behavior unchanged.
- 2026-05-31T12:50+02:00 — `onboarding_refresh_plan_for_context` now gates the sidecar-storage check on the boolean `resolver.is_sidecar_storage(storage)` predicate, replacing the label-returning `resolver.sidecar_storage_label(storage)`; behavior-preserving (truthiness unchanged). Added a Code Commentary note naming the predicate (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Gave the refresh-plan producers precise `TypedDict` return types and removed the now-redundant `isinstance` guards in `require_updated_sidecar_content`; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-29T07:36+02:00: Added `require_updated_sidecar_content` and wired it into `validate_onboarding_refresh_plan_for_context` (direct and worktree) so a changed source file with an unmodified sidecar body fails closeout instead of receiving a metadata-only verification refresh.
- 2026-05-28T15:24+02:00: Updated after closeout began refreshing route overview metadata and generated route indexes before memory quality and memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
