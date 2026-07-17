# dashboard/src/panels/session-cockpit/SessionRail.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom rail suite (260715-FEUI-L2 S4/R11): every ruled rail behavior asserted on REAL DOM over
the shared `FLEET` fixtures.

## Code Commentary

### Logic

- **Rail-state matrix (R14)** — every fixture row's dot carries exactly the `stateGrammar` visual
  (`data-state`/color/pulse per row).
- **Vocabulary negative (R6)** — plants `resolvedModel`/`resolvedEffort` in fixtures and asserts
  they appear NOWHERE in the rail container; anatomy order dot | role | title | status | End
  proven via `compareDocumentPosition`; the `input?` chip tooltip carries the R16 prompt preview.
- **Ruled hierarchy (R5)** — spine flat, managers flat inside the master box, clusters indented
  with the active seat on top; the tree toggle swaps to the spawn-edge provenance view.
- **Fleet attention (R12)** — live rollup counts as filter buttons focusing the first matching
  seat; **highlight expiry** (fix round 1, finding 3): click → ring, resolve the seat via the poll
  path, re-render → ring gone (fails on the old snapshot-Set code); ZERO-STATE renders nothing
  even with seats working; master headers carry the dominant rollup badge.
- **Gate + brief joins (R13, R8)** — gate badge on rows whose leaf holds an UNDECIDED gate; the
  brief column is strictly two-state.
- **Completed folder + bulk end (R17)** — per-master fold collapsed by default and expandable
  (dormant rows render the compact `✕` End — fix round 1, finding 5); bulk end arms an inline
  preview NAMING every removed session, and the fetch-level assertion captures the exact posted
  sessionIds.
- **Freshness + footer (R15, R8)** — the stale banner past the missed-beat cutoff; anchored bus
  numbers; the honest never-ticked line (never fake numbers).
- **Cross-surface consistency (R14)** — renders the rail AND a HeaderStrip and diffs the two
  dots' `data-state`/color/pulse attributes (two surfaces, not one function twice).
- **Zero state (R9)** — the empty rail explains itself; waiting(reason) renders steady
  muted-amber when supplied.

### Invariants And Boundaries

DOM-position and DOM-negative assertions are the anatomy/vocabulary regression net; fetch is
stubbed per case; stores reset between cases. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L342-L744 | [SessionRail.tsx](SessionRail.tsx) |
| The shared fixtures every case builds from. | L10-L172 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The grammar the matrix compares against. | L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R11; fix round 1 added the
  highlight-expiry case and the dormant-✕ assertion): the rail-state matrix, anatomy +
  model-leakage negatives, ruled hierarchy + tree toggle, attention strip incl. expiry +
  zero-state, gate/brief joins, completed folder + naming bulk end, freshness/footer honesty, the
  cross-surface dot comparison, and the explained zero state. Verification metadata pinned to the
  leaf base until closeout stamps the L2 code commit.
