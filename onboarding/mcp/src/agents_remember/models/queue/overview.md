# mcp/src/agents_remember/models/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

The closeout-queue wire model package (260815-DAG master full-gate repair): `closeout_queue.py`
(the typed `CloseoutQueueRequest`/response models) moved here from `models/` (flat) so the queue
contracts own one package.

## Hot Path Summary

The closeout queue application/tool surfaces read and write these typed models; the registered
response models are consumed by the dashboard's CloseoutQueue panel projection.

## Conventions

- Queue models are JSON-primary and round-trip; changes must stay backward-readable.

## Invariants And Boundaries

- This package holds wire models only — queue behavior lives in `worktrees/queue/` and
  `application/closeout_queue.py`.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `models/queue` route —
  `closeout_queue.py` moved from `models/` (flat). Verified at code commit e5cb139f.
