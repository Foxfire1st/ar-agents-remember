# dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx

## Governing Overview

[Session cockpit overview](overview.md)

## 260731-EFA-L8 Change

The suite gained the keep-alive assertions (B1: harness↔terminal keeps the PTY
stack alive through focus handoff) as part of the e2e-driven repair; existing
assertions are unchanged.

## Purpose

Exercises the structured-stage orchestration seams: bridge readiness, per-session mounted surfaces,
epoch attribution, freshness, and the interaction between view switches and scroll geometry.

## Code Commentary

### Logic

The suite mocks only the authority and conversation network edges while retaining the real stores.
It seeds warm projection pages, drives focused-session changes, and proves transient boot retries,
fail-loud bounds, LRU pool eviction, stale-epoch isolation, and view-switch restoration behavior.

The warm pages it seeds are now built by `conversationIdentity` / `conversationItem` /
`conversationStatus` / `conversationPage` (`test/fixtures/conversationWire.ts`) rather than cast
literals — 260731-EFA-L4. The seeded page is therefore materially more complete than it used to be,
and it is worth knowing which parts: the status previously carried only `revision` / `process.state` /
`turn` and now carries `identity`, `observedAt`, `freshness`, `evidence` and `process.generation`;
`capabilities` was an explicit `undefined` on a required field and is now the full 23-leaf tree;
`page.totalItems` is set; and each item carries a `turnId`. Note that "freshness" here and the M9
**authority** freshness case are unrelated facts — M9 is about the submission-authority cache having
no TTL, not about `ConversationStatus.freshness`.

### Conventions

Tests use explicit fake-timer windows and mock projection data rather than a live bridge. The PTY and
ambient telemetry are substituted only where their rendering is irrelevant to the stage contract.

### Invariants And Boundaries

A warm surface must remain mounted but hidden; a cold or evicted surface must not be reused. A slow
boot gets bounded transient retries, while terminal answers fail loud rather than being masked.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- Harness setup preserves real stores while replacing the authority and conversation network edges at their module boundaries. [1]
- Teardown unmounts while timers are fake, discards the virtualizer's orphaned debounce, and only then restores real time. [2]
- Boot, pool, epoch/freshness, scroll-restore, and persistent-layer matrices cover the stage seams (six describes). [3]
- Implementation under test (`ChatsStageBody`). [4]
- The typed page/item/status builders the warm seeds now use. [5]
- The `live.completeness` reason stays `null` under the all-`supported` tree. [6]
- The `history.toolCompleteness`/`history.completeness` cue stays `null` under the all-`supported` tree. [7]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.

## 260815-DAG Master Full-Gate Repair

`afterEach` is now async and flushes the virtualizer's 150 ms scroll-observer debounce (fake-timer clear + real-timer 200 ms settle) before jsdom teardown.
