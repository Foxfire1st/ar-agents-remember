# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/worker.md`. It gives installed runtimes the same one-real-leaf
builder lifecycle and owns no independent worker doctrine.

## Logic

The packaged source carries the canonical worker's brief/task-document intake, worktree and coding-
guideline orientation, implementation loop, leaf-scoped checks, mandatory turn report, structural
parent escalation, and separation from curator/closeout machinery. The complete tree is copied from
canonical skills; package-only workflow additions are forbidden drift.

The synchronized quality boundary uses the pinned Dagger graph for Agents Remember acceptance.
Worker/leaf checks select targeted mode with the explicit leaf diff base; full mode belongs once
to master integration. Host pytest/wrapper runs are refused, and a constrained lifecycle
environment alone explicitly configures a hard cap.

## Conventions

- Change worker doctrine only in canonical `skills/`.
- Propagate and verify through `scripts/sync-skills.py`.
- Keep this file byte-identical while retaining its own path-specific verification metadata.
- Do not append task-local deltas to the packaged artifact card.

## Invariants And Boundaries

- Installation cannot grant workers gates, closeout, integration, task-state, or memory authority.
- Worker identity remains canonical leaf document plus role.
- Durable turn report and terminal/finalizer truth remain the completion evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged worker is one leaf-scoped builder with a report terminal state. | "## What This Seat Is" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:7-17 |
| Its build phase produces evidence for a separate curator. | "### 3 — Build" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md:59-69 |
| The canonical source owns this doctrine. | "# Lifecycle — Worker" | skills/l-01-agent-lifecycles/roles/worker.md:1-33 |
| MCP package data is copied from canonical skills and checked for drift. | "mcp package data"; `sync_target`; `check_targets` | scripts/sync-skills.py:43-47; scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## R39 Generic Worker Checks

Workers copy repository-specific acceptance requirements from the resolved workflow, coding
guidelines, and tools memory; they may not choose a familiar runner. Leaf closeout owns change-set
acceptance, leaf integration does not rerun it, and full acceptance belongs to master integration.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: replaced repository-specific worker commands with the
  resolved contract and fixed cadence. Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized Dagger-only leaf acceptance,
  required explicit diff base, master-owned full mode, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  canonical worker boundary: leaf checks remain targeted and master full gates
  use host-managed RAM/swap by default.

- 2026-08-11T14:25+02:00 — Replaced accumulated copy-specific/task-delta prose with the exact
  synchronized worker-artifact contract and current source evidence.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay and idle-safety doctrine.
- 2026-08-08T02:00+02:00 — Synchronized leaf/master quality altitude boundaries.
- 2026-07-05T01:30+02:00 — Established the self-contained packaged worker lifecycle.
