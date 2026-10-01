# mcp/src/agents_remember/worktrees/closeout_input.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the single route- and contract-aware closeout-input normalizer. It captures candidate provenance, derives enabled versus not-applicable legs, validates explicit messages, and returns the only `EffectiveCloseoutInput` value permitted below the public boundary.

## Code Commentary

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Logic

The normalized Git plan has exactly two possible legs, code and memory. Ledger rendering is a cache refresh and contributes neither a commit message nor enabledness to admission, retries, or corrected-call arguments.

`resolve_closeout_plan` derives leg state from route, the already-validated contract model, memory mode, and the captured code candidate rather than from blank sentinels or memory dirtiness. Direct landing has verified-existing code, so code is not applicable; the external memory-content leg is enabled. Worktree leaf code is enabled only when the stable candidate tree differs from HEAD, and external-memory leaves enable memory content. Series and non-external legs receive typed reasons. Unsupported contract kinds are rejected at the model boundary; this owner does not duplicate that impossible-state guard.

`normalize_closeout_input` strips enabled messages once, reports omitted/empty/whitespace or stale/forged values as `CloseoutInputError`, and includes `invalidFields`, `resolvedPlan`, and `correctedCall`. The candidate snapshot is rechecked so a tree or HEAD change during normalization refuses. `require_effective_closeout_plan` validates durable retries against the accepted plan rather than re-deriving it after partial mutation.

`capture_closeout_candidate` delegates ordinary-leaf observation to the strict future-code
identity owner. That owner records the observed HEAD and configured base around the canonical
isolated-index add-all tree computation. Series closeout remains branch-addressed and continues
through its existing committed-tree route.

#### Invariants And Boundaries

- Preview, fingerprint, journal, worker, recovery, and commit code consume the same effective input.
- Validation happens before integration-authority observation, lifecycle journal creation, worker launch, landing lock, mutation intent, or Git.
- Enabledness is contract/candidate truth, not current memory worktree dirtiness.
- A failed request has no queue, authority, journal, or Git effect.
- This module does not select or invalidate closeout-queue candidates.
- Candidate acceptance and lifecycle-operation identity are distinct: this adapter supplies exact
  Git facts, while the lifecycle journal continues to guard unproven HEAD movement.

### Todos

Revision and public recovery controls are deferred to L2.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `resolve_closeout_plan` derives code/memory enabledness from the admitted route and candidate. [1]
- `normalize_closeout_input` validates the two explicit messages and returns one effective input. [2]
- `effective_message_arguments` renders only enabled code/memory messages for next-call guidance. [3]

- Leaf candidate capture consumes the strict plane-derived future-code identity, while series capture remains branch-addressed. (`capture_closeout_candidate`) [4]
- Enabled/not-applicable legs derive from validated route, contract, and candidate facts. (`resolve_closeout_plan`) [5]
- Typed refusal and corrected-call data are emitted together. (`CloseoutInputError`; `normalize_closeout_input`) [6]
- Retried durable input is checked against its accepted plan. (`require_effective_closeout_plan`) [7]

### Cross-Repo References

No meaningful cross-repository reference applies.

No additional cross-repository evidence applies.
