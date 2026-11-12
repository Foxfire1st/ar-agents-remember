# mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

One task-intent source for closeout, door, and lifecycle consumers (CCR-R02@v2). It resolves the
exact contract-owned leaf task document — never caller prose — computes its canonical
`task-intent/v1` identity, and requires a live closeout door to bind the exact current canonical
intent before closeout admission proceeds.

## Code Commentary

### Logic

- `contract_task_intent_candidate` (line 22) resolves the exact candidate: a supplied typed
  `TaskDocumentRef` via `TaskDocumentTopology.resolve`, or, for a leaf enclosure contract, the
  terminal leaf document through `resolve_terminal_leaf_doc`. It refuses a missing leaf document
  (`task-intent-task-document-missing`), requires an explicit typed reference for series closeout
  (`task-intent-candidate-required`), refines `TaskDocumentRefError` into `TaskIntentError`,
  refuses candidates outside the contract task root
  (`task-intent-task-document-outside-root`), and refuses master documents
  (`task-intent-leaf-required`).
- `contract_task_intent` (line 61) runs the candidate resolution and returns the canonical
  `task_intent_identity(contract.task_root, candidate)` digest.
- `current_door_task_intent` (line 70) is the admission boundary: it requires a live closeout
  door generation (`closeout-door-missing`, next action `closeout_door.declare`), recomputes the
  current intent from the door's own `taskDocumentRef`, and raises
  `closeout-door-task-intent-stale` (next action `closeout_door.update-provenance`) unless the
  door binds exactly the current digest. A missing-intent door is rejected by the same seam.

### Conventions

The closeout request never supplies the intent digest itself; it may only name the candidate document.

### Invariants And Boundaries

- The contract's own typed reference and task root are the only addressing authorities.
- No consumer synthesizes an intent digest, searches history for one, or accepts a caller-supplied
  substitute; absence is a typed refusal, never a fallback.
- Integration generations do not carry leaf task intent and never reach this seam.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

### Repo-Internal References

- Exact contract-owned candidate resolution with confinement and leaf-only rules. [1]
- Canonical identity computation over the resolved candidate. [2]
- Live-door currentness requirement used by closeout admission. [3]
- The identity producer it delegates to. [4]
- The terminal leaf-doc resolver used by leaf contracts. [5]
- The typed models behind the intent state. [6]

## CCR-R02@v2 Normative Task-Intent Identity

This seam is the closeout-side consumer of the canonical identity required by CCR-R02@v2
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`): every closeout admission and door
provenance update binds the exact current leaf intent, so an obligation change that alters the
digest stales the door before any evidence reuse. It is part of the L25 landed candidate
(`99dc249b`).
