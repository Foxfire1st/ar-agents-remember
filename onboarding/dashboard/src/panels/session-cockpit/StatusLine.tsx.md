# dashboard/src/panels/session-cockpit/StatusLine.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/StatusLine.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the persistent focused-seat footer in a contractual order, combining proven launch,
state, work-queue, and freshness facts while leaving the UA-5 context/cost slot visibly absent.

## Code Commentary

### Logic

- Order is harness → model/effort plus `EvidenceBadge` → state dot/word and observed working
  elapsed → leaf/seat → pending sets and queued messages → exact `ctx — / cost — (UA-5 slot)`.
- Freshness follows with PTY websocket state, quiet duration, poll health/misses/beat age; optional
  panel actions and the keyboard hint sit at the right edge.
- Model/effort uses effective selection and exact-session snapshot truth, including explicit
  effort-not-echoed copy. Timers run only when elapsed/freshness needs to advance.

### Invariants And Boundaries

- Segment order and the literal UA-5 absence slot are product contracts.
- No token, cost, latency, or effort evidence may be synthesized.
- Elapsed is client-measured from an observed state transition and is labelled as bounded truth.

### Todos

UA-5 may replace the reserved context/cost placeholder when authoritative telemetry exists.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Derivations, bounded clocks, and contractual render order. | L56-L184 | [StatusLine.tsx](StatusLine.tsx) |
| Launch-evidence tier machine. | L1-L70 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| Model-local capability selection. | L1-L246 | [../../data/sessionCapabilities.ts](../../data/sessionCapabilities.ts) |
| Shared state grammar. | L1-L126 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  contractual status order and honest UA-5 absence. Verification metadata remains pinned to the
  leaf base until closeout.
