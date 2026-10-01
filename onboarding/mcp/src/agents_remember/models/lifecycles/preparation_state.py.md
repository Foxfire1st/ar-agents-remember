# mcp/src/agents_remember/models/lifecycles/preparation_state.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Append-only preparation commands and selected private output state.

## Code Commentary

### Logic

Selected preparations form an ordered prefix of at most two legs: code, then memory
content. A later leg still requires the prior selected output, and command evidence remains
append-only. Code retention does not manufacture memory output; a successor prepares memory
through its own owner. There is no selected ledger leg.

The state selects exact intents and outputs in code and memory-content order. Command records retain original worker identity, bounded argv, start and succeeded/failed/unknown terminal observations. Later commands require successful predecessors; command starts and outputs cannot be rewritten into a retry. Current ownership is required for starts while an original terminal can remain retainable after cancellation. Private evidence cannot be combined with published mutation or approval claims. `SelectedPreparation._require_output_command` requires the retained original commit-command observation for a created output. `_validate_command_observation` separates terminal readback from command start: it retains the same command prefix and accepts only the original worker's terminal under the existing current/exited-owner rules.

### Conventions

Use the named source owners directly. The source is present in the landed IAS baseline. This preparation pass updates its description; review of an uncommitted candidate does not establish final publication proof.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- Selection is an ordered prefix of at most two preparations: code followed by memory content. [1]
- `PreparationCommandTerminal` owns the corresponding behavior described above. [2]
- `PreparationCommand` owns the corresponding behavior described above. [3]
- `OperationPreparationState` owns the corresponding behavior described above. [4]
- `validate_preparation_owner` owns the corresponding behavior described above. [5]
- `validate_preparation_transition` owns the corresponding behavior described above. [6]
- `_validate_leg_transition` owns the corresponding behavior described above. [7]

### Cross-Repo References

No cross-repository source is needed for this card.
