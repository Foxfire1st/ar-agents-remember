# mcp/src/agents_remember/worktrees/knowledge_validation.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The knowledge validator at the worktree layer's memory commit routes (MIK-R22 rule 8).** A route calls `memory_commit_refusal` with the exact tree it is about to commit, its comparison bases and its paired code commit, before it commits. The validator ranks above this layer and is reached through `services.KnowledgeValidationPort`.

## Code Commentary

### Logic

- `PairedCode(repository, commit)` names the code commit a memory commit is paired with.
- `has_layout_marker(repository, treeish)` runs `git ls-tree --name-only <tree> -- knowledge/layout.json`. Empty output means absent. A non-zero exit raises `LayoutProbeError`, so an unreadable side is never taken for unconverted memory (review R1 finding 6). Since MIK-R09 (leaf 260928-MIK-L09, review R1 F9) a `subprocess.SubprocessError` (the probe failed or timed out) raises `LayoutProbeError` too, naming it ("the Git probe failed or timed out"), so every caller's refusal is named instead of an escaping error. The mandatory gate and the worklist now probe through this function as well.
- `memory_commit_refusal(*, memory_repository, candidate_tree, bases, paired_code, leaf_publication=False)` probes the candidate and every base. A probe error is a refusal. If no side is converted it returns `None`. Otherwise it refuses when the paired code commit is unknown or when `worktree_services().knowledge_validation` is unbound, and else returns the port's answer: since MIK-R09, `leaf_refusal(...)` when `leaf_publication` is set (a commit that publishes a leaf: the leaf's own history file is re-anchor-checked whatever its `closed` flag, review R1 F1), else `refusal(...)`. Since L37 `leaf_publication` is `True` or a `LeafPublication(candidate_tree, bases, frozen)`: a route that knows the commit its candidate sits on names it in `frozen`, and the publication's own tree and bases are then the ones probed and judged. `True` builds the publication from the call's `candidate_tree` and `bases`, with nothing frozen.

### Conventions

- It imports only the kernel Git runner, the L21 layout constant and `worktrees.services`; the validator itself stays behind the port.
- Callers: `sync_transaction_git._finish_staged_memory_merge`; since MIK-R09 (the carried L22 obligation) also the worktree closeout's exact tree (`closeout_external._refuse_ungated_memory`, with the leaf's recorded closeout commit frozen), direct landing's exact tree (`direct_landing._close_gated_leaf`), and record, master and checkpoint landing (`knowledge_gate.landing_gate_refusal`), the leaf routes with `leaf_publication=True`.

### Invariants And Boundaries

- A converted memory commit is never made without a passing validator run: an unbound validator, an unknown paired code commit, or an unreadable tree refuses.
- Unconverted memory returns `None` before the validator is touched, so no route commits differently before the cutover (MIK-R37).
- There is no parameter that skips validation.

### Todos

Resolved by MIK-R09 (leaf 260928-MIK-L09): closeout, direct and record landing, and master and checkpoint landing call this helper, each with its comparison base (the parent line's memory tip for a leaf, the series head for direct landing, the task's `memory_base_commit` for a recorded landing, the parent source for a master), with a refusal test through each public route entry (`test_knowledge_gate_routes.py`).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The route gate and its callers.

- The paired code commit. [1]
- The marker probe fails closed, since MIK-R09 on a timed-out probe too. [2]

- The refusal: unconverted passes, converted needs a paired code commit and a bound validator; since MIK-R09 a leaf publication takes the port's `leaf_refusal`, with the judged candidate, bases and frozen commit of a `LeafPublication` when the route names one. [3]

- The port it calls. [4]

- The sync's memory merge calls it before committing, after closing any master-line crossing history file the merge adds (MIK-R24). [5]
- The route never commits converted memory unvalidated. [6]

- The route entry takes a leaf publication that may name the frozen commits. [7]

### Cross-Repo References

The memory and code repositories are addressed explicitly by the caller; no external system is involved.

No cross-repo boundary is crossed by this file.
