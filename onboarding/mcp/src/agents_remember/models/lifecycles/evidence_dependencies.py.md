# mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

The shared typed dependency-edge encoding of CCR-R03@v1: one versioned direct-dependency
declaration per evidence record type. It models only the one-way relation "evidence content-addresses
its declared direct inputs" — it does not select a current record, infer domain semantics, or place
evidence back into topology or task intent
cit:([module docstring], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:1-6).

## Code Commentary

### Logic

`EvidenceDependency` is one named direct input with kind, name, digest algorithm
(`git-object` for tree/blob identities, `sha256` otherwise), and a 40-64 hex digest
cit:([`EvidenceDependency`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:68-96).
`EvidenceDependencies` is the canonical `ar-evidence-dependencies/v1` declaration for one
`EvidenceRecordType`; it enforces unique identities and canonical sort order and fingerprints the
declaration deterministically cit:([`EvidenceDependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-119).
`EVIDENCE_DEPENDENCY_POLICIES` is the frozen per-record-type allowlist of required and permitted
direct dependency kinds for every evidence domain: memory-quality attestation, route review, curator
coherence, quality report, closeout door, and the three lifecycle operation kinds
cit:([`EVIDENCE_DEPENDENCY_POLICIES`, `EvidenceDependencyPolicy`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:122-213).
`build_evidence_dependencies` validates an owner's declared inputs against its exact policy, and
`require_evidence_dependencies` refuses missing, extra, wrong-type, or unsupported declarations
with typed `EvidenceDependencyError` statuses
cit:([`build_evidence_dependencies`, `require_evidence_dependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:228-275).
`validate_evidence_dependency_graph` rejects a cycle among the supplied content-addressed records
while treating edges to records outside the supplied set as external roots — no historical file scan
cit:([`validate_evidence_dependency_graph`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:289-324).
`dependency` and `canonical_sha256` are the two builder helpers every domain uses to construct edges
cit:([`dependency`, `canonical_sha256`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:216-225, 327-331).

### Conventions

- One `EvidenceDependencyPolicy` per record type at all times; the module-level registry is the only
  authority for which kinds a record may bind.
- Digests are content-addressed (git-object tree identities or SHA-256 of declared bytes); names are
  canonical nonblank text.
- Edge direction is acyclic by contract: semantic projections and candidate trees point into
  evidence, never the reverse.

## Invariants And Boundaries

- A direct dependency may be omitted only when the record-type policy proves the record never reads
  it; a dependency may not be added merely for convenience.
- Missing mandatory kinds, undeclared extra kinds, digest/version mismatches, or a dependency cycle
  refuse publication/currentness.
- This module never selects a current record, never searches historical files, and never creates a
  second evidence ledger.
- Unrelated topology or intent changes must not stale a memory or quality result that does not
  consume them — only declared direct/transitive closure members invalidate their consumers.

## Docs References

No configured Domain Documentation applies; the dependency encoding is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The encoding has no external authority. | — | — |

## Repo-Internal References

Every consumer record type binds its own edges through this single encoding; the mutation/cycle
matrix in the evidence-dependency test suite fixes the contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory-quality attestation binds candidate-state, code/memory trees, report bytes, and validators. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-129 |
| The closeout door binds code/memory candidate trees, topology, intent, and the review/memory/ledger/admission/scheduling provenance records. | `closeout_door_dependencies` | mcp/src/agents_remember/models/lifecycles/door.py:161-202 |
| Lifecycle operations declare the admitted candidate, door, plan, and normalized operation input. | `lifecycle_operation_dependencies` | mcp/src/agents_remember/models/lifecycles/operation.py:428-484 |
| Route review binds code tree, task intent, per-evidence-file SHA-256, and validator. | `build_route_review`; `_require_current_dependencies` | mcp/src/agents_remember/worktrees/route_review.py:56-116, 229-271 |
| Policy registry shape, refusal statuses, and graph-cycle guard are fixed by focused tests. | `test_every_record_type_has_one_versioned_policy`; `test_missing_extra_wrong_type_and_duplicate_dependencies_fail_closed`; `test_supplied_record_closure_refuses_cycles_without_scanning_for_external_roots` | mcp/tests/test_evidence_dependencies.py:88-90, 159-187, 202-242 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): created the card for the new shared typed evidence-dependency encoding introduced by the R03 leaf; no prior sidecar existed.