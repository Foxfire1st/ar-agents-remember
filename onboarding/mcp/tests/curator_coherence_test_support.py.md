# curator_coherence_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/curator_coherence_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T18:40+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
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
| Production resolves the exact leaf, master, and sprint and rejects missing topology. | `_task_context` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:355-377 |
| Production publication refuses a changed contract under the task lock before atomically replacing the authority. | "curator-coherence-contract-stale" | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:163-203 |

## Cross-Repo References

No meaningful cross-repository reference applies. Temporary external-memory repositories are
always addressed through the fixture contract and do not own coherence authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository authority is introduced by this helper. | n/a | n/a |

## Update History

- 2026-08-29T18:40+02:00 — Re-read the task-topology claim against the current production
  `_task_context` resolver and regenerated its exact range; the complete-topology fixture contract
  remains unchanged.

- 2026-08-29T11:41+02:00 — Created for the shared structured-authority fixture repair after the
  closeout Dagger gate exposed stale task ordering, incomplete task topology, and stale contract
  objects across multiple suites. Verification metadata remains closeout-owned.
