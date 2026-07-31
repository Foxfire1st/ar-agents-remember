# mcp/src/agents_remember/serving/conversation/active/status.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/status.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The canonical conversation status authority (leaf R3): the one revisioned mapping from
`AdapterSnapshot` evidence to the canonical `ConversationStatus` vocabulary, consumed
identically by the Chats serving routes (through the active projector) and by orchestration
(through `hosted_control_projection.snapshot_turn_state`). Neither consumer maps adapter
evidence on its own, and neither derives state from rendered events, PTY output, or the last
timeline mutation.

## Code Commentary

### Logic

`classify_process` (L101-L110) maps adapter control state to the canonical process vocabulary
(connected/starting/disconnected/failed). `classify_turn` (L103-L140) maps activity/raw
evidence to one canonical turn evidence value: pending interaction (exact, carrying the
interaction id), blocked-without-interaction (`declared-external-wait`), running
(`active-native-turn`, codex-only turn id from raw, L193-L200), settling (per-harness raw keys —
claude `claudeStatus`/`retryAttempt`, pi `isCompacting`/`auto_retry_start`, L203-L234), and
idle+ready (`settled-dispatchable`); unusable evidence returns `None` so callers retain their
last known turn state. `snapshot_seat_turn_state` (L205-L223) is the single orchestration seat
projection: `seat_turn_state_for` (L165-L202) reproduces the pre-canonical mapping exactly
(live turn states → `working`, wait states → `awaiting-input`, settled-with-connected →
`turn-ended`, else `stale`), pinned over the full control×activity product.
`ConversationStatusService` (L252-L447) folds observations into the revisioned envelope per
exact identity: `_apply` (L324-L365) prefers observed terminal settlements (exact strength,
interrupted/failed map directly, completed settles) over activity classification, preserves a
completed outcome across the settling → ready transition (L348-L354), and `_set_turn`
(L350-L379) advances state only on semantic change. The revision (L283-L300) advances only on
semantic transitions — turn/process/stale changes; freshness timestamps are derived metadata
recomputed per observation under the same revision (`_envelope` L437-L465), never a mutation
trigger. Staleness is one liveness-sweep cadence plus slack (`STALE_AFTER_MS` L46), and the
observation bound is honestly `poll` (`OBSERVATION_BOUND`, L59-L60).

### Conventions

Evidence-first classification: unknown evidence never becomes `ready` (enforced by the contract
model), and a session without usable turn evidence keeps its last known turn state while
process/freshness evidence advances honestly. Terminal outcomes feed the canonical machine from
native evidence only.

### Invariants And Boundaries

- This module is the ONLY classification of adapter evidence into the canonical vocabulary;
  consumers never re-map `AdapterSnapshot` fields.
- Revision never advances for polling cadence or timestamps — equal-revision envelopes are
  semantically identical.
- Orchestration parity is exact by construction: the seat projection consumes the same
  classification, never a parallel mapping.
- The orchestration entry point stays signature-compatible (`snapshot_turn_state` delegates with
  an optional harness parameter); `terminal_liveness.py` is untouched.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The canonical vocabulary and
revision rules are the repository-owned strict wire contract cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this authority. | — | — |

## Repo-Internal References

The canonical evidence→state map and status envelope models live in the parent contract module;
orchestration consumes this authority through the one delegated projection; the projector feeds
it observations and terminal settlements.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CANONICAL_TURN_STATE_BY_EVIDENCE` fixes the evidence-to-turn-state vocabulary this service classifies into. | L429-L439 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| `ConversationStatus` and its freshness/process/turn products define the revisioned envelope shape. | L514-L571 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Orchestration's `snapshot_turn_state` delegates here with a documented function-local import; signature unchanged. | L71-L91 | [hosted_control_projection.py](agents-remember/mcp/src/agents_remember/serving/hosted_control_projection.py) |
| The projector observes snapshots and pending terminal settlements through this service per poll. | L84; L129-L144 | [projector/rebuild_coordinator.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py) |
| `SeatTurnState` is the orchestration vocabulary the single projection rule emits. | L38 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No cross-repository implementation participates in this status authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Status freshness now reflects evidence-expected active states rather than making a quiet, ready conversation look stale. Fresh active pages and events retain their canonical turn state and cursor semantics while genuine working or settlement evidence can still surface staleness.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

**`TurnTransition`** (`state`, `strength`, `turn_id`, `reason`, `waiting`, `terminal_outcome`) is
now the single argument of the internal `_set_turn(transition, *, now)`: **one proposed turn-state
change, and the evidence strength that justifies it**. The state, its turn, what it is waiting on
and how it ended are one observation; the strength is what decides whether this observation may
overwrite the last one. Deciding them separately is how a weak observation overwrites a strong one.
The precedence rules themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations in Logic, all
  read back. `classify_process` L91-L100 → L101-L110; `snapshot_seat_turn_state` L178-L190 → its
  full body L205-L223, and `seat_turn_state_for` in the same sentence L155-L175 → L165-L202 (the
  cited span stopped before the `starting`/no-prior-claim rule the sentence describes). The
  observation bound was cited at L49, which is now the `EVIDENCE_EXPECTED_TURN_STATES` frozenset;
  `OBSERVATION_BOUND = "poll"` is L59-L60. `STALE_AFTER_MS` L46 was verified still correct. NOT
  fixed (beyond this worklist): the same paragraph's remaining anchors also drifted —
  `classify_turn` L103-L140 → L113-L150, the codex turn id L193-L200 → `_active_turn_id` L226-L237,
  settling raw keys L203-L234 → `_classify_settling` L240-L271, `ConversationStatusService`
  L252-L447 → L306-L508, `_apply` L324-L365 → L361-L412, the completed-outcome carry L348-L354 →
  L390-L397, `_set_turn` L350-L379 → L414-L434, the revision advance L283-L300 → L346-L354 inside
  `observe`, and `_envelope` L437-L465 → L480-L508.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose target
  file no longer exists. `serving/conversation/active/projector.py` was split into the
  `active/projector/` package; the per-poll observation the row names now lives in
  `projector/rebuild_coordinator.py` — the coordinator constructs `ConversationStatusService` at L84
  and `poll_once` calls `self._status.observe(snapshot, harness_id, terminal=self._stream.consume_terminal())`
  at L129-L144. Repointed both the link path and the range; no claim text changed.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `TurnTransition` as the one proposed change plus the strength that justifies it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the canonical
  status authority — the one evidence classification, revisioned envelope, single seat
  projection, terminal-outcome handling. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
