# mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Canonical lifecycle selection for private preparation evidence and explicit predecessor-history proof.

## Code Commentary

### Logic

`_require_preparation_certificates` checks four exact original code certificates for every intent and the selected fifth certificate for memory legs. These requirements apply to admitted private closeout preparation; they do not impose a gate prerequisite on interactive memory-quality preparation.

This owner loads exact content-addressed intent/output objects, binds operation/generation and original selected certificate predecessors, and applies single journal compare-and-swap transitions. Command start is selected before launch. Output selection checks the original raw commit relationship. Logical refs are independently observed; private commands and objects do not consume approval or prove published commits.

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
- `select_preparation_intent` owns the corresponding behavior described above. [3]
- `_require_intent_owner` owns the corresponding behavior described above. [4]
- `_last` owns the corresponding behavior described above. [5]
- `_replace_last` owns the corresponding behavior described above. [6]
- `_select` owns the corresponding behavior described above. [7]

### Cross-Repo References

No cross-repository source is needed for this card.
