# mcp/src/agents_remember/certification/lifecycle_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/lifecycle_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3`|
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the immutable, content-addressed lifecycle boundary records of CCR-R05: the exact-candidate
observation, the prior-red corrective dispositions, the lifecycle admission manifest, the
certificate recovery record, and the durable finalization journal and manifest. Every record
self-verifies its digest over the exact canonical JSON of its semantic envelope.

## Code Commentary

### Logic

The status literals fix the vocabulary at the top of the module (`lifecycle_models.py:31-40`):
`AuthorityStatus`, `GeneratedArtifactStatus`, `CorrectiveDispositionKind` (`direct-repair`
/ `repaired-root`), `FinalizationLeg` and its `FinalizationLegState`.
`ExactCandidateObservation` (`lifecycle_models.py:50-83`) freezes every owner-produced
authority fingerprint plus the three authority statuses and the worktree state, and rejects a
`conflicted` status without exactly its sorted unique conflict paths.
`CorrectiveInputChange` (`lifecycle_models.py:86-102`) requires a real digest movement;
`RedCatalogDisposition` (`lifecycle_models.py:105-134`) enforces the direct-repair versus
repaired-root shape. The prior-red envelope and manifest
(`lifecycle_models.py:137-170`), the admission envelope and manifest
(`lifecycle_models.py:173-198`), the recovery envelope and record
(`lifecycle_models.py:201-223`), and the finalization envelope and manifest
(`lifecycle_models.py:308-338`) all verify their content digests in model validators.
`FinalizationBoundaryObservation` (`lifecycle_models.py:226-239`) revalidates the current
owner-produced authorities immediately before publication. `DurableFinalizationLeg`
(`lifecycle_models.py:242-267`) and `FinalizationJournalState`
(`lifecycle_models.py:270-305`) fix the four-leg durable order, allow at most one unfinished
write intent, require monotonic progress, and expose `next_leg`; the finalization envelope forces
`nextLeg == journal.next_leg` (`lifecycle_models.py:319-323`).

### Conventions

Every model is a frozen `FrozenContractModel` with digest fields pattern-checked to lowercase
hex; digest verification is a model invariant, never a caller responsibility.

### Invariants And Boundaries

- All `*Digest` fields are content-addressed SHA-256 values; a record whose digest does not match
  its semantic envelope refuses construction.
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


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact-candidate observation is the admission boundary's owner-produced input. | `ExactCandidateObservation` | mcp/src/agents_remember/certification/lifecycle_models.py:50-83 |
| Prior-red corrective and recovery records bind digests to semantic envelopes. | `RedCatalogDisposition`; `PriorRedDispositionManifest`; `CertificationRecoveryRecord` | mcp/src/agents_remember/certification/lifecycle_models.py:105-134; mcp/src/agents_remember/certification/lifecycle_models.py:158-170; mcp/src/agents_remember/certification/lifecycle_models.py:211-223 |
| The durable leg journal fixes order, intent exclusivity, monotonic progress, and the resume edge. | `FinalizationJournalState`; `LifecycleFinalizationSemanticEnvelope` | mcp/src/agents_remember/certification/lifecycle_models.py:270-305; mcp/src/agents_remember/certification/lifecycle_models.py:308-323 |
| Model-edge proofs cover the exact-candidate, leg, disposition, and journal refusal shapes. | `test_exact_candidate_rejects_contradictory_conflict_shapes`; `test_finalization_leg_rejects_state_shape_mismatches`; `test_red_disposition_and_journal_reject_noncanonical_shapes` | mcp/tests/test_certification_contract_model_edges.py:238-265; mcp/tests/test_certification_contract_model_edges.py:280-293; mcp/tests/test_certification_contract_model_edges.py:296-352 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Certificate identities and creation provenance are imported from the R21 certificate owners. | `GateCertificateIdentity`; `CreationProvenance` | mcp/src/agents_remember/certification/certificate_models.py:79-86; mcp/src/agents_remember/certification/certificate_models.py:102-106 |

## Update History

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): created the card for the new immutable lifecycle boundary records; no prior sidecar existed.
