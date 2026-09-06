# mcp/tests/test_conversation_active_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation projector ordering, native-history merge and gap behavior.

## Code Commentary

### Logic

A scripted bridge exercises stable IDs and ordinals, settled-turn deduplication even with disjoint native IDs, prior-session history and older paging. Epoch changes and regressed evidence tips refuse. Split results remain ordered across polls, and pending zipper frames make total_items unknown without inventing an older cursor.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Pending newer content is not older history. Native re-walks must not duplicate settled turns; retained assertions are projection behavior rather than wire-level harness execution.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Hydration orders items and mints stable ids. | `test_hydration_orders_items_and_mints_stable_ids` | mcp/tests/test_conversation_active_service.py:223-244 |
| Settled live turns project once when native ids disjoint. | `test_settled_live_turns_project_once_when_native_ids_disjoint` | mcp/tests/test_conversation_active_service.py:246-331 |
| Prior session native history survives live turns. | `test_prior_session_native_history_survives_live_turns` | mcp/tests/test_conversation_active_service.py:333-353 |
| Native page hydration and older paging. | `test_native_page_hydration_and_older_paging` | mcp/tests/test_conversation_active_service.py:355-383 |
| Gap on epoch flip. | `test_gap_on_epoch_flip` | mcp/tests/test_conversation_active_service.py:385-392 |
| Zipper handles split result across polls. | `test_zipper_handles_split_result_across_polls` | mcp/tests/test_conversation_active_service.py:424-480 |
| Page never claims completeness while frames pend. | `test_page_never_claims_completeness_while_frames_pend` | mcp/tests/test_conversation_active_service.py:482-541 |
| Regressed evidence tip gaps instead of freezing. | `test_regressed_evidence_tip_gaps_instead_of_freezing` | mcp/tests/test_conversation_active_service.py:543-555 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 12 citation findings across the six projector, ingestion, stream, store, and bridge-model rows and normalized 10 additional current prose citations to exact `cit:` form.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the last cross-file citation still pointing at the deleted `active/projector.py`. Replaced the single "projector engine under test" row with four verified rows against the `active/projector/` package: `facade.py` L59-L221 (poll loop, gap classification, dormant release), `rebuild_coordinator.py` L94-L104; L129-L144; L150-L192 (hydration, poll-channel order, paging), `native_ingestion.py` L36-L41; L116-L146 (`ZipperEvidenceEvicted` / `EvidenceTimelineRegressed`), and `mutation_stream.py` L165-L197 (retention, retention-overflow gap, gap envelope).
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: followed the projector construction seam and
  re-anchored every self-citation. `_projector` now builds `ActiveSessionProjector` from a
  `ProjectedSession` (identity, authorization, entry, mapper, secret) plus a `BridgeReaders` bundle
  (evidence, native_page, transcript, provenance, snapshot) imported from `projector.facade` and
  `projector.wiring`, so the Logic and Conventions paragraphs now name both instead of describing
  ten loose keywords. Recorded the tightened double: `_ScriptedBridge.read_native_page` dropped its
  `byte_budget` parameter so the fake accepts exactly what the production
  `read_control_native_page` seam accepts. Corrected the stale class citations against the current
  file — `_ScriptedBridge` L75-L170, `_projector` L177-L196, `CodexEngineTests` L233-L551,
  `ClaudeEngineTests` L553-L846, `PiEngineTests` L848-L890, `StoreTests` L892-L911,
  `ToolConvergenceTests` L913-L1200, `OverflowGapTests` L1435-L1479, `ZipperEvictionGapTests`
  L1481-L1914, and the reordered-binder case L982-L1053 — and named the rehydration-realignment
  block that closes the eviction class. No test was added, removed, or renamed; assertions are
  unchanged apart from `ruff format` reflow. Verification metadata remains pinned until closeout.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: followed the projector
  decomposition in the existing behavior suite: zipper, status revision, overflow bound,
  native-live buckets, retained envelopes, and dormant release now assert against their owning
  components. Test meaning is unchanged and proves the split preserved behavior. Verification
  metadata remains pinned until closeout.

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the reordered-binder regression
  (`test_reordered_task_started_tagging_never_regresses_a_terminal_phase` — fix-round finding 9:
  an Agent tool_result settling before `task_started` keeps the terminal phase while the agent
  ref still lands) and followed the dormant-release assertions to the L7 per-thread dict shape of
  `_live_turn_ids`/`_live_request_ids`. Verification metadata stays pinned (uncommitted); closeout
  re-stamps the candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R3 echo-honesty test
  (`test_nonuser_transcript_entries_mint_no_echo_unknown_vendor_rows` — non-user transcript entries
  no longer mint `claude:echo` rows) and the new `DormantReleaseTests`
  (`test_release_dormant_state_frees_heavy_projection_and_retires_shell` — R5: the idle-break frees
  the heavy per-session projection and retires the shell instead of leaving a resident tombstone).
  Verification metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: recorded the H2 and F1 projector-tier
  regressions added by L5 — `test_native_remap_after_resolution_stays_model_valid` (H2, drives the
  real poll path, pre-fix raises the exact E2 `ValidationError`) and the three F1 tests
  (`…_project_once_when_native_ids_disjoint`, `…_when_hosted_renumbers_turn_ids`, and
  `…prior_session_native_history_survives_live_turns`) that fail on stashed `projector.py` with the
  exact native twins and pass with `_drop_live_settled_natives`. Always-run companions to the
  installed F1 real-wire regression. Verification metadata stays pinned until L5 closeout stamps the
  candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the engine/store
  suite — hydration/ordering/idempotence/provenance/rehydration plus the F1/F2/F3 fix pins (19
  tests). Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
