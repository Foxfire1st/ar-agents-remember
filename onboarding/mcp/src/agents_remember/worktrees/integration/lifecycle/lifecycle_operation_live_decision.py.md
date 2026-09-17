# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Bounded live-evidence refusals shared by lifecycle controls.

## Code Commentary

### Logic

Live refusal dispatch retains initial-door, direct-landing, and immutable-Git evidence checks. It no longer invokes a ledger-recovery classifier, so malformed or missing computed cache bytes cannot become a developer-decision refusal.

The public surface is `raise_live_evidence_decision`, `immutable_recovery_refusal`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `raise_live_evidence_decision` dispatches genuine publication and Git contradictions without inspecting ledger bytes. | `raise_live_evidence_decision` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py:32-72 |
| `immutable_recovery_refusal` turns immutable-evidence contradictions into bounded recovery refusals. | `immutable_recovery_refusal` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py:75-116 |

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `raise_live_evidence_decision`; `immutable_recovery_refusal` as its public seam. | n/a | [mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py](mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=d406e65c6fed439e79d0e1e5b98e10e8ea7dbe7f2abf65985ec36b14b37b6c2e. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed initial-door, ledger-recovery, and worker-termination package relocations; live lifecycle decisions are unchanged.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
