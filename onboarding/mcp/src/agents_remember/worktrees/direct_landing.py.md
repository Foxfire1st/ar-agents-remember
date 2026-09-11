# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T12:02+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The durable branch-addressed counterpart of worktree closeout commit execution for a sanctioned
leaf implemented without its own worktree enclosure. It is not ordinary master/series closeout or
master-to-parent integration. It binds the task-root series contract, consumes the exact closed admission result,
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

Under CCR-R03@v1 the claimed direct-landing operation carries its typed dependency declaration
(`lifecycle_operation_dependencies`). Since the closeout-door cut (commit `fad9808e`) that binding no
longer includes a door: a direct landing is admitted by its own request — the series contract, the
branch HEAD commit and tree, and the effective commit messages — not by a claimed closeout door. All
five former door reads are gone, `_claim_waiting_direct_landing` no longer exists, and the record
carries no `doorPublication`.

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
- A series-shaped contract is necessary but not sufficient: the route is only for an explicitly
  selected leaf delivery without an enclosure. Ordinary series closeout and integration never
  become direct execution and never require `directExecutionEnabled`.
- The gate stays strictly pre-commit via `candidate_tree`; commit-then-gate is the accepted-risk
  exception only where the developer rules it (documented, L16-R7).
- External memory only for apply; internal/disabled memory refuses
  (`direct-landing-memory-required`).
- A memory commit followed by a crash or ledger conflict remains attached to the same journal
  generation and must reconcile/recover before any successor attempt.
- Observing an existing action-required journal is a public refusal (`ok: false`, `state: refused`)
  with the lifecycle operation nested; intermediate journal states never escape as top-level
  direct-landing outcomes.
- The claimed direct-landing operation is admitted by its own request; no declared closeout-door
  dependency is bound before persistence.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The policy-gated coordinator consumes the admitted contract and one journal generation. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:117-129 |
| Journaled memory/ledger execution and recovery own all partial-output cuts. | `execute_direct_landing`; `execute_or_require_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:73-110; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:113-170 |
| The same ledger semantics the worktree path uses. | `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:236-303 |
| The application boundary performs closed configured-contract admission and typed projection. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:55-104 |
| R03 dependency binding is gone from the direct-landing claim: a fresh generation is admitted by the request itself (series contract, branch HEAD commit and tree, effective commit messages) and carries no door publication. | `_create_direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:473-507 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `DirectLandingRequest`, `direct_landing`, `require_direct_landing_enabled` at this ownership boundary. | `DirectLandingRequest`; `direct_landing`; `require_direct_landing_enabled` | mcp/src/agents_remember/worktrees/direct_landing.py:89-104; mcp/src/agents_remember/worktrees/direct_landing.py:117-129; mcp/src/agents_remember/worktrees/direct_landing.py:132-140; mcp/src/agents_remember/worktrees/direct_landing.py:147-155 |

## 260821-DAGQC-L2 Action-Required Outcome

When the root journal already requires recovery or operator action, the coordinator preserves that
durable operation evidence but returns a closed refused direct-landing outcome. This prevents a
running/action-required journal state from masquerading as success while retaining the exact nested
generation a caller must recover.


## PDLS Reconciliation

Direct landing now attaches the durable lifecycle operation projection to successful and convergent responses through one helper; it does not add a fallback route.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.

## 260831-CCR-R03 Dependency-Declared Direct Landing

The claimed direct-landing generation carries `lifecycle_operation_dependencies`, binding the
candidate, plan, and input (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md). The admitted door was dropped from that binding by
the closeout-door cut (commit `fad9808e`). That dependency declaration is no longer bound on the
direct-landing path: `_create_direct_landing` admits a fresh generation from the request itself and
the record carries no `doorPublication`.

## Update History
- 2026-09-11T23:05:00+00:00: Repaired the R03 claim, which anchored `_claim_waiting_direct_landing` at lines 678-701 of a 576-line file. That helper no longer exists anywhere in the tree and the closeout-door cut (commit `fad9808e`) already removed the door reads; `_create_direct_landing` (473-507) now admits a fresh generation from the request itself (series contract, branch HEAD commit and tree, effective commit messages) with no door publication and no bound `lifecycle_operation_dependencies`.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `direct_landing` repointed to mcp/src/agents_remember/worktrees/direct_landing.py:117-129. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that all five door reads are gone and admission is now the request itself plus the `directExecutionEnabled` policy gate; replaced the `_claim_waiting_direct_landing` binding claim with the current dependency declaration (candidate, plan, input — no door). Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the direct-landing claim dependency binding and its launch/currentness re-requirement; prior policy-gated and journaled-execution prose preserved.

- 2026-08-31T20:30+02:00 — 260831-DER: made the direct-execution boundary explicit. Direct landing
  is the policy-gated delivery route for a leaf intentionally implemented without its own enclosure;
  ordinary series/master closeout and integration remain lifecycle operations and do not use the
  direct-execution flag.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: normalized existing action-required journal observation to the closed public refused outcome while retaining nested lifecycle evidence. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R7/R8 — the direct landing operation:
  code-commit verification plus sequential memory and ledger commits under the integration
  authority lock, with the strictly pre-commit staged-candidate gate. Verified at code commit
  a9d50e08; the crash-durability boundary was clarified by 260821-CLIVE-L1.