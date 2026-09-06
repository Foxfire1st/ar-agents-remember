# mcp/src/agents_remember/models/lifecycles/preparation_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/preparation_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:39:50+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Append-only preparation commands and selected private output state.

## Code Commentary

### Logic

The state selects exact intents and outputs in code, memory-content and ledger order. Command records retain original worker identity, bounded argv, start and succeeded/failed/unknown terminal observations. Later commands require successful predecessors; command starts and outputs cannot be rewritten into a retry. Current ownership is required for starts while an original terminal can remain retainable after cancellation. Private evidence cannot be combined with published mutation or approval claims. `SelectedPreparation._require_output_command` requires the retained original commit-command observation for a created output. `_validate_command_observation` separates terminal readback from command start: it retains the same command prefix and accepts only the original worker's terminal under the existing current/exited-owner rules.

### Conventions

Use the named source owners directly. The source is present in the landed IAS baseline. This preparation pass updates its description; final memory and ledger proof remains pending.

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
| `OperationPreparationState` owns the corresponding behavior described above. | `OperationPreparationState` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:111-129` |
| `validate_preparation_owner` owns the corresponding behavior described above. | `validate_preparation_owner` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:132-146` |
| `validate_preparation_transition` owns the corresponding behavior described above. | `validate_preparation_transition` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:149-175` |
| `_validate_leg_transition` owns the corresponding behavior described above. | `_validate_leg_transition` | `mcp/src/agents_remember/models/lifecycles/preparation_state.py:178-202` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

- 2026-09-06T21:39:50+00:00 — Reconciled the landed validation/helper extraction against IAS d3610903; retained ownership and refusal semantics and refreshed same-file evidence ranges. Verification stamps and final acceptance were not advanced.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
