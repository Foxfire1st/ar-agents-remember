# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

The closeout-queue mechanism package (260815-DAG master full-gate repair): `closeout_queue.py` and
its helpers (`closeout_preview`, `closeout_queue_blocker`, `closeout_queue_candidate_evidence`,
`closeout_queue_errors`, `closeout_queue_evidence`, `closeout_queue_graph`,
`closeout_queue_lifecycle`, `closeout_recovery`, `closeout_staged_quality`) moved here from
`worktrees/` (flat) / `worktrees/modules/` so the queue mechanism owns one package.

## Hot Path Summary

Closeout operations claim/publish queue candidates through the queue store; the lifecycle module
certifies and claims candidates for closeout; `closeout_staged_quality` gates staged code. The
application `closeout_queue.py` and the `worktrees/modules/*` operations consume this package.

## Conventions

- Queue errors carry `task-closeout-queue-*` / `task-sprint-linkage-*` typed statuses.
- The queue remains a bounded, evictable mechanism; the closeout register/sections stay canonical.

## Invariants And Boundaries

- Only the queue mechanism lives here; application entry points (`application/closeout_queue.py`)
  and models (`models/queue/`) are separate.
- The staged-quality gate refuses without a Dagger-certified candidate; no host fallback.

## 260821-CLIVE-L1 Preview And Recovery Boundary

This route's closeout preview renders the already-normalized effective plan and includes messages only for enabled legs. Its recovery helper brackets code and ledger Git mutations with journal intent/proof and treats verified-existing commits as projection facts, not fabricated mutations. These helpers do not make the scheduling queue an owner of input, commit evidence, operation generations, or lifecycle state; the queue redesign remains L3.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/queue` route —
  ten modules moved from `worktrees/` (flat) and `worktrees/modules/`. Verified at code commit
  e5cb139f.
