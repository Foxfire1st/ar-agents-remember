# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:58 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Constructs queued lifecycle records and captures exact integration branch authority for the lifecycle coordinator.

## Code Commentary

### Logic

External-memory integration snapshots use `memory_content_commit` as the task output and compare its ancestry with the actual memory target tip. Both the integration authority and any replay-conflict transaction carry that content commit directly; neither needs a ledger pairing or ledger commit.

`queued_operation_record` carries the supplied candidate state/tree, task intent and fingerprint into the operation identity, report locator and queued state. Closeout records receive initial mutation evidence; integrate records bind their declared dependencies. `snapshot_integration_authority` requires a completed closeout code commit, reads the actual target branch tips and ancestry, and captures both sides for external memory. Replay drift creates a conflict transaction for leaves; atomic series refuse opening a leaf conflict worktree.

### Conventions

The queued constructor and integration snapshot were extracted from the coordinator without changing their core behavior. The snapshot reads repository authority; the constructor returns an in-memory record.

#### Invariants And Boundaries

- Returning a queued record does not persist it or select certification: the lifecycle/store composition owns atomic initial selection, predecessor archival, door publication and launch.
- External-memory integration requires the memory repository and exact accepted content commit.
- Exact source refs and candidate commits remain distinct; observed drift cannot be replaced with guessed branch state.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `queued_operation_record` retains accepted candidate/task identity and initializes kind-specific evidence. | `queued_operation_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71 |
| `snapshot_integration_authority` captures actual code/memory target tips and accepted content outputs. | `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-137 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Queued records retain candidate/task identity and initialize kind-specific evidence. (`queued_operation_record`) | `queued_operation_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71 |
| Integration authority is captured from completed output and current target refs, with explicit replay boundaries. (`snapshot_integration_authority`) | `snapshot_integration_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:74-137 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:58 UTC — Rechecked the formatted L9 working candidate and rebound current references after source cleanup; source-sha256=c0056ffe05fc5db99243472347d8a2d60a2ade05fdaef726ec5bde755dad69bb. The older working-candidate snapshot and verification provenance are retained.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=4cf732837171012c13c681030dd8f8d20ec0c646ec05c52d4a2fc3049fd76553. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
