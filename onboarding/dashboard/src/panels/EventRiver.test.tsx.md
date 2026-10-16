# dashboard/src/panels/EventRiver.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Virtualized EventRiver assertions retain read.packet privacy, tool/host outcomes, raw hydration, full-window retention and newest-valid-time heading. Lifecycle joins/context-ready/phase/blocked/heartbeat cases are removed.

## Code Commentary

### Logic

The suite uses raw observer-event fixtures and store event/time state. No lifecycle, enclosure or task-document label join is seeded by these current cases.

### 260928-MIK-L114 Host-Path And Last-Fed Cases

The suite now mounts the host-path rows (caller, refused-with-code, reached state, target
role, chat rows, silent-river line) and the newest-timestamp head: late older arrivals
never move it back, and an empty window falls back to the store time.

ev uses typed observerEvent with default id/time/model actor and caller overrides. Restored nonzero layout getters let TanStack mount virtual rows in jsdom. Store setup is raw events/hydration/time, not lifecycle-context fixtures.

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






- Unknown raw event kinds remain an honest verbatim fallback.

### Invariants And Boundaries

Stubbed layout permits render assertions, not browser geometry/live delivery. Full-window header counts and visible virtual rows differ. read.packet exposes paths only; removed lifecycle-context gates/heartbeat filters are not current coverage.

## Evidence

### Repo-Internal References

- The panel under test (now a virtualized list; the `read.packet` per-kind row on an otherwise-generic river). [1]



- The hydration, virtualization, and jsdom-layout-stub regressions pin no premature empty state and that the full window is retained + virtualized (header count `Event river · 66`, newest row mounts). [4]

- `ev` delegates to the shared `observerEvent` builder and drops the `as ObserverEvent` cast. [5]
- `observerEvent` — the shared envelope builder supplying `schema`/`trust`, typed against the mirror. [6]


- read.packet rows are synthetic compatibility fixtures in these declared rendering cases, not evidence that the removed ambient emitter still exists. Source inspection, not execution. [7]

- The `ObserverEvent` shape (trust/actor/kind/data) the helper builds. [8]
