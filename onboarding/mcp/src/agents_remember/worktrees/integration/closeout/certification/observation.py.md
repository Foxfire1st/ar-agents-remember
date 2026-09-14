# mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
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
| The request/result separate prepared inputs from observed candidate and authority records. | `CandidateObservationRequest`; `ObservedCertificationCandidate` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:49-54; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:58-60 |
| Canonical input snapshots and structured refusal preserve real nested evidence. | `_snapshot`; `_finding_value`; `refuse` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:63-70; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:73-81; mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:84-95 |
| Task/door authority, generated declarations and semantic projections are assembled from actual owners. | `observe_certification_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:98-194 |
| Mutation authority binds effective input and the actual memory work branch. | `_mutation_authority` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:197-215 |
| The linked checkout, prepared index and add-all tree must agree. | `_worktree_rules` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:218-251 |
| Every source edge is current, ancestral and unchanged across paired ref observations. | `_source_authority` | mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py:254-299 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## CCR-L42 current candidate

Certification observation now binds `admittedMemoryTree` from the closeout door's memory candidate tree and omits it when no tree is admitted, preserving legacy authority projections while recording the fresh memory-tree owner.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the live-door import
  shift was already re-derived. Re-checked all nine ranges against the frozen file
  (`observe_certification_candidate` `:98-194`, `_mutation_authority` `:197`): they hold. No wording
  changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/closeout/certification/observation.py` changed
  since the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  `live_closeout_door` import and now reads the door live, shifting every definition below by one
  line. Re-derived all nine cited ranges against the current source. No claim text changed;
  verification metadata remains closeout-owned.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Certification observation now binds `admittedMemoryTree` from the closeout door's memory candidate tree and omits it when no tree is admitted, preserving legacy authority projections while recording the fresh memory-tree owner.

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
