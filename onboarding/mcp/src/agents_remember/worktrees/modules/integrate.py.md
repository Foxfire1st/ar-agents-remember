# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

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

**The mandatory invariant gate at master and checkpoint landing (MIK-R09 rule 4, leaf 260928-MIK-L09).**
`_handover_or_apply_integration` now calls `_knowledge_gate_block(contract, args, commits, sources)` after the handover
gates and before the memory-ancestry proof, in preview and apply alike, over the route's own commits
(`_route_commits`: the closeout cells, or the checkpoint's live pair). For a series contract with external memory it
asks `worktrees.knowledge_gate.landing_gate_refusal` with a `LandingGateRequest` naming the master's memory commit
(validated against the parent line's current memory source, the carried L22 obligation) and the master's code commit
with the parent line's current code source as `code_base`, so every entry of the master's memory tree at a path the
master's net code diff changed must be `current` at the master's code commit: `stale`, `unverifiable` (review R1 F4)
and a Git read failure all refuse. A refusal is the blocked payload `knowledge-gate-refused` (exit 2, persisted only on
apply, no developer decision), naming every finding and the remedy (a knowledge-maintenance leaf within the master,
`knowledgeMaintenanceScope: true`). Unconverted memory is not gated (the probe returns `None`); the cutover lock
refuses it instead once the repository holds converted memory (L37, MIK-R09 rule 6). Since L37 the block also
runs for a **leaf's** integration with external memory: `_leaf_landing_lock` returns `None` when no memory lands or
when the landed memory commit or the line it lands on holds the layout marker (the leaf was gated at its closeout),
names a probe Git cannot answer, and otherwise asks `leaf_cutover_refusal(contract, "the leaf's integration")`.
So the converting leaf's own integration onto its unconverted line is never locked. Tests:
`test_a_master_or_checkpoint_landing_waits_until_no_entry_at_a_changed_path_is_stale` and, through the route,
`test_the_master_and_checkpoint_landings_refuse_through_the_integration_route`; on real data `closeout.txt` step 4
(`integrate`'s dry run returns `(2, knowledge-gate-refused)` for the unmaintained master).

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
- MIK-R09 rule 4: the gate before the ancestry proof, preview and apply alike. [5]
- Final and checkpoint result publication differ without performing reclamation. [6]
- The shared writer records the two accepted output commits. [7]

- A leaf's closed-out memory lands only when converted, or in a repository that holds no converted memory. [8]
- The block runs for leaves (the lock) and for series contracts (the landing gate). [9]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
