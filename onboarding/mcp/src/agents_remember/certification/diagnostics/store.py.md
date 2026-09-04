# mcp/src/agents_remember/certification/diagnostics/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/diagnostics/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Durable, content-addressed owner of the one stable diagnostic manifest per exact candidate for the CCR-R13 non-certifying diagnostic lane (leaf 260831-CCR-L13, code commit 4ba18bb2). It keeps every attempt and terminal result inside one candidate manifest file in an isolated namespace that can never overwrite or satisfy the certifying quality-report manifest. Each mutation is an atomic read-modify-write with a compare after the write, so a concurrent publisher either converges on the newest state or fails closed with a typed CAS refusal; earlier results are never deleted, rewritten, reset to not-requested-optional, or mutated into certification.

## Code Commentary

### Logic

- `DiagnosticStorePolicy` (lines 44-50) is the frozen isolation/durability policy: store id, forbidden certifying roots, and CAS retry count (default 5).
- `DiagnosticManifestStore` (lines 53-288) opens one isolated durable namespace per candidate (constructor lines 56-59, `_require_isolated_namespace` lines 273-288 refusing any overlap with a forbidden certifying quality-report root).
- Read surface (lines 63-87): `manifest` fully revalidates the stored candidate manifest, `newest_terminal` returns its newest terminal result, `live_attempt` returns the newest non-terminal attempt, `next_attempt_number` derives the gapless next slot, and `has_attempts` reports attempt presence. Absence is represented by no file and a None read, never by a not-requested-optional marker.
- Write surface (lines 91-224): `reserve` (lines 91-114) refuses a live in-flight attempt (`diagnostic-already-in-flight`) and enforces the exact next attempt number (`diagnostic-attempt-number-mismatch`); `mark_running` (lines 116-143) advances only the exact reserved slot (`diagnostic-attempt-nonce-mismatch`, `diagnostic-attempt-state-transition`) and read-backs the running record; `publish_terminal` (lines 145-185) requires the exact running attempt (`diagnostic-attempt-not-running`), verifies the draft binds the attempt identity (`diagnostic-draft-attempt-mismatch`, lines 304-334), computes the chain predecessor from the newest retained result, and finalizes one immutable result (`_finalize_result`, lines 370-381); `abandon` (lines 187-224) drops only the newest never-started live slot (`diagnostic-attempt-not-abandonable`, `diagnostic-attempt-not-newest`) and can never erase or rewrite a terminal result.
- `_update` (lines 228-246) runs every mutation as an atomic read-modify-write: canonical bytes are written with the shared atomic writer and the file is read back and compared, retrying under the policy and failing closed with `diagnostic-manifest-cas-collision` on non-convergence.
- `_read_manifest` (lines 248-264) fails closed (`diagnostic-manifest-corrupt`) on corrupt, non-object, or digest-invalid stored payloads.
- State-transition helpers (lines 337-367) allow only reserved-to-running and running-to-terminal and re-digest the mutated attempt.
- Manifest builder and canonical bytes (lines 397-420) render sorted compact JSON with the schema `diagnostic-run-manifest/v1` constant (line 40).

### Conventions

All refusals raise `CertificationContractError` with typed finding code/path/detail. Every manifest file lives under a content-addressed candidate directory (lines 269-271) so candidates are fully isolated.

### Invariants And Boundaries

- One candidate manifest file holds gapless immutable attempts and results; earlier records are never deleted, rewritten, or promoted.
- The store namespace can never overlap a certifying quality-report manifest root.
- Concurrent writers converge on one stable state or fail closed with a typed CAS refusal.
- The empty lane is represented by absence; the store never writes a not-requested-optional marker.
- Only the exact running attempt may publish a terminal; only the newest live slot may be abandoned; no double terminalization.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) requires one stable diagnostic manifest per exact candidate in an isolated namespace; task artifact paths are not repo-relative citations, so the clause is recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store must keep one stable manifest per exact candidate that never overwrites or satisfies the certifying quality-report manifest. | `DiagnosticManifestStore._require_isolated_namespace` | mcp/src/agents_remember/certification/diagnostics/store.py:273-288 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Atomic read-modify-write uses the shared kernel atomic writer. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:1-80 |
| Digest helpers and typed findings come from the certification contract foundation. | `content_digest`; `CertificationContractFinding` | mcp/src/agents_remember/certification/digests.py:1-22; mcp/src/agents_remember/certification/models.py:120-180 |
| The store revalidates the frozen records defined in the diagnostics models. | `DiagnosticRunManifest`; `DiagnosticAttemptRecord` | mcp/src/agents_remember/certification/diagnostics/models.py:149-177; mcp/src/agents_remember/certification/diagnostics/models.py:347-375 |
| The run controller publishes attempt and terminal results exclusively through this store. | `DiagnosticExecutionEngine` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:176-267 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store is filesystem-local and repository-neutral; no Dagger, service, or external store is touched. | `DiagnosticManifestStore._update` | mcp/src/agents_remember/certification/diagnostics/store.py:228-246 |

## Update History

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 durable diagnostic manifest store delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
