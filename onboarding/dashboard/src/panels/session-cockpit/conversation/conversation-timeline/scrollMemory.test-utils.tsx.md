# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The describe-scoped geometry shim for the split scroll-memory suites, extracted from
`renderer.test.tsx` by the 260731-EFA-L8 split. `installScrollMemoryGeometry` stubs
the DOM geometry the virtualizer needs; `feedOf`/`pinGeometry` build feeds and pin
viewport geometry for the assertions.

## Code Commentary

### Logic

`alignedTops` records the stubbed row tops; `pinGeometry` sets scrollHeight/
clientHeight so scroll-restore assertions are deterministic.

### Conventions

Test-only; installed per describe scope.

### Invariants And Boundaries

Must be restored/installed per suite to avoid leaking geometry across test files.

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
| The geometry shim helpers. | `installScrollMemoryGeometry`; `feedOf`; `pinGeometry` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:11-31; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:33-37; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory.test-utils.tsx:39-42 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  scroll-memory geometry shim extracted from `renderer.test.tsx`. Verification
  pinned to the leaf base until closeout stamps the code commit.
