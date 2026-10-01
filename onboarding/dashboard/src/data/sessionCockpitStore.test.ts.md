# dashboard/src/data/sessionCockpitStore.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the cockpit client store (260715-FEUI-L2 S3) — the design-§4.3 honesty invariants
pinned as store behavior.

## Code Commentary

### Logic

- **perSession skeleton** — honest defaults materialize on first touch (evidence tier `pending`,
  empty ledgers); pending sets are PER KIND (a model set never clobbers an in-flight effort set).
- **Set ledger + acknowledgment (F22)** — entries append unacknowledged and are acknowledged
  explicitly; **"QUEUED NEVER MOVES THE EFFECTIVE MARKER"** — ledger writes leave `launchEvidence`
  untouched (the core L4-honesty regression case).
- **Client queue (F13)** — enqueue, supersede the LAST live item (the alt+↑ pop-back; requestId
  never resent), dequeue by requestId.
- **Freshness + poll health (R15)** — per-pane ws state + last output; three missed beats flip
  `healthy`, one success restores it.
- **Turn clock** — starts on an observed transition INTO working, clears on leaving it; the
  `startCockpitMirror` case drives it through a real `sessionStore` write.
- **Orchestration-tree toggle** — persists per user via localStorage (the leaf's open-question
  decision).

### Invariants And Boundaries

Store reset between cases; localStorage cleared. The marker-invariance case must keep failing if
any ledger path ever writes `launchEvidence`. Test-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The module under test. [1]
- The registry the mirror case writes through. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

The store suite now locks authoritative queue derivation, protected-active retention, pending
withdrawal, one-slot recovery, and exact draft/answer revision-CAS behavior. It also proves newer
edits and successor requests cannot be cleared, restored, or dismissed by stale actions.
