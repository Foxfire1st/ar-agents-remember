# mcp/src/agents_remember/worktrees/queue/closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

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

`accepted_code_commit` receives the already validated `EffectiveCloseoutInput` explicitly, then either proves the journaled code commit at clean task HEAD, adopts a clean
post-claim HEAD during recovery, or creates a leaf commit through the already-selected strict or
non-strict commit primitive. A series/master contract always requires a clean checkout and records
its already-landed HEAD; this recovery layer cannot create master code. It then proves the commit
tree equals the immutable accepted candidate and journals the code cell before returning.
`resume_external_commits` receives that same typed input rather than rereading optional args, requires a clean memory
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
| The typed outcome carries external-memory refresh and commit results across normal and recovered closeout. | `MemoryCloseoutOutcome` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:49-58 |
| Finalization recovery proves exact clean heads, the ledger mapping, and memory ancestry without replaying mutation. | `prove_closeout_recovery_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:61-76 |
| Code recovery receives typed intent, proves clean HEAD and the accepted tree, then journals the code cell. | `accepted_code_commit` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:170-226 |
| External recovery receives the same intent, reconciles the exact memory and ledger edge, then journals the full tuple. | `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:229-296 |
| The regression suite exercises the extracted proof owner directly for mismatch and reachability refusals. | `test_recovery_rejects_code_and_contract_memory_mismatches`; `test_recovery_rejects_unproven_memory_commits` | mcp/tests/test_worktree_closeout_recovery.py:309-342; mcp/tests/test_worktree_closeout_recovery.py:344-383 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## R39 Series Closeout Recovery

Non-leaf closeout now records already-landed clean code: it requires a clean series/master checkout
and takes current HEAD. Leaf recovery retains commit/retry reconciliation. Series closeout cannot
become another code-commit or acceptance owner.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Evidence-Aware Commit Recovery

Code and ledger commits use messages only from accepted `EffectiveCloseoutInput`. Before a new Git commit the module publishes mutation intent; after the exact commit it publishes proof. Verified-existing commits report recovery projection without inventing mutation evidence. Ledger recovery has no generated-message fallback, and any recorded cell is evidence to prove rather than authority to overwrite. Memory-before-ledger direct-landing recovery is outside this worktree journal owner.

## 260821-CLIVE-L2 Current Contract

The current source seams include `MemoryCloseoutOutcome`, `prove_closeout_recovery_commits`, `accepted_code_commit`. Despite its transitional package location under `worktrees/queue`, this module proves and publishes root-journal mutation evidence for the accepted closeout generation. It does not make the queue row recovery authority. Moving or deleting residual queue lifecycle structure is L3 scope.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `MemoryCloseoutOutcome`, `prove_closeout_recovery_commits`, `accepted_code_commit` at this ownership boundary. | `MemoryCloseoutOutcome`; `prove_closeout_recovery_commits`; `accepted_code_commit` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:48-58; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:61-76; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:170-226 |

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input and ledger-recovery package relocations; journal-owned recovery proof and exact tuple reconciliation are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

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
