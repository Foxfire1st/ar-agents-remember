# test_read_ar_files.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_read_ar_files.py`                  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated | 2026-09-21T15:14+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l19`, uncommitted; base `0fca5c69766aa95eebe950c19fbcdc83864ec35a` |
| lastVerifiedCommitHash | `c755cec64fa9dc12e797c9fcfb4c96822718330c`         |
| lastVerifiedCommitDate | 2026-09-21T15:29:12+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks paired source reading: exact ranges and full bytes, binary omission, traversal and symlink confinement, first-read overview attachment, unchanged-onboarding deduplication, changed/refresh reservation, compact-marker reset and committed-source payload reading. Since 260921-ICR-L19 the same module is also the suite for the route's **published-intent half** (ICR-R19@v1): the ordinary read resolves the repository's published knowledge dataset from its coordination context and reads the recorded intent about each requested path at that dataset's own snapshot — or names, by its exact binding, why it could not. It does not claim the removed broad served-ledger durability or facts-packet suites remain here.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The published-intent half is two classes. `PublishedIntentRouteTests` drives the application entry point
with a real dataset written at the memory layer's own name: the identity round trip, the four named
absences and refusals, the source-pair observation, an identity-seeded page, and one carrier-parity case
that derives the payload's field spellings from a real page rather than restating them.
`PublishedIntentMountedRouteTests` drives the **mounted** `read_ar_files` route over a real coordination
tree, so the block is measured through the call an agent actually makes rather than only beside it.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Range request returns exact slice | `test_range_request_returns_exact_slice` | mcp/tests/test_read_ar_files.py:203-208 |
| Full read is not truncated | `test_full_read_is_not_truncated` | mcp/tests/test_read_ar_files.py:210-217 |
| Binary source is omitted | `test_binary_source_is_omitted` | mcp/tests/test_read_ar_files.py:219-221 |
| Path confinement rejects escape | `test_path_confinement_rejects_escape` | mcp/tests/test_read_ar_files.py:223-225 |
| Symlink file escape rejected | `test_symlink_file_escape_rejected` | mcp/tests/test_read_ar_files.py:227-235 |
| Symlink dir escape rejected | `test_symlink_dir_escape_rejected` | mcp/tests/test_read_ar_files.py:237-246 |
| First read attaches overview and route chain | `test_first_read_attaches_overview_and_route_chain` | mcp/tests/test_read_ar_files.py:287-293 |
| Second read dedups unchanged pieces | `test_second_read_dedups_unchanged_pieces` | mcp/tests/test_read_ar_files.py:295-299 |
| Changed overview is reserved | `test_changed_overview_is_reserved` | mcp/tests/test_read_ar_files.py:301-308 |
| Refresh forces reserve | `test_refresh_forces_reserve` | mcp/tests/test_read_ar_files.py:310-314 |
| Compact marker resets served | `test_compact_marker_resets_served` | mcp/tests/test_read_ar_files.py:316-329 |
| Payload reads committed source | `test_payload_reads_committed_source` | mcp/tests/test_read_ar_files.py:350-357 |
| **The published-intent half's headline case: the ordinary read returns the repository's published intent at its exact identities, and the source bytes ride in the same payload.** | `test_the_ordinary_read_returns_the_published_intent_at_its_exact_identities` | mcp/tests/test_read_ar_files.py:426-461 |
| **The carrier-parity case: the payload's real field spellings are derived from a real page, and the camelCase variants are rejected.** | `test_the_carrier_uses_the_field_spellings_the_payload_actually_returns` | mcp/tests/test_read_ar_files.py:521-544 |
| **The four named absences and refusals: nothing published, bytes that are not a dataset, a directory at the publication path, and a seed that is not a typed seed.** | `test_a_repository_that_publishes_nothing_reports_not_recorded`; `test_a_dataset_that_is_not_a_dataset_names_the_failed_binding`; `test_a_directory_at_the_publication_path_is_not_reported_as_nothing_recorded`; `test_a_seed_that_is_not_a_typed_seed_is_refused_rather_than_raising` | mcp/tests/test_read_ar_files.py:463-472; mcp/tests/test_read_ar_files.py:474-481; mcp/tests/test_read_ar_files.py:483-499; mcp/tests/test_read_ar_files.py:501-519 |
| **The four selection and identity refusals: another repository's dataset, a path the snapshot records nothing about, an identity the snapshot does not hold, and a path no recorded anchor could carry.** | `test_a_dataset_bound_to_another_repository_is_never_silently_read`; `test_a_path_the_snapshot_records_nothing_about_is_a_named_absence`; `test_an_identity_the_snapshot_does_not_hold_is_a_named_absence`; `test_a_path_no_recorded_anchor_could_carry_is_refused_as_a_seed` | mcp/tests/test_read_ar_files.py:546-557; mcp/tests/test_read_ar_files.py:559-567; mcp/tests/test_read_ar_files.py:569-594; mcp/tests/test_read_ar_files.py:596-603 |
| **The source pair and the identity seed: the resolved pair is what recorded anchors are observed against, and an identity-seeded page carries the exact retained revisions.** | `test_the_resolved_source_pair_is_what_recorded_anchors_are_observed_against`; `test_an_identity_seeded_page_carries_exact_retained_revisions`; `_identity_seeded_page` | mcp/tests/test_read_ar_files.py:605-631; mcp/tests/test_read_ar_files.py:633-659; mcp/tests/test_read_ar_files.py:661-677 |
| **The mounted route, which is the call an agent actually makes: the publication at the memory layer is read, and the absence is named before anything is published.** | `test_the_mounted_route_reads_the_memory_layer_publication`; `test_the_mounted_route_names_the_absence_before_anything_is_published` | mcp/tests/test_read_ar_files.py:703-719; mcp/tests/test_read_ar_files.py:721-736 |
| The published-intent fixtures, including the `_selection()` narrowing helper the type-checked call sites need. | `PublishedIntentRouteTests`; `_selection`; `PublishedIntentMountedRouteTests` | mcp/tests/test_read_ar_files.py:360-369; mcp/tests/test_read_ar_files.py:412-424; mcp/tests/test_read_ar_files.py:680-686 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **body updated — this suite gained a second half.** The module now holds 14 new cases in two classes, `PublishedIntentRouteTests` (12, application layer) and `PublishedIntentMountedRouteTests` (2, the mounted `read_ar_files` route), so the card's Purpose and Logic state what the published-intent half measures rather than leaving the suite described as paired-reading only. **Every row of the reference table was re-derived against the candidate, not shifted**: this leaf's insertions moved the twelve retained cases (for example `test_range_request_returns_exact_slice` `176-181` → `203-208`, `test_payload_reads_committed_source` `323-325` → `350-357`) and five rows were added for the new inventory — the headline identity round trip, the carrier-parity case, the four named absences/refusals, the four selection and identity refusals, the source-pair and identity-seed pair, the two mounted-route cases, and the class fixtures including the `_selection()` narrowing helper. No case was renamed, no anchor was dropped, and no claim was re-worded to fit a stale pointer. **Stamp accounting:** `reviewedWorkingCandidate` names this leaf's candidate; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded, because no commit contains the body as it now stands and the governed closeout owns the real stamp. No commit was made and no test run is claimed here beyond the leaf's own reported suite result.

- 2026-09-06T22:41:21+00:00: Generated citation repair: "\"coordinationRoot\": str(coordination_root)" repointed to mcp/tests/test_config.py:31-31. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:32+02:00 — W2-B08 curator: anchored 10 citation findings to the application entry point, payload builder, ranged reader, served ledger, and config helper evidence. Verification metadata stays pinned until closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — No content impact: the only non-format edit is the ambient-lifecycle
  construction in the `FrontDoorDedupTests` and `ServedLedgerAndEventTests` fixtures, which now
  passes `timing=AmbientTiming(heartbeat_seconds=3600)` instead of the loose `heartbeat_seconds`
  keyword; the card names neither the keyword nor the heartbeat value, and both fixtures still
  install a real ambient lifecycle over a temp `EventStore` and reset the singleton around each
  case. The rest is `ruff format` reflow of `_write_route_index`, the two `_read` helpers, and one
  trailing comma. Re-checked the five test classes and every enumerated case against the source:
  none was added, removed, renamed, or re-asserted, so the status-semantics, path-confinement,
  dedup, served-ledger, facts-only `read.packet`, and five-file-cap claims all still hold.
- 2026-06-23T01:40+02:00 — Slice 07b v1: the emission test now also asserts the `read.packet`'s `data.repoId == REPO` (the read's repo carried alongside the per-file facts). Body only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07: the `read_ar_files` test suite (ranged read, status semantics, path-confinement, facts-only `read.packet`, served-ledger dedup/reset, five-file cap + payload end-to-end). Verification metadata pinned until closeout stamps the slice-07 code commit.
