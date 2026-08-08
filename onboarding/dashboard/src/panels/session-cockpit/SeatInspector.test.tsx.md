# dashboard/src/panels/session-cockpit/SeatInspector.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SeatInspector.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af` |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tab navigation and hidden-panel draft retention. | "exposes keyboard-navigable Evidence, Capabilities, and Bus tabs"; "retains an open Bus draft across click and keyboard tabs while hiding inactive controls" | dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:29-46; dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:48-91 |
| Off-tab success/error settlement and no-focus Bus. | "settles posted and error replies on their exact entries while the Bus tab is inactive" | dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:93-160 |
| Carried L6 evidence cases. | "names the pane archetype for controlled vs legacy raw seats (R1)"; "shows the verbatim pending-interaction payload (the unrepresentable fallback's target)" | dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:187-196; dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:212-222 |
| Explicit mark-seen and seat-switch regressions. | "viewing the ledger does not acknowledge; the explicit mark-seen action does (F22)"; "switching seats never acknowledges the newly focused seat" | dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:251-273; dashboard/src/panels/session-cockpit/SeatInspector.test.tsx:275-292 |
| Composition host under test. | `SeatInspector` | dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-161 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 10 citation finding(s); scoped recheck clean.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 added integrated tab/hidden/off-tab settlement/no-focus
  coverage and retained the earlier evidence contracts. Verification metadata remains pinned to the
  leaf base until closeout.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 added set-ledger and explicit mark-seen coverage.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 archetype, residual, and raw evidence.
