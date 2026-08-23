# mcp/src/agents_remember/models/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

The closeout-queue wire model package (260815-DAG master full-gate repair): `closeout_queue.py`
(the typed `CloseoutQueueRequest`/response models) moved here from `models/` (flat) so the queue
contracts own one package.

## Hot Path Summary

This route still models the transitional pre-L3 queue: waiting/scheduling facts plus selected,
closeout-in-flight, certified, and integration-in-flight candidate states and commit-shaped evidence.
L2 makes the root journal authoritative for the new operation controls; L3 owns removing these
lifecycle-shaped queue fields and reducing this route to a disposable waiting-door projection.

The closeout queue application/tool surfaces read and write these typed models; the registered
response models are consumed by the dashboard's CloseoutQueue panel projection.

## Conventions

- Queue models are JSON-primary and round-trip; changes must stay backward-readable.

## Invariants And Boundaries

- This package holds wire models only — queue behavior lives in `worktrees/queue/` and
  `application/closeout_queue.py`.

## 260821-CLIVE-L2 Current Architecture

The current model still permits candidate lifecycle states, owner fingerprints, and exact closeout commit fields inherited from the pre-L3 queue. L2 does not use those rows as authority for retry, recover, cancel, revise, worker termination, direct landing, or legacy migration; those operations use the root journal. Removing the remaining lifecycle-shaped fields and rebuilding only from current task/door facts are explicit L3 work.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Queue projection vocabulary. | L71-L130; L259-L336; L355-L405 | `mcp/src/agents_remember/models/queue/closeout_queue.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `models/queue` route —
  `closeout_queue.py` moved from `models/` (flat). Verified at code commit e5cb139f.
