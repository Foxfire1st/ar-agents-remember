# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The direct landing operation (L16-R8): the branch-addressed counterpart of the worktree closeout
commit phase for sanctioned direct execution. It binds the task-root series contract, verifies the
exact code commit on the series branch, then atomically commits external-memory content and
prepends the code-to-memory ledger row — replacing hand-written ledger sync rows in direct mode
with the same ledger semantics as the worktree path.

## Code Commentary

### Logic

`direct_landing(config, request)` is policy-gated (`directExecutionEnabled`, fail-closed) and
synchronous by design (direct mode has no worktree group or detached worker, so the durable shape
is the lock-guarded validate-then-mutate of `worktree_sync`, not the `start_or_observe_operation`
worker). Under `integration_authority_lock(config.coordination_root, contract.repo_name)` it
re-loads the contract (a changed contract refuses `direct-landing-contract-changed` — the TOCTOU
guard), then previews or applies.

`_verify_code_commit` proves the exact commit is the current series branch HEAD (`branch_commit`),
resolves its tree, and — when `candidate_tree` is given (the staged candidate the owner gated
through the Dagger `--source`/`--repository-bundle` contract) — refuses a moved tree
(`direct-landing-candidate-tree-moved`), keeping the gate strictly pre-commit (L16-R7).
`_memory_facts` reads external-memory + ledger facts for the preview. `_direct_landing_apply`
requires external memory (the ledger row needs a real mapping), verifies the memory checkout is on
the series memory branch, commits memory content when dirty (`commit_if_dirty`), loads the ledger,
reuses an idempotent matching mapping (re-land with the same memory commit is a no-op), refuses a
conflicting existing mapping (`direct-landing-ledger-conflict` — stricter than the worktree path,
which reuses mappings for recovery), writes the prepended ledger row, adds `memory.md`, commits,
and finally checks `is_ancestor(memory_commit, ledger_commit)`.

### Conventions

Same helper sequence as the worktree external closeout path
(`worktrees/modules/closeout.py resume_external_commits`): `find_mapping` → `commit_if_dirty`
(returns HEAD when clean) → `write_ledger(prepend_mapping)` → `add memory.md` → `commit_if_dirty`
→ `is_ancestor`. The code commit is verified, never created.

### Invariants And Boundaries

- All facts are pre-validated before any mutation; every refusal carries a typed `status`.
- `directExecutionEnabled` must be set; `intent_note` is required (the commit approval).
- Only the task-root series contract binds; leaf contracts refuse (`direct-landing-series-required`).
- The gate stays strictly pre-commit via `candidate_tree`; commit-then-gate is the accepted-risk
  exception only where the developer rules it (documented, L16-R7).
- External memory only for apply; internal/disabled memory refuses
  (`direct-landing-memory-required`).

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The policy-gated, lock-guarded entry point with contract reload under the lock. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:74-126 |
| Exact commit verification and the moved-candidate pre-commit refusal. | `_verify_code_commit` | mcp/src/agents_remember/worktrees/direct_landing.py:129-159 |
| Ledger + memory commit with idempotent re-land and conflict refusal. | `_direct_landing_apply` | mcp/src/agents_remember/worktrees/direct_landing.py:206-266 |
| The same ledger semantics the worktree path uses. | `resume_external_commits` | mcp/src/agents_remember/worktrees/closeout_recovery.py:194-235 |
| The application boundary that translates operation errors. | `direct_landing_tool` | mcp/src/agents_remember/application/direct_landing.py:13-27 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R7/R8 — the direct landing operation:
  atomic code-commit verification + memory commit + ledger row under the integration authority
  lock, with the strictly pre-commit staged-candidate gate. Verified at code commit a9d50e08.
