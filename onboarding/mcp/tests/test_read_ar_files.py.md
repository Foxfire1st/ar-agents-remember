# test_read_ar_files.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_read_ar_files.py`                  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated | 2026-09-21T15:14+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`         |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks paired source reading: exact ranges and full bytes, binary omission, traversal and symlink confinement, first-read overview attachment, unchanged-onboarding deduplication, changed/refresh reservation, compact-marker reset and committed-source payload reading. Since 260921-ICR-L19 the same module is also the suite for the route's **published-intent half** (ICR-R19@v1): the ordinary read resolves the repository's published knowledge dataset from its coordination context and reads the recorded intent about each requested path at that dataset's own snapshot — or names, by its exact binding, why it could not. Since MIK-R24 the ordinary read of unconverted memory is `legacy-format`, so these cases measure the database block beside the read rather than inside it (see Logic). It does not claim the removed broad served-ledger durability or facts-packet suites remain here.

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

**Since MIK-R24 (rule 9) both classes run on unconverted memory, which `read_ar_files` now reads as
`legacy-format`.** `PublishedIntentRouteTests._read` asserts that the payload's block is
`legacy-format`, then replaces it with `published_intent_block(context, paths)`. So the ICR-R19 cases still
measure the database publication route itself, directly rather than through the tool. The carrier-parity
case measures the unrequested block the same way. The two mounted cases were rewritten: one asserts that
an unconverted memory tree holding a database and a card returns `legacy-format`, with the memory root,
a detail naming the crossing sync, and the source bytes. The other asserts `legacy-format` before anything
is published. The converted-tree knowledge section is asserted through `read_ar_files` in
`test_knowledge_conversion_toolchain.py`, and at block level by MIK-R23's index tests; the reviewer
accepted this as equivalent coverage (architect ruling).

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
| Range request returns exact slice | `test_range_request_returns_exact_slice` | mcp/tests/test_read_ar_files.py:204-209 |
| Full read is not truncated | `test_full_read_is_not_truncated` | mcp/tests/test_read_ar_files.py:211-218 |
| Binary source is omitted | `test_binary_source_is_omitted` | mcp/tests/test_read_ar_files.py:220-222 |
| Path confinement rejects escape | `test_path_confinement_rejects_escape` | mcp/tests/test_read_ar_files.py:224-226 |
| Symlink file escape rejected | `test_symlink_file_escape_rejected` | mcp/tests/test_read_ar_files.py:228-236 |
| Symlink dir escape rejected | `test_symlink_dir_escape_rejected` | mcp/tests/test_read_ar_files.py:238-247 |
| First read attaches overview and route chain | `test_first_read_attaches_overview_and_route_chain` | mcp/tests/test_read_ar_files.py:288-294 |
| Second read dedups unchanged pieces | `test_second_read_dedups_unchanged_pieces` | mcp/tests/test_read_ar_files.py:296-300 |
| Changed overview is reserved | `test_changed_overview_is_reserved` | mcp/tests/test_read_ar_files.py:302-309 |
| Refresh forces reserve | `test_refresh_forces_reserve` | mcp/tests/test_read_ar_files.py:311-315 |
| Compact marker resets served | `test_compact_marker_resets_served` | mcp/tests/test_read_ar_files.py:317-325 |
| Payload reads committed source | `test_payload_reads_committed_source` | mcp/tests/test_read_ar_files.py:351-353 |
| **The published-intent half's headline case: the ordinary read returns the repository's published intent at its exact identities, and the source bytes ride in the same payload.** | `test_the_ordinary_read_returns_the_published_intent_at_its_exact_identities` | mcp/tests/test_read_ar_files.py:434-469 |
| **The carrier-parity case: the payload's real field spellings are derived from a real page, and the camelCase variants are rejected.** | `test_the_carrier_uses_the_field_spellings_the_payload_actually_returns` | mcp/tests/test_read_ar_files.py:529-552 |
| **The four named absences and refusals: nothing published, bytes that are not a dataset, a directory at the publication path, and a seed that is not a typed seed.** | `test_a_repository_that_publishes_nothing_reports_not_recorded`; `test_a_dataset_that_is_not_a_dataset_names_the_failed_binding`; `test_a_directory_at_the_publication_path_is_not_reported_as_nothing_recorded`; `test_a_seed_that_is_not_a_typed_seed_is_refused_rather_than_raising` | mcp/tests/test_read_ar_files.py:471-480; mcp/tests/test_read_ar_files.py:482-489; mcp/tests/test_read_ar_files.py:491-507; mcp/tests/test_read_ar_files.py:509-527 |
| **The four selection and identity refusals: another repository's dataset, a path the snapshot records nothing about, an identity the snapshot does not hold, and a path no recorded anchor could carry.** | `test_a_dataset_bound_to_another_repository_is_never_silently_read`; `test_a_path_the_snapshot_records_nothing_about_is_a_named_absence`; `test_an_identity_the_snapshot_does_not_hold_is_a_named_absence`; `test_a_path_no_recorded_anchor_could_carry_is_refused_as_a_seed` | mcp/tests/test_read_ar_files.py:554-565; mcp/tests/test_read_ar_files.py:567-575; mcp/tests/test_read_ar_files.py:577-602; mcp/tests/test_read_ar_files.py:604-611 |
| **The source pair and the identity seed: the resolved pair is what recorded anchors are observed against, and an identity-seeded page carries the exact retained revisions.** | `test_the_resolved_source_pair_is_what_recorded_anchors_are_observed_against`; `test_an_identity_seeded_page_carries_exact_retained_revisions`; `_identity_seeded_page` | mcp/tests/test_read_ar_files.py:613-637; mcp/tests/test_read_ar_files.py:639-665; mcp/tests/test_read_ar_files.py:667-683 |
| **The mounted route, which is the call an agent actually makes: on unconverted memory it returns no knowledge section and names the legacy format, with and without a database.** | `test_the_mounted_route_returns_no_knowledge_section_for_unconverted_memory`; `test_the_mounted_route_names_the_legacy_format_before_anything_is_published` | mcp/tests/test_read_ar_files.py:709-723; mcp/tests/test_read_ar_files.py:725-729 |
| The route-class read helper asserts `legacy-format`, then measures the database block directly. | `_read`; `published_intent_block` | mcp/tests/test_read_ar_files.py:408-418 |
| The published-intent fixtures, including the `_selection()` narrowing helper the type-checked call sites need. | `PublishedIntentRouteTests`; `_selection`; `PublishedIntentMountedRouteTests` | mcp/tests/test_read_ar_files.py:361-683; mcp/tests/test_read_ar_files.py:420-432; mcp/tests/test_read_ar_files.py:686-729 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update (MIK-R24 rule 9).** The ICR-R19 route cases now assert `legacy-format` and measure the database block through `published_intent_block` directly. The two mounted cases were renamed and rewritten for the legacy-format read. The Logic paragraph says where the converted-tree coverage lives (architect ruling). The reopened mounted-route row now names the new cases, and a row for the `_read` helper was added.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **body updated — this suite gained a second half.** The module now holds 14 new cases in two classes, `PublishedIntentRouteTests` (12, application layer) and `PublishedIntentMountedRouteTests` (2, the mounted `read_ar_files` route), so the card's Purpose and Logic state what the published-intent half measures rather than leaving the suite described as paired-reading only. **Every row of the reference table was re-derived against the candidate, not shifted**: this leaf's insertions moved the twelve retained cases (for example `test_range_request_returns_exact_slice` `176-181` → `203-208`, `test_payload_reads_committed_source` `323-325` → `350-357`) and five rows were added for the new inventory — the headline identity round trip, the carrier-parity case, the four named absences/refusals, the four selection and identity refusals, the source-pair and identity-seed pair, the two mounted-route cases, and the class fixtures including the `_selection()` narrowing helper. No case was renamed, no anchor was dropped, and no claim was re-worded to fit a stale pointer. **Stamp accounting:** the recorded working candidate names this leaf's candidate; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded, because no commit contains the body as it now stands and the governed closeout owns the real stamp. No commit was made and no test run is claimed here beyond the leaf's own reported suite result.

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
