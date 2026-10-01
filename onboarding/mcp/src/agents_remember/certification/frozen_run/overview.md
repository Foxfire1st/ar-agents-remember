# Frozen Certification Run Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/certification/frozen_run` |

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

## Evidence

### Repo-Internal References

- A frozen run revalidates exact original admission and complete-record identity. [1]
- Candidate records separate semantic projections from exact derivation bytes and provenance. [2]
- Production admission prepares and observes a candidate before compiling lifecycle recovery. [3]

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

### Cross-Repo References

No cross-repository implementation boundary is owned by this route.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.
