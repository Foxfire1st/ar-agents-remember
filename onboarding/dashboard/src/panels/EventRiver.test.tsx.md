# dashboard/src/panels/EventRiver.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EventRiver.test.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T03:10+02:00                           |
| lastVerifiedCommitHash | `4cdb1ef68e2c5f661ea11e12d46a68441ef18088`       |
| lastVerifiedCommitDate | 2026-07-06T01:49:54+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render tests for the Event River's readable activity-feed behavior.
The suite renders a **virtualized** EventRiver, so a `beforeAll` stubs `HTMLElement.prototype`
`offsetHeight`/`offsetWidth` to give jsdom a non-zero viewport (otherwise TanStack measures zero and no
rows mount). It preserves the original `read.packet` guarantees and pins known event summaries, task
context joins, task-document labels for lifecycle-only history rows, actor display labels, heartbeat
suppression, raw fallback behavior, the context-ready reload gate for lifecycle-bound rows, raw-stream
hydration empty-state behavior, and that the full window is retained and virtualized (no newest-60
display cap).

## Code Commentary

### Logic

Since L11 the suite's enclosure fixtures carry the REQUIRED `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags (default `true`) — the river renders events, not task rows, so behavior under test is unchanged.

A small `ev(...)` helper builds an `ar-observer-event/v1` event (defaulting `ts`/`trust`/`actor`/`id`).
Fixture helpers build minimal `LifecycleProjection`, `EnclosureNode`, `TaskDocNode`, and `Analytics`
objects so the tests can exercise the same task-label join the live dashboard uses. A `beforeAll` defines
`HTMLElement.prototype.offsetHeight`/`offsetWidth` as non-zero getters (restored in `afterAll`) so the
TanStack virtualizer measures a real viewport + rows in jsdom — without it every box reports 0 and nothing
mounts. Each test seeds the real Zustand store via `dashboardStore.setState(...)` and renders
`<EventRiver />`; `beforeEach` resets `events`, `lifecycles`, `enclosures`, and `analytics`, and `afterEach`
runs RTL `cleanup`. Cases cover:

- a single `read.packet` (its `data` carrying `repoId` + a one-entry `files` allowlist `{path, lines,
  status, bytes}`) renders the label **"Read: contracts.py"** (basename of the repo-relative path), its
  `title` attribute is the full path (hover affordance), and the row's text contains the repo
  (`agents-remember`);
- a multi-file `read.packet` summarizes as **"Read: one.py +2 more"** with every path present in the
  `title` (newline-joined);
- the river shows `Syncing event history.` until `eventsHydrated` is true, and a 66-event list is
  retained and virtualized beyond the old newest-60 cap — the test asserts the retained count in the
  header (`Event river · 66`) and that the newest row mounts, since off-screen rows are virtualized out
  of the DOM rather than dropped from the feed;
- `tool.completed` renders friendly tool copy, success state, token count, and protocol actor `model`
  as display actor `agent`;
- `lifecycle.phase-changed` renders the destination phase;
- `lifecycle.blocked` renders the structured ask prompt and ask kind;
- lifecycle-attached rows use existing task/enclosure labels rather than raw lifecycle ids;
- lifecycle-only history rows with no live lifecycle projection use the projected task document title
  instead of the cryptic lifecycle id;
- lifecycle-bound rows without live lifecycle, enclosure, or task-document context stay hidden until
  projected context arrives, preventing reload-order flicker from briefly painting raw ids;
- `lifecycle.heartbeat` is hidden from the default river while other rows still render;
- unknown lifecycle-less event kinds fall back to raw `event.kind`.

### Invariants And Boundaries

Pure render assertions over the real store, relying on the shared `test/setup.ts` jsdom stubs plus a
suite-local `beforeAll` that stubs element layout (`offsetHeight`/`offsetWidth`) so the virtualizer mounts
rows — virtualization means only the visible window is in the DOM, so off-screen rows are asserted via the
retained header count, not by querying every row. The `read.packet` cases preserve the privacy posture by
construction: only `path` (and its basename) reaches the DOM; no file content reaches the UI. The task-context case proves Event River presentation
uses the same projected lifecycle/enclosure/task-document facts as the rest of the dashboard rather
than parsing ids or filenames. Lifecycle-bound rows are intentionally gated until that projected context
exists; lifecycle-less workspace diagnostics still render their honest raw fallback.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The panel under test (now a virtualized list; the `read.packet` per-kind row on an otherwise-generic river). | — | [EventRiver.tsx](EventRiver.tsx) |
| The summary layer whose known-kind behavior, lifecycle-only task-document label fallback, and context-ready gate the render tests exercise. | L99-L110; L145-L158; L296-L357 | [eventSummary.ts](eventSummary.ts) |
| The render regression pins that a lifecycle-bound row stays hidden until task-document context is available. | L233-L258 | [EventRiver.test.tsx](EventRiver.test.tsx) |
| The hydration, virtualization, and jsdom-layout-stub regressions pin no premature empty state and that the full window is retained + virtualized (header count `Event river · 66`, newest row mounts). | L19-L34; L137-L145; L189-L211 | [EventRiver.test.tsx](EventRiver.test.tsx) |
| The `read.packet` emitter that carries `data.repoId` + facts-only `files`. | — | [observer/ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The `ObserverEvent` shape (trust/actor/kind/data) the helper builds. | — | [types/event.ts](../types/event.ts) |
| The task identity helpers used by the lifecycle-attached and lifecycle-only row tests. | L77-L108 | [data/taskIdentity.ts](../data/taskIdentity.ts) |

## Update History

- 2026-07-06T10:45+02:00 — L11 body note: enclosure fixtures carry the required existence flags (default true); river behavior unchanged. Verification metadata pinned until closeout stamps the L11 commit.

- 2026-07-06T03:10+02:00 — 260703-L11: the local `enclosure(...)` fixture now defaults the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags to `true`, matching the projection
  contract; no assertion change — the river does not filter rows on worktree existence. Verification
  metadata pinned until closeout stamps the L11 commit.
- 2026-06-28T13:54+02:00 — Task 34: the suite now renders a **virtualized** EventRiver — a `beforeAll`
  stubs `HTMLElement.prototype.offsetHeight`/`offsetWidth` so TanStack measures a non-zero viewport in
  jsdom (otherwise no rows mount). The old "renders events beyond the newest-60 window" test is now
  "retains and virtualizes the full window beyond the old newest-60 cap" and asserts the retained header
  count (`Event river · 66`) + the newest row, since off-screen rows are virtualized out of the DOM.
  Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: added/recorded Event River regressions for the raw
  stream hydration empty state and for rendering events beyond the old newest-60 frontend display window.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29: added reload-order coverage for context-ready
  Event River display shaping; lifecycle-bound rows now require lifecycle/enclosure/task-document
  context before rendering, while unrelated unknown workspace rows still fall back honestly. Verification
  metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-26T19:40+02:00 — Task 20 lifecycle label follow-up: added render
  coverage for retained event-history rows whose lifecycle id still exists on
  the event but whose live lifecycle projection is gone; the row must show the
  projected task document title and hide the raw lifecycle id. Verification
  metadata pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:14+02:00 — Task 20 readability pass: expanded Event River
  coverage from `read.packet` only to tool translation, phase changes, blocked
  ask prompts, task-context joins, actor display copy, heartbeat hiding, and
  unknown-kind fallback. Verification metadata pinned until closeout stamps the
  task-20 code commit.
- 2026-06-23T01:40+02:00 — Created for slice 07b v1: render test pinning the Event River's `read.packet`
  per-kind treatment ("Read: <basename>" + the read's repo + full-path-on-hover, "+N more" for a batch,
  generic fallback for other kinds). Verification metadata pinned until closeout stamps the slice-07b
  code commit.
