# mcp/src/agents_remember/models/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

Owns the public status/rebuild request and response models for the disposable sprint scheduling
projection.

## Hot Path Summary

This route models only invalid-empty/valid-built service state, exact source identity/problems,
waiting-generation members, first-ready identity, and the next legal scheduling action. Claims,
workers, commits, certification, integration, cancellation, recovery, and terminal evidence belong
to their door/journal owners and are absent here.

The closeout queue application/tool surfaces read and write these typed models; the registered
response models are consumed by the dashboard's CloseoutQueue panel projection.

## Conventions

- Queue models are JSON-primary, strict, and generated into the public projection contract.
- Retired lifecycle fields are removed, not accepted through compatibility readers.

## Invariants And Boundaries

- This package holds wire models only — source census, member computation, publication, and rebuild
  behavior live in `worktrees/queue/`; application/tool adapters do not own lifecycle evidence.

## 260821-CLIVE-L2 Historical Intermediate Architecture

L2 still permitted lifecycle-shaped queue rows while moving operational authority to the root
journal. L3 completed their removal; this paragraph records that migration boundary and is not the
current model contract.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Queue projection vocabulary. | L71-L130; L259-L336; L355-L405 | `mcp/src/agents_remember/models/queue/closeout_queue.py` |

## 260821-CLIVE Final Projection-Only Model

This route no longer models a mutable closeout queue. `closeout_queue.py` defines only status and
idempotent rebuild requests plus the effective response: invalid-empty/valid-built service
condition, source classification and fingerprints, bounded source problems, waiting-generation
members, first-ready identity, and next action. Candidate claim/certification, grades, blockers,
receipts, commits, integration, and lifecycle transitions are intentionally absent.

The projection answers one question: which waiting candidates are currently schedulable from the
exact current canonical source? It may be discarded and rebuilt at any time without losing
operation evidence.

## Update History

- 2026-08-24T16:00+02:00 — Final cumulative closeout audit: corrected the route's
  top-level purpose, hot path, conventions, and invariants so the final projection-only contract is
  the live description and L2 remains history only.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the transitional mutable queue model with the final disposable projection response. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `models/queue` route —
  `closeout_queue.py` moved from `models/` (flat). Verified at code commit e5cb139f.
