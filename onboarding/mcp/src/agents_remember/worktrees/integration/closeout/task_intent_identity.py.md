# mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00                  |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview      | `overview.md`                             |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

One task-intent source for closeout, door, and lifecycle consumers (CCR-R02@v2). It resolves the
exact contract-owned leaf task document — never caller prose — computes its canonical
`task-intent/v1` identity, and requires a live closeout door to bind the exact current canonical
intent before closeout admission proceeds.

## Code Commentary

### Logic

- `contract_task_intent_candidate` (line 21) resolves the exact candidate: a supplied typed
  `TaskDocumentRef` via `TaskDocumentTopology.resolve`, or, for a leaf enclosure contract, the
  terminal leaf document through `resolve_terminal_leaf_doc`. It refuses a missing leaf document
  (`task-intent-task-document-missing`), requires an explicit typed reference for series closeout
  (`task-intent-candidate-required`), refines `TaskDocumentRefError` into `TaskIntentError`,
  refuses candidates outside the contract task root
  (`task-intent-task-document-outside-root`), and refuses master documents
  (`task-intent-leaf-required`).
- `contract_task_intent` (line 60) runs the candidate resolution and returns the canonical
  `task_intent_identity(contract.task_root, candidate)` digest.
- `current_door_task_intent` (line 69) is the admission boundary: it requires a live closeout
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

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact contract-owned candidate resolution with confinement and leaf-only rules. | `contract_task_intent_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py:21-57 |
| Canonical identity computation over the resolved candidate. | `contract_task_intent` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py:60-66 |
| Live-door currentness requirement used by closeout admission. | `current_door_task_intent` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py:69-85 |
| The identity producer it delegates to. | `task_intent_identity` | mcp/src/agents_remember/tasks/task_intent.py:180-193 |
| The terminal leaf-doc resolver used by leaf contracts. | `resolve_terminal_leaf_doc` | mcp/src/agents_remember/tasks/leaf_doc.py:74-88 |
| The typed models behind the intent state. | `TaskIntentIdentity`; `TaskIntentState` | mcp/src/agents_remember/models/task_intent/__init__.py:55-59; mcp/src/agents_remember/models/task_intent/__init__.py:68-68 |

## CCR-R02@v2 Normative Task-Intent Identity

This seam is the closeout-side consumer of the canonical identity required by CCR-R02@v2
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`): every closeout admission and door
provenance update binds the exact current leaf intent, so an obligation change that alters the
digest stales the door before any evidence reuse. It is part of the L25 landed candidate
(`99dc249b`).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new closeout task-intent source (`contract_task_intent_candidate`,
  `contract_task_intent`, `current_door_task_intent`); documented the contract-addressed
  candidate resolution, leaf-only confinement, and the live-door currentness refusal. Verified at
  code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
