# Frozen Certification Run Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/certification/frozen_run` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T14:47:06+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## What This Area Is

Immutable retained inputs for closeout certification. A frozen run keeps the original registry,
plans, profile, admission and creation evidence together. Candidate authority records preserve
semantic mutation/source/worktree/generated-input projections alongside the original bytes used
to derive them. The package supplies contracts to the execution and lifecycle owners.

## Hot Path Summary

Read `models.py` for `FrozenCertificationRun` and `freeze_certification_run`; read `authorities.py`
for `CandidateAuthorityRecords`, exact input snapshots and semantic projections. Run identity
includes original provenance; certificate semantic identity has its own narrower contract.

## Operating Model

The admitted lane is frozen into a self-validating run. Its admission is recompiled from retained
owners and compared exactly; the complete record digest is then checked. Separately, the worktree
observation owner gathers current authorities and retains their semantic envelope plus top-level derivation
bytes. The generated-input declarations snapshot belongs inside that envelope and participates in
its semantic digest. Subsequent lifecycle selection and gate execution consume these objects through their own
owners; a valid retained object is not evidence that any gate passed.

## Local Invariants And Traps

- Retain original creation evidence; do not reconstruct it from a later generation.
- An exact run record and a semantic gate certificate have different digest domains.
- Generated-input declarations start with unknown freshness.
- No package import, constructor or digest check grants process or mutation authority.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `authorities.py` | [authorities.py.md](authorities.py.md) | covered |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A frozen run revalidates exact original admission and complete-record identity. | `FrozenCertificationRun`; `freeze_certification_run` | mcp/src/agents_remember/certification/frozen_run/models.py:25-80 |
| Candidate records separate semantic projections from exact derivation bytes and provenance. | `CandidateAuthorityEnvelope`; `CandidateAuthorityRecords` | mcp/src/agents_remember/certification/frozen_run/authorities.py:100-128 |
| Production admission prepares and observes a candidate before compiling lifecycle recovery. | `prepare_closeout_certification` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:75-142 |

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

## Cross-Repo References

No cross-repository implementation boundary is owned by this route.

## Update History

- 2026-09-06T14:47:06+00:00 — Created the governing route from actual source at c69d5171187fa1957025e393270db9f5a864ab14, separating original frozen inputs from execution and certification authority.
