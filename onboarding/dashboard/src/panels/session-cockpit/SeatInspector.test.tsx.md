# dashboard/src/panels/session-cockpit/SeatInspector.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SeatInspector.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the integrated inspector contract: accessible tab navigation, native hidden semantics,
off-tab Bus interaction continuity, no-focus honesty, and the carried-forward L6/L4 evidence rules.

## Code Commentary

### Logic

- Keyboard tests cover Right/Left wrap, Home/End focus movement, selected state, and stable tabpanel
  relationships.
- Draft, posted, and retained-error cases prove the same Bus instances settle on exact `entryId`s
  while the panel is inactive. Accessibility queries prove hidden controls leave the active tree.
- No-focus coverage keeps fleet Bus rows reachable while Evidence/Capabilities state their limits.
- Carried-forward cases pin archetype/raw evidence, informational retire residuals, newest-first set
  lines, explicit mark seen, and the rule that render or seat changes do not acknowledge.

### Invariants And Boundaries

- State continuity must be tested through real tab transitions, not an isolated pane render.
- Native `hidden` semantics and mounted-instance persistence are both required.

### Todos

None recorded; browser integration smoke remains a leaf-level residual.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Tab navigation and hidden-panel draft retention. | L28-L92 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |
| Off-tab success/error settlement and no-focus Bus. | L93-L185 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |
| Carried L6 evidence cases. | L187-L223 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |
| Explicit mark-seen and seat-switch regressions. | L225-L305 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |
| Composition host under test. | L18-L151 | [SeatInspector.tsx](SeatInspector.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 added integrated tab/hidden/off-tab settlement/no-focus
  coverage and retained the earlier evidence contracts. Verification metadata remains pinned to the
  leaf base until closeout.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 added set-ledger and explicit mark-seen coverage.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 archetype, residual, and raw evidence.
