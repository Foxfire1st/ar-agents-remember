# mcp/tests/test_diagnostic_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 diagnostic contract tests for the closed models and invariants (leaf 260831-CCR-L13, code commit 4ba18bb2). It proves the structural separation that makes diagnostics non-certifying by construction: acceptanceEligible/certifying false literals, outcome/manifest shape rules, immutable attempt/manifest chains, namespace isolation, and promotion refusal. It imports only the package under test plus stdlib/pytest - no test-support modules - so the evidence-lifecycle catalog observes no transitive test-support consumers.

## Code Commentary

### Logic

The suite is registered in the `unit-regression` lane (test-evidence-lanes.toml). Its scenario builders mirror the canonical portable registry: `RailSpec` (lines 82-96), `_rail` (lines 103-159) builds one rail definition over the certifying (portable-ci) and diagnostic (diagnostic-ci) profiles, `scenario_registry` (lines 162-181) canonicalizes the five-gate registry with the diagnostic profile planning gates 1-4, `certifying_plan`/`diagnostic_plan` (lines 184-208) compile the altitude plans, `manifest_for` (lines 211-260) builds green/red gate result manifests, and the draft/finalize helpers (lines 263-399) construct attempts, plans, bindings, drafts, and content-bound results.

`ModelContractTests` (lines 402-681) covers: structural non-certifying result with the R16 nonce (lines 403-414); extra-field refusal on every record (lines 416-430); literal promotion refusal for certifying/acceptanceEligible (lines 432-437); pass/fail requiring the complete diagnostic-altitude manifest (lines 439-443); fail requiring its exact scenario failure (lines 445-462); scenario failure naming the exact checkpoint rail (lines 464-472); typed infrastructure/parser hard failures (lines 474-500); bounded hard-failure evidence (lines 502-510); no failure record on aborted/pass (lines 512-521); altitude/gate manifest matching (lines 523-541); a green pass still not acceptance-eligible (lines 543-553); content-bound result/attempt digests (lines 555-564); nonce pattern and attempt numbers (lines 566-574); artifacts confined to the diagnostic namespace (lines 576-593); gapless immutable run-manifest chains (lines 605-624); broken-chain and mixed-nonce refusal (lines 626-650); gapless-prefix refusal (lines 652-661); plan-record digest verification (lines 663-672); and JSON dumps carrying no delivery/closeout/operation identity fields (lines 674-681). `ForbiddenOverreachTests` (lines 684-725) proves a certifying-altitude manifest cannot be promoted into a diagnostic outcome.

### Conventions

Every negative case asserts through `pydantic.ValidationError` or typed code checks; builders reuse the canonical certification models rather than duplicating registry logic.

### Invariants And Boundaries

- Diagnostic results are structurally non-certifying: acceptanceEligible/certifying are false literals and extra delivery/closeout identity fields are forbidden.
- Pass/fail embed a complete diagnostic-altitude manifest; aborted/hard-failure never do; failures are typed and bounded.
- Manifest attempts/results are gapless immutable chains with unique nonces and intact predecessor links.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The CCR-R13@v2 packet (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) requires structural rather than conventional separation; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostic records must be non-certifying by construction and immune to promotion. | `test_promotion_to_acceptance_or_certifying_literals_is_refused` | mcp/tests/test_diagnostic_models.py:432-437 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the models of the diagnostics package directly. | `DiagnosticRunResult`; `DiagnosticAttemptRecord`; `DiagnosticRunManifest` | mcp/src/agents_remember/certification/diagnostics/models.py:149-177; mcp/src/agents_remember/certification/diagnostics/models.py:295-344; mcp/src/agents_remember/certification/diagnostics/models.py:347-375 |
| Uses the canonical portable five-gate registry to build altitude plans. | `scenario_registry`; `compile_certification_plan` | mcp/tests/test_diagnostic_models.py:162-208 |
| The manifest/plan/result builders are reused by the sibling diagnostic suites and the diff-coverage closure module. | `test_diagnostic_models` | mcp/tests/test_diagnostic_diff_coverage.py:80-98 |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 model-contract suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
