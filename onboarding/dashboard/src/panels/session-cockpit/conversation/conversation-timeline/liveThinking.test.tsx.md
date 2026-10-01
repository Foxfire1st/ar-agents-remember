# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/liveThinking.test.tsx

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

## Evidence

### Repo-Internal References

- The timeline component under test. [1]
