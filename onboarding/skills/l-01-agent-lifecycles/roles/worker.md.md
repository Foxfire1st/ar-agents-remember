# skills/l-01-agent-lifecycles/roles/worker.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/roles/overview.md` |

## Governing Overview

[roles overview](overview.md)

## Purpose

The worker is one short-lived implementation seat on one canonical leaf document. It reads its
complete brief and leaf task document, changes code in the named worktree, runs prescribed
leaf-scoped checks, and writes the mandatory builder turn report. Its terminal state is checks green
plus report written.

## Logic

The worker orients by pairing current worktree reads with onboarding and coding guidelines before
the first edit. It implements the approved leaf, fills only small unambiguous gaps, and records
changed paths, diff summary, tests, retrieval evidence, escalations, and onboarding observations in
the turn report. Observations are evidence for a separate curator; the worker does not write
accepted onboarding.

Closeout, integration, finalization, gates, task-document status, and memory quality belong to the
owning seat/curator chain. The worker communicates upward with structural `message_parent`; the
control plane derives the current parent occupant. Completion follows the durable report plus
terminal/finalizer truth, not a runtime-addressed model post.

## Conventions

- One leaf, one worker seat, one appendable report artifact.
- Native reads in the actual worktree are the edit precondition.
- Read/search fan-out may assist, but the main worker owns edits and the report.
- Fix rounds resume the same worker when possible and append round evidence.
- A plan delta beyond blank filling escalates one rung to the owning seat.

## Invariants And Boundaries

- Worker identity is the canonical leaf document plus `worker` role.
- Worker never commits, closes out, integrates, decides gates, or mutates accepted memory.
- Worker never absorbs manager, reviewer, curator, architect, orchestrator, or strategist work.
- No seat-local watcher or polling loop substitutes for the agent-notifier fact relay.
- Runtime session and lifecycle ids remain private control-plane correlation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The worker is one leaf-scoped builder whose terminal state is checks plus report. | "## What This Seat Is" | skills/l-01-agent-lifecycles/roles/worker.md:7-17 |
| Intake binds writes to the named code worktree and report path. | "### 1 — Intake" | skills/l-01-agent-lifecycles/roles/worker.md:35-42 |
| Orientation requires current worktree reads and coding guidelines before edits. | "### 2 — Orient (paired reads before edits)" | skills/l-01-agent-lifecycles/roles/worker.md:44-57 |
| Build produces implementation plus evidence for the separate curator. | "### 3 — Build" | skills/l-01-agent-lifecycles/roles/worker.md:59-69 |
| The mandatory turn report is the durable builder artifact. | "### 5 — The Turn Report (mandatory, your last act)" | skills/l-01-agent-lifecycles/roles/worker.md:81-90 |
| Tool authority excludes lifecycle, gates, task state, and memory writes. | "## Tool Surface (positive statement — this is all of it)" | skills/l-01-agent-lifecycles/roles/worker.md:92-105 |

## R39 Generic Worker Doctrine

The canonical worker role requires the brief to carry the repository-resolved acceptance
environment and evidence. Workers do not select a host runner or compatibility fallback; leaf
closeout and master integration own the only acceptance runs.

## Update History

- 2026-08-14T11:29+02:00 — R39 curator: reconciled canonical worker guidance with generic
  repository-resolved policy. Verification remains closeout-owned.

- 2026-08-11T14:20+02:00 — Rewrote the default body around real-leaf implementation, durable
  evidence, structural escalation, and separate curator ownership.
- 2026-08-09T12:08+02:00 — Fact-relay supervision replaced seat-local watcher/ladder language.
- 2026-08-08T02:00+02:00 — Leaf checks became change-set scoped; full quality remained master-owned.
- 2026-07-05T01:30+02:00 — Established the self-contained worker lifecycle and report terminal state.
