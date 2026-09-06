# mcp/src/agents_remember/models/lifecycles/preparation_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/preparation_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Append-only preparation commands and selected private output state.

## Code Commentary

### Logic

The state selects exact intents and outputs in code, memory-content and ledger order. Command records retain original worker identity, bounded argv, start and succeeded/failed/unknown terminal observations. Later commands require successful predecessors; command starts and outputs cannot be rewritten into a retry. Current ownership is required for starts while an original terminal can remain retainable after cancellation. Private evidence cannot be combined with published mutation or approval claims.

### Conventions

Use the named source owners directly. This card describes the current uncommitted implementation; commit-based verification remains pending.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `PreparationCommandTerminal` owns the corresponding behavior described above. | `PreparationCommandTerminal` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:21-39` |
| `PreparationCommand` owns the corresponding behavior described above. | `PreparationCommand` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:42-74` |
| `OperationPreparationState` owns the corresponding behavior described above. | `OperationPreparationState` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:107-125` |
| `validate_preparation_owner` owns the corresponding behavior described above. | `validate_preparation_owner` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:128-142` |
| `validate_preparation_transition` owns the corresponding behavior described above. | `validate_preparation_transition` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:145-171` |
| `_validate_leg_transition` owns the corresponding behavior described above. | `_validate_leg_transition` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:174-210` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
