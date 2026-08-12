# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`                  |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The intent-lock suite split from `renderer.test.tsx` by the 260731-EFA-L8 test
split. Pins the B3 intent lock, follow-on-growth, and latest-chip behavior of the
timeline.

## Code Commentary

### Logic

Asserts that streamed growth follows the live bottom only while the user intent is
locked to bottom, and that the latest chip remains reachable.

The suite now installs the shared `installScrollMemoryGeometry()` fixture instead of duplicating
geometry hooks and switching fake timers back to real time inside individual tests. It imports
`feedOf` and `pinGeometry` from the same helper while retaining the local `msg` builder for
test-specific streamed rows. The shared fixture owns RTL unmount, pending-TanStack-debounce
discard, geometry cleanup, and only then real-timer restoration, so all ten passing assertions can
finish without a delayed 150 ms Virtualizer callback escaping jsdom teardown.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.
- Fake timers remain active through React Testing Library cleanup; no test may restore real timers
  while a rendered Virtualizer can still hold a pending debounce.

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
| The intent-lock suite owns its shared hermetic geometry/timer fixture at the unique B3 suite boundary. | "ConversationTimeline — intent lock, follow-on-growth, latest chip (B3)" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx:12-12 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-12T17:04+02:00 — 260731-EFA-L23 dashboard-gate repair: replaced duplicated geometry and
  per-test fake/real timer ownership with `installScrollMemoryGeometry`, `feedOf`, and `pinGeometry`.
  Focused Vitest is 10/10 with no unhandled teardown error; verification provenance remains
  closeout-owned.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  intent-lock suite split from `renderer.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
