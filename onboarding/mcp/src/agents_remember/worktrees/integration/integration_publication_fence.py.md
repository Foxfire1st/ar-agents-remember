# mcp/src/agents_remember/worktrees/integration/integration_publication_fence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_publication_fence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T20:30+02:00 |
| lastVerifiedCommitHash | `205c0b664e7dbf6efd07c2c811d0d8295aa07c91` |
| lastVerifiedCommitDate | 2026-08-31T20:38:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Pure exact closeout-door classifier for integration authority. Leaf publication still requires
one exact claimed closeout/direct-landing source. An ordinary series integration is the aggregation
boundary above those leaf claims, so a fresh series contract with no closeout door is explicitly
valid `not-applicable`; it is not direct execution and does not consult `directExecutionEnabled`.

## Code Commentary

### Logic

The public surface is `IntegrationDoorAuthorityEvidence`, `IntegrationDoorAuthorityConflict`,
`classify_integration_door_authority`, `integration_door_decision_payload`. The classifier first
separates two legitimate door-absence cases: a fresh ordinary series contract and an already
journaled operation whose accepted publication recorded `not-applicable`. A fresh leaf without a
claimed source remains `preclaim-refused`. Claimed leaf authority is then compared against exact
live door and journal evidence. A moved, missing, unreadable, or contradictory ref is never
discarded: the same landing generation must reconcile or complete, with an executable
task-addressed handoff for any later repair or revert planning.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Series-level integration without a door is ordinary lifecycle integration, not branch-addressed
  direct execution; it neither requires nor authorizes `directExecutionEnabled`.
- An already-journaled `not-applicable` door state remains recoverable for its exact generation,
  while a fresh leaf may not use door absence as admission.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `IntegrationDoorAuthorityEvidence`; `IntegrationDoorAuthorityConflict`; `classify_integration_door_authority` as its public seam. | `IntegrationDoorAuthorityEvidence`; `IntegrationDoorAuthorityConflict`; `classify_integration_door_authority` | mcp/src/agents_remember/worktrees/integration/integration_publication_fence.py:27-47; mcp/src/agents_remember/worktrees/integration/integration_publication_fence.py:50-59; mcp/src/agents_remember/worktrees/integration/integration_publication_fence.py:62-83 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Exact Door-And-Journal Fence

The pure fence proves a claimed door plus a completed, active, retained closeout/direct source
journal. Journaled integration intent binds sprint, candidate, door generation, source kind,
generation, fingerprint, key, and source-journal digest. A proven post-intent mismatch is residual
conflict; a preclaim mismatch is refusal. Queue state and projection rows are never publication
evidence.

## Update History

- 2026-08-31T20:30+02:00 — 260831-DER: corrected the integration authority classifier so a fresh
  ordinary series integration records door authority as `not-applicable` without consulting the
  direct-execution policy flag. Preserved exact claimed-door enforcement for fresh leaves and the
  existing same-generation recovery semantics for already-journaled no-door operations.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced queue-derived publication proof with the exact claimed door/source journal fence. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
