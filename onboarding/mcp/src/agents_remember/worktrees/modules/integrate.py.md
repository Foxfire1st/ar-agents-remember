# mcp/src/agents_remember/worktrees/modules/integrate.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Land an accepted code/memory pair into its named source branches, or checkpoint an unfinished atomic master's live pair without closing the master.

## Code Commentary

### Logic

Ordinary integration validates completed approved closeout, the exact work branches and accepted code/memory heads, and clean substantive content. Memory cleanliness excludes root `memory.md`. `IntegrationSources` captures source tips and fast-forward/replay facts once; source movement routes through the owning sync and a fresh closeout or the explicit resolution handoff. Transitive lineage and current source tips are re-proved at publication.

A checkpoint obtains `CheckpointLanding` from the live series refs instead of closeout cells an unfinished master cannot have. The same captured pair feeds preview and apply, and publication rechecks it. A completed master cannot use this weaker route. Source code advancing without a matching memory trailer is not a refusal: the actual memory ref is still the accepted memory output.

Handover gates are folded across gate logs by matching master/task identity. Preview evaluates the addressed gate without writing; apply enforces it. Unmatched open gates produce the existing addressing diagnostic. Normal integration does not run code quality, memory quality, certification, curator coherence, or independent review; since MIK-R09 a series (master or checkpoint) landing on converted memory does run the mandatory invariant gate (below).

`_publish_integration_edge` reloads the exact contract, checks atomic/series or ordinary authority, re-proves the source snapshot, and delegates expected-old CAS. A CAS race reports the operation that actually ran, including the checkpoint tool on that route. The shared landing writer records `completed` plus pending cleanup for final integration, or `checkpointed` while preserving cleanup for a checkpoint. Neither landing reclaims the task; finalization owns that step.

**The invariant gate before every landing.** `_handover_or_apply_integration` delegates admission to `integration_gate.integration_gate_block` before ancestry proof or ref publication, in preview and apply. A leaf with converted memory rejudges the closeout-cell pair through the shared leaf validator and recomputed worklist gate against the current parent-memory tip; the earlier closeout verdict is not trusted as landing authority. A master final or checkpoint route runs validator, net staleness and newly closed history ownership, then the chain proof up to its actual pair. Final requires the complete canonical non-abandoned leaf population; checkpoint examines the leaves already landed.

A refusal projects `knowledge-gate-refused` (exit 2) without persisting the contract or recomputed worklist, even on apply. Git read failures are named unreadable inputs. Unconverted memory retains the cutover lock; a converted side is gated rather than locked. These judgments do not add code-quality, full MQC, coherence or independent-review gates. [5]

### Conventions

`IntegratedCommits(code, memory_content)` is the sole delivered pair. Preview's memory ancestry proof and the protected boundary use the same real-Git predicate. The final/checkpoint difference is captured data and recorded lifecycle state, not a second ref transaction.

### Invariants And Boundaries

- No cache row, file, header, ordering rule, or ledger-only output authorizes or blocks integration.
- Accepted output identities must match the route's captured or recorded candidate.
- Each protected ref update keeps its expected old value; a memory CAS race must not erase concurrent work or falsely claim that both refs landed.
- A checkpoint remains a publication with an open master; it is separate from a stop-only pause.
- Landing and task finalization remain distinct operations.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.


- Ordinary admission requires the accepted code/memory work heads and substantive cleanliness. [1]


- Source snapshots and replay/lineage decisions retain current Git facts. [2]


- Checkpoint capture, route output selection, and shared memory ancestry. [3]

- Addressed handover gates and publication preserve the operation's real identity. [4]

- Admission before ancestry and publication judges leaf or master pairs without writing refused state. [5]

- Final and checkpoint result publication differ without performing reclamation. [6]
- The shared writer records the two accepted output commits. [7]


- The converted leaf rejudges its exact closeout pair; unconverted memory keeps the cutover lock. [8]



- One admission owner dispatches leaf pair judgment or master validator/staleness/history and chain judgment. [9]


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
