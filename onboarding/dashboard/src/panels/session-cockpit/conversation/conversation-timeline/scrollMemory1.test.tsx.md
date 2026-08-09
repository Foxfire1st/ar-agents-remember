# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `a8693de1c5cad77767f10e5b9b80298d3ffa8faa`                  |
| lastVerifiedCommitDate | 2026-08-09T22:37:12+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The first scroll-memory suite split from `renderer.test.tsx` by the 260731-EFA-L8 test split.
Pins the F-ac scroll-memory matrix: middle/top and bottom restoration, later inflow at bottom,
geometry settling, and the persistent latest control. Fake-timer cases explicitly unmount and
discard pending callbacks before returning to real time, matching the shared fixture's hermetic
teardown contract.

## Code Commentary

### Logic

Uses the describe-scoped geometry/timer shim (`scrollMemory.test-utils.tsx`) to drive restore
scenarios deterministically. Each explicit fake-timer `finally` performs `cleanup` and
`clearAllTimers` before `useRealTimers`, so a TanStack scroll debounce cannot be promoted into the
next case or the destroyed jsdom environment.

### Invariants And Boundaries

Assertions preserved from the monolithic suite. Timer restoration must follow render cleanup.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The first scroll-memory suite. | "describe(\"ConversationTimeline — scroll memory (F-ac)\", () => {" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx:12-12 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T22:22+02:00 — 260713-TES master integration repair: made every explicit
  fake-timer case unmount and clear pending Virtualizer callbacks before restoring real timers.
  Five repeated focused runs (80/80 test executions) and the full 1,551-test dashboard suite pass
  without the former post-suite `window is not defined` exception.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the first
  scroll-memory suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
