# mcp/src/agents_remember/application/knowledge_gate/adapter.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The composition-bound `KnowledgeGatePort` of the worktree layer (MIK-R09).** The worktree layer ranks below the
application layer and reaches the gate only through `worktrees.services.KnowledgeGatePort`. `KnowledgeGate` is its
one implementation; `application/worktree_services.py` binds it as `knowledge_gate=KnowledgeGate()` in the default
services.

## Code Commentary

### Logic

- `leaf_refusal(contract, *, code_tree, memory_tree, parent_memory_tip)` evaluates `evaluate_leaf_gate` over
  `CandidateTrees(code, memory)` with the tip the caller read, and returns `None` (not applicable, or a pass) or
  `GateResult.refusal()`.
- `direct_verdict(contract, *, code_commit, memory_tree)` delegates to `direct.direct_verdict`.
- `landing_refusal(request)` delegates to `landing.landing_refusal`.

### Conventions

- A frozen, stateless dataclass: the memo lives in [`memo`](memo.py.md), so the curator publication and the closeout
  validator's port call compute the same key and one memory-quality run recomputes once.

### Invariants And Boundaries

- **No bypass (rule 5).** A converted route with no bound gate is refused (`GATE_UNBOUND` in
  `worktrees/knowledge_gate.py`), never committed ungated; proved by the closeout-validator test with `ports(gate=False)`.

### Todos

- None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

No configured live documentation source was available for this pass.

### Repo-Internal References

- The port implementation: recompute over the exact trees, decide, validate. [1]
- The leaf refusal over the candidate trees. [2]
- The direct and landing answers. [3]
- The default composition binds it. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is crossed by this file.
