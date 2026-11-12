# dashboard/e2e/document-chat-cross-workspace.spec.ts

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

Browser fixtures exercise selected document chat steering across native workspace identities without treating a delayed open answer as a dead application.

## Code Commentary

The simulated frame host keeps answering while its agent-display reply is stalled. The case requires a named waiting line, no agent problem or unavailable banner, and no automatic agent-URL load after the first deadline. Explicit Retry after the fixture recovers loads the worker page and the displayed agent becomes the worker. This is controlled browser-host evidence, not the developer's post-landing installation walk or a real plugin upgrade.

## Evidence

- Responsive late display remains waiting without URL fallback; explicit Retry loads the selected worker page after fixture recovery. [1]
