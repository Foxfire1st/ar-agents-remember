# mcp/src/agents_remember/models/queue

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/queue` |

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

- Queue projection vocabulary. [1]

## 260821-CLIVE Final Projection-Only Model

This route no longer models a mutable closeout queue. `closeout_queue.py` defines only status and
idempotent rebuild requests plus the effective response: invalid-empty/valid-built service
condition, source classification and fingerprints, bounded source problems, waiting-generation
members, first-ready identity, and next action. Candidate claim/certification, grades, blockers,
receipts, commits, integration, and lifecycle transitions are intentionally absent.

The projection answers one question: which waiting candidates are currently schedulable from the
exact current canonical source? It may be discarded and rebuilt at any time without losing
operation evidence.
