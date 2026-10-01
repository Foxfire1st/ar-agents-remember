# curator_coherence_test_support.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Provides the shared structured curator-coherence fixture boundary for lifecycle tests. The helper
creates a complete leaf/master/sprint task lineage when a low-level closeout fixture needs one,
authors the upstream memory-quality attestation plus explicit agent judgments, and drives the same
prepare/publish implementation used by the public tool. It never hand-writes the canonical
coherence authority or its Markdown projection.

## Code Commentary

### Logic

`write_curator_task_topology` writes the exact organizational master and commanding sprint around
an already-authored leaf and returns the sprint reference that may publish as architect.
`write_curator_evidence` preserves an existing attestation's candidate tuples during task-only
fixture refreshes, writes the structured `ar-curator-memory-quality/v1` source attestation, builds
one explicit judgment per tuple, then performs prepare and publish with all optimistic-concurrency
identities. Repeated exact input may return `already-current`; changed task truth publishes a new
canonical generation.

Under CCR-R03@v1 the fixture attestation now stamps the exact code candidate tree
(`capture_future_code_candidate`) and memory candidate tree (scratch-indexed `worktree_candidate_tree`
over the memory worktree) and embeds the `memory-quality-attestation/v1` dependency declaration —
so the fixture can only produce attestations whose declared inputs match the production currentness
validator's expectations cit:([`write_curator_evidence`], mcp/tests/curator_coherence_test_support.py:105-202).

### Conventions

Callers mutate their task fixtures first, then call this helper with the exact curator leaf or
owning architect sprint identity. External-memory closeout fixtures use the complete-topology
helper; fixtures that already own canonical topology call only the evidence publisher.

### Invariants And Boundaries

- The helper supplies test inputs, never a parallel canonical-record writer.
- Semantic requirement revision, delivery attempt, and physical record digest remain separate
  fields even in fixture data.
- Candidate tuples are preserved only from the exact current structured attestation; filenames
  are not searched and Markdown is not reparsed as authority.
- Publication remains fail-closed on contract, task, code, memory, attestation, predecessor, or
  judgment drift because the production CAS implementation performs the write.
- The fixture derives candidate trees through the production capture/scratch-index helpers; it
  cannot fabricate a tree that mismatches the declaration.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository-internal fixture.

No relevant external documentation is required for the fixture contract.

### Repo-Internal References

The helper mirrors the production task-resolution and publication boundaries rather than
reimplementing their authority logic.

- The fixture writes a complete leaf/master/sprint lineage and returns the architect's exact sprint reference. [1]
- The fixture authors structured source evidence and routes prepare/publish through the production action owner with exact CAS identities. [2]
- Production resolves the exact leaf, master, and sprint and rejects missing topology. [3]
- Production publication refuses a changed contract under the task lock before atomically replacing the authority. [4]
- R03 attestation declaration builder used by the fixture. [5]

### Cross-Repo References

No meaningful cross-repository reference applies. Temporary external-memory repositories are
always addressed through the fixture contract and do not own coherence authority.

No cross-repository authority is introduced by this helper.

## MCAR-L03 Fixture Pair Authority

Fixture attestations now derive their mandatory pair through the production resolver after
creating the real onboarding root. Tests therefore cannot hand-author a pair that bypasses branch,
base, repository, or path checks.

## 260831-CCR-R03 Fixture Tree Binding

The fixture now captures the exact code/memory candidate trees and declares them in the
attestation dependencies (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).
