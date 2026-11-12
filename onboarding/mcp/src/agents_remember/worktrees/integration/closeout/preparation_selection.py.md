# mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Read-only reopening of exactly selected preparation intents and outputs, logical-reference observation, and bounded explicit predecessor-history proof. This module selects no new preparation and publishes no successor wrapper.

## Code Commentary

### Logic

`selected_preparation_intents` reopens exact selected intent/output objects, checks operation ownership and matching output, and requires three retained command records for a write-enabled selected output. New-intent certificate checking, command selection and successor code rebinding are absent; no four-certificate successor-prefix check is performed by this remaining reader.

This owner reopens selected originals and independently proves logical roots/refs. `require_preparation_logical_refs` compares canonical existing roots, repository identity, symbolic HEAD, HEAD commit and the exact logical branch tip with the retained intent. `_require_intent_owner` checks operation kind/key/generation, contract path, frozen run, candidate authorities and the exact code or memory logical root. `retain_prepared_code_for_successor` and its raw-output, prefix and rebound-wrapper helpers were removed, not moved to a new publisher here. The surviving readers start no preparation command, publish no object and perform no journal CAS.

`selected_prepared_code_history_commits` walks only the selected code preparation and its explicit certification predecessors. It revalidates each selected intent/output, logical-reference binding, candidate-tree match, and predecessor generation/fingerprint link, then returns unique prepared code commits as retained provenance anchors. It never searches unrelated Git history or substitutes a prepared tree for the current candidate.

### Conventions

Use the named source owners directly. The implementation is present in landed IAS; this preparation pass does not advance verification stamps.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- `selected_preparation_intents` owns the corresponding behavior described above. [1]
- `selected_prepared_code_history_commits` validates selected code and explicit predecessor history. [2]

- `_require_intent_owner` owns the corresponding behavior described above. [4]


### Cross-Repo References

No cross-repository source is needed for this card.
