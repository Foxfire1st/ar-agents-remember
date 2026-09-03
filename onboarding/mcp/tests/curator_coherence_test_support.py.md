# curator_coherence_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/curator_coherence_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

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
validator's expectations cit:([`write_curator_evidence`], mcp/tests/curator_coherence_test_support.py:111-160).

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

## Docs References

No external Domain Documentation source is configured for this repository-internal fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is required for the fixture contract. | n/a | n/a |

## Repo-Internal References

The helper mirrors the production task-resolution and publication boundaries rather than
reimplementing their authority logic.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture writes a complete leaf/master/sprint lineage and returns the architect's exact sprint reference. | `write_curator_task_topology` | mcp/tests/curator_coherence_test_support.py:28-80 |
| The fixture authors structured source evidence and routes prepare/publish through the production action owner with exact CAS identities. | `write_curator_evidence` | mcp/tests/curator_coherence_test_support.py:83-158 |
| Production resolves the exact leaf, master, and sprint and rejects missing topology. | `_task_context` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:382-404 |
| Production publication refuses a changed contract under the task lock before atomically replacing the authority. | "curator-coherence-contract-stale" | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:163-203 |
| R03 attestation declaration builder used by the fixture. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-129 |

## Cross-Repo References

No meaningful cross-repository reference applies. Temporary external-memory repositories are
always addressed through the fixture contract and do not own coherence authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository authority is introduced by this helper. | n/a | n/a |

## MCAR-L03 Fixture Pair Authority

Fixture attestations now derive their mandatory pair through the production resolver after
creating the real onboarding root. Tests therefore cannot hand-author a pair that bypasses branch,
base, repository, or path checks.

## 260831-CCR-R03 Fixture Tree Binding

The fixture now captures the exact code/memory candidate trees and declares them in the
attestation dependencies (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the fixture's exact candidate-tree capture and attestation dependency declaration; prior lineage, CAS, and pair prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: routed coherence fixtures through the production exact-pair
  resolver. Dagger verification remains closeout-owned.

- 2026-08-29T18:40+02:00 — Re-read the task-topology claim against the current production
  `_task_context` resolver and regenerated its exact range; the complete-topology fixture contract
  remains unchanged.

- 2026-08-29T11:41+02:00 — Created for the shared structured-authority fixture repair after the
  closeout Dagger gate exposed stale task ordering, incomplete task topology, and stale contract
  objects across multiple suites. Verification metadata remains closeout-owned.