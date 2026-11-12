# mcp/src/agents_remember/certification/readiness_models.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root; the governing artifacts are the
CCR-R09@v3 requirement packet and the 260831-CCR-L27 successor repair manifest recorded in the
leaf task.

- The required states (lifecycle, gate, rail, certificate, profile) are closed typed literals. [1]

### Repo-Internal References

- The closed surface catalog drives dispatch in the readiness compiler. [2]
- The readiness input model fixes exactly five gate observations and the admission/finalization authorities. [3]
- Compilation consumes these observation models and emits these projections. [4]
- The projection digest self-verification rejects tampered outputs. [5]
- The transition-rule shape is consumed by the canonical same-generation transition table. [6]
- The certification facade imports and re-exports the readiness observations and projection models. [7]

### Cross-Repo References

No cross-repository implementation boundary is owned here.
