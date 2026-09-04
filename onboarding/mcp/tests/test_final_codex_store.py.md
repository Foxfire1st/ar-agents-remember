# mcp/tests/test_final_codex_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 store tests for the two-fresh CAS run-manifest owner (leaf 260831-CCR-L14, code commit 54ff803a). Covers reservation with retry disabled for the exact same plan, in-flight refusal, exact slot ordering, the immutable digest chain, terminalization only after both repetitions publish, namespace isolation, and corrupt-file fail-closed reads. Fully standalone: imports only the leaf-local builder module and the package under test.

## Code Commentary

### Logic

`gate4` (lines 35-38), `draft` (lines 39-49), and `publish_two` (lines 50-57) build the fixtures. `FinalCodexStoreTests` (lines 58-154) covers: reserve then publish the two repetitions advancing the manifest (59-79); retry disabled for the exact same plan (80-87); a second live attempt refused (88-96); fixed-order slot publication (97-112); drafts binding the reserved identity (113-128); corrupt manifests failing closed (129-139); namespace collision refusal (140-148); and candidates keeping separate manifests (149-154).

### Conventions

Every refusal asserts typed `CertificationContractError` codes (`final-codex-already-in-flight`, `final-codex-retry-disabled`, `final-codex-repetition-out-of-order`, `final-codex-manifest-corrupt`, `final-codex-namespace-collision`, ...).

### Invariants And Boundaries

- One candidate manifest file with immutable gapless slots and self-verified digests.
- The final-codex namespace can never overlap a forbidden certifying or diagnostic quality-report root.
- The attempt becomes terminal only when both fresh repetitions publish.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the durable two-fresh CAS run manifest; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retry is disabled and publication is exact-order and immutable. | `FinalCodexStoreTests` | mcp/tests/test_final_codex_store.py:58-154 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the durable CAS run store public and guarded internals. | `FinalCodexManifestStore` | mcp/src/agents_remember/certification/final_codex/store.py:62-274 |
| Store builders are shared with the diff-coverage closure module. | `attempt_record`; `make_store`; `publish_two` | mcp/tests/test_final_codex_models.py:341-368; mcp/tests/test_final_codex_models.py:468-479; mcp/tests/test_final_codex_store.py:50-57 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 durable store suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
