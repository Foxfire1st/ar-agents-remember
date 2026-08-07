# dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Background filtering, collapse, focus, and acknowledgment UI. | `SetOutcomeToasts` | dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx:58-142 |
| Persistence and collapse regression cases. | "persists until explicitly marked seen; view alone only focuses the seat", "SEVERAL sessions with outcomes collapse into ONE stack (§9.8 toast discipline)" | dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx:46-63; dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx:65-75 |
| Shared attention and chip derivation. | `deriveSetChips` | dashboard/src/data/setChips.ts:58-216 |
| Explicit acknowledgment driver. | `acknowledgeSetAttention` | dashboard/src/data/setClient.ts:386-391 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 4 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 aligned the visible action with the authoritative
  `mark seen` wording; focus/view remains non-acknowledging. Verification metadata remains pinned
  to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R6 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the uncommitted code lands.
