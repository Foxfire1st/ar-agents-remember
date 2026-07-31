# mcp/src/agents_remember/serving/hosted_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

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
`control_snapshot_entry` (L35-L57) also projects `control_pending_interactions` (L47-L54): every entry of the snapshot's plural `pending_interactions` tuple
is serialized through the same `pending_interaction_json` wire shape and stored as a list —
purely additive, so the singular `control_pending_interaction` slot stays the parent-thread
entry exactly as before, and an empty tuple serializes as `None` (no claim) rather than `[]`.
Legacy raw-TUI harness rows are explicitly marked unsupported. `snapshot_turn_state` (L78-L101)
now delegates to `snapshot_seat_turn_state` in the canonical status authority with an optional
harness parameter: the same canonical classification the Chats serving consumes produces the
turn state, and the single seat projection rule translates it — parity with the pre-canonical
activity/control mapping is exact and pinned over the full control×activity product. The
canonical import is function-local with the cycle documented: `terminal_liveness` imports this
module, and the conversation package `__init__` imports the runtime that imports
`terminal_liveness`, so a module-level import would close that cycle (worker round-2 issue 4).
The public signature is backward-compatible and `terminal_liveness.py` is untouched.

### Conventions

Projection is evidence storage, not delivery or consumption. Orchestration never re-derives
seat state from adapter fields; the canonical authority is the only classification.

### Invariants And Boundaries

- `paneDiagnostic` remains diagnostic detail and cannot authorize readiness, delivery, or
  supervisor action.
- Neither orchestration nor Chats derives state from rendered events or PTY output.
- The delegated mapping must keep exact parity with the pre-canonical seat vocabulary; any
  vocabulary change belongs to the canonical authority, not a local mapping.
- The function-local import cycle documentation must stay with the delegation.
- The plural pending projection is additive only: the singular
  `control_pending_interaction` slot remains the parent-thread entry and must not be fed from
  the agent tuple; consumers that do not understand the multiplexed form see exactly the pre-multiplexing
  row shape (empty tuple → `None`, never `[]`).

### Todos

None.

## Docs References

No relevant external/domain documentation was configured; catalog and projection tests are authoritative.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The canonical status authority classifies adapter evidence once for every consumer; the catalog
owns the persisted additive fields the projection writes, including the multiplexed plural pendings; the
snapshot grammar defines the multiplexed tuple this module serializes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The canonical status authority this module now delegates to (classification plus single seat projection rule). | L205-L224 | [status.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/status.py) |
| The full-product parity suite pinning the delegated mapping against the pre-canonical one. | L168-L250 | [test_conversation_active_status.py](agents-remember/mcp/tests/test_conversation_active_status.py) |
| `terminal_catalog.py` owns persisted additive fields and the `SeatTurnState` vocabulary. | L38 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The catalog field this projection fills: `control_pending_interactions` persisted additively and serialized as `controlPendingInteractions`. | L121; L271 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| `AdapterSnapshot.pending_interactions` is the multiplexed sub-agent pending tuple this module serializes end-to-end; the singular slot stays the parent-thread entry (D3). | L224-L231 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Canonical Turn-Status Delegation Delta

Hosted control projection now consumes the canonical conversation turn-status authority rather than maintaining a divergent local interpretation. This keeps dashboard and orchestration-facing status vocabulary aligned.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/hosted_control_projection.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 2 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `terminal_catalog.py`, `test_conversation_active_status.py`; those
  ranges shifted because this task edited those files, so treat the cited numbers as approximate
  and the linked cards as authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: recorded the multiplexed sub-agent pendings
  projection (review R6): `control_snapshot_entry` now serializes every entry of the snapshot's
  plural `pending_interactions` into the additive `control_pending_interactions` catalog field
  (L47-L53), while the singular slot stays the parent-thread entry exactly as before and an
  empty tuple serializes as `None`. Refreshed stale line citations (`snapshot_turn_state`
  L77-L100, status authority L205-L224, parity suite L168-L258) and added the
  catalog-field and snapshot-grammar reference rows. Verification metadata stays pinned — the
  L7 change is uncommitted, so no commit hash can attest it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the R3 orchestration migration —
  `snapshot_turn_state` delegates to the canonical status authority with an optional harness
  parameter and a documented function-local import; the legacy inline activity/control mapping
  is gone, parity is test-pinned, `terminal_liveness.py` untouched. Verification hash stays
  pinned at the last commit that touched the source until closeout stamps the candidate commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented additive adapter projection, legacy unsupported
  labeling, and protocol-derived turn state.
