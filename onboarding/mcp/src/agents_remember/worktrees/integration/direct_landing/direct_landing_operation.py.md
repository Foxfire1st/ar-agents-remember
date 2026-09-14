# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Durable synchronous coordinator for one direct-landing generation.

## Code Commentary

### Logic

The public surface is `DirectLandingRuntime`, `direct_landing_store`, `direct_landing_record`, `reconcile_direct_landing`, `reset_reconciled_attempt`. Direct landing is one journaled task/contract-addressed generation. Accepted code and repository state are immutable, intent precedes each memory or ledger mutation, produced commits are journaled before the next leg, and restart resumes the same generation instead of repeating raw Git from scratch.

`direct_landing_record` builds the journal snapshot for one exact request and carries no door
publication: a direct landing is admitted by its own request — the series contract, the branch HEAD
commit and tree, and the effective commit messages — not by a claimed closeout door
cit:([`direct_landing_record`], mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:169-213).

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- A direct-landing record never carries a door publication and declares no dependency set; admission
  is by the request's own contract, commit, tree and message inputs.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `DirectLandingRuntime`; `direct_landing_store`; `direct_landing_record` as its public seam. | `DirectLandingRuntime`; `direct_landing_store`; `direct_landing_record` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:45-161; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:167-168; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:168-206 |
| The record builder for one exact direct-landing request; it carries no door publication. | `direct_landing_record` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:169-213 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Door Intent And Convergent Recovery

The initial direct-landing record is built from the request alone and carries no door publication.
Reconciliation may record missing memory or ledger output commits only when the pure
recovery classifier proves them from accepted mutation lineage and deterministic bytes. The same
operation generation is resumed; ambiguous output remains a developer decision.

## 260831-CCR-R03 Dependency-Declared Direct-Landing Records

CCR-R03 taught records with an admitted door to declare their exact direct inputs at construction
(worker handover: notes/reports/260902-CCR-L03-worker-delivery.md). That declaration was removed when
`closeout_door` left the worktree contract and the integration path, so a direct-landing record now
names no dependencies; the section is kept as the record of what the R03 shape was.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the door-free record
  shape this card records is the frozen one. Re-read the card against the source:
  `direct_landing_store` `:165-167` and `direct_landing_record` `:169-213` both hold. No wording
  changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` changed
  since the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit — `closeout_door` left the contract and the integration path.
  Corrected four stale claims: the Logic paragraph, the invariant, the R03 reference row and the
  door-intent section no longer say a direct-landing record carries or declares a door publication
  or a dependency set, and the R03 section now records the removal. Verification metadata remains
  closeout-owned.
- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card claims against the frozen candidate source and repaired exact citation coordinates (direct_landing_store→167-168). Preserved claim prose; source-sha256=ee66d86bd49ae1b5457a9318b77cfa0badd1e6cf9082e0ba25f667f1fcd73e41; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): widened the `direct_landing_record` ranges to 169-213 so the cited ranges hold the declaration line.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the admitted-door dependency declaration on direct-landing records; prior door-intent and recovery prose preserved.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; door-bound direct landing and crash convergence are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded door-bound direct landing and classifier-authorized crash convergence. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
