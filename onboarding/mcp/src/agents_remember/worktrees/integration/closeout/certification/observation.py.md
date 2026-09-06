# mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:58:25+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Derives distinct certification candidate authorities from the actual leaf contract, canonical task observer, Git state and declared generated inputs.

## Code Commentary

### Logic

The observer requires one addressed leaf with a waiting or claimed door. It obtains canonical topology and task intent through the bound memory-quality service and matches the door's contract/task/topology/intent identities. It then observes the linked checkout's branch, conflict set, index and isolated add-all tree; all must match the prepared candidate.

Source authority requires complete current lineage. For each edge it captures source and descendant tips, verifies ancestry and rereads both tips to detect movement. Mutation authority binds the effective closeout input, code work ref and external-memory work ref. Generated authority binds profile declarations to the candidate; generated-artifact status remains `unknown` until the relevant producer proves freshness.

The result separates the semantic authority envelope from canonical input snapshots and original creation provenance. Snapshots retain the actual task, contract, effective-input, lineage and profile-declaration observations. `refuse` recursively projects typed evidence into the existing structured error boundary without accepting unsupported payloads.

### Conventions

Use the service port for canonical task observation; this worktree package does not import or duplicate the memory-quality observer. Semantic digests describe separate mutation/source/worktree/generated projections rather than one reused arbitrary fingerprint.

### Invariants And Boundaries

- Canonical topology and intent must both exist; topology alone cannot authorize a door.
- A detached/primary checkout, wrong branch, conflict, or difference between prepared/index/add-all trees refuses.
- Lineage or branch observations are read from their real owners, not inferred from task prose.
- Generated declarations are authority input, not a generated-output success claim.
- This observation does not issue a certificate or mutate a lifecycle journal; its isolated Git observation may materialize candidate objects.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The request/result separate prepared inputs from observed candidate and authority records. | `CandidateObservationRequest`; `ObservedCertificationCandidate` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:48-53; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:57-59 |
| Canonical input snapshots and structured refusal preserve real nested evidence. | `_snapshot`; `_finding_value`; `refuse` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:62-69; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:72-80; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:83-94 |
| Task/door authority, generated declarations and semantic projections are assembled from actual owners. | `observe_certification_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:97-189 |
| Mutation authority binds effective input and the actual memory work branch. | `_mutation_authority` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:192-210 |
| The linked checkout, prepared index and add-all tree must agree. | `_worktree_rules` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:213-246 |
| Every source edge is current, ancestral and unchanged across paired ref observations. | `_source_authority` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:249-294 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
