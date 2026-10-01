# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/test-utils.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The shared conversation-item fixture builder for the split timeline test files,
extracted from `renderer.test.tsx` by the 260731-EFA-L8 split. `msg` builds a typed
`ConversationItem` with the required `itemId`/`globalOrdinal`.

## Code Commentary

### Logic

`msg` fills required wire fields with typed overrides, so the split suites author
feed rows through one typed factory.

### Conventions

Test-only; typed through the conversation wire types.

### Invariants And Boundaries

Never imported by production code.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shared item builder. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
