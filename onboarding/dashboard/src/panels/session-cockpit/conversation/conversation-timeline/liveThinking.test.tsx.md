# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/liveThinking.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/liveThinking.test.tsx`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../overview.md`                                          |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The 260731-EFA-L7 R15/R17 acceptance pins for live-thinking coalescing, re-applied onto the L8 conversation-timeline split. An interleaved stream of repeated empty reasoning items, repeated `turn/diff/updated` notifications, and one genuinely unknown vendor notification must render at most one live thinking indicator, zero diff-update unknown-vendor rows, and preserve the truly unknown notification as addressable evidence.

## Code Commentary

- `render one live indicator for repeated empty reasoning and preserves unrelated unknown evidence` — empty streaming thinking items coalesce into one `live-thinking` row; completed substantive reasoning renders as an ordinary row; the unknown vendor item stays addressable.
- Completion cleanup and content-bearing streaming variants are pinned per the L7-FIX-3 interleaved pins (earlier-turn finalize then later-turn content-bearing update/completion).
- The harness imports the timeline family's `test-utils`/`msg`; the scenarios are verbatim from the pre-split acceptance test.

## Invariants And Boundaries

- At most one live indicator per active turn identity; completed reasoning with real content is never deleted.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The timeline component under test. | `ConversationTimeline` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/ConversationTimeline.tsx:56-106 |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the live-thinking acceptance suite. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
