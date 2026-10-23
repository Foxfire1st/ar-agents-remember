# dashboard/src/cockpit/Cockpit.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.test.tsx` proves the production shell's standing contracts on attention rows that now declare their `itemClass` and `dismissible` like any other served row: the Operations detail hydration
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

The scanline-removal case mounts `CockpitShell` and asserts that `.crt-overlay` is absent.
It reads the actual `index.css` and requires no overlay selector, flicker keyframe or repeating
line gradient, while retaining the alarm `pulse` and `html[data-effects="off"]` rules. This is
source/render regression coverage, not a browser contrast measurement or a fresh execution here.

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

Native direct/master/child/worktree-bound entries hydrate once per unchanged body revision through task deltas. Late task-A answers cannot contaminate task B. Fetch stubs model mounted composition, not production fallback or a real server.

A local `seed(stateName)` applies a `GALLERY` fixture projection to the real Zustand store
(`dashboardStore.getState().applySnapshot(...)`) — the same hydration the dev bench uses. The removed Terminal mock and sessions-store cleanup are not current fixture seams. `afterEach` runs RTL `cleanup`, restores stubbed globals, and resets the dashboard store.

- "keeps the rails for Operations and Memory" — switching to Memory stays railed (`data-fullbleed="false"`).
- "directly shows one persistent Role chats pane without an old-chat selector" — finds the
  `[data-testid="role-chats-pane"]` node in its hidden persistent layer. Chats reveals the same
  node full-bleed, exposes no Chats-mode tablist and mounts no SessionsView child; returning to
  Operations hides the same pane. This is role-pane existence/persistence coverage, not a PTY-owner
  assertion; the sole current RoleChatsPane JSX mount establishes source cardinality.
- Header rollup reads published taskCounts. The initial-nonzero case asserts the stage counts, exactly one `host activity unavailable` notice, and no works/paused wording in the header. The separate 0→1→0 case asserts initial works/paused figures and no notice; at one it asserts a notice and no works wording; on return to zero it asserts only notice removal. It does not assert post-return figure restoration, paused suppression or exact notice count in the one phase, per-row suppression, or native host availability.
- Rail cases distinguish task activity from attention severity, preserve accessible names and scope axe checks under existing jsdom exclusions.
- Gallery severity counts and server order remain; qualified native task selection no longer comes from an attention-origin lifecycle opener. The sidebar selection case clicks first, second, then first native task, waits for each task id in the reader, and asserts its option is focused with `aria-selected="true"`; the `scrollIntoView` spy is called three times. This preserves the reveal/focus/selection contract under native sidebar selection rather than the retired attention-layer opener. Render assertions are not browser/backend persistence proof.

Typed taskEntry/taskSummary/projection/taskTree replace local taskDoc, parallel SeriesNode and metricsFor lifecycle rollups: identity/status stay on the entry, reader prose in summary.

The listed `totalTokens`/`stalenessHistogram` cells describe the superseded literals, not the current metrics contract. Current `Metrics` carries only `ignoredHostAgents`, and task counts live in `taskCounts` (planned, started, aborted, completed, works, paused, unknown); neither `lifecycleCount` nor `metricsFor` exists.

### Invariants And Boundaries

Shared jsdom stubs and CSS.escape support radio-name/test-id queries. Body cases stub fetch and publish task deltas for refresh/selection timing; no browser or host execution is implied.

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



- Direct/master/child/worktree-bound body hydration stays revision-owned through task deltas and late A-to-B responses. [31]





- `CockpitShell` under test, and the `fullBleed` derivation the rails-hide cases exercise. [28]



- `GALLERY` fixtures + the `applySnapshot` hydration pattern. [29]


- The shared jsdom stubs the render relies on. [30]


- The current Chats case proves existence of a `role-chats-pane` node, no Sessions route or old-chat selector, and same-node hide/reveal persistence. [32]



- The production source census establishes the sole current `<RoleChatsPane>` JSX mount. [33]


- Header totals use published taskCounts, retaining the zero paused bucket but showing unknown only while populated. [34]


- Rail cases distinguish task activity from severity and retain accessible names plus scoped axe checks. [35]



- The `role="img"` + `aria-label` wrapper (`severityMark`, `data-testid="attn-severity"`) the accessibility-tree assertion targets. [36]


- The task-state mark labels itself Task progress: <statusLabel(taskStatusKey(entry))> with no phase suffix. Presentation takes the served activity when present, otherwise the served stage. The Cockpit accessibility case asserts a React Aria option named Task progress: paused before opening the attention layer, preserving the row-name absorption behavior rather than a lifecycle-phase label. [37]

- Typed entry/summary/projection builders keep the composition fixtures checked against the served contract; the former taskDoc/metricsFor anchors are retired.

- Sidebar selection reveals each native task, focuses and marks its option aria-selected=true, and invokes scrollIntoView three times for first/second/first selections. [43]





- The toggle cases assert the same document-chat node across the River/Chat switch. [40]





- Both rail asides stay mounted under full-bleed views. [41]





- The mounted shell and actual stylesheet omit the scanline layer while retaining pulse and the effects-off freeze. [42]


- The initial-nonzero case asserts one notice and no works/paused wording; the separate transition case asserts initial figures, notice/no works at one, and only notice removal on return to zero. No restored figures or native host availability are asserted. [44]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

Historical CLIVE SeriesNode discard-field alignment is no longer current fixture setup. Native entries retain the composition boundaries above.
