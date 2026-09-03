# mcp/src/agents_remember/certification/readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/readiness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T13:30+02:00 |
| lastVerifiedCommitHash | `cb906188` |
| lastVerifiedCommitDate | 2026-09-03T18:04:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Implements the single closeout-readiness vocabulary of CCR-R09@v3 (successor repair manifest
260831-CCR-L27): lossless compilation of one generation-coherent `CloseoutReadinessProjection`
from the exact certifying Gate 1-5 plan, R22 repository profile, admission authority, gate result
manifests, certificates, diagnostics, and lifecycle observations. It is the adapters' shared
compiler: every supported entry point (interactive, admission, gate-execution, diagnostic, status,
wait, journal, dashboard, finalization) projects through the same semantics so no surface can
translate a red, blocked, not-applicable, or unavailable fact into pass/skip/generic failure.

## Code Commentary

### Logic

`compile_closeout_readiness` (`readiness.py:43-89`) is the single entry point. It first
`_require_certifying_plan` (`readiness.py:120-132`) - the plan must be profileKind `certifying`
with the exact gate tuple `(1, 2, 3, 4, 5)` - then `_require_one_revision` (`readiness.py:135-144`)
which rejects mixed-generation observations, then `_require_admission` (`readiness.py:147-193`)
which binds the admission envelope to the exact repository/candidate/profile/R11 plan and refuses
gate starts before exact admission. `_compile_profile` (`readiness.py:196-230`) reconciles the
observed profile state with the admitted R22 digests via `_require_repository_plan_identity`
(`readiness.py:233-245`) and `_repository_plan_is_admitted` (`readiness.py:248-257`).
`_compile_gate` (`readiness.py:260-310`) enforces Gate 1-5 catalog order, exact ordered rail
catalog preservation (`_require_manifest`, `readiness.py:313-351`), the typed result contract and
every declared bounded evidence reference (`_require_result_contract`, `readiness.py:354-374`),
and the current-green certificate/result binding. `_compile_rails`/`_compile_rail`
(`readiness.py:377-404`) map to `RailReadinessProjection` including the report-only pass/fail and
not-applicable states. `_require_current_certificate_chain` (`readiness.py:407-434`) validates the
current-green Gate 1-5 certificate chain through `validate_certificate_chain`;
`_require_gate_barriers` (`readiness.py:437-457`) blocks later gate starts after a red Gate 1-4 and
requires earlier current-green certificates before any start. `_compile_diagnostics`
(`readiness.py:460-471`) keeps diagnostic previews explicitly non-certifying and same-candidate
(`_compile_diagnostic`, `readiness.py:474-517`). `_certification_ready`
(`readiness.py:520-531`) is true only when admission exists, profile is admitted-current, and every
gate is passed/current-green. `_require_lifecycle` (`readiness.py:534-570`) gates finalization
states on that certification and validates finalization currentness via
`validate_finalization_currentness` when finalized. `_raise` (`readiness.py:573-578`) emits a typed
`CertificationContractFinding` inside `CloseoutReadinessContractError`.
`project_closeout_readiness` (`readiness.py:92-101`) dispatches on the closed `READINESS_SURFACES`
catalog and refuses unknown surfaces; `readiness_projection_bytes` (`readiness.py:104-117`) renders
byte-identical compact canonical JSON for every entry point. The developer dead-branch ruling of
2026-09-03 removed three provably unreachable defensive raises (profile state contradiction,
repository-plan admission-None, certificate-admission-missing) without changing semantics.

### Conventions

All refusals raise `CloseoutReadinessContractError` with finding code/path/detail; the projection
digest is `content_digest` over the payload so readers validate integrity.

### Invariants And Boundaries

- One observation generation/revision across profile, lifecycle, gates, and diagnostics.
- A red Gate 1-4 prevents every later gate start; current-green earlier certificates are required
  before any run/pass/fail state; a red Gate 5 or missing certification blocks finalization.
- Not-applicable, report-only pass/fail, blocked, and unavailable are preserved as typed states and
  never translated into pass/skip.
- Finalization authority and inputs appear only in finalized state and must validate currentness.
- Diagnostics stay explicitly non-certifying and must name the exact same candidate.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing artifacts are the
CCR-R09@v3 requirement packet and the 260831-CCR-L27 successor repair manifest, recorded in the
leaf task and Update History below.

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary must project one typed readiness semantics with no entry point translating red or unavailable facts into pass/skip/generic failure. | `compile_closeout_readiness` | mcp/src/agents_remember/certification/readiness.py:43-89 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The certifying-plan precondition and one-revision guard fix the exact Gate 1-5 scope and forbid mixed generations. | `_require_certifying_plan`; `_require_one_revision` | mcp/src/agents_remember/certification/readiness.py:120-144 |
| Admission binds the envelope to the exact repository, candidate, profile, and plan and forbids pre-admission gate starts. | `_require_admission` | mcp/src/agents_remember/certification/readiness.py:147-193 |
| Gate compilation preserves ordered rail catalog, typed result contract, bounded evidence, and current-green certificate binding. | `_compile_gate`; `_require_manifest`; `_require_result_contract` | mcp/src/agents_remember/certification/readiness.py:260-374 |
| Current-green certificate chain validation and the red-gate/currentness barriers gate later starts and finalization. | `_require_current_certificate_chain`; `_require_gate_barriers` | mcp/src/agents_remember/certification/readiness.py:407-457 |
| Lifecycle finalization is gated on certification readiness and validated for currentness when finalized. | `_require_lifecycle` | mcp/src/agents_remember/certification/readiness.py:534-570 |
| The certification facade imports and re-exports the readiness compiler and surface catalog. | `readiness` | mcp/src/agents_remember/certification/__init__.py:32-37 |
| The readiness projection model self-verifies its content digest. | `CloseoutReadinessProjection`; `_verify_digest` | mcp/src/agents_remember/certification/readiness_models.py:229-249 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Readiness semantics are consumed by the public certification facade and the focus coverage suite. | `project_closeout_readiness` | mcp/src/agents_remember/certification/readiness.py:92-101 |

## Update History
- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the certification-facade row to the import module identifier `readiness` and verified every row range against the current worktree. Verification remains pinned to the staged candidate tree until closeout.

- 2026-09-03T13:45+02:00 — 260831-CCR-L27 Gate-5: verification stamp advanced from the staged candidate tree to the certified commit cb906188 (tree 74d188bb).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: created for the new single
  closeout-readiness vocabulary compiler (CCR-R09@v3 successor repair): surface catalog dispatch,
  exact certifying-plan/admission/profile/gate/certificate/diagnostic/lifecycle guards, report-only
  and not-applicable state preservation, byte-identical canonical rendering, and the developer-
  authorized dead-branch deletions. Verification is pinned to the staged candidate tree
  `74d188bbee`; the final commit stamp is closeout-owned.