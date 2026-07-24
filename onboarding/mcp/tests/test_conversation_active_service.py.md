# mcp/tests/test_conversation_active_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Projector-engine and store tests for 260718-CHATS-L1 (R2/R4): hydration, ordering, idempotence,
provenance resolution, rehydration, and the review-fix gap mechanics — driven through a scripted
in-memory bridge seam, plus the review-F1 tool-convergence proofs through the real mappers and
store.

## Code Commentary

### Logic

A `_ScriptedBridge` (L65-L218) plays scripted evidence/native/transcript/provenance/snapshot
answers through the projector's injected reader seams. `CodexEngineTests` (L221-L335): hydration
from native pages plus the live window with stable identity and ordinals; live polling appends
in order; idempotent re-feeds mint no duplicates; provenance resolves through the batch;
ephemeral-thread native refusal stays honestly partial; rehydration reproduces the identical
projection with a new generation. `ClaudeEngineTests` (L336-L441): the echo zipper merges
submission echoes and frames in exact turn order (echo first, result in a later poll, multiple
turns) with no duplicate or inverted items. `PiEngineTests` (L442-L487): eager native
continuation anchors live items to durable-entry identity and live tool upserts converge.
`StoreTests` (L488-L508): identical upsert replays are no-ops. `ToolConvergenceTests`
(L509-L692, review finding F1): claude `tool_use` → `tool_result`, pi live start → update →
end (including the result-less update as a true no-op), and pi entry call → `toolResult` all
converge to items carrying BOTH input and output blocks with completed phase; codex full-item
re-maps are byte-identical under the block union. `OverflowGapTests` (L693-L740, review finding
F2): with a clamped undrained subscriber queue the consumer receives exactly one
`retention-overflow` gap (requiresRepage + closeAfterEvent) then the close sentinel, and the
retention sequence set is contiguous with no hole. `ZipperEvictionGapTests` (L741-L820, review
finding F3): an advancing eviction floor raises `ZipperEvidenceEvicted` for the echo-zipper
projector (mapped to one ordering-fault gap), does NOT gap the codex projector (totals clear
honestly), and a fresh claude projector rehydrates from the remaining window without raising.

### 260718-CHATS-L5 additions (H2 + F1 projector-tier regressions)

Two proven-failure families extend `CodexEngineTests`, both driving the REAL L1 poll path and
re-validating every emitted item — the surface the intermittent active-page 500 and the native
twins actually reach:

- **H2** — `test_native_remap_after_resolution_stays_model_valid`: a resolved user item re-mapped by
  a native frame must stay model-valid; before the store's `_preserved_input_authority` pin this
  raised the exact E2 `ValidationError: unknown-input cannot claim exact or correlated provenance`
  when `UpsertItemMutation` re-validated the split authority triple. The pre-existing
  `test_provenance_resolution_exact_then_unknown` resolved provenance but never re-mapped afterward —
  the coverage gap that let E2 through.
- **F1** — `test_settled_live_turns_project_once_when_native_ids_disjoint` and
  `…_when_hosted_renumbers_turn_ids`: after settling live turns, the native-tip re-walk must project
  each settled turn ONCE; on stashed `projector.py` they fail with the exact 4 / 2 `item-N` native
  twins and pass with `_drop_live_settled_natives`. `test_prior_session_native_history_survives_live_turns`
  proves genuine prior-session native history (both live sets empty at hydration) is untouched. These
  are the always-run (no opt-in) companions to the installed F1 real-wire regression in
  `test_conversation_control_installed.py`.

### 260718-CHATS-L5F additions (R3 echo honesty + R5 dormant release)

`ClaudeEngineTests` gains `test_nonuser_transcript_entries_mint_no_echo_unknown_vendor_rows` (R3):
the echo poller now consumes only `role == "user"` transcript entries and advances past
assistant/result entries, so a mixed-role transcript no longer mints `claude:echo: unrecognized
submission echo shape` unknown-vendor rows. A new `DormantReleaseTests` adds
`test_release_dormant_state_frees_heavy_projection_and_retires_shell` (R5): when the poll loop goes
idle the projector's `_release_dormant_state` clears the full heavy per-session state
(`ProjectionStore` items, the L5 live-turn/request id sets, retention and pending frames) and
retires the shell, so a dead session's state frees immediately on the idle-break instead of lingering
as a registered tombstone until 32-LRU eviction.

### Conventions

Engine tests run on `IsolatedAsyncioTestCase` with injected reader callables — no socket, no
real IPC; the scripted bridge records calls so channel discipline (page sizes, cursors, epoch
parameters) is asserted too.

### Invariants And Boundaries

- Ordering assertions cover both sequence monotonicity and item-level turn order.
- Gap assertions always require exactly one typed gap with the exact reason and the close
  sentinel — never silent loss.
- Rehydration must reproduce items, revisions, and ordinals identically.
- A resolved user item re-mapped by a native frame must stay model-valid (H2), and a live-settled
  turn must project exactly once through the native re-walk (F1) — the L5 regressions drive the real
  poll path and re-validate every emitted item, non-vacuous on stashed source.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the engine contract is
repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The projector engine under test: hydration, poll channels, zipper, retention, gap mechanics. | L134-L791 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The store under test: idempotent apply, block union, delta buffering. | L101-L319 | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| The evidence/native/provenance page products the scripted bridge mimics. | L320-L380 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Active-service coverage now pins the updated hydrate/page/event recovery sequence and bounded release behavior. It verifies that a fresh page or a re-page after a dead stream remains server-cursor authoritative.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

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
