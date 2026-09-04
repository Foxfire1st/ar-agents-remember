# mcp/tests/test_final_codex_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 leaf builders and model contract tests (leaf 260831-CCR-L14, code commit 54ff803a). This module owns the leaf scenario-registry and record builders the other final-codex test modules share, plus the closed two-fresh model/invariant contract tests. Fully standalone: it imports only the package under test and stdlib/pytest, and every case runs in-process with no Dagger or external service.

## Code Commentary

### Logic

Builders: `scenario_registry` (lines 168-193) canonicalizes the leaf scenario rail registry; `certifying_plan` (lines 195-202) compiles the certifying plan; `green_gates` (lines 256-260) and `manifest_for` (lines 203-255) build the green Gate-1..3 result manifests; `plan_record` (lines 316-340), `attempt_record` (lines 341-368), `fresh_identities` (lines 312-315), `environment_binding` (lines 369-375), `authority_binding` (lines 376-400), `teardown_record` (lines 401-425), `make_draft` (lines 426-467), `make_store` (lines 468-479), `publish_run` (lines 480-494), and `finalize_result` (lines 495-508) compose the two-fresh fixtures; the fake Dagger inspector (`FakeInspector`, lines 513-543) and `engine_environ` (lines 545-559) back the executor tests; `store_codes` (lines 509-512) extracts refusal codes. `FinalCodexModelTests` (lines 619-725) covers the structural certifying literals and retry-zero (lines 620-630), distinct-fresh-identity enforcement (631-635), self-verified plan/digest records, manifest-required pass/fail, no-manifest aborted/hard failures, green-only-when-both-pass (673-687), no-compensation (688-699), shared-authority enforcement (700-714), and draft digest self-verification (715-725).

### Conventions

All refusals assert typed `CertificationContractError` codes; every digest-carrying record verifies its own content digest.

### Invariants And Boundaries

- Exactly two fresh distinct certifying repetitions with retryCount zero.
- One passing repetition never compensates the other.
- Pass/fail carry the complete certifying Gate-4 manifest; aborted/hard-failure never do.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the closed two-fresh model semantics; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two-fresh no-compensation and structural literal contracts are enforced at the model layer. | `FinalCodexModelTests` | mcp/tests/test_final_codex_models.py:619-725 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the closed final-codex model contracts. | `FinalCodexRunManifest`; `FinalCodexRepetitionResult` | mcp/src/agents_remember/certification/final_codex/models.py:333-373; mcp/src/agents_remember/certification/final_codex/models.py:376-413 |
| The leaf builders are shared by every other final-codex test module. | `scenario_registry`; `attempt_record`; `make_draft` | mcp/tests/test_final_codex_models.py:168-193; mcp/tests/test_final_codex_models.py:341-368; mcp/tests/test_final_codex_models.py:426-467 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 builder/model-contract suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
