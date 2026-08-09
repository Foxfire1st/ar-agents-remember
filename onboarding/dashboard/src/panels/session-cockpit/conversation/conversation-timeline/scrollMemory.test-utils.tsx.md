# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `a8693de1c5cad77767f10e5b9b80298d3ffa8faa`                  |
| lastVerifiedCommitDate | 2026-08-09T22:37:12+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The describe-scoped geometry and timer-hygiene shim for the split scroll-memory suites, extracted
from `renderer.test.tsx` by the 260731-EFA-L8 split. `installScrollMemoryGeometry` stubs the DOM
geometry the virtualizer needs and keeps every suite case on fake timers; teardown unmounts all
renders, clears pending Virtualizer debounce callbacks, and only then restores real timers.
`feedOf`/`pinGeometry` build feeds and pin viewport geometry for the assertions.

## Code Commentary

### Logic

`alignedTops` records the stubbed row tops; `pinGeometry` sets scrollHeight/clientHeight so
scroll-restore assertions are deterministic. The before/after hooks deliberately bracket both
React cleanup and timer restoration: TanStack's scroll-observer unsubscribe removes listeners but
does not cancel its pending 150 ms debounce, so switching to real timers before unmount can let a
callback outlive jsdom and call React after `window` is gone.

### Conventions

Test-only; installed per describe scope.

### Invariants And Boundaries

Must be restored/installed per suite to avoid leaking geometry or timer callbacks across test
files. Renders must be unmounted and pending fake timers discarded before real timers return.

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
| The geometry and hermetic timer hooks, plus the feed and viewport helpers. | `installScrollMemoryGeometry`; `feedOf`; `pinGeometry` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:12-44; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:46-50; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:52-55 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T22:22+02:00 — 260713-TES master integration repair: made the shared
  scroll-memory fixture own fake-timer setup and teardown. It now unmounts renders and clears the
  Virtualizer's orphanable scroll debounce before restoring real timers, preventing callbacks from
  escaping jsdom teardown.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  scroll-memory geometry shim extracted from `renderer.test.tsx`. Verification
  pinned to the leaf base until closeout stamps the code commit.
