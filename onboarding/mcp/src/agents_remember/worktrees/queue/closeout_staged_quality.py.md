# mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Own exact staged-candidate materialization and repository-profile quality enforcement for
closeout. The extraction keeps disposable-worktree refusal, conflict refusal, candidate-tree
proof, configured fast-hook handling, and the strict targeted profile gate in one cohesive
pre-commit boundary. Since CCR-R22@v1 (L22, commit `685f83c44055`) the gate consumes a
`QualityGateTarget` (checkout, worktree group, repository id, profile reference) instead of a
bare checkout plus a settings executor; the executor identity and the exact staged contract now
come from the repository's admitted profile.

## Code Commentary

### Logic

`gate_staged_code(target, *, diff_base, candidate_tree)` reads `code_worktree`/
`worktree_group` from the `QualityGateTarget`, refuses the primary checkout and unresolved
conflicts before replacing the index, proves an accepted candidate before staging, resets and
stages the entire task worktree, proves the staged tree, runs the configured pre-commit hook,
restages, proves the hook did not change the reviewed tree, and finally invokes the targeted
strict profile gate with `QualityGatePlan(mode="targeted")`. The old `executor="dagger"`
parameter and `code_worktree`/`worktree_group`/`executor` positional signature were removed:
executor identity belongs to the profile.

### Conventions

Candidate comparisons use exact Git tree ids; the fast hook is a reviewed pre-gate transformer,
while `commit_verified_staged` later commits the certified index without rerunning hooks.

### Invariants And Boundaries

- Only a disposable linked task worktree may have its index replaced.
- Conflicts are refused before `git reset --mixed` can erase unmerged-index evidence.
- The candidate tree is immutable across acceptance, staging, and the configured hook.
- Acceptance runs through `QualityGatePlan(mode="targeted")` against the admitted repository
  profile; there is no host test compatibility path and no settings-level executor.
- This module stages and certifies; approval claim and commit ordering remain in `closeout.py`.

### Todos

None recorded.

## Evidence

### Docs References

CCR-R22@v1 requires the exact staged candidate to run through the profile-declared adapter before
any commit, with missing/invalid profile authority refusing as certification-profile-invalid.

- Invalid profile resolution produces typed admission failure before any Gate-1 command starts. [1]

### Repo-Internal References

- Linked-worktree and conflict refusals precede any index rewrite. [2]
- The staged gate proves the accepted tree around reset, staging, hook execution, and the targeted profile call. [3]
- Closeout no longer imports this owner: the staged-quality gate lives only in its own module, and the transaction-only closeout imports no code-quality gate. [4]
- The strict closeout preflight no longer exists in the closeout transaction; `gate_staged_code` remains the exact-staged-candidate owner and is reached by its own callers. [5]
- The strict gate admits the same target/profile and certifies the index. [6]

### Cross-Repo References

No cross-repository implementation source governs this module.

## 260824-PDLS — Closeout Accepts Certifying Evidence Only

The staged closeout quality edge requires `CertifyingTestEvidence` for the closeout consumer
after the profile gate returns. A direct diagnostic exit code, JSON payload, node report, or
candidate binding cannot authorize the commit.

## Current Landed Composition

`prepare_staged_code` now separates strict-hook settlement and exact candidate materialization from certification admission. It returns the actual `PreparedStagedCode(candidate_tree, pre_commit_hook_ran)` so the lifecycle can freeze admission after hooks settle. `gate_staged_code` composes that preparer with a fresh targeted gate; retained selected execution is owned elsewhere.
