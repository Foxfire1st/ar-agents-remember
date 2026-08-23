# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The durable branch-addressed counterpart of worktree closeout commit execution for sanctioned
direct work. It binds the task-root series contract, consumes the exact closed admission result,
creates or resumes one canonical root-journal generation, verifies the exact code commit/tree and
memory/ledger pre-state, then records intent and proof around each sequential external Git commit.
The landing lock excludes concurrent writers while held; restart recovery comes from the journal.

## Code Commentary

### Logic

`direct_landing(config, request)` is policy-gated (`directExecutionEnabled`, fail-closed) and
synchronous by design, but synchronous execution no longer means unjournaled execution. Before
Git it consumes the accepted configured contract, derives the verified-existing-code,
external-memory, and ledger plan, normalizes the required explicit messages, and creates or resumes
the exact direct-landing generation. Under
`integration_authority_lock(config.coordination_root, contract.repo_name)` it re-loads the
contract (a changed contract refuses `direct-landing-contract-changed`), then applies the already
validated plan. This lock serialization is concurrency control, not crash durability.

`_verify_code_commit` proves the exact commit is the current series branch HEAD (`branch_commit`),
resolves its tree, and — when `candidate_tree` is given (the staged candidate the owner gated
through the Dagger `--source`/`--repository-bundle` contract) — refuses a moved tree
(`direct-landing-candidate-tree-moved`), keeping the gate strictly pre-commit (L16-R7).
`_memory_facts` reads external-memory + ledger facts for preview. Apply now enters
`_start_or_observe_direct_landing`, which creates or resumes one root-journal generation and calls
the focused `integration/direct_landing_*` owners. Those owners preserve accepted repository/input
identity, write intent before memory and ledger mutation, journal each produced commit, and resume
the same generation across crash cuts or unreadable-ledger recovery.

### Conventions

The sequence uses a direct-landing record in the same canonical root journal architecture while
retaining its own typed input and ledger-intent vocabulary: journal intent → memory
`commit_if_dirty` → journal memory proof → ledger intent/write/commit → journal ledger proof.
The code commit is verified, never created. No generated subject, message fallback, or repeat-from-
scratch recovery exists.

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
- A memory commit followed by a crash or ledger conflict remains attached to the same journal
  generation and must reconcile/recover before any successor attempt.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The policy-gated coordinator consumes the admitted contract and one journal generation. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:111-123 |
| Journaled memory/ledger execution and recovery own all partial-output cuts. | `execute_direct_landing`; `execute_or_require_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:68-105; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:108-165 |
| The same ledger semantics the worktree path uses. | `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:229-296 |
| The application boundary performs closed configured-contract admission and typed projection. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:51-94 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Direct Landing Boundary

Direct landing normalizes memory and ledger messages before journal publication, landing-lock
acquisition, or Git. Its code leg is verified-existing/not-applicable. Preview and apply expose the
same stripped `effectiveInput`, and apply uses those exact messages with no generated subjects or
fallbacks. L2 supersedes the deferred-durability clause: memory and ledger remain sequential, while
the canonical journal records intent/proof and resumes the same generation after partial output.

## 260821-CLIVE-L2 Current Contract

The current source seams include `DirectLandingRequest`, `direct_landing`, `require_direct_landing_enabled`. The L2 candidate preserves this file at its existing altitude while routing lifecycle authority through the canonical root journal and the closed configured-contract admission boundary.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `DirectLandingRequest`, `direct_landing`, `require_direct_landing_enabled` at this ownership boundary. | L84-L98; L111-L123; L126-L134 | `mcp/src/agents_remember/worktrees/direct_landing.py` |

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R7/R8 — the direct landing operation:
  code-commit verification plus sequential memory and ledger commits under the integration
  authority lock, with the strictly pre-commit staged-candidate gate. Verified at code commit
  a9d50e08; the crash-durability boundary was clarified by 260821-CLIVE-L1.
