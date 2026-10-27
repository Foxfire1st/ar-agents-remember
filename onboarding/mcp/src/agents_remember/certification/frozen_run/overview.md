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

The retained `CandidateAuthorityEnvelope` contains semantic projections, generated-input declarations and an optional `admittedMemoryTree`; `CandidateAuthorityRecords` separately retains derivation snapshots and original provenance and validates the semantic digest. These model fields and retained bytes do not establish a current runtime observer or prove that a current closeout door populates them. The former `observe_certification_candidate` runtime observer was removed.

Requested certification still freezes the complete admitted profile, plans and original provenance before executing a gate. Recovery reopens the supplied immutable frozen run and verifies its stored reference without rediscovering a profile or summary journal. The removed automatic closeout admission helper no longer stages or observes a candidate for this purpose; ordinary closeout publishes its accepted tree through the invariant-gated transaction instead.

The memory-quality controller revalidates the admitted candidate, refuses unconverted input, runs converted validation and the onboarding trace gate, and retains its checklist/readiness owners. It does not call the removed legacy sidecar/Update History refresh composition for an unconverted leaf. These application checks do not alter the immutable frozen-run contracts or certify any execution. No external Domain Documentation source is configured.

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

- Requested certification freezes the admitted repository profile, plans, registry and original provenance before gate execution; selected recovery reopens the exact retained frozen run without profile or journal rediscovery. Ordinary closeout is not this certification route. [3]

- Retained authority models carry generated declarations, an optional admittedMemoryTree, input snapshots and provenance; model validation does not prove a current runtime observer or gate execution. [4]



- Historical pre-R65 refresh composition checked sidecars and route overviews; that legacy composition is removed. The surviving converted controller uses its trace gate.  Anchor: `validate_memory_refresh_attestations` `_onboarding_refresh_gate` [5]
