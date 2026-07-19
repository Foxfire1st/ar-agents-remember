# mcp/src/agents_remember/serving/hosted_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2` |
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Projects adapter snapshots into additive terminal catalog fields and converts protocol activity
to the serving turn-state vocabulary. Since 260718-CHATS-L1 the turn-state projection delegates
to the canonical conversation status authority, so orchestration and Chats serving consume one
classification of adapter evidence (leaf R3).

## Code Commentary

### Logic

Snapshot projection preserves existing catalog schema members while adding control state,
activity, acceptance, vendor identity, pending interaction, sequence, and raw vendor detail.
Legacy raw-TUI harness rows are explicitly marked unsupported. `snapshot_turn_state` (L70-L90)
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

### Todos

None.

## Docs References

No relevant external/domain documentation was configured; catalog and projection tests are authoritative.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The canonical status authority this module now delegates to (classification plus single seat projection rule). | L155-L190 | [status.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/status.py) |
| The full-product parity suite pinning the delegated mapping against the pre-canonical one. | L159-L216 | [test_conversation_active_status.py](agents-remember/mcp/tests/test_conversation_active_status.py) |
| `terminal_catalog.py` owns persisted additive fields and the `SeatTurnState` vocabulary. | L38 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No meaningful cross-repo references.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the R3 orchestration migration —
  `snapshot_turn_state` delegates to the canonical status authority with an optional harness
  parameter and a documented function-local import; the legacy inline activity/control mapping
  is gone, parity is test-pinned, `terminal_liveness.py` untouched. Verification hash stays
  pinned at the last commit that touched the source until closeout stamps the candidate commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented additive adapter projection, legacy unsupported
  labeling, and protocol-derived turn state.
