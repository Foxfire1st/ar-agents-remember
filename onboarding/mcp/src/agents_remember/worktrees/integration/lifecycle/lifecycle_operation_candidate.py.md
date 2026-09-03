# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle operation integration overview](overview.md)

## Purpose

Builds the stable lifecycle-operation candidate identity used for duplicate detection, retry binding, and candidate-change decisions.

## Code Commentary

### Logic

`LifecycleOperationCandidate` carries a canonical state payload, output tree, and SHA-256 fingerprint. The fingerprint serializes durable operation input, candidate state/tree, integration authority, and closeout candidate HEAD/tree in canonical JSON, making semantically relevant admission facts one immutable identity.

Since 260831-CCR (commit `99dc249b`) the candidate carries the canonical task intent:
`LifecycleOperationCandidate.task_intent` (line 22) and `LifecycleOperationCandidateBinding.task_intent`
(line 35) are typed `TaskIntentIdentity | None` fields; `lifecycle_operation_candidate` (line
34-79) folds the bound intent into the fingerprint payload (`payload["taskIntent"] =
binding.task_intent.model_dump(...)`, line 64-65) and returns the typed candidate with the intent
attached (line 79). The closeout admission path always supplies it, so the durable fingerprint now
covers the exact intent bytes; a changed or missing intent cannot be laundered into the same replay
identity.

### Invariants And Boundaries

- Equivalent candidates serialize identically; a changed accepted input, tree, HEAD, integration authority, or task intent changes identity.
- Closeout passes normalized effective input, never raw messages, into the fingerprint.
- This fingerprint is operation-journal identity, not queue-owned lifecycle evidence.
- A closeout candidate without intent has no canonical replay identity; callers treat it as not
  reusable.

### Todos

None recorded.

## Docs References

See task `260821-CLIVE-L1` L1-R3 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate identity has explicit state/tree/fingerprint/intent fields. | `LifecycleOperationCandidate` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:16-22 |
| Canonical JSON binds normalized input, Git provenance, and task intent. | `lifecycle_operation_candidate` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:34-79 |
| The binding carrier for the exact intent. | `LifecycleOperationCandidateBinding.task_intent` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:30-35 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Bundled Candidate Identity

`LifecycleOperationCandidateBinding` bundles every route-specific identity fact instead of spreading
optional keyword arguments across callers. Its fingerprint covers input, state/tree, closeout
snapshot, integration authority, and the exact optional door generation id. Two operations that
differ at any authority surface cannot collapse into one replay identity.

## CCR-R02@v2 Intent-Bound Candidate Identity

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, candidate identity now includes
the canonical task intent digest; a closeout or direct-landing operation whose intent differs cannot
replay as the accepted generation. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the lifecycle-operation candidate and binding now carry typed `task_intent` and include it in the
  durable fingerprint; documented the intent-bound replay identity invariant. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded the typed candidate binding and door-aware fingerprint. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits closeout.
