# mcp/tests/test_conversation_active_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Projector-engine and store tests: hydration, ordering, idempotence,
provenance resolution, rehydration, and the review-fix gap mechanics — driven through a scripted
in-memory bridge seam, plus the review-F1 tool-convergence proofs through the real mappers and
store.

## Code Commentary

### Logic

A cit:([`_ScriptedBridge`], mcp/tests/test_conversation_active_service.py:66-164) plays scripted evidence/native/transcript/provenance/snapshot
answers through the projector's injected reader seams; its `read_native_page` double takes exactly
the production seam's parameters (`entry`, `cursor`, `limit`, `expected_bridge_epoch`) and
deliberately does NOT accept a `byte_budget`, so a caller cannot pass the double an argument the
real `read_control_native_page` would reject. cit:([`_projector`], mcp/tests/test_conversation_active_service.py:168-187) assembles the projector from
a `ProjectedSession(identity, authorization, entry, mapper, secret)` and a
`BridgeReaders(evidence, native_page, transcript, provenance, snapshot)` bundle rather than ten
loose keywords. cit:([`CodexEngineTests`], mcp/tests/test_conversation_active_service.py:224-541): hydration
from native pages plus the live window with stable identity and ordinals; live polling appends
in order; idempotent re-feeds mint no duplicates; provenance resolves through the batch;
ephemeral-thread native refusal stays honestly partial; rehydration reproduces the identical
projection with a new generation. cit:([`ClaudeEngineTests`], mcp/tests/test_conversation_active_service.py:544-836): the echo zipper merges
submission echoes and frames in exact turn order (echo first, result in a later poll, multiple
turns) with no duplicate or inverted items. cit:([`PiEngineTests`], mcp/tests/test_conversation_active_service.py:839-880): eager native
continuation anchors live items to durable-entry identity and live tool upserts converge.
cit:([`StoreTests`], mcp/tests/test_conversation_active_service.py:883-901): identical upsert replays are no-ops. `ToolConvergenceTests` cit:([`ToolConvergenceTests`], mcp/tests/test_conversation_active_service_queues.py:31-326) (review finding F1): claude `tool_use` → `tool_result`, pi live start → update →
end (including the result-less update as a true no-op), and pi entry call → `toolResult` all
converge to items carrying BOTH input and output blocks with completed phase; codex full-item
re-maps are byte-identical under the block union. `OverflowGapTests` cit:([`OverflowGapTests`], mcp/tests/test_conversation_active_service_gaps.py:22-65) (review finding
F2): with a clamped undrained subscriber queue the consumer receives exactly one
`retention-overflow` gap (requiresRepage + closeAfterEvent) then the close sentinel, and the
retention sequence set is contiguous with no hole. `ZipperEvictionGapTests` cit:([`ZipperEvictionGapTests`], mcp/tests/test_conversation_active_service_gaps.py:68-500) (review
finding F3): an advancing eviction floor raises `ZipperEvidenceEvicted` for the echo-zipper
projector (mapped to one ordering-fault gap), does NOT gap the codex projector (totals clear
honestly), and a fresh claude projector rehydrates from the remaining window without raising,
followed by the rehydration-realignment cases over evicted, in-flight, echoless, settled-close,
non-turn-trailing, lifecycle-only, and paged-transcript evidence.

### Projector-tier regressions (H2 model-validity + F1 project-once)

Two proven-failure families extend `CodexEngineTests`, both driving the REAL projector poll path and
re-validating every emitted item — the surface the intermittent active-page 500 and the native
twins actually reach:

- **H2** — `test_native_remap_after_resolution_stays_model_valid` cit:([`test_native_remap_after_resolution_stays_model_valid`], mcp/tests/test_conversation_active_service.py:273-318): a resolved user item re-mapped by
  a native frame must stay model-valid; before the store's `_preserved_input_authority` pin this
  raised the exact E2 `ValidationError: unknown-input cannot claim exact or correlated provenance`
  when `UpsertItemMutation` re-validated the split authority triple. The pre-existing
  `test_provenance_resolution_exact_then_unknown` resolved provenance but never re-mapped afterward —
  the coverage gap that let E2 through.
- **F1** — `test_settled_live_turns_project_once_when_native_ids_disjoint` cit:([`test_settled_live_turns_project_once_when_native_ids_disjoint`], mcp/tests/test_conversation_active_service.py:320-405) and
  `test_settled_live_turns_project_once_when_hosted_renumbers_turn_ids` cit:([`test_settled_live_turns_project_once_when_hosted_renumbers_turn_ids`], mcp/tests/test_conversation_active_service.py:407-456): after settling live turns, the native-tip re-walk must project
  each settled turn ONCE; on stashed `projector.py` they fail with the exact 4 / 2 `item-N` native
  twins and pass with `_drop_live_settled_natives`. `test_prior_session_native_history_survives_live_turns` cit:([`test_prior_session_native_history_survives_live_turns`], mcp/tests/test_conversation_active_service.py:458-478)
  proves genuine prior-session native history (both live sets empty at hydration) is untouched. These
  are the always-run (no opt-in) companions to the installed F1 real-wire regression in
  `test_conversation_control_installed.py`.

### Echo honesty and dormant release (R3 + R5)

`ClaudeEngineTests` gains `test_nonuser_transcript_entries_mint_no_echo_unknown_vendor_rows` cit:([`test_nonuser_transcript_entries_mint_no_echo_unknown_vendor_rows`], mcp/tests/test_conversation_active_service.py:591-660) (R3):
the echo poller now consumes only `role == "user"` transcript entries and advances past
assistant/result entries, so a mixed-role transcript no longer mints `claude:echo: unrecognized
submission echo shape` unknown-vendor rows. A new `DormantReleaseTests` adds
`test_release_dormant_state_frees_heavy_projection_and_retires_shell` cit:([`test_release_dormant_state_frees_heavy_projection_and_retires_shell`], mcp/tests/test_conversation_active_service_gaps.py:504-528) (R5): when the poll loop goes
idle the projector's `_release_dormant_state` clears the full heavy per-session state
(`ProjectionStore` items, the live-turn/request id maps, retention and pending frames) and
retires the shell, so a dead session's state frees immediately on the idle-break instead of lingering
as a registered tombstone until 32-LRU eviction.

### Sub-agent binding regressions

`ToolConvergenceTests` gains `test_reordered_task_started_tagging_never_regresses_a_terminal_phase` cit:([`test_reordered_task_started_tagging_never_regresses_a_terminal_phase`], mcp/tests/test_conversation_active_service_queues.py:104-177)
(fix-round review finding 9): reordered claude evidence — the Agent `tool_result`
settles the call BEFORE `task_started` binds the agent identity — keeps the terminal phase while
the agent ref still lands through the real claude mapper and store. The dormant-release assertions
follow the multiplexed sub-agent demux: `_live_turn_ids` / `_live_request_ids` are now per-thread
DICTS (keyed by thread id), so the freed-state assertions compare against `{}` instead of empty
sets.

### Conventions

Engine tests run on `IsolatedAsyncioTestCase` with injected reader callables — no socket, no
real IPC; the scripted bridge records calls so channel discipline (page sizes, cursors, epoch
parameters) is asserted too. Those callables reach the projector as one `BridgeReaders` bundle
beside the `ProjectedSession` that carries identity, authorization, entry, mapper, and secret, both
imported from the decomposed `projector.wiring` and `projector.facade` modules.

### Invariants And Boundaries

- Ordering assertions cover both sequence monotonicity and item-level turn order.
- Gap assertions always require exactly one typed gap with the exact reason and the close
  sentinel — never silent loss.
- Rehydration must reproduce items, revisions, and ordinals identically.
- A resolved user item re-mapped by a native frame must stay model-valid (H2), and a live-settled
  turn must project exactly once through the native re-walk (F1) — these regressions drive the real
  poll path and re-validate every emitted item, non-vacuous on stashed source.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the engine contract is
repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projector engine under test is now the `active/projector/` package. Its facade owns the poll loop, the gap classification (`generation-changed` vs `ordering-fault`, plus the consecutive-read-failure ceiling) and dormant release. | `ActiveSessionProjector` | mcp/src/agents_remember/serving/conversation/active/projector/facade.py:59-221 |
| Hydration (`ensure_hydrated` -> `_rebuild`), the fixed channel-poll order, and paging live in the rebuild coordinator. | `RebuildCoordinator` | mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:63-192 |
| The zipper faults under test — `ZipperEvidenceEvicted` and `EvidenceTimelineRegressed` — are raised by the native evidence walk. | `ZipperEvidenceEvicted`; `EvidenceTimelineRegressed`; `poll_evidence` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:37-38; mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:41-42; mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:114-144 |
| Retention, the retention-overflow gap on a full subscriber queue, and the gap envelope shape live in the mutation stream. | `ProjectionMutationStream`; `_publish`; `_gap_envelope` | mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py:49-197 |
| The store under test: idempotent apply, block union, delta buffering. | `ProjectionStore`; `apply_item`; `apply_delta` | mcp/src/agents_remember/serving/conversation/active/store.py:135-445 |
| The evidence/native/provenance page products the scripted bridge mimics. | `EvidencePage`; `NativeEvidencePage`; `SubmissionProvenanceBatch` | mcp/src/agents_remember/models/conversations/control_wire.py:281-284; mcp/src/agents_remember/models/conversations/evidence.py:105-113; mcp/src/agents_remember/models/conversations/evidence.py:127-134 |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Hydrate/Page Recovery And Bounded Release Delta

Active-service coverage now pins the updated hydrate/page/event recovery sequence and bounded release behavior. It verifies that a fresh page or a re-page after a dead stream remains server-cursor authoritative.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260727-CHATS-IM-L2 Current Delta

The behavior suite now addresses decomposed owners (`_echo`, `_coordinator`, `_native`, `_stream`)
and patches the subscriber bound in `mutation_stream`. Hydration, status, gap, twin suppression,
and dormant-release assertions remain behavior-identical, demonstrating that the refactor did not
change the public projector contract.

## Update History

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
