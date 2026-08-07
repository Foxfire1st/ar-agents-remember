# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/baseline.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/baseline.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The 10k tool-heavy DOM/interaction baseline suite split from `renderer.test.tsx` by
the 260731-EFA-L8 test split. Pins the R5.2/R5.10/L4.4 bounded-DOM invariant and the
axe pass at depth.

## Code Commentary

### Logic

Mounts 10,000 rotating items through the landed renderer and asserts the mounted DOM
stays bounded (`> 0`, `< 80`, AND `< total/100`), `aria-posinset` rides the 1-based
server ordinal, `aria-setsize="10000"` is honest, and a second `it` runs axe over
the deep feed.

### Invariants And Boundaries

The `mount < 3000 ms` ceiling is a jsdom tripwire, not a hardware ranking.

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
| The 10k baseline suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/baseline.test.tsx:9-120 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the 10k
  baseline suite split from `renderer.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
