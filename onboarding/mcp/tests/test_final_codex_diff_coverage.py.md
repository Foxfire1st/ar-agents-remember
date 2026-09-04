# mcp/tests/test_final_codex_diff_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_diff_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 run-2 diff-coverage closure tests (leaf 260831-CCR-L14, code commit 54ff803a). Closes the run-1 python-diff-coverage gap for the changed final-codex modules: every uncovered line and untaken branch of certification/final_codex/{models,store,planning,projection,certificate}.py and worktrees/modules/quality/final_codex_executor.py is exercised with real model construction, store round-trips, and engine admissions - never by changing production code. The module is fully standalone: it imports only the package under test, stdlib/pytest, and the leaf's own shared builders.

## Code Commentary

### Logic

The module reuses the leaf's shared builders plus module-level fixture helpers (`teardown_evidence`, `two_pass_results`, `manifest_dict`, `green_manifest_dict`, `rebound_result`, `predecessor_identities`, lines 103-175) and then closes refusal and boundary gaps in seven class blocks: `FinalCodexModelRefusalClosureTests` (176-382), `FinalCodexRunManifestClosureTests` (383-500), `FinalCodexStoreClosureTests` (501-639), `FinalCodexProjectionClosureTests` (640-707), `FinalCodexPlanningClosureTests` (708-853), `FinalCodexCertificateClosureTests` (854-984), and `FinalCodexExecutorClosureTests` (985-1053) - including the abort-continues-past-an-already-published-slot arm and the default clock/nonce helpers.

### Conventions

Coverage is closed through real behavior only; no production line is edited to make a test pass.

### Invariants And Boundaries

- The module is a diff-coverage closure for the leaf change-set, not a second contract catalog.
- Every case stays in-process with temporary directories and fake inspection.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the final real-codex lane and its diff-coverage closure; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The closure exercises every uncovered final-codex module surface in-process. | `FinalCodexModelRefusalClosureTests`; `FinalCodexExecutorClosureTests` | mcp/tests/test_final_codex_diff_coverage.py:176-382; mcp/tests/test_final_codex_diff_coverage.py:985-1053 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closes coverage over the changed final-codex production modules. | `final_codex`; `final_codex_executor` | mcp/src/agents_remember/certification/final_codex/models.py:1-491; mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:1-679 |
| Reuses the leaf's shared builders without importing other test suites. | `attempt_record`; `make_draft`; `make_store` | mcp/tests/test_final_codex_models.py:341-368; mcp/tests/test_final_codex_models.py:426-467; mcp/tests/test_final_codex_models.py:468-479 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 diff-coverage closure suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
