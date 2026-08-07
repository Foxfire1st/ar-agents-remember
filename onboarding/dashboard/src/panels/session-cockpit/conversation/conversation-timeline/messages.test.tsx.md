# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/messages.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/messages.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The message-grammar and diagnostics suite split from `renderer.test.tsx` by the
260731-EFA-L8 test split. Pins `MessageItem` grammar/images/clamp (R3), the
default-off `TerminalDiagnosticsDrawer` (R2/R7), and the structural axe pass over the
rendered grammar.

## Code Commentary

### Logic

Asserts image-ref alt/provenance with no fabricated fetch URL, the exact-count clamp
button, the agent-bus source badge, the closed drawer's `inert`/no-PTY-frame proof,
and zero structural axe violations.

### Invariants And Boundaries

The axe pass disables contrast/region because jsdom cannot lay out geometry.

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
| The grammar/diagnostics/axe suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/messages.test.tsx:2-2 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  messages/grammar suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
