# mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Executes only the suffix admitted by the current selected closeout generation and hands exact remaining work to the bound memory/finalization owner.

## Code Commentary

### Logic

**Since MIK-R09 (leaf 260928-MIK-L09, ruling 2026-09-30T14:38:47 gap 3)** `execute_selected_closeout` first asks `worktrees.knowledge_gate.prepared_closeout_refusal(contract)`, before recovery: this certified (prepared) path binds its memory commit to the curator-attested candidate, so it cannot set `closed: true` in the leaf's history file (MIK-R07 rule 7), and on converted memory it refuses through the path's own `refuse(...)` with `prepared-closeout-knowledge-history-unclosable`, naming why and that the leaf should close out through the worktree closeout commit. Unconverted memory gets `None` from that check. Since L37 the next check is `prepared_closeout_lock(contract)`: for unconverted memory in a repository that holds converted memory it refuses with `unconverted-memory-locked`, naming the crossing sync (MIK-R09 rule 6); in a repository that holds none the path is untouched. The path has no production caller today; `application/prepared_certification._realize_prepared_memory` carries the same check. Tested by `test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

`execute_selected_closeout` then resumes already prepared publication through `resume_prepared_closeout`. For a selected certification run, `_refresh_selected_recovery` prepares the code view and reobserves current memory before deciding which original certificates remain reusable. This preserves the selected suffix and explicit successor requirements.

`execute_selected_closeout` begins with a live running owner, current contract/profile/route authority and the fully reopened selection. Selected red evidence refuses unchanged retry. The exact original certificate pool and retained terminal publications form `CodeCertificationExecution`; the current recovery decision determines the first gate to run.

Code execution uses the configured profile path and contract code base, supplying callbacks that select real recorded terminals, protect every referenced publication and recheck the live owner immediately before a start. After publication it reopens current state and appends a recovery decision derived from the actual selected prefix. An incomplete code prefix cannot enter memory.

An existing or inherited Gate-5 certificate requires a bound continuation and an actual current `GateFiveSemanticInputs` observation before reuse is considered. The observation is reparsed canonically and followed by a live journal check. Recovery decisions retain exact memory bytes; an unchanged decision is idempotent. Changed inputs for an already selected fifth terminal require an explicit successor. A current inherited fifth terminal is retained by its exact original reference.

First gate 5 hands off to `run_memory`. Finalization-only reuse performs a second current memory observation and exact equality check before `finalize`. The default service bundle binds `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter`; completion still requires the corresponding current runtime evidence.

### Conventions

`CloseoutCertificationHandoff` carries the actual contract, journal record/store and loaded selection. The reuse compiler owns gate choice; the executor does not infer success from missing work or manufacture replacement certificates.

### Invariants And Boundaries

- Wrong/stale owner, cancellation or a non-running record refuses before private execution.
- Original Gate-5 authority cannot be reused from unknown memory state; unavailable current memory invalidates reuse rather than becoming an unchanged assumption.
- The selected graph is rechecked around terminal publication, pruning protection and handoff; only allowed heartbeat-only journal changes are tolerated by the observation owner.
- A finalization result is whatever the bound owner actually returns. An absent continuation still produces an explicit refusal.

### Todos

No missing default continuation binding remains in this IAS source. Runtime certification and finalization evidence remain separate from source composition.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Exact owner and selected objects passed to memory or finalization composition. [1]
- Reprove the live worker and selected authorities for a continuation action. [2]
- Execution inputs use original selected and predecessor evidence without latest lookup. [3]
- Actual memory changes and selected certificate progress drive append-only recovery decisions. [4]
- The code gate receives explicit selection, publication protection and last-moment authorization callbacks. [5]
- Current memory inputs are canonically reparsed after a live-owner observation. [6]
- The prepared path refuses on converted memory before recovery (MIK-R09 gap 3). [7]
- Suffix, Gate-5 observation and second-observation finalization dispatch remain explicit. [8]
- The default application service bundle binds the prepared continuation and memory certification adapter (beside, since MIK-R24, the knowledge validator's base converter and the knowledge crossing). [9]

- The unclosable-history refusal, then the cutover lock, both before recovery. [10]
- Both prepared-closeout entries refuse by the lock. [11]

### Cross-Repo References

No cross-repository implementation or external protocol is owned here.


No separately configured cross-repository source is used for this card.
