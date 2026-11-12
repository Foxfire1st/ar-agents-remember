# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_errors.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `DirectLandingError` as its public seam. [1]
- The typed recovery next-action carried by the error. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-R02@v2 Recovery Guidance

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, consumers return the exact
unavailable/stale reason and route the record through its canonical operation. The optional
`next_action` on `DirectLandingError` is the typed carrier the application payload forwards
(`application/lifecycle/direct_landing.py`). Part of the landed L25 candidate `99dc249b`.
