# dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Persistent background-session surface for unacknowledged set outcomes.

## Code Commentary

### Logic

Filters running, unfocused sessions to those with set attention. One affected session renders its
evidence chips; several collapse into one disciplined stack. Each row can focus the seat or use
the explicitly labelled `mark seen` action to acknowledge its evidence.

### Conventions

The focused seat uses its inline chips instead of a duplicate toast. Mark seen acknowledges local
attention; it does not delete server evidence.

### Invariants And Boundaries

Outcomes persist through unrelated focus changes until acknowledged. Several background outcomes
never produce several competing toast stacks.

### Todos

None recorded; shared chip derivation caveats are recorded in `setChips.ts.md`.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Background filtering, collapse, focus, and acknowledgment UI. | L58-L142 | [SetOutcomeToasts.tsx](SetOutcomeToasts.tsx) |
| Persistence and collapse regression cases. | L33-L74 | [SetOutcomeToasts.test.tsx](SetOutcomeToasts.test.tsx) |
| Shared attention and chip derivation. | L1-L232 | [../../data/setChips.ts](../../data/setChips.ts) |
| Explicit acknowledgment driver. | L326-L336 | [../../data/setClient.ts](../../data/setClient.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 aligned the visible action with the authoritative
  `mark seen` wording; focus/view remains non-acknowledging. Verification metadata remains pinned
  to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R6 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the uncommitted code lands.
