# dashboard/src/panels/EventRiver.test.tsx

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

A small `ev(...)` helper builds an `ar-observer-event/v1` event. It no longer assembles the envelope
itself: it delegates to `observerEvent(...)` from `test/fixtures/wire`, passing a suite-local `id`
(`e-<kind>-<random>`), the frozen `ts` `2026-06-23T10:11:12+00:00`, and `actor: "model"` ahead of the
caller's `...partial`, while `schema` and `trust: "observed"` come from the shared builder. The
`as ObserverEvent` cast at the end is gone, and the parameter type is now
`Partial<ObserverEvent> & Pick<ObserverEvent, "kind">` — so the helper is checked against the mirror
instead of asserting past it, and an event-envelope contract change fails this file. Spread order is
unchanged, so an explicit `partial.id` still wins.
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

## Evidence

### Repo-Internal References

- The panel under test (now a virtualized list; the `read.packet` per-kind row on an otherwise-generic river). [1]
- The summary layer whose known-kind behavior, lifecycle-only task-document label fallback, and context-ready gate the render tests exercise. [2]
- The render regression pins that a lifecycle-bound row stays hidden until task-document context is available. [3]
- The hydration, virtualization, and jsdom-layout-stub regressions pin no premature empty state and that the full window is retained + virtualized (header count `Event river · 66`, newest row mounts). [4]
- `ev` delegates to the shared `observerEvent` builder and drops the `as ObserverEvent` cast. [5]
- `observerEvent` — the shared envelope builder supplying `schema`/`trust`, typed against the mirror. [6]
- The `read.packet` emitter that carries `data.repoId` + facts-only `files`. [7]
- The `ObserverEvent` shape (trust/actor/kind/data) the helper builds. [8]
- `qualifiedLeafKey`/`leafTitleForKey` — the task identity helpers used by the lifecycle-attached and lifecycle-only row tests. [9]
