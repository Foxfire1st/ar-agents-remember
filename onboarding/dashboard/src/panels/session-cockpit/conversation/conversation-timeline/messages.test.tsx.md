# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/messages.test.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The grammar/diagnostics/axe suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
