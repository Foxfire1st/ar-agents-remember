# mcp/src/agents_remember/worktrees/integration/integration_resolution_handoff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_resolution_handoff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Executable task-addressed handoff for reversible integration source drift.

## Code Commentary

### Logic

The public surface is `integration_resolution_required`. Protected-ref and door state are classified from exact live and journal evidence. A moved, missing, unreadable, or contradictory ref is never discarded: the same landing generation must reconcile or complete, with an executable task-addressed handoff for any later repair or revert planning.

The refusal's `summary` and `cancel_note` now route recovery through `worktree_sync` for the owning contract — settle any retained code or memory conflict (re-running the targeted test utility after code resolutions) — and then a new targeted closeout. They no longer instruct the operator to absorb a recorded source delta by hand; the refusal sentence itself is unchanged, and `replay` remains the carryover vehicle rather than this route's prompt.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `integration_resolution_required` as its public seam. | `integration_resolution_required` | mcp/src/agents_remember/worktrees/integration/integration_resolution_handoff.py:14-108 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/integration_resolution_handoff.py` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the resolution summary and cancel note were reworded). Re-read
  the card: it already records the reworded summary and its cited whole-file range still holds. No
  wording changed; verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Recorded the source-drift recovery rewording: the handoff summary and cancel note now route through `worktree_sync` plus a new targeted closeout, while the refusal sentence and protected-ref/door classification are unchanged. Re-derived the public-surface anchor against the current working tree. Verification metadata remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
