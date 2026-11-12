# dashboard/src/cockpit/document-chat/newChatWhilePageReadPending.test.tsx

## Governing Overview

[src overview](../../overview.md)

## Purpose

Pin the operation-level chat binding while a left page's reads are still slow: the selected leaf's
chat is dispatched and bound before any abandoned page producer completes.

## Tested Boundary

The mounted case holds the body, summary and both change-set producers for the old selection, clicks
Start role, and asserts the dispatch to the selected task reference, the request-ID-bound document
chat lookup, the selected agent/workspace in `ar.open`, and the host `shown` event before the old
producers complete. It is a mounted client operation, not a live host or an installed timing.

## Evidence

- The case named `dispatches and binds the selected leaf chat while four abandoned page reads remain
  slow`.
- The production chat binding and the page stores it exercises.
