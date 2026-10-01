# mcp/src/agents_remember/certification/final_codex/store.py

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

## Evidence

### Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

- Reservation and publication enforce the exact fixed two-slot order with retry disabled. [1]

### Repo-Internal References

- Atomic manifest writes reuse the kernel atomic-write helper. [2]
- The manifest and record contracts are defined in the final-codex models. [3]
- The namespace isolation guard keeps final-codex manifests disjoint from certifying and diagnostic roots. [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The store stays repository-neutral and is consumed by the trusted R12 launcher through the run controller. [5]
