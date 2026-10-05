# dashboard/src/cockpit/Cockpit.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The component suite checks production shell navigation, persistent layers, projections and accessibility against repository fixtures.

The current Chats case pins Operations as initial, one Chats item, no Sessions route and a directly mounted persistent RoleChatsPane with no old-chat mode selector. Source cardinality comes from the sole JSX mount in Cockpit.tsx rather than a singular test query; accepted-session highlight routing retains its separate existing assertions.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The serving-build suite now distinguishes a stale executing bundle from a matching one. It pins
`data-client-build-current="false"` plus an explicit reload control for a mismatch, and `true` with
no reload control for an exact fingerprint match. The test never exercises an automatic reload
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

- "rails the Operations view but goes full-bleed for the Engine Room" — seeds `engine-fleet`, renders
  `<CockpitShell />`, asserts the default Operations view has `.shell__body[data-fullbleed="false"]`
  plus both `.rail--left`/`.rail--right`; clicks the `role="radio"` "Engine Room" mode-bar toggle and
  asserts `data-fullbleed="true"`, both rails gone, and the room's `engine-room-header` +
  `engine-room-diagnostics` zones present.
- "keeps the rails for Operations and Memory" — switching to Memory stays railed (`data-fullbleed="false"`).
- "directly shows one persistent Role chats pane without an old-chat selector" — finds the
  `[data-testid="role-chats-pane"]` node in its hidden persistent layer. Chats reveals the same
  node full-bleed, exposes no Chats-mode tablist and mounts no SessionsView child; returning to
  Operations hides the same pane. This is role-pane existence/persistence coverage, not a PTY-owner
  assertion; the sole current RoleChatsPane JSX mount establishes source cardinality.
- "toggles the right rail between the Event River and the leaf chat" (slice L5) — on a railed view the
  default `rail--right` shows the Event River; clicking the `rail-toggle-chat` `role="radio"` segment
  swaps in the single-instance `RailChat` (`rail-chat` testid), and clicking `rail-toggle-river` swaps
  the Event River back, pinning the `railView` switch without unmounting the railed body.
- "rail chat keys by the drilled leaf" (L5 fix 1) — a local `seedDrillableMaster` (+ a
  `taskDoc` factory) seeds a lifecycle-bound master with one authored, drillable leaf. The test selects
  the master, toggles the rail to chat, and asserts the master overview shows no leaf slot yet
  (`rail-chat-no-leaf`); drilling into the master's `subtask-open-1` then makes the `rail-chat-heading`
  contain the **leaf** id (`leaf-one`) and not the master id (`master-x`) — pinning that the rail keys off
  the displayed leaf (via `DetailPanel.onViewLeaf` → the shell's `viewedLeafKey`).
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

### 2026-07-24 Curator Delta

The shell suite now checks dirty/stale serving-stamp cues, mounted rail and Engine Room identity across
full-bleed switches, and the React.memo export contract for all persistent cockpit layers.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

The current source extents below record the reviewed UI contract. Inline test names/facets are source-bound evidence; the installed writer cannot create typed proves from those call titles, and these citations do not claim such a proof or a rerun.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `directly shows one persistent Role chats pane` | `dashboard/src/cockpit/Cockpit.test.tsx:768-798` |
| Current source owner or exact assertion described above. | `exports every persistent layer` | `dashboard/src/cockpit/Cockpit.test.tsx:830-860` |
| Directly places RoleChatsPane in the persistent ViewLayer and supplies taskDocuments and series with active visibility. | `MainLayers` | `dashboard/src/cockpit/Cockpit.tsx:757-819` |

- `CockpitShell` under test, and the `fullBleed` derivation the rails-hide cases exercise. [1]
- `GALLERY` fixtures + the `applySnapshot` hydration pattern. [2]
- The shared jsdom stubs the render relies on. [3]
- The L1 composition cases cover all four reader entry paths, unchanged-revision analytics churn, and late A-to-B response discard. [4]
- The current Chats case proves existence of a `role-chats-pane` node, no Sessions route or old-chat selector, and same-node hide/reveal persistence. [5]
- The production source census, separately from the singular test query, establishes the sole current `<RoleChatsPane>` JSX mount. [6]
- The `withStates` helper + the two `task-metrics` cases (`2 awaiting you`; nothing at zero). [7]
- `railProjection` / `WARN_ROW` and the three rail cases: differing dot markup, `getByRole("img", { name: "Severity: warn" })` + `getByRole("option", …)`, and the scoped `axe.run`. [8]
- The `role="img"` + `aria-label` wrapper (`severityMark`, `data-testid="attn-severity"`) the accessibility-tree assertion targets. [9]
- The `Task progress: …; phase: …` label on `data-testid="task-state"` that React Aria's `role="option"` absorbs. [10]
- The typed builder the local `taskDoc` factory now delegates to (and the header explaining why the `createdAt` it removed compiled before). [11]
- `metricsFor()` — the client mirror of `reducer.py::_metrics` these seeds now call instead of listing buckets. [12]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Historical FEUI-L8 Reviewed Candidate Delta

Pins the L8 product cutover: Operations is the initial route, the mode bar has one Chats item and no
Sessions item, and one persistent `SessionsView` layer survives route changes. Highlight delivery
switches/focuses only the accepted exact session.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which identifies the recorded historical FEUI-L8 review point.

## 260821-CLIVE Projection Fixture Alignment

No production behavior or assertion changed in this file. The local projected `SeriesNode` fixture
now supplies the required `discardedCount: 0` and `discardedSubTasks: []` cells so cockpit tests remain
type-aligned with the canonical projection contract. Discard rendering is owned by the task-reader and
lifecycle-list routes, not by this cockpit composition suite.
