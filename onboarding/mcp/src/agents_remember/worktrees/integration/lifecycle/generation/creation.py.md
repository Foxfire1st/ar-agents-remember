# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:08+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Package overview](overview.md)

## Purpose

Constructs queued lifecycle records and captures exact integration branch authority for the lifecycle coordinator.

## Code Commentary

### Logic

`queued_operation_record` carries the supplied candidate state/tree, task intent and fingerprint into the operation identity, report locator and queued state. Closeout records receive initial mutation evidence; integrate records bind their declared dependencies. `snapshot_integration_authority` requires a completed closeout code commit, reads the actual target branch tips and ancestry, and captures both sides for external memory. Replay drift creates a conflict transaction for leaves; atomic series refuse opening a leaf conflict worktree.

### Conventions

The queued constructor and integration snapshot were extracted from the coordinator without changing their core behavior. The snapshot reads repository authority; the constructor returns an in-memory record.

### Invariants And Boundaries

- Returning a queued record does not persist it or select certification: the lifecycle/store composition owns atomic initial selection, predecessor archival, door publication and launch.
- External-memory integration requires the memory repository, content commit and ledger commit.
- Exact source refs and candidate commits remain distinct; observed drift cannot be replaced with guessed branch state.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Queued records retain candidate/task identity and initialize kind-specific evidence. | `queued_operation_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71 |
| Integration authority is captured from completed output and current target refs, with explicit replay boundaries. | `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-143 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
