# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory2.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory2.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The second scroll-memory suite split from `renderer.test.tsx` by the 260731-EFA-L8 test split.
Pins the remaining F-ac matrix: hidden-collapse clamps, trusted-user override, virtual measurement
shifts, and late-clamp protection. Its explicit fake-timer cases follow the shared suite rule:
unmount and discard pending callbacks before real timers return.

## Code Commentary

### Logic

Drives the geometry shim for clamp/override/measurement-shift scenarios and asserts the scroll
position never fights trusted input. Both `finally` blocks clean their render and fake-timer queue
before `useRealTimers`, preventing a pending Virtualizer debounce from crossing test teardown.

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
| The second scroll-memory suite. | "describe(\"ConversationTimeline — scroll memory (F-ac)\", () => {" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory2.test.tsx:12-12 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T22:22+02:00 — 260713-TES master integration repair: aligned both explicit
  fake-timer cases with the shared hermetic teardown order (unmount, clear, restore real time).

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the second
  scroll-memory suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
