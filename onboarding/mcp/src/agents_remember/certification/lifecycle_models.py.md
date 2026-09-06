# mcp/src/agents_remember/certification/lifecycle_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/lifecycle_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:02:26+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the immutable, content-addressed lifecycle boundary records of CCR-R05: the exact-candidate
observation, prior-red disposition envelope/manifest, lifecycle admission manifest, certificate
recovery record, and durable finalization journal/manifest. The digest-bearing manifests and recovery
record verify their semantic-envelope digests; observation and journal models enforce their own
shape constraints. Shared individual corrective dispositions now live in the model-layer package.

## Code Commentary

### Logic

The local literals fix authority/generated-input status and the four durable finalization legs.
`ExactCandidateObservation` carries owner-produced identities and statuses; conflicted worktrees
must name exactly their sorted unique conflict paths. Shared `CorrectiveInputChange` and
`RedCatalogDisposition` values are imported from `models/certification/corrective.py` by their
consumers; this domain module retains the prior-red envelope and manifest.

Prior-red, admission, recovery and finalization manifests verify their own semantic-envelope
hashes. Admission declares zero gate starts in its semantic shape; recovery binds the original
admitted certificate identities, input changes and compiled reuse plan. These literals and hashes
are not process-execution evidence.

`FinalizationBoundaryObservation` carries current owner observations for the finalization
validator; constructing it does not re-observe Git, approval or door authority. `DurableFinalizationLeg`
validates authority/intended/proven-output shape. `FinalizationJournalState` preserves ordered
code, external-memory, ledger and contract legs, permits at most one unfinished intent, and
requires monotonic progress. Its `next_leg` prefers the retained intent before a pending leg.
The finalization envelope requires its explicit `nextLeg` to equal that derived journal edge.

### Conventions

Every model is a frozen `FrozenContractModel` with digest fields pattern-checked to lowercase
hex. Digest-bearing manifests verify their own envelopes; the actual authority observations and
read/write currentness remain responsibilities of the admission and finalization owners.

### Invariants And Boundaries

- Digest fields use lowercase SHA-256 shape. Each digest-bearing manifest refuses a mismatch
  with its own envelope; supplied authority digests still require their owner’s evidence.
- An applicable finalization leg always carries write authority; `not-applicable` legs carry
  none.
- The finalization journal never reorders the durable code/memory/ledger/contract legs and never
  retains two unfinished write intents.
- The candidate observation is admission input; the model checks shape, not authority truth.

### Todos

Authority observation and engine behavior are owned by `lifecycle_admission` /
`lifecycle_recovery`, not by the model layer.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the finalization journal semantics.

CCR-R05@v3 (requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md, "Finalization
Required Behavior") requires preserving current code-commit, external-memory-commit, ledger,
and contract-finalization owners and ordering; journaling every durable leg so an unchanged
interruption resumes without any gate rerun; and resuming the exact durable path on partial
publication.


| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external Domain Documentation source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact-candidate observation is the admission boundary's owner-produced input. | `ExactCandidateObservation` | mcp/src/agents_remember/certification/lifecycle_models.py:48-81 |
| Prior-red corrective and recovery records bind digests to semantic envelopes. | `RedCatalogDisposition`; `PriorRedDispositionManifest`; `CertificationRecoveryRecord` | mcp/src/agents_remember/models/certification/corrective.py:41-70; mcp/src/agents_remember/certification/lifecycle_models.py:105-117; mcp/src/agents_remember/certification/lifecycle_models.py:158-170 |
| The durable leg journal fixes order, intent exclusivity, monotonic progress, and the resume edge. | `FinalizationJournalState`; `LifecycleFinalizationSemanticEnvelope` | mcp/src/agents_remember/certification/lifecycle_models.py:217-252; mcp/src/agents_remember/certification/lifecycle_models.py:255-270 |
| Certificate identities and creation provenance are imported from the R21 certificate owners. | `GateCertificateIdentity`; `CreationProvenance` | mcp/src/agents_remember/certification/certificate_models.py:100-102; mcp/src/agents_remember/certification/certificate_models.py:77-82 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation is referenced. | N/A | N/A |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-06T15:02:26+00:00 — Reviewed the complete card and current source at c69d5171187fa1957025e393270db9f5a864ab14; corrected identity/observation ownership claims, retained the moved model semantics, and regenerated each active source range from its unique current construct. All prior history is preserved.

- 2026-09-06T14:48:58+00:00 — Repaired the moved corrective-value references against `c69d5171187fa1957025e393270db9f5a864ab14` after confirming identical class ASTs; lifecycle envelopes/finalization prose remain for their source-card review. Prior verification stamps and all earlier history are preserved.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): created the card for the new immutable lifecycle boundary records; no prior sidecar existed.
