# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T10:09+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Live Git evidence used to authorize lifecycle cancellation and recovery.

## Code Commentary

### Logic

The public surface is `prove_cancellable_git`, `unchanged_integration_refs`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor. Output-free cancellation proves branch identity, HEAD/tree, and reflog identity unchanged while preserving a staged or repaired working-tree candidate as distinct successor input.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- A failed pre-commit gate may leave the old candidate staged, and a repair may change the live
  candidate. Neither is generation-owned Git output. Cancellation records both accepted and
  observed candidate/index/status identities while protecting refs and commits from silent change.
- An unattributed protected-ref change is a developer decision; it is never routed to a same-
  generation recovery action that the current evidence does not legally admit.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `prove_cancellable_git`; `unchanged_integration_refs` as its public seam. | `prove_cancellable_git`; `unchanged_integration_refs` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:29-78; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:182-202 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-29T10:09+02:00 — Separated protected Git output identity from staged/repaired candidate
  identity so an output-free failed gate can be cancelled without discarding its successor; retained
  loud developer-decision refusal for unattributed protected-ref changes.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; control evidence classification is unchanged.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
