# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Same-generation journal recovery and direct-landing execution ownership.

## Code Commentary

### Logic

Direct recovery enters through `recover_direct_landing_under_authority`; same-generation requeue is supplied by `generation.resume.requeued_same_generation`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor; ambiguity routes to same-generation recovery.

`recover_direct_landing_under_authority` delegates the pre-attempt recoverability guard, typed
post-failure translation, and strict-current-record selection to named helpers. Only the
integration boundary's typed `DirectLandingError` enters public recovery translation. An
unexpected `RuntimeError` is an invariant defect and propagates instead of being mislabeled as a
recoverable operation outcome. This centralizes the public error vocabulary without hiding defects.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Every typed direct-attempt failure is reclassified once against the latest journal record before
  a public refusal is returned; callers do not reproduce the lower-level failure family. Untyped
  invariant failures remain loud.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `recover_direct_landing`; `direct_recovery_refusal`; `reconcile_control_mutations` as its public seam. | `recover_direct_landing_under_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py:39-70 |
| One translator reclassifies typed direct failures against current evidence while invariant runtime errors remain loud. | `_direct_recovery_failure`; `_current_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py:82-109 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Caller-Owned Recovery Authority

`recover_direct_landing_under_authority` no longer acquires the integration lock internally; its
caller must already own that authority. Recovery stays in the same generation, uses strict current
reads, and routes ambiguous classifier states to developer decision. The retired successor-WAL
bypass and synthetic recovery paths are absent.

## Update History

- 2026-08-28T14:18+02:00 — Corrected the recovery boundary and source citations: typed direct
  errors are translated for tools, while invariant-breaking runtime errors remain loud.

- 2026-08-28T11:32+02:00 — Restricted public recovery translation to `DirectLandingError`; raw
  runtime invariant failures now propagate and cannot masquerade as same-generation recovery.

- 2026-08-27T18:33+02:00 — Consolidated repeated recovery exception translation and current-record
  lookup into one typed boundary. Public behavior remains unchanged; the former CRAP offender now
  has cyclomatic complexity 3.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; caller-owned same-generation recovery remains unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded caller-owned integration authority and same-generation strict recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
