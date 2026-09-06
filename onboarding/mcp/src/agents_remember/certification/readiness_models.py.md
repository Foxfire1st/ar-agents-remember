# mcp/src/agents_remember/certification/readiness_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/readiness_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T13:30+02:00 |
| lastVerifiedCommitHash | `cb906188` |
| lastVerifiedCommitDate | 2026-09-03T18:04:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Hosts the closed typed contracts of the single closeout-readiness vocabulary (CCR-R09@v3,
successor manifest 260831-CCR-L27): the literal state unions for lifecycle, gates, rails,
certificates, profiles, and readiness surfaces; the frozen observation and input models; the
compiled projection models; and the canonical transition-rule record. Every readiness consumer
compiles through these exact shapes so pass, fail, blocked, not-applicable, report-only, and
unavailable stay typed and never collapse into an inferred default.

## Code Commentary

### Logic

The state unions fix the vocabulary: `LifecycleReadinessState` (`readiness_models.py:30-38`),
`GateReadinessState` (`readiness_models.py:39-46`), `RailReadinessState`
(`readiness_models.py:47-54`), `CertificateReadinessState` (`readiness_models.py:55-61`),
`ProfileReadinessState` (`readiness_models.py:62-62`), `ReadinessSurface`
(`readiness_models.py:63-73`), and `ReadinessTransitionDomain` (`readiness_models.py:74-74`).
`READINESS_SURFACES` (`readiness_models.py:76-86`) is the closed nine-surface catalog the
compiler dispatches on. The frozen input models carry generation/revision and bounded fields:
`ReadinessRevision` (`readiness_models.py:92-96`), `ReadinessEvidenceReference`
(`readiness_models.py:99-103`), `ProfileReadinessObservation` (`readiness_models.py:106-109`),
`LifecycleReadinessObservation` (`readiness_models.py:112-129`) whose
`_require_refusal_payload` validator forces typed failure evidence exactly on refused states,
`GateReadinessObservation` (`readiness_models.py:132-158`) whose `_require_state_shape`
validator forces blockedBy on blocked, typed manifests on passed/failed, and current-green
certificate bytes, `DiagnosticReadinessObservation` (`readiness_models.py:161-164`), and
`CloseoutReadinessInput` (`readiness_models.py:167-181`) which fixes exactly five gates plus
admission/gate-five/finalization authorities. The projection models mirror the same vocabulary:
`ProfileReadinessProjection` (`readiness_models.py:184-188`), `LifecycleReadinessProjection`
(`readiness_models.py:191-196`), `RailReadinessProjection` (`readiness_models.py:199-207`),
`GateReadinessProjection` (`readiness_models.py:210-218`),
`DiagnosticReadinessProjection` (`readiness_models.py:221-226`), and
`CloseoutReadinessProjection` (`readiness_models.py:229-249`) with a `_verify_digest`
validator that recomputes `content_digest` over the payload and refuses tampering.
`ReadinessTransitionRule` (`readiness_models.py:252-255`) is the domain/before/after rule
shape consumed by the canonical transition table.

### Conventions

All models subclass the frozen certification contract model; fields use digest/id/pattern
constraints so the compiler can bind exact identities.

### Invariants And Boundaries

- Exactly five gate observations and exactly five gate projections; other cardinalities are invalid.
- Blocked requires blockedBy; passed/failed require a typed result manifest; only current, stale,
  or invalidated certificate states carry certificate bytes.
- Refused lifecycle states require typed failure evidence (code, corrective owner, evidence).
- The projection digest is content-addressable: any payload mutation invalidates the model.
- Diagnostics stay explicitly non-certifying and same-candidate by model contract.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing artifacts are the
CCR-R09@v3 requirement packet and the 260831-CCR-L27 successor repair manifest recorded in the
leaf task.

| Finding | Anchor | Source |
| --- | --- | --- |
| The required states (lifecycle, gate, rail, certificate, profile) are closed typed literals. | `LifecycleReadinessState`; `GateReadinessState` | mcp/src/agents_remember/certification/readiness_models.py:30-62 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closed surface catalog drives dispatch in the readiness compiler. | `READINESS_SURFACES` | mcp/src/agents_remember/certification/readiness_models.py:76-86 |
| The readiness input model fixes exactly five gate observations and the admission/finalization authorities. | `CloseoutReadinessInput` | mcp/src/agents_remember/certification/readiness_models.py:167-181 |
| Compilation consumes these observation models and emits these projections. | `CloseoutReadinessProjection`; `GateReadinessObservation` | mcp/src/agents_remember/certification/readiness_models.py:132-158; mcp/src/agents_remember/certification/readiness_models.py:229-249 |
| The projection digest self-verification rejects tampered outputs. | `_verify_digest` | mcp/src/agents_remember/certification/readiness_models.py:244-249 |
| The transition-rule shape is consumed by the canonical same-generation transition table. | `ReadinessTransitionRule` | mcp/src/agents_remember/certification/readiness_transitions.py:14-113 |
| The certification facade imports and re-exports the readiness observations and projection models. | `readiness_models` | mcp/src/agents_remember/certification/__init__.py:88-88 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.

- 2026-09-05T06:24:16+00:00: Generated citation repair: `readiness_models` repointed to mcp/src/agents_remember/certification/__init__.py:88-88. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the certification-facade row to the import module identifier `readiness_models` and verified every row range against the current worktree. Verification remains pinned to the staged candidate tree until closeout.

- 2026-09-03T13:45+02:00 — 260831-CCR-L27 Gate-5: verification stamp advanced from the staged candidate tree to the certified commit cb906188 (tree 74d188bb).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: created for the closed typed
  readiness vocabulary (CCR-R09@v3 successor repair): literal state unions, frozen observations and
  input, compiled projections with content-digest self-verification, and the transition-rule
  record. Verification is pinned to the staged candidate tree `74d188bbee`; the final commit
  stamp is closeout-owned.