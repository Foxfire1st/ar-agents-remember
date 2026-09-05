# mcp/src/agents_remember/certification/diagnostics/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/diagnostics/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the closed, immutable vocabulary of the CCR-R13 optional non-certifying diagnostic E2E lane (leaf 260831-CCR-L13, code commit 4ba18bb2). CCR-R13 allows at most one real-Codex replication of the canonical ARSPAWN scenario as explicitly non-certifying diagnostic evidence after the exact candidate's R12 Gates 1-3 are green. These records make the separation structural rather than conventional: every result and artifact carries acceptanceEligible=false and certifying=false and binds the exact candidate, diagnostic plan version, environment identity, R12 runtime-authority snapshot digest, and the R16 diagnostic nonce; no record can name a delivery attempt, closeout operation generation, door claim, or accepted certification state; pass/fail outcomes embed the complete diagnostic-altitude gate result manifest while aborted and hard-failure outcomes carry teardown evidence but never a pass; and infrastructure/parser failures remain typed hard diagnostic failures.

## Code Commentary

### Logic

Type aliases (lines 42-44) fix the four dispositions (pass/fail/aborted/hard-failure), the three failure classes (scenario/infrastructure/parser), and the three attempt states (reserved/running/terminal). Frozen contracts in the certification-domain style follow, each digest-verifying its own content:

- `DiagnosticArtifact` (lines 66-73) - one content-addressed artifact with a diagnostic-only namespace literal.
- `DiagnosticFailureRecord` (lines 76-92) - a scenario failure must name the exact checkpoint rail (lines 88-89); infrastructure/parser failures require bounded evidence (lines 90-91).
- `DiagnosticTeardownRecord` (lines 95-106) - an owner release requires bounded teardown evidence (lines 102-105).
- `DiagnosticRuntimeAuthorityBinding` (lines 109-132) - the frozen R12 host runner/store snapshot copy; a binding, never an authority of its own, with self-verified bindingDigest (lines 127-132).
- `DiagnosticEnvironmentBinding` (lines 135-146) - one frozen environment identity/digest pair (digest verified lines 141-146).
- `DiagnosticAttemptRecord` (lines 149-177) - one immutable in-flight or terminal reservation slot binding attempt number, R16 diagnostic nonce, candidate, and plans before any scenario step starts (digest verified lines 172-177).
- `DiagnosticPlanRecord` (lines 180-205) - one immutable diagnostic-plan identity binding the canonical registry, certifying and diagnostic plan digests, profile, scenario gate, and frozen plan version.
- Outcome shape helpers (lines 208-256) enforce manifest carriage, failure carriage, and manifest binding: pass/fail require the complete diagnostic-altitude manifest whose disposition matches and whose gate/candidate match the result; aborted/hard-failure never embed a manifest; fail requires its exact scenario failure; hard-failure requires a typed infrastructure/parser failure.
- `DiagnosticRunResultDraft` (lines 259-292) - a terminal outcome before the store binds its chain identity (no predecessorDigest/resultId).
- `DiagnosticRunResult` (lines 295-344) - one immutable terminal result with acceptanceEligible/certifying as structural false literals (lines 320-321), optional diagnostic-altitude manifest, typed failure, teardown, and self-verified resultDigest (lines 334-339) plus outcome-shape revalidation (lines 341-344).
- `DiagnosticRunManifest` (lines 347-375) - one stable projection over a candidate's durable attempt journal with newestTerminal property (lines 363-365) and three model validators (lines 378-409): gapless attempt-number prefix with unique nonces (lines 378-385), gapless result prefix with intact predecessorDigest chain (lines 388-396), and terminal cross-check tying every result to its terminal attempt slot and exact nonce (lines 399-408).

### Conventions

All records subclass `FrozenContractModel`, so extra fields are rejected; every digest-bearing record verifies its own content digest on validation. Literal types keep certifying/acceptance-eligible facts out of reach by construction.

### Invariants And Boundaries

- No diagnostic record can be promoted into an accepted or certifying one: acceptanceEligible and certifying are structural false literals.
- A scenario pass or fail embeds the complete diagnostic-altitude gate result manifest for the exact gate and candidate; aborted and hard-failure outcomes carry teardown evidence and never a pass.
- Attempt numbers are gapless per candidate; result chain predecessor links are immutable and revalidated on every read.
- The runtime-authority binding only copies the frozen R12 snapshot; it never selects, replaces, or provisions an engine or layer store.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The approved CCR-R13@v2 packet (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the leaf doc 13_non-certifying-diagnostic-e2e.md carry the lane clauses; task artifacts are recorded as prose because their paths are not repo-relative citations.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane may run at most one real-Codex replication as non-certifying evidence after R12 Gates 1-3 are green, and no diagnostic evidence can satisfy or promote into R14. | `DiagnosticRunResult`; `acceptanceEligible` | mcp/src/agents_remember/certification/diagnostics/models.py:295-344; mcp/src/agents_remember/certification/diagnostics/models.py:320-321 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary reuses the certification-domain frozen-model base, candidate identity, gate identity, manifest, and evidence contracts. | `FrozenContractModel`; `CandidateIdentity`; `GateResultManifest` | mcp/src/agents_remember/certification/models.py:46-67; mcp/src/agents_remember/certification/models.py:52-58; mcp/src/agents_remember/certification/models.py:457-501 |
| Content digests follow the shared certification digest helper. | `content_digest` | mcp/src/agents_remember/certification/digests.py:1-22 |
| The public package facade re-exports every model here. | `__all__`; `DiagnosticRunManifest`; `DiagnosticRunResult`; `DiagnosticAttemptRecord` | mcp/src/agents_remember/certification/diagnostics/__init__.py:11-25; mcp/src/agents_remember/certification/diagnostics/__init__.py:43-67 |
| The durable store serializes and revalidates these records on every read and write. | `_read_manifest`; `_update`; `_canonical_bytes` | mcp/src/agents_remember/certification/diagnostics/store.py:228-264; mcp/src/agents_remember/certification/diagnostics/store.py:414-420 |
| The run controller builds attempt records, drafts, and runtime bindings from these models. | `_attempt_record`; `_draft` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:434-516 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R12 runtime-authority snapshot is the only host identity a diagnostic result binds. | `DiagnosticRuntimeAuthorityBinding` | mcp/src/agents_remember/certification/diagnostics/models.py:109-132 |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 closed diagnostic vocabulary delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).