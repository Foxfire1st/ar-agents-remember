# mcp/src/agents_remember/worktrees/closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T11:48:55+02:00 |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate |  2026-08-14T13:35:55+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Own the restart-safe proof and journaling around closeout's irreversible code, memory, and ledger
Git boundaries. This module lets the durable lifecycle worker resume an accepted candidate without
recommitting code, selecting a stale pre-attempt memory commit, or duplicating a ledger edge.
It also owns the typed memory-closeout outcome and the exact proof used when contract finalization
resumes after code, memory, and ledger commits already exist.

## Code Commentary

### Logic

`MemoryCloseoutOutcome` carries the committed memory/ledger identities and all refresh results back
to the coordinator. `prove_closeout_recovery_commits` validates clean code and memory worktrees,
exact recorded heads, the code-to-memory ledger row, and reachability of memory content before
returning that outcome without replaying a mutation.

`accepted_code_commit` either proves the journaled code commit at clean task HEAD, adopts a clean
post-claim HEAD during recovery, or creates a leaf commit through the already-selected strict or
non-strict commit primitive. A series/master contract always requires a clean checkout and records
its already-landed HEAD; this recovery layer cannot create master code. It then proves the commit
tree equals the immutable accepted candidate and journals the code cell before returning.
`resume_external_commits` requires a clean memory
worktree, reconciles the exact code-to-memory row, creates only a missing matching row, proves an
existing memory commit is reachable, and journals the complete tuple.

### Conventions

Recovery state is passed through typed `WorktreeArgs` and published through
`report_operation_progress`; Git and ledger writes use the existing guarded primitives.

### Invariants And Boundaries

- A non-empty journaled commit cell is evidence to prove, never a hint to overwrite.
- The accepted candidate tree must equal the committed code tree.
- A conflicting ledger mapping, wrong memory HEAD, or unreachable memory commit fails closed.
- Contract-finalization recovery proves already-created commits here; `modules/closeout.py` only
  coordinates the proof and contract amendment.
- Each irreversible Git boundary is journaled before the next one begins.
- This module does not run quality, claim approval, or amend the task contract.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal recovery seam.

## Repo-Internal References

The production helpers and focused recovery suite are the direct evidence for this boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed outcome carries external-memory refresh and commit results across normal and recovered closeout. | `MemoryCloseoutOutcome` | mcp/src/agents_remember/worktrees/closeout_recovery.py:26-36 |
| Finalization recovery proves exact clean heads, the ledger mapping, and memory ancestry without replaying mutation. | `prove_closeout_recovery_commits` | mcp/src/agents_remember/worktrees/closeout_recovery.py:39-86 |
| Code recovery proves clean HEAD and the accepted tree before journaling the code cell. | `accepted_code_commit` | mcp/src/agents_remember/worktrees/closeout_recovery.py:89-127 |
| External recovery reconciles the exact memory and ledger edge before journaling the full tuple. | `resume_external_commits` | mcp/src/agents_remember/worktrees/closeout_recovery.py:130-171 |
| The regression suite exercises the extracted proof owner directly for mismatch and reachability refusals. | `test_recovery_rejects_code_and_contract_memory_mismatches`; `test_recovery_rejects_unproven_memory_commits` | mcp/tests/test_worktree_closeout_recovery.py:180-247 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## R39 Series Closeout Recovery

Non-leaf closeout now records already-landed clean code: it requires a clean series/master checkout
and takes current HEAD. Leaf recovery retains commit/retry reconciliation. Series closeout cannot
become another code-commit or acceptance owner.

## Update History

- 2026-08-14T11:48:55+02:00 — R42 curator: recorded the move of `MemoryCloseoutOutcome` and
  `prove_closeout_recovery_commits` from the closeout coordinator into the recovery owner; updated
  direct forcing-test citations. Verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: documented clean landed-code recovery for series/master
  closeout. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 acceptance ownership: series/master recovery records only
  a clean, already-landed code HEAD so no post-approval path can create an unreviewed master commit.
- 2026-08-14T05:26Z — Created for the L23 final candidate: documented monotonic closeout commit
  recovery and the exact code-to-memory-to-ledger reconciliation boundary. Verification remains
  closeout-owned until the source commit exists.
