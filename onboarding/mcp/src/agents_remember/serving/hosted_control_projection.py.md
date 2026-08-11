# mcp/src/agents_remember/serving/hosted_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T01:21+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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
cit:([`control_snapshot_entry`], mcp/src/agents_remember/serving/hosted_control_projection.py:35-57) also projects cit:([`control_pending_interactions`], mcp/src/agents_remember/serving/hosted_control_projection.py:47-54): every entry of the snapshot's plural `pending_interactions` tuple
is serialized through the same `pending_interaction_json` wire shape and stored as a list —
purely additive, so the singular `control_pending_interaction` slot stays the parent-thread
entry exactly as before, and an empty tuple serializes as `None` (no claim) rather than `[]`.
Legacy raw-TUI harness rows are explicitly marked unsupported. cit:([`snapshot_turn_state`], mcp/src/agents_remember/serving/hosted_control_projection.py:78-101)
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

### Todos

None.

## Docs References

No relevant external/domain documentation was configured; catalog and projection tests are authoritative.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The canonical status authority classifies adapter evidence once for every consumer; the catalog
owns the persisted additive fields the projection writes, including the multiplexed plural pendings; the
snapshot grammar defines the multiplexed tuple this module serializes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical status authority this module now delegates to (classification plus single seat projection rule). | `snapshot_seat_turn_state` | mcp/src/agents_remember/serving/conversation/active/status.py:205-223 |
| The full-product parity suite pinning the delegated mapping against the pre-canonical one. | `test_projection_across_control_activity_product` | mcp/tests/test_conversation_active_status.py:188-200 |
| `terminal_catalog.py` owns persisted additive fields and the `SeatTurnState` vocabulary. | `SeatTurnState` | mcp/src/agents_remember/models/terminal_catalog.py:32-32 |
| The catalog field this projection fills: `control_pending_interactions` persisted additively and serialized as `controlPendingInteractions`. | `control_snapshot_entry` | mcp/src/agents_remember/serving/hosted_control_projection.py:35-57 |
| `AdapterSnapshot.pending_interactions` is the multiplexed sub-agent pending tuple this module serializes end-to-end; the singular slot stays the parent-thread entry (D3). | `AdapterSnapshot`, `pending_interaction_json` | mcp/src/agents_remember/models/conversations/control_wire.py:126-151; mcp/src/agents_remember/models/conversations/control_wire.py:305-316 |

## Cross-Repo References

No meaningful cross-repo references.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Canonical Turn-Status Delegation Delta

Hosted control projection now consumes the canonical conversation turn-status authority rather than maintaining a divergent local interpretation. This keeps dashboard and orchestration-facing status vocabulary aligned.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the forwarded `terminal` parameter
  and terminal precedence in `snapshot_turn_state` (and superseded the "terminal_liveness
  untouched" claim). Verification metadata pinned until closeout stamps the 260713-TES-L2
  commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 9 citations (citation_anchor_missing=4, citation_prose_not_in_cit_form=1, citation_source_malformed=4); final scoped citation check clean.
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
  cit:([`control_snapshot_entry`], mcp/src/agents_remember/serving/hosted_control_projection.py:35-57), while the singular slot stays the parent-thread entry exactly as before and an
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
