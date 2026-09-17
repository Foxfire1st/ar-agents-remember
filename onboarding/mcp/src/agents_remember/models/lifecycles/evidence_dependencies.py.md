# mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

The shared typed dependency-edge encoding of CCR-R03@v1: one versioned direct-dependency
declaration per evidence record type. It models only the one-way relation "evidence content-addresses
its declared direct inputs" — it does not select a current record, infer domain semantics, or place
evidence back into topology or task intent
cit:(["Typed direct-input identities for immutable lifecycle evidence"], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:1-1).

## Code Commentary

### Logic

`ledger-provenance` is not a dependency kind. The `closeout-door/v1` policy requires only
the direct code, topology, intent, review/coherence, admission, scheduling, and validator inputs
actually consumed, with memory tree and predecessor optional. The computed ledger is not an
input to this authority graph.

`EvidenceDependency` is one named direct input with kind, name, digest algorithm
(`git-object` for tree/blob identities, `sha256` otherwise), and a 40-64 hex digest
cit:([`EvidenceDependency`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:67-95).
`EvidenceDependencies` is the canonical `ar-evidence-dependencies/v1` declaration for one
`EvidenceRecordType`; it enforces unique identities and canonical sort order and fingerprints the
declaration deterministically cit:([`EvidenceDependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-118).
`EVIDENCE_DEPENDENCY_POLICIES` is the frozen per-record-type allowlist of required and permitted
direct dependency kinds for every evidence domain: memory-quality attestation, route review, curator
coherence, quality report, closeout door, and the three lifecycle operation kinds
cit:([`EVIDENCE_DEPENDENCY_POLICIES`, `EvidenceDependencyPolicy`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:141-211; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:122-126).
CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) makes the `admission` dependency kind optional for
`quality-report/v2` records: a published quality report binds the shared-Dagger-authority snapshot digest as a
`shared-dagger-authority` edge whenever the manifest carries `runtimeAuthorityDigest`, and the record stays
valid without one (ownerless admission, preview, fixtures). The policy registry remains the single authority for the
kinds each record may bind.
`build_evidence_dependencies` validates an owner's declared inputs against its exact policy, and
`require_evidence_dependencies` refuses missing, extra, wrong-type, or unsupported declarations
with typed `EvidenceDependencyError` statuses
cit:([`build_evidence_dependencies`, `require_evidence_dependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:226-235; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-273).
`validate_evidence_dependency_graph` rejects a cycle among the supplied content-addressed records
while treating edges to records outside the supplied set as external roots — no historical file scan
cit:([`validate_evidence_dependency_graph`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:287-322).
`dependency` and `canonical_sha256` are the two builder helpers every domain uses to construct edges
cit:([`dependency`, `canonical_sha256`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-223; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:325-329).

### Conventions

- One `EvidenceDependencyPolicy` per record type at all times; the module-level registry is the only
  authority for which kinds a record may bind.
- Digests are content-addressed (git-object tree identities or SHA-256 of declared bytes); names are
  canonical nonblank text.
- Edge direction is acyclic by contract: semantic projections and candidate trees point into
  evidence, never the reverse.

### Invariants And Boundaries

- A direct dependency may be omitted only when the record-type policy proves the record never reads
  it; a dependency may not be added merely for convenience.
- Missing mandatory kinds, undeclared extra kinds, digest/version mismatches, or a dependency cycle
  refuse publication/currentness.
- This module never selects a current record, never searches historical files, and never creates a
  second evidence ledger.
- Unrelated topology or intent changes must not stale a memory or quality result that does not
  consume them — only declared direct/transitive closure members invalidate their consumers.

### Todos

No additional file-local TODO is established by this candidate review.

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
| The dependency-kind vocabulary and closeout-door policy contain no ledger-provenance input. | `EvidenceDependencyKind` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:31-50 |
| The memory-quality attestation binds candidate-state, code/memory trees, report bytes, and validators. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:94-131 |
| The closeout door binds code/memory candidate trees, topology, intent, and the review/memory/admission/scheduling provenance records. | `closeout_door_dependencies` | mcp/src/agents_remember/models/lifecycles/door.py:158-196 |
| Lifecycle operations declare the admitted candidate, door, plan, and normalized operation input. | `lifecycle_operation_dependencies` | mcp/src/agents_remember/models/lifecycles/operation.py:438-493 |
| Route review binds code tree, task intent, per-evidence-file SHA-256, and validator. | `build_route_review` | mcp/src/agents_remember/worktrees/route_review.py:292-347 |


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation source applies. | — | — |

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Retired the ledger-provenance kind and mandatory closeout-door edge. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `_require_current_dependencies`, `build_route_review` repointed to mcp/src/agents_remember/worktrees/route_review.py:292-347, mcp/src/agents_remember/worktrees/route_review.py:449-491. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the `quality-report/v2` policy change - `admission` became an optional dependency kind so a published report binds the shared-Dagger-authority snapshot digest when present and stays valid without one.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): repaired the prose cit anchor (quoted module docstring) and separated the two-range source with a semicolon.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): created the card for the new shared typed evidence-dependency encoding introduced by the R03 leaf; no prior sidecar existed.
