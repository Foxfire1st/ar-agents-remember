# dashboard/src/cockpit/Cockpit.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.test.tsx` proves the production shell's standing contracts: the Operations detail hydration
and rollup, the serving-build stamp, the full-bleed/railed layout flip, rail keep-alive across view
switches, the right-rail River/Chat toggle and its persistence, and the resizable rails.

## Code Commentary

### Logic

- The suite mounts `CockpitShell`. MIK-R79 moved the opening view from Operations to Chats, so cases
  that need the railed Operations context now mount `CockpitShell initialView="operations"`.
- The full-bleed case now switches to **File Viewer** and asserts the File Viewer pane is present;
  the Engine Room's removed dashboard entry is covered instead by the initial-view matrix, which
  mounts `memory`, `hangar`, `engine` and `topology` through `initialView` and asserts each page
  renders with its expected `data-fullbleed` and rail visibility.
- Keep-alive, rail-toggle, persistence and rail-width assertions are otherwise unchanged.
- Since MIK-R122 the toggle cases assert the same document-chat node across the River/Chat
  switch (hidden, never unmounted) and both rail asides stay mounted under full-bleed views.

### Conventions

Vitest + Testing Library; views are selected by their radio name; fixtures come from the gallery.

### Invariants And Boundaries

The suite binds the shell's default view, the layout bleed set, the hidden-not-unmounted layer
behavior and the retained pages' layout through injected views. It does not re-test the Knowledge
reader's own behavior.

### Todos

No additional work is asserted by this card.

### FEUI-L9R Reviewed Candidate Delta

The serving-build suite now distinguishes a stale executing bundle from a matching one. It pins
`data-client-build-current="false"` plus a tooltip reload cue for a mismatch (no explicit
reload-dashboard-client control exists), and `true` with no redundant reload button
for an exact fingerprint match. The test never exercises an automatic reload
because the product contract requires operator timing.

### Logic

The current canonical Chats test asserts one directly mounted Role chats pane, Operations initial state and no separate Sessions route. Chats has neither the old mode selector nor a SessionsView child. Hide/show uses the same pane; the export-shape check retains the other memoized layers without claiming SessionsView as a current Chats mount.

L15 adds the servingBuild stamp assertions (renders commit + boot time when present; absent-field tolerance for old payloads).

260712-TRH-L1 adds a shape-accurate Operations projection and fetch stub for the permanently mounted
cockpit surfaces. It clicks a direct leaf, master, drilled subtask, and lifecycle-bound row while
changing only summary projection objects; each path proves one body request for the unchanged revision
and renders the complete objective after resolution. A second case holds task A, switches to task B,
resolves A late, and proves A cannot contaminate B; B remains one request and hydrates only after its
own response. The fetch fixture returns the response shapes required by the mounted file, harness,
terminal, change-set, and notes surfaces, modeling composition rather than adding production fallback
behavior.

A local `seed(stateName)` applies a `GALLERY` fixture projection to the real Zustand store
(`dashboardStore.getState().applySnapshot(...)`) — the same hydration the dev bench uses. The lazy
`../panels/Terminal` is mocked to a jsdom-safe stub so toggling the rail to chat never pulls xterm (a
canvas probe) into jsdom. `afterEach` runs RTL `cleanup`, resets the `sessions` store, and resets the
dashboard store.

- "keeps the rails for Operations and Memory" — switching to Memory stays railed (`data-fullbleed="false"`).
- "directly shows one persistent Role chats pane without an old-chat selector" — finds the
  `[data-testid="role-chats-pane"]` node in its hidden persistent layer. Chats reveals the same
  node full-bleed, exposes no Chats-mode tablist and mounts no SessionsView child; returning to
  Operations hides the same pane. This is role-pane existence/persistence coverage, not a PTY-owner
  assertion; the sole current RoleChatsPane JSX mount establishes source cardinality.
- "workspace rollup — the handoff reaches the header" (**260731-EFA-L4**) — a `withStates(...states)`
  helper clones the `calm` GALLERY lifecycle once per requested state and derives the rollup with
  `metricsFor(lifecycles)` rather than hand-listing buckets beside it. Two cases pin the new top-bar
  segment from both sides: three lifecycles (two `awaiting-developer`, one `running`) put
  `2 awaiting you` inside `[data-testid="task-metrics"]`; a `running` + `blocked` pair makes the same
  node contain no `"awaiting"` at all while still reading `1 running` and `1 blocked` — the segment is
  appended, it displaces nothing, and it never renders a reassurance zero.
- "the left rail shows lifecycle states and attention severities at the same time" (**260731-EFA-L4**) —
  three cases, and they render the **whole `CockpitShell`** rather than the two panels, because the
  panels being siblings in one always-visible rail is exactly the claim under test (the justification
  `grammar/Dot.tsx` previously used for `warn` and `awaiting-developer` sharing amber was true per LIST
  and false per VIEW). A local `railProjection(attentionQueue)` seeds one `awaiting-developer` lifecycle
  plus its `liveEnclosure` (the rail renders a leaf only while a worktree exists) and a `warn`
  `actionable-drift` row. (1) `[data-testid="task-state"]` and `[data-testid="attn-severity"]` both
  resolve a first child, and their `outerHTML` differ — both are amber, so telling them apart is the
  glyph's job. (2) The severity is queried BY ROLE AND NAME — `getByRole("img", { name: "Severity: warn" })`
  must be the `attn-severity` node — because the wrapper used to be a bare `<span aria-label>`, and ARIA
  prohibits naming a `generic`: a `getAttribute("aria-label")` assertion would have passed while the
  computed tree carried nothing. The state dot's label reaches the tree by a different route and is
  asserted as such: React Aria gives the row `role="option"`, whose name-from-content absorbs the span,
  so it is matched by `getByRole("option", { name: /Task progress: awaiting-developer; phase: build/ })`.
  (3) An `axe.run` over a standalone `<AttentionQueue>` render must report zero violations, with
  `color-contrast` and `region` disabled because jsdom has no layout engine; `aria-prohibited-attr` is
  `serious` and is what would fail. Scoped to the panel, not the shell, because axe walks every node it
  is given. (`axe-core` was already a `dashboard` devDependency; this is its first use in this suite.)

**Fixtures are now built through the typed wire builders (260731-EFA-L4).** The local `taskDoc(over)`
factory no longer returns an `as TaskDocNode` object literal — it delegates to
`taskDoc as wireTaskDoc` from `test/fixtures/wire.ts`, so an excess property fails `tsc -b` at the call
site instead of being erased by the assertion. That immediately paid: the master's `subTasks[0]` row in
`seedDrillableMaster` carried `createdAt: "2026-06-20T09:00:00+00:00"`, a field
`TaskSubTaskRefNode` does not declare on either side (`projection.py::TaskSubTaskRefNode` is
`extra="forbid"`), so the server could never have sent it — and it is gone. (`TaskDocNode.createdAt`
itself IS declared and is still set on the doc bases.) Both hand-written `metrics: { lifecycleCount, runningCount, blockedCount, pausedCount,
totalTokens, stalenessHistogram }` literals — in `seedDrillableMaster` and `taskReaderProjection` — are
replaced by `metricsFor([...lifecycles])`, the client mirror of `reducer.py::_metrics` (the two new
projections use it from birth). The hand-kept bucket lists were the reason a new state could be counted
nowhere. Note what this DID change for the older cases: those seeds now receive complete rollups derived
from their own lifecycles rather than the numbers the author typed.

### Invariants And Boundaries

Relies on the shared jsdom stubs in `test/setup.ts` (`matchMedia` for `useShouldAnimate`, `ResizeObserver`
 for React Aria). The ModeBar items are queried by `role="radio"` (React Aria `ToggleButtonGroup`,
single-select), driven by `fireEvent.click`. Uses plain `container.querySelector` + vitest `expect`
(no `@testing-library/jest-dom`). Older cases are pure render assertions; the new body cases stub
browser `fetch` and drive `dashboardStore.applyDelta("analytics", ...)` to reproduce analytics churn
and selection timing.

### Conventions

Shell tests drive the shared gallery fixtures and query stable test ids rather than private styles.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rules 1 and 16) fixes the opening view, the product bar and the retained pages; it
lives outside the code and memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The suite mounts the shell and switches views through the mode bar. [13]
- The layout matrix sources the retained pages only through their injected views. [14]
- The view list the bar renders. [15]
- The L1 composition cases cover all four reader entry paths, unchanged-revision analytics churn, and late A-to-B response discard. [31]

- `CockpitShell` under test, and the `fullBleed` derivation the rails-hide cases exercise. [28]
- `GALLERY` fixtures + the `applySnapshot` hydration pattern. [29]
- The shared jsdom stubs the render relies on. [30]
- The current Chats case proves existence of a `role-chats-pane` node, no Sessions route or old-chat selector, and same-node hide/reveal persistence. [32]
- The production source census establishes the sole current `<RoleChatsPane>` JSX mount. [33]
- The `withStates` helper + the two `task-metrics` cases (`2 awaiting you`; nothing at zero). [34]
- `railProjection` / `WARN_ROW` and the three rail cases: differing dot markup, `getByRole("img", { name: "Severity: warn" })` + `getByRole("option", …)`, and the scoped `axe.run`. [35]
- The `role="img"` + `aria-label` wrapper (`severityMark`, `data-testid="attn-severity"`) the accessibility-tree assertion targets. [36]
- The `Task progress: …; phase: …` label on `data-testid="task-state"` that React Aria's `role="option"` absorbs. [37]
- The typed builder the local `taskDoc` factory now delegates to (and the header explaining why the `createdAt` it removed compiled before). [38]
- `metricsFor()` — the client mirror of `reducer.py::_metrics` these seeds now call instead of listing buckets. [39]

- The toggle cases assert the same document-chat node across the River/Chat switch. [40]
- Both rail asides stay mounted under full-bleed views. [41]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

No production behavior or assertion changed in this file. The local projected `SeriesNode` fixture
now supplies the required `discardedCount: 0` and `discardedSubTasks: []` cells so cockpit tests remain
type-aligned with the canonical projection contract. Discard rendering is owned by the task-reader and
lifecycle-list routes, not by this cockpit composition suite.
