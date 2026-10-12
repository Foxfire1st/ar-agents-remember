# Frozen Certification Run Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/certification/frozen_run` |

## Governing Overview

[Certification contract overview](../overview.md)

## What This Area Is

This package defines immutable retained inputs for closeout certification. A frozen run keeps the original registry, plans, profile, admission and creation evidence together. Candidate authority records preserve semantic mutation, source, worktree and generated-input projections alongside the original bytes used to derive them. These contracts supply inputs to the execution and lifecycle owners.

## Hot Path Summary

Read `models.py` for `FrozenCertificationRun` and `freeze_certification_run`; read `authorities.py` for `CandidateAuthorityRecords`, exact input snapshots and semantic projections. Run identity includes original provenance; certificate semantic identity has its own narrower contract.

## How It Is Built

`freeze_certification_run` retains the admitted lane and repository profile using the lane admission's original creation provenance. The resulting run recompiles admission from its retained registry, plans, profile and provenance, compares that admission exactly, and checks the digest of the complete record.

The worktree observation owner gathers current authorities and retains their semantic envelope plus top-level derivation snapshots. The generated-input declarations snapshot belongs inside that envelope and participates in its semantic digest. The envelope also carries an optional admitted memory-tree binding; current observations populate it from the closeout door when present.

For a new closeout admission, the production owner strictly prepares the staged candidate, prepares the frozen run and observes candidate authorities before compiling lifecycle admission and recovery. An already queued or running generation instead validates its selected currentness. Lifecycle selection loads the retained objects, and gate execution consumes the selected run and recovery inputs through its own owner.

Memory refresh validation belongs to the memory-quality owners. `worktrees/modules/onboarding.py::validate_memory_refresh_attestations` composes the sidecar and governing route overview body/history checks and reports failures from either surface. The memory-quality controller calls it for an unconverted external-memory leaf; a converted memory tree uses the onboarding trace gate instead. This validation wiring does not alter the frozen-run contracts. No external Domain Documentation source is configured; the inspected owners describe repository-local contract inputs, not an external protocol.

### File-Level Onboarding Map

The following retained coverage metadata describes the onboarding map, not lifecycle status or certification results.

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `authorities.py` | [authorities.py.md](authorities.py.md) | covered |


## Invariants And Boundaries

- Retain original creation evidence; do not reconstruct it from a later generation.
- An exact run record and a semantic gate certificate have different digest domains.
- Generated-input declarations start with unknown freshness. Their retained status is not evidence of a freshness check or a passed gate.
- Package import, construction and digest validation establish retained contract consistency; process execution and mutation authority remain with the lifecycle and execution owners. A valid retained object is not evidence that any gate passed.

## Evidence

- A frozen run revalidates exact original admission and complete-record identity. [1]
- Candidate records separate semantic projections from exact derivation bytes and provenance. [2]
- Production admission prepares and observes a candidate before compiling lifecycle recovery. [3]

- Current candidate observation retains generated declarations, derivation snapshots and the admitted memory-tree binding. [4]
- Memory refresh composition checks sidecars and route overviews; converted trees use the trace gate instead. [5]
