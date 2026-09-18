# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Live Git evidence used to authorize lifecycle cancellation and recovery.

## Code Commentary

### Logic

Closeout cancellation reconciles only actual code and memory mutation evidence, then derives the matching recovery cells. There is no cancellation-specific ledger intent to preserve; exact protected-ref, worker-exit, and private-preparation proofs remain required.

The public surface is `prove_cancellable_git`, `unchanged_integration_refs`. Task-addressed retry, recover, cancel, resume, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; successor publication remains separately bound to exact cancellation and current candidate evidence. Output-free cancellation proves branch identity, HEAD/tree, and reflog identity unchanged while preserving a staged or repaired working-tree candidate as distinct successor input.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

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

### CCR private preparation boundary

Cancellation of retained private preparation first reopens the contract and verifies the preparation’s unchanged logical refs. Those per-intent facts are returned even when no Git mutation evidence exists, and are combined with mutation reconciliation when it does. Absence of published Git mutation is not enough to discard private preparation.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `_cancellable_closeout_facts` boundary implements the preparation contract above. | `_cancellable_closeout_facts` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:126-191 |

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_reconciled_closeout_record` reconciles actual mutations and derives their two recovery commit cells. | `_reconciled_closeout_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:86-123 |
| `_cancellable_closeout_facts` combines protected-output and private-preparation facts for cancellation. | `_cancellable_closeout_facts` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:126-191 |

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `prove_cancellable_git`; `unchanged_integration_refs` as its public seam. | `prove_cancellable_git` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py:34-83 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## CCR-L42 current candidate

The legacy-output recovery refusal now states that proven migrated output cannot be cancelled or resumed; the exact recovery path remains required before any successor action.

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=35f4eb8970d6f5d42663570e8f120218c60dee703489b040b747816bd8cb9ed1. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The legacy-output recovery refusal now states that proven migrated output cannot be cancelled or resumed; the exact recovery path remains required before any successor action.

- 2026-09-06T23:07:14+00:00 — History-format repair at the actual recorded repair time. The earlier reconciliation note recorded only a local calendar date; its time of day is unknown. Original note preserved verbatim: "- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins."


- 2026-08-29T10:09+02:00 — Separated protected Git output identity from staged/repaired candidate
  identity so an output-free failed gate can be cancelled without discarding its successor; retained
  loud developer-decision refusal for unattributed protected-ref changes.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; control evidence classification is unchanged.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
