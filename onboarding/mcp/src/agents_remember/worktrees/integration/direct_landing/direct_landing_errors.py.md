# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Typed refusals shared by direct-landing admission and recovery.

## Code Commentary

### Logic

The public surface is `DirectLandingError`. Direct landing is one journaled task/contract-addressed generation. Accepted code and repository state are immutable, intent precedes each memory or ledger mutation, produced commits are journaled before the next leg, and restart resumes the same generation instead of repeating raw Git from scratch.

Since 260831-CCR (commit `99dc249b`) `DirectLandingError` carries an optional typed
`next_action` (constructor keyword, line 15-18; stored at line 24), so a refusal caused by
missing/stale canonical task intent can advertise exactly the republish/recover route the public
tool should follow without leaking private operation identity.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- A missing-intent direct-landing generation cannot be recovered or retried as current; the typed
  error names the republish route.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `DirectLandingError` as its public seam. | `DirectLandingError` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py:8-25 |
| The typed recovery next-action carried by the error. | `next_action` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py:15-24 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-R02@v2 Recovery Guidance

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, consumers return the exact
unavailable/stale reason and route the record through its canonical operation. The optional
`next_action` on `DirectLandingError` is the typed carrier the application payload forwards
(`application/lifecycle/direct_landing.py`). Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  `DirectLandingError` now carries an optional typed `next_action` so task-intent refusals
  advertise the exact recovery route; documented the new seam. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
