# dashboard/src/data/sessionCockpitStore.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionCockpitStore.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `setOrchestrationTreeView` | dashboard/src/data/sessionCockpitStore.ts:227-227 |
| The registry the mirror case writes through. | `useSessions` | dashboard/src/data/sessions.ts:527-528 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The store suite now locks authoritative queue derivation, protected-active retention, pending
withdrawal, one-slot recovery, and exact draft/answer revision-CAS behavior. It also proves newer
edits and successor requests cannot be cleared, restored, or dismissed by stale actions.

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02: anchored 2 Repo-Internal citation rows with exact
  store identifiers and repository-relative sources; verification metadata and non-repo references
  remain unchanged.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — FEUI-L5: added store regression coverage for reliable-submit state,
  retention, withdrawal, recovery, and revision guards.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S3 (R11): skeleton defaults, per-kind
  pending sets, ledger acknowledgment + the queued-never-moves-the-marker invariant, queue
  supersession, freshness/poll-health cutoffs, turn-clock observation + mirror, and toggle
  persistence. Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
