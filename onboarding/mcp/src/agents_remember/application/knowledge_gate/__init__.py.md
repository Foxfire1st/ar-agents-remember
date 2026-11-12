# mcp/src/agents_remember/application/knowledge_gate/__init__.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The package of the mandatory invariant closeout gate (MIK-R09@v2, leaf 260928-MIK-L09).** D5: "Invariant work is
MANDATORY! Never just reporting." No route that commits a leaf's memory commits while an item of the leaf's
**recomputed** worklist (MIK-R08) lacks a current satisfying row in its history file (MIK-R07), while the worklist run
is `incomplete`, or while the validator (MIK-R22) fails; a master lands only when no entry at a path it changed is
stale (MIK-R03). The package docstring names the six modules and where each route calls the gate; the module
re-exports the public surface.

## Code Commentary

### Logic

- The package map, in the docstring:
  - [`predicates`](predicates.py.md): each registered kind's own satisfying rule over a stored item, and the
    currentness of invariant and family rows (rule 2);
  - [`gate`](gate.py.md): one leaf's recompute over the exact candidate, the findings and the refusal;
  - [`memo`](memo.py.md): the bounded memo of verdicts, keyed by the exact trees, contract, parent tip, task document
    and build;
  - [`direct`](direct.py.md): the gate at direct landing, the branch-addressed leaf closeout;
  - [`landing`](landing.py.md): master and checkpoint landing (rule 4) and record landing (rule 3);
  - [`adapter`](adapter.py.md): the worktree layer's `KnowledgeGatePort`.
- Where each route calls it (docstring): the curator's memory-quality run counts the findings toward
  `curatorActionableCount` (`application/memory_quality/controller.py`); the closeout validator refuses
  (`worktrees/integration/closeout/curator_coherence.py`); the closeout and direct-landing memory commits close the
  leaf's history file and validate their exact tree; record, master and checkpoint landing refuse through the port.
- Re-exports: `KnowledgeGate`; `GATE_CHECK`, `GateFinding`, `GateResult`, `GateTrees`, `evaluate_leaf_gate`, `judge`,
  `recompute_for_gate`; `GATE_PREDICATES`, `GateContext`, `item_open_reason`, `register_gate_predicate`. Importing
  the package imports `predicates`, which registers every kind's predicate.

### Conventions

- The package ranks in `application/`, above the worktree layer, which reaches it only through
  `worktrees.services.KnowledgeGatePort` (bound in `application/worktree_services.py`). No sub-route overview exists,
  following the `knowledge_worklist/`, `knowledge_currentness/` and `knowledge_reader/` precedent; every module is
  governed by the application overview.

### Invariants And Boundaries

- **Inert until the cutover.** Every gate path runs only on converted memory (the layout marker on K_B or K_C,
  MIK-R09 rule 6). On unconverted memory, which is all production memory before MIK-R37, closeout, landing and sync
  behave exactly as on base: the leaf's `unconverted.sh` evidence compares the base build with this build on the real
  unconverted memory and finds them identical apart from the build label.
- MIK-R09 rule 6's second bullet (refuse unconverted trees at the routes, naming the crossing sync) is **not** built
  here; it is carried to L37 (ruling 2026-09-30T14:38:47, gap 1).

### Todos

- None of its own. The carried L37 items are on the [`gate`](gate.py.md) card.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R09@v2` of task
`260928_maintained-invariant-knowledge` and the leaf document `09_mandatory-invariant-closeout-gate.json`; they live
outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The package docstring: the rule, the six modules and where each route calls the gate. [1]
- The public surface. [2]

### Cross-Repo References

No meaningful cross-repo references found: the package reads the leaf's code and memory repositories through Git.

No cross-repo boundary is crossed by this file.
