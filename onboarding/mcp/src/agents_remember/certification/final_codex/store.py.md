# mcp/src/agents_remember/certification/final_codex/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Durable, content-addressed owner of one two-repetition Gate-4 run (leaf 260831-CCR-L14, code commit 54ff803a). CCR-R14@v3 requires one stable certifying run per exact candidate holding exactly two fresh no-retry certifying repetitions in fixed slot order. The store keeps every attempt and repetition result inside one candidate manifest file; each mutation is an atomic read-modify-write with a compare after the write, so a concurrent publisher either converges on the newest state or fails closed with a typed CAS refusal.

## Code Commentary

### Logic

- `FinalCodexStorePolicy` (lines 53-59) fixes the store id, forbidden roots, and CAS retry budget.
- `FinalCodexManifestStore` (lines 62-274) is the isolated durable namespace:
  - reads (`manifest`, `live_attempt`, `attempt_number`, lines 72-91) fully revalidate the stored manifest;
  - `reserve` (lines 95-135) refuses a second live attempt, a terminal same-plan retry (retry disabled), and a successor attempt that is not the exact next attempt number; the first attempt must be number one;
  - `mark_running` (lines 137-159) transitions the exact reserved attempt to running;
  - `publish_repetition` (lines 161-210) atomically binds the chain identity and publishes one repetition slot, refusing an already-published slot, an out-of-order slot, a draft that does not bind the exact running attempt, or a draft whose fresh identity differs from the reservation; publishing the second slot terminalizes the attempt.
- Internals: `_update` (lines 214-232) is the retried atomic write with post-write compare; `_read_manifest` (lines 234-250) fails closed on corrupt payloads; `_require_isolated_namespace` (lines 259-274) refuses a store root overlapping any forbidden certifying/diagnostic quality-report root.
- State-transition guards (`_advance_attempt_state`/`_allowed_transition`, lines 346-374) allow only reserved-to-running-to-terminal.
- `_finalize_result` (lines 377-384) derives the result id and self-digest from the published draft.

### Conventions

Every refusal is a typed `CertificationContractError` under the `final-codex-` code family via `_raise_store` (lines 430-435).

### Invariants And Boundaries

- Retry is disabled: a live attempt refuses any second admission and a terminal same-plan attempt refuses a successor; a code/config/runtime repair changes the plan identity.
- Repetition results are immutable and occupy the exact ordered slots one and two; no slot can be rewritten, reordered, or promoted.
- The attempt becomes terminal only when both fresh repetitions publish; a partial run can never be converted into a pass.
- Earlier results are never deleted, reset, or mutated into a different disposition.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Reservation and publication enforce the exact fixed two-slot order with retry disabled. | `reserve`; `publish_repetition` | mcp/src/agents_remember/certification/final_codex/store.py:95-135; mcp/src/agents_remember/certification/final_codex/store.py:161-210 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Atomic manifest writes reuse the kernel atomic-write helper. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:51-70 |
| The manifest and record contracts are defined in the final-codex models. | `FinalCodexRunManifest`; `FinalCodexAttemptRecord`; `FinalCodexRepetitionResult` | mcp/src/agents_remember/certification/final_codex/models.py:202-242; mcp/src/agents_remember/certification/final_codex/models.py:333-373; mcp/src/agents_remember/certification/final_codex/models.py:376-413 |
| The namespace isolation guard keeps final-codex manifests disjoint from certifying and diagnostic roots. | `FinalCodexStorePolicy` | mcp/src/agents_remember/certification/final_codex/store.py:53-59 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store stays repository-neutral and is consumed by the trusted R12 launcher through the run controller. | `FinalCodexManifestStore` | mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:179-600 |

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `atomic_write_bytes` repointed to mcp/src/agents_remember/kernel/atomic_write.py:51-70. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 durable CAS run store delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
