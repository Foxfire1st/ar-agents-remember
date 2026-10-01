# mcp/src/agents_remember/worktrees/modules/guidance.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Build lifecycle status payloads and typed next-operation guidance from the worktree contract and observed Git state.

## Code Commentary

### Logic

`lifecycle_guidance` preserves three ordered groups: reclaimed/abandoned contracts first, attempted integration next, then pre-integration work. Dirty worktree diagnostics do not manufacture a commit-approval gate. A completed integration whose accepted outputs are carried home routes to `lifecycle_finalize_task`; a checkpointed series remains `worktree-started` with `continue_work`, because its master is still open.

`carryover_done` proves that the recorded code and memory outputs are ancestors of their named source tips. It uses integrated output cells when populated and otherwise the recorded closeout outputs. Missing repositories, output identities, source refs, or ancestry return false. Internal/disabled memory passes without an external-memory milestone. The timestamp is read from the accepted memory commit, not a cache row. Missing or malformed `memory.md` cannot change this completion proof.

**The `validate` step now travels with the hint (260915-KS-L23, D-25).** Two helpers were added
between `lifecycle_guidance` and the phase helpers, and one phase branch changed:

- `_published_coherence_authority(contract)` returns the digest of the leaf's **published**
  curator-coherence authority, or `""`. It answers `""` for a series contract, a leaf whose
  `memory_mode` is not `external`, and a leaf with no memory worktree, and it swallows
  `CuratorCoherenceError`/`OSError` — so an applicability miss or an unreadable authority degrades to
  the ordinary integration step instead of sending an operator to a tool that would refuse.
- `_canonical_curator_caller(contract)` builds the exact `caller` payload the coherence route expects
  (`role: "curator"` plus a `task_document_ref` derived from the contract's own `task_root` and
  `leaf_id`). It exists because the refusal that asks for that argument is the same
  instructions-do-not-travel defect one level up: a hint that names a tool while leaving its one
  identity argument blank is not a usable move (D-26).
- The `closeout_status == "completed"` branch of `_pre_integration_phase` now returns, **when an
  authority is published**, the `integration-pending` phase with the `curator_coherence` tool,
  `action="validate"`, that canonical caller, and a summary that states the reason: finalize's
  automatic cleanup collects the enclosure root, so the validate window closes with it. When no
  authority is published the branch is unchanged — those contracts still route straight to
  `worktree_integrate`. The move itself is still the integration decision; the validation is its
  precondition, which is why `NextOperation` was not widened (see `models/worktree.py`).

`NextGuidance`, `LifecycleGuidance`, `WorktreeStatusFacts`, and `WorktreeStatusPayload` retain typed response boundaries. `WorktreePhase`, `NextOperation`, and `NextTool` are imported from `models.worktree`; only the recovery vocabulary is declared locally. The separate `recovery_guidance` builder serves blocked/gated flexible responses without widening lifecycle phases.

Status retains `ledger_path` as consumer metadata, exposes contract/enclosure identity, providers, source lineage, local base freshness, and optional landing observations. `unknown_contract_cells` remains an explicit degraded-read diagnostic. Interactive status calls the landing observation owner; projected status accepts an already-observed snapshot.

### Conventions

Next-move keys are omitted when they have no value. Guidance keys are merged after factual status keys. Local base freshness is separate from upstream fetch and remote landing observation.

### Invariants And Boundaries

- Lifecycle position, rather than raw dirtiness, selects the next operation.
- A published coherence authority must be validated **before** integration, and the hint says so: the
  step is named while the enclosure root still exists, because `lifecycle_finalize_task`'s automatic
  cleanup collects it and the standalone validate is then no longer reachable.
- The coherence route is offered only where it applies. `_published_coherence_authority` answers `""`
  — and the branch falls back to the plain integration step — for a series contract, a non-external
  memory leaf, a leaf with no memory worktree, an unpublished leaf, and an unreadable authority; it
  never raises into the guidance path.
- Code and memory completion require real Git reachability; cached mappings carry no completion authority.
- Finalization owns reclamation; a checkpoint does not close the master or make cleanup pending.
- Lifecycle wire vocabulary has one model owner; recovery guidance keeps its separate response vocabulary.
- Consumer ledger paths and raw status diagnostics remain available without becoming admission facts.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Typed payloads and separate lifecycle/recovery builders. [1]
- Carryover completion is a real two-repository ancestry proof. [2]
- Phase precedence, finalization guidance, and the still-working checkpoint branch. [3]
- Freshness, consumer paths, identity fields, and interactive/projected observation. [4]
- The canonical lifecycle wire vocabularies. [5]
- External completion remains valid with damaged caches and rejects unlanded commits. [6]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
