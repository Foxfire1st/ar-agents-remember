# mcp/src/agents_remember/certification/lifecycle_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/lifecycle_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3`|
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the CCR-R05 certificate-reuse journal and the exact durable finalization-leg recovery: an
unchanged interruption resumes and journals the R21 certificate reuse decision without searching
for another candidate, and finalization revalidates the same candidate and binds the exact
unfinished durable leg before any publication write.

## Code Commentary

### Logic

`compile_certification_recovery_record` (`lifecycle_recovery.py:53-81`) orders the submitted
certificate input changes by content digest and journals the exact R21 reuse decision produced by
`plan_certificate_reuse` over the admitted chain. `compile_lifecycle_finalization`
(`lifecycle_recovery.py:84-109`) first proves the boundary is current — operation status
`ready`/`finalizing`, door `claimed`, approval `current` — and that the observed code tree,
memory tree, topology/intent/commit-intent digests, and journal authority equal the admitted
candidate and journal (`_require_finalization_alignment`, `lifecycle_recovery.py:162-220`),
then compiles the R21 finalization authority and binds `nextLeg` to the journal edge.
`validate_lifecycle_finalization_currentness` (`lifecycle_recovery.py:112-133`) refuses any
movement; `authorize_finalization_leg` (`lifecycle_recovery.py:136-159`) authorizes only the
exact journaled `next_leg` after that currentness reread.
`revalidate_certificate_authority` (`lifecycle_recovery.py:223-254`) exposes the R21 certificate
reread without changing finalization or gate state. All refusals are typed
`CertificationContractError` findings with `gateStarts: 0` (`_refuse`,
`lifecycle_recovery.py:257-275`).

### Conventions

Recovery composes existing certificate and finalization authorities; it never creates a
replacement candidate or a fallback path by inference.

### Invariants And Boundaries

- Certificate reuse is decided by R21 against the exact admitted chain and changed inputs; no
  newest-result or path search exists.
- Partial publication resumes the exact durable leg with zero certification starts.
- The operation, door, and approval state must remain current immediately before publication.

### Todos

The durable leg execution and repository writes are later lifecycle owners; this module freezes
the boundary records only.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for recovery and finalization semantics.

CCR-R05@v3 (requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md, "Recovery
Decision") requires resuming the exact durable finalization leg with zero certification
starts, reusing every exact green predecessor, and refusing when candidate or authority
movement precedes a write.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The recovery record journals the exact R21 reuse decision. | `compile_certification_recovery_record` | mcp/src/agents_remember/certification/lifecycle_recovery.py:53-81 |
| Finalization revalidates the exact admitted candidate and journal, then binds the unfinished leg. | `compile_lifecycle_finalization`; `_require_finalization_alignment` | mcp/src/agents_remember/certification/lifecycle_recovery.py:84-109; mcp/src/agents_remember/certification/lifecycle_recovery.py:162-220 |
| Currentness reread and exact-leg authorization gate every publication write. | `validate_lifecycle_finalization_currentness`; `authorize_finalization_leg` | mcp/src/agents_remember/certification/lifecycle_recovery.py:112-133; mcp/src/agents_remember/certification/lifecycle_recovery.py:136-159 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate certificate and invalidation contracts are imported from the R21 owners. | `GateCertificate`; `GateFiveSemanticInputs`; `plan_certificate_reuse` | mcp/src/agents_remember/certification/certificate_models.py:152-176; mcp/src/agents_remember/certification/certificate_models.py:221-240; mcp/src/agents_remember/certification/certificate_invalidation.py:124-164 |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): created the card for the new certificate-reuse recovery and durable finalization-leg module; no prior sidecar existed.
