# mcp/tests/test_diagnostic_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 durable diagnostic manifest store tests (leaf 260831-CCR-L13, code commit 4ba18bb2). The store owns one stable manifest per exact candidate in an isolated namespace: immutable attempts and results, gapless chain identity, newest-terminal selection, in-flight refusal, and namespace isolation from the certifying quality-report manifest. Every case uses temporary directories and no Dagger or external service.

## Code Commentary

### Logic

The suite is registered in the `unit-regression` lane. Its helpers build environment/authority bindings, evidence, teardown records, attempts, failure records, and terminal drafts (lines 45-153) and construct a store under a forbidden quality-report root (lines 156-163). `DiagnosticStoreTests` (lines 170-359) covers: an empty optional lane before any request (lines 171-177); the reserve/run/publish sequence advancing the manifest (lines 179-202); an in-flight attempt blocking a fresh request (lines 204-213); attempt-number mismatch refusal (lines 215-222); double terminalization refusal (lines 224-234); wrong state transitions and wrong nonce refusal (lines 236-241); newest-terminal selection with immutable chain links (lines 243-266); full candidate isolation (lines 268-280); abandon clearing only the newest never-started slot (lines 282-298); manifest corruption failing closed (lines 300-318); namespace collision with the certifying manifest root (lines 320-336); the store never writing a not-requested-optional marker (lines 338-350); and fail-closed behavior when a live attempt has no manifest (lines 352-359).

### Conventions

All refusals are asserted through typed `CertificationContractError` finding codes (diagnostic-already-in-flight, diagnostic-attempt-number-mismatch, diagnostic-attempt-not-running, diagnostic-nonce-mismatch, diagnostic-manifest-corrupt, diagnostic-namespace-collision, diagnostic-manifest-missing).

### Invariants And Boundaries

- One candidate manifest file with gapless immutable attempts/results and intact predecessor chains.
- The store namespace can never overlap the certifying quality-report manifest.
- The empty lane is represented by absence, never by a not-requested-optional marker.
- Corrupt or tampered manifests fail closed on revalidation.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) requires the durable isolated per-candidate manifest; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store namespace is isolated from the certifying quality-report manifest and never writes an optional marker. | `DiagnosticStoreTests.test_namespace_collision_with_the_certifying_manifest_is_refused` | mcp/tests/test_diagnostic_store.py:320-336 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the durable manifest store public and guarded internals. | `DiagnosticManifestStore` | mcp/src/agents_remember/certification/diagnostics/store.py:53-288 |
| Store builders are shared with the diff-coverage closure module. | `store_attempt`; `store_terminal_draft` | mcp/tests/test_diagnostic_diff_coverage.py:96-97 |

## Update History

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 durable store suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
