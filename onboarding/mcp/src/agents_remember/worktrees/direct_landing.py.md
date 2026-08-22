# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The direct landing operation: the branch-addressed counterpart of the worktree closeout commit
phase for sanctioned direct execution. It binds the task-root series contract, verifies the exact
code commit on the series branch, normalizes explicit external-memory and ledger messages, then
performs the two external Git commits sequentially under the landing lock. The lock excludes
concurrent landing writers while held; it provides neither rollback nor durable crash recovery.

## Code Commentary

### Logic

`direct_landing(config, request)` is policy-gated (`directExecutionEnabled`, fail-closed) and
synchronous by design: direct mode has no worktree lifecycle journal or detached worker. Before
intent, lock, or Git it derives the verified-existing-code/external-memory/ledger plan and
normalizes the required explicit messages. Under
`integration_authority_lock(config.coordination_root, contract.repo_name)` it re-loads the
contract (a changed contract refuses `direct-landing-contract-changed`), then applies the already
validated plan. This lock serialization is concurrency control, not crash durability.

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

The sequence mirrors the ledger semantics of journaled worktree closeout without sharing its
journal: `find_mapping` → memory `commit_if_dirty` with the accepted explicit message →
`write_ledger(prepend_mapping)` → `add memory.md` → ledger `commit_if_dirty` with the accepted
explicit message → `is_ancestor`. The code commit is verified, never created. No generated subject
or message fallback exists.

### Invariants And Boundaries

- All facts are pre-validated before any mutation; every refusal carries a typed `status`.
- `directExecutionEnabled` must be set; `intent_note` is required (the commit approval).
- Memory and ledger messages are explicit, stripped, and nonblank before lock or Git; code is
  verified-existing/not-applicable and has no message.
- Only the task-root series contract binds; leaf contracts refuse (`direct-landing-series-required`).
- The gate stays strictly pre-commit via `candidate_tree`; commit-then-gate is the accepted-risk
  exception only where the developer rules it (documented, L16-R7).
- External memory only for apply; internal/disabled memory refuses
  (`direct-landing-memory-required`).
- A memory commit followed by a crash before the ledger commit is not recovered durably in L1;
  L2-R11/L5-R15 own that boundary.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The policy-gated, lock-guarded entry point with contract reload under the lock. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:82-152 |
| Exact commit verification and the moved-candidate pre-commit refusal. | `_verify_code_commit` | mcp/src/agents_remember/worktrees/direct_landing.py:155-185 |
| Ledger + memory commit with idempotent re-land and conflict refusal. | `_direct_landing_apply` | mcp/src/agents_remember/worktrees/direct_landing.py:236-314 |
| The same ledger semantics the worktree path uses. | `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:216-276 |
| The application boundary that translates operation errors. | `direct_landing_tool` | mcp/src/agents_remember/application/direct_landing.py:14-37 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Direct Landing Boundary

Direct landing normalizes memory and ledger messages before recording intent, acquiring the landing lock, or invoking Git. Its code leg is verified-existing/not-applicable. Preview and apply expose the same stripped `effectiveInput`, and apply uses those exact messages with no generated subjects or fallbacks. The lock prevents concurrent landing writers only while held; memory and ledger remain sequential commits with no rollback or durable crash recovery. L2-R11/L5-R15 own that deferred durability work.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R7/R8 — the direct landing operation:
  code-commit verification plus sequential memory and ledger commits under the integration
  authority lock, with the strictly pre-commit staged-candidate gate. Verified at code commit
  a9d50e08; the crash-durability boundary was clarified by 260821-CLIVE-L1.
