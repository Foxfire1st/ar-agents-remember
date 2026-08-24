# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Builds the stable lifecycle-operation candidate identity used for duplicate detection, retry binding, and candidate-change decisions.

## Code Commentary

### Logic

`LifecycleOperationCandidate` carries a canonical state payload, output tree, and SHA-256 fingerprint. The fingerprint serializes durable operation input, candidate state/tree, integration authority, and closeout candidate HEAD/tree in canonical JSON, making semantically relevant admission facts one immutable identity.

### Invariants And Boundaries

- Equivalent candidates serialize identically; a changed accepted input, tree, HEAD, or integration authority changes identity.
- Closeout passes normalized effective input, never raw messages, into the fingerprint.
- This fingerprint is operation-journal identity, not queue-owned lifecycle evidence.

### Todos

None recorded.

## Docs References

See task `260821-CLIVE-L1` L1-R3 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate identity has explicit state/tree/fingerprint fields. | `LifecycleOperationCandidate` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:16-20 |
| Canonical JSON binds normalized input and Git provenance. | `lifecycle_operation_candidate` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:28-60 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Bundled Candidate Identity

`LifecycleOperationCandidateBinding` bundles every route-specific identity fact instead of spreading
optional keyword arguments across callers. Its fingerprint covers input, state/tree, closeout
snapshot, integration authority, and the exact optional door generation id. Two operations that
differ at any authority surface cannot collapse into one replay identity.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded the typed candidate binding and door-aware fingerprint. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits closeout.
