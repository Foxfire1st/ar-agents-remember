# mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py

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
cit:([`EvidenceDependency`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:96-124).
`EvidenceDependencies` is the canonical `ar-evidence-dependencies/v1` declaration for one
`EvidenceRecordType`; it enforces unique identities and canonical sort order and fingerprints the
declaration deterministically cit:([`EvidenceDependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:127-149).
`EVIDENCE_DEPENDENCY_POLICIES` is the frozen per-record-type allowlist of required and permitted
direct dependency kinds for every evidence domain: memory-quality attestation, route review, curator
coherence, review assessment, quality report, closeout door, and the three lifecycle operation kinds
cit:([`EVIDENCE_DEPENDENCY_POLICIES`, `EvidenceDependencyPolicy`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:172-270; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:153-157).
`quality-report/v2` makes `admission` optional. When `runtimeAuthorityDigest` is present, the published
quality report binds an `admission` edge named `shared-dagger-authority` to that snapshot digest; the record
remains valid without it. The policy registry remains the single authority for the
kinds each record may bind.
`build_evidence_dependencies` validates an owner's declared inputs against its exact policy, and
`require_evidence_dependencies` refuses missing, extra, wrong-type, or unsupported declarations
with typed `EvidenceDependencyError` statuses
cit:([`build_evidence_dependencies`, `require_evidence_dependencies`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:285-294; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:297-332).
`validate_evidence_dependency_graph` rejects a cycle among the supplied content-addressed records
while treating edges to records outside the supplied set as external roots — no historical file scan
cit:([`validate_evidence_dependency_graph`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:346-381).
`dependency` constructs typed edges, and `canonical_sha256` computes canonical JSON digests
cit:([`dependency`, `canonical_sha256`], mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:273-282; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:384-388).

`MAX_EVIDENCE_DEPENDENCIES` is derived from the coherence model's bounded judgment and assessment populations, fixed dependencies and validator edge. It covers record builders whose own models bound their payloads, without changing dependency schema, names or meaning. Coherence judgments may cite distinct evidence files; sharing evidence is valid when that file actually supports each judgment, never a workaround for an arbitrary cap. Master-scope route review has no own finite model bound and remains subject to the shared refusal, as the explicit scope ruling states.

### Conventions

- One `EvidenceDependencyPolicy` per record type at all times; the module-level registry is the only
  authority for which kinds a record may bind.
- Digests are content-addressed (git-object tree identities or SHA-256 of declared bytes); names are
  canonical nonblank text.
- Evidence records name their upstream semantic and candidate identities; the model does not add
  evidence back to topology or task intent.

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



## Evidence

- Shared evidence capacity follows from the bounded coherence payload. [6]


### Docs References

No configured Domain Documentation applies; the dependency encoding is repository-owned.

The encoding has no external authority.

### Repo-Internal References

The record-type policies share this encoding; dependency-bound tests verify maximum publication,
oversize refusal and old-record loading.


- The dependency-kind vocabulary and closeout-door policy contain no ledger-provenance input. [1]

- The memory-quality attestation binds candidate-state, code/memory trees, report bytes, and validators. [2]

- Route review binds code tree, task intent, per-evidence-file SHA-256, and validator. [5]



### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.

## KS-R15@v1 Assessment Policy And The Coherence Record's Own Edge

`curator-coherence/v1` permits `review-record` edges that declare stored assessment content addresses
as direct dependencies. The record's own edge
to the assessment is the only direction: the assessment does not declare the record it lives in,
because a record citing itself is the self-invalidating sequence the design exists to avoid.

The `review-assessment/v1` policy requires exactly the inputs `KS-R15@v1` §5.1 enumerates and
nothing else: `candidate-state` is the exact knowledge snapshot identity, `code-tree` and the optional
`memory-tree` are the source trees, `semantic-topology` is the registered-scope manifest,
`task-intent` is the task/requirement identity pair, `evidence-bytes` is the cited bytes, and
`validator` is the resolver/policy version pair. `review-record` is deliberately **not** required
there, for the direction reason above.

- The closeout door binds the code tree, an optional memory tree, topology, intent and review/memory/admission/scheduling provenance. [3]
- Lifecycle operations bind the admitted candidate, gate policy and normalized input; closeout and direct landing also bind code tree, task intent and admitted door. [4]
