# mcp/src/agents_remember/serving/hosted_control_projection.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Projects adapter snapshots into additive terminal catalog fields and converts protocol activity
to the serving turn-state vocabulary. The turn-state projection delegates
to the canonical conversation status authority, so orchestration and Chats serving consume one
classification of adapter evidence. The snapshot projection also
carries the multiplexed sub-agent pendings end-to-end into the catalog row.

## Code Commentary

### Logic

Snapshot projection preserves existing catalog schema members while adding control state,
activity, acceptance, vendor identity, pending interaction, sequence, and raw vendor detail.
cit:([`control_snapshot_entry`], mcp/src/agents_remember/serving/hosted_control_projection.py:36-58) also projects cit:([`control_pending_interactions`], mcp/src/agents_remember/serving/hosted_control_projection.py:50-55): every entry of the snapshot's plural `pending_interactions` tuple
is serialized through the same `pending_interaction_json` wire shape and stored as a list —
purely additive, so the singular `control_pending_interaction` slot stays the parent-thread
entry exactly as before, and an empty tuple serializes as `None` (no claim) rather than `[]`.
Legacy raw-TUI harness rows are explicitly marked unsupported. cit:([`snapshot_turn_state`], mcp/src/agents_remember/serving/hosted_control_projection.py:86-112)
now delegates to `snapshot_seat_turn_state` in the canonical status authority with an optional
harness parameter: the same canonical classification the Chats serving consumes produces the
turn state, and the single seat projection rule translates it — parity with the pre-canonical
activity/control mapping is exact and pinned over the full control×activity product. The
canonical import is function-local with the cycle documented: `terminal_liveness` imports this
module, and the conversation package `__init__` imports the runtime that imports
`terminal_liveness`, so a module-level import would close that cycle (worker round-2 issue 4).
The public signature is backward-compatible; since 260713-TES-L2 it additionally accepts an
optional `terminal` observation that `terminal_liveness._observe_alive` forwards from the
evidence lift.

## 260713-TES-L2 Current Delta — Terminal Precedence

`snapshot_turn_state` cit:([`snapshot_turn_state`], mcp/src/agents_remember/serving/hosted_control_projection.py:79-104) gained `terminal: TurnTerminalEvidence | None = None` and
forwards it into `snapshot_seat_turn_state`, so the lifted per-vendor settlement takes the same
canonical precedence the status service applies: an interrupted/failed settlement is never
re-read as a clean end, and `done ≠ interrupted` at seat granularity.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

### Conventions

Projection is evidence storage, not delivery or consumption. Orchestration never re-derives
seat state from adapter fields; the canonical authority is the only classification.

### Invariants And Boundaries

- `paneDiagnostic` remains diagnostic detail and cannot authorize readiness, delivery, or
  agent-notifier action.
- Neither orchestration nor Chats derives state from rendered events or PTY output.
- The delegated mapping must keep exact parity with the pre-canonical seat vocabulary; any
  vocabulary change belongs to the canonical authority, not a local mapping.
- The function-local import cycle documentation must stay with the delegation.
- The plural pending projection is additive only: the singular
  `control_pending_interaction` slot remains the parent-thread entry and must not be fed from
  the agent tuple; consumers that do not understand the multiplexed form see exactly the pre-multiplexing
  row shape (empty tuple → `None`, never `[]`).
- Projection construction and persistence are separable: `control_snapshot_entry` and
  `legacy_control_unsupported_entry` are pure row builders, and persistence happens only through
  the guarded wrappers (`project_control_snapshot`, `mark_legacy_control_unsupported`) or through
  the caller's own single `upsert`. A live-observation path must build the FINAL row (snapshot
  projection plus `paneDiagnostic`) before its one write, so no intermediate projection variant
  is persisted and later overwritten.

### Todos

None.

## Evidence

### Docs References

No relevant external/domain documentation was configured; catalog and projection tests are authoritative.

No configured domain documentation was available.

### Repo-Internal References

The canonical status authority classifies adapter evidence once for every consumer; the catalog
owns the persisted additive fields the projection writes, including the multiplexed plural pendings; the
snapshot grammar defines the multiplexed tuple this module serializes.

- The canonical status authority this module now delegates to (classification plus single seat projection rule). [1]

| `terminal_catalog.py` owns persisted additive fields and the `SeatTurnState` vocabulary. | `SeatTurnState` | mcp/src/agents_remember/models/terminal_catalog.py:32-32 |
| The catalog field this projection fills: `control_pending_interactions` persisted additively and serialized as `controlPendingInteractions`. | `control_snapshot_entry` | mcp/src/agents_remember/serving/hosted_control_projection.py:36-58 |
| The pure raw-TUI unsupported projection the liveness sweep composes before its one final upsert; the persistence wrapper delegates to it. | `legacy_control_unsupported_entry`; `mark_legacy_control_unsupported` | mcp/src/agents_remember/serving/hosted_control_projection.py:72-83; mcp/src/agents_remember/serving/hosted_control_projection.py:61-69 |
| `AdapterSnapshot.pending_interactions` is the multiplexed sub-agent pending tuple this module serializes end-to-end; the singular slot stays the parent-thread entry (D3). | `AdapterSnapshot`, `pending_interaction_json` | mcp/src/agents_remember/models/conversations/control_wire.py:126-151; mcp/src/agents_remember/models/conversations/control_wire.py:305-316 |

### Cross-Repo References

No meaningful cross-repo references.

No meaningful cross-repo references found.

## Canonical Turn-Status Delegation Delta

Hosted control projection now consumes the canonical conversation turn-status authority rather than maintaining a divergent local interpretation. This keeps dashboard and orchestration-facing status vocabulary aligned.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260831-LOCR-L22 Current Delta — Pure Legacy Projection Before One Final Upsert

`legacy_control_unsupported_entry` (cit:([`legacy_control_unsupported_entry`], mcp/src/agents_remember/serving/hosted_control_projection.py:72-83))
returns the raw-TUI unsupported projection without persisting it; `mark_legacy_control_unsupported`
(cit:([`mark_legacy_control_unsupported`], mcp/src/agents_remember/serving/hosted_control_projection.py:61-69))
retains its public persistence behavior — it delegates, then upserts only when the projection
actually differs from the row. The liveness sweep's alive path now composes the FINAL row
(unsupported projection plus `paneDiagnostic`, or `control_snapshot_entry` plus `paneDiagnostic`)
and issues exactly one `catalog.upsert`, so an intermediate hosted snapshot or unsupported row is
never written and then replaced in the same observation. Equal-row upserts no longer dirty the
caller's catalog batch, which is what makes a repeated clean sweep a zero-replacement sweep.

Observed while reconciling: after this change `project_control_snapshot` and
`mark_legacy_control_unsupported` have no in-tree caller — only their definitions match. They remain
public wrappers of the pure builders; removing or repurposing them is not authorized by this leaf
and would need its own ruling. `control_snapshot_entry` remains a live consumer surface through
`hosted_readiness.py`. The `paneDiagnostic`-is-diagnostic-only invariant is unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
