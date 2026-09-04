# mcp/src/agents_remember/certification/final_codex/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Closed immutable contracts for the final real-Codex Gate-4 certification lane (leaf 260831-CCR-L14, code commit 54ff803a). CCR-R14@v3 requires exactly two fresh independent no-retry certifying repetitions of the exact candidate's canonical scenario before one bound Gate-4 certificate can publish. Every record mirrors the frozen-contract style of the certification domain and makes the R14 semantics structural rather than conventional: terminal repetition results carry acceptanceEligible=true and certifying=true literals, retryCount is a fixed zero literal, retry is disabled (no successor slot for the same plan), one passing repetition can never compensate the other, and diagnostic (CCR-R13) evidence has no shape that can enter this lane.

## Code Commentary

### Logic

- `CERTIFYING_GATE` and `REPETITION_COUNT` (lines 66-67) fix gate 4 and the two-slot repetition budget.
- `FinalCodexArtifact` (lines 70-77) is one content-addressed artifact in the isolated final-codex namespace.
- `FinalCodexFailureRecord` (lines 80-96) is the typed scenario/infrastructure/parser failure; scenario failures name the failing checkpoint rail, infrastructure/parser failures require bounded evidence.
- `FinalCodexTeardownRecord` (lines 99-113) carries exact-owner release plus process cleanliness with bounded evidence.
- `FinalCodexRuntimeAuthorityBinding` (lines 116-139) is the frozen R12 host runner/store snapshot copied into every certifying result - a binding, never an authority; it verifies its own digest.
- `FinalCodexEnvironmentBinding` (lines 142-153) freezes the environment identity/digest.
- `FinalCodexRepetitionIdentity` (lines 156-170) is one fresh client/process identity per repetition; the two repetitions must stay distinct.
- `FinalCodexPlanRecord` (lines 173-199) freezes the certifying-plan identity (registry, certifying plan, Gate-4 plan, scenario/plan version, profile) with self-verified digest.
- `FinalCodexAttemptRecord` (lines 202-242) is the immutable in-flight/terminal reservation carrying both fresh repetition identities in fixed order; the two identities must be distinct.
- `FinalCodexRepetitionResultDraft` (lines 300-330) and `FinalCodexRepetitionResult` (lines 333-373) are terminal outcomes: pass/fail embed the complete certifying Gate-4 result manifest with matching disposition, aborted/hard-failure embed no manifest, and the shape validators (`_require_outcome_shape` family, lines 245-297) enforce the carrier rules.
- `FinalCodexRunManifest` (lines 376-413) holds the reserved attempt plus both terminal repetition results in fixed slot order; the derived `aggregate` is green only when both pass with distinct fresh identities under one exact plan/runtime authority/environment; `complete` means both slots published.
- Manifest validators (lines 416-471) enforce candidate binding, gapless fixed-slot order, exact attempt plan identity per result, reserved identity slot order, and one shared authority plus one shared environment across both repetitions.

### Conventions

Records use `FrozenContractModel`, forbid extra fields, and every digest-bearing record verifies its own content digest over the exact payload.

### Invariants And Boundaries

- Retry is structurally disabled: retryCount is the literal 0 and no successor slot exists for the same plan identity.
- One passing repetition can never compensate a failed, aborted, timed-out, retried, stale, or authority-mismatched repetition.
- A terminal attempt requires both terminal repetition results; a reserved attempt can carry none.
- Diagnostic evidence has no shape in this lane and no projection path here can satisfy or be satisfied by diagnostic evidence.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every terminal repetition result is acceptance-eligible and certifying with retryCount zero. | `FinalCodexRepetitionResultDraft`; `FinalCodexRepetitionResult` | mcp/src/agents_remember/certification/final_codex/models.py:300-330; mcp/src/agents_remember/certification/final_codex/models.py:333-373 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The run manifest aggregate is green only for two fresh passing repetitions under one exact plan. | `aggregate`; `complete` | mcp/src/agents_remember/certification/final_codex/models.py:392-404 |
| The Gate-4 result manifests come from the shared certifying result-manifest contracts. | `GateResultManifest` | mcp/src/agents_remember/certification/models.py:1-200 |
| Content digests use the shared certification digest helper. | `content_digest` | mcp/src/agents_remember/certification/digests.py:1-80 |
| The outer facade re-exports the full model surface. | `final_codex.models` | mcp/src/agents_remember/certification/__init__.py:38-67 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen R12 host snapshot is a binding copied from the trusted launcher, never selected or provisioned in this lane. | `FinalCodexRuntimeAuthorityBinding` | mcp/src/agents_remember/certification/final_codex/models.py:116-139 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 closed two-fresh repetition model vocabulary delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
