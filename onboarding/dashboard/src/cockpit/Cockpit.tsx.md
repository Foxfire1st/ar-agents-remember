# dashboard/src/cockpit/Cockpit.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The production shell owns dashboard chrome, the product view bar, takeover selection and the shared
projection consumers. Since MIK-R79 the product bar is exactly Chats, Operations, Knowledge and File
Viewer; the dashboard opens on Chats; and the four pages that left the bar (Engine Room, Memory,
Topology, Hangar) have no dashboard entry and are not built or fetching at page load. Knowledge and
File Viewer are full-width retained layers on the File Viewer shell, so a document and its reading
position survive a tab switch.

## Code Commentary

### Logic

- **The product bar.** `VIEWS` is the single ordered list (`chats`, `operations`, `knowledge`,
  `files`); `ModeBar` renders it. `CockpitShell` defaults `initialView` to `"chats"`. The retained
  pages are reachable only through an injected `initialView`, which the development scenarios and the
  layout tests use; `MainLayers` renders Memory/Topology/Hangar transiently and Engine Room only when
  that view is explicitly selected, so a normal load mounts neither.
- **Full-width layers.** `useCockpitShellState` derives `fullBleed` for `files`, `knowledge`,
  `engine`, `topology` and `chats`. `MainLayers` keeps the Knowledge reader mounted in a `filesLayer`
  `ViewLayer` that is hidden, never unmounted, so leaving and returning to Knowledge shows the same
  document at the same place; the File Viewer, Chats and the Operations detail panel use the same
  hidden-not-unmounted pattern.
- **Rails and takeovers.** The left attention queue/lifecycle list and the right event river stay
  mounted and are hidden while full-bleed. Takeovers (change set, intent review, notes/requirements,
  a review target) render over the hidden railed body, and closing one returns to where it was
  opened. `IntentEntryRevalidation` wraps the tree and re-reads the Operations entry once per showing
  (`view === "operations" && !takeover`).
- **Shared consumers.** `Cockpit` wires `connectState` and one `connectEvents` connection with two
  consumers (the Event River and the gated seat-event reconciler). `CockpitShell` owns the refcounted
  catalog poll driver, the eager/cross-tab reconciler and the screen wake lock. The
  top bar carries the master caution, the serving-build stamp (with a proven client/serving mismatch
  offered as an operator reload) and the agent-notifier heartbeat badge (absent tick renders
  nothing).
- **Selection and chat.** `selectedId` is a typed selection key normalized through
  `lifecycleSelectionKey`; `selectedLifecycleId` derives the lifecycle context. The right rail's
  River/Chat toggle keeps the Event River on one side and mounts `DocumentChat` on the canonical
  viewed task on the other (MIK-R95); the removed `RailChat` and its `viewedLeafKey` plumbing are
  gone. The highlight composer is mounted once and filters targets by the current selection; its
  former direct leaf-chat target was removed with the old panel.

### Conventions

Panda `css`/`cva`/`cx`; `shell__body` carries `data-fullbleed` for the rails-hide assertions. The
marker classes (`cockpit--shell`, `rail`, `viewport`) are kept for tests. `useShouldAnimate` is the
shared honest-motion gate.

### Invariants And Boundaries

- Server authority is read-only; selection and view state are local and lifted. The one browser
  mutation is the operator's explicit reload on a proven bundle mismatch.
- The shell pins to `100vh` with `overflow:hidden`, so rails and viewport scroll internally and the
  bars stay fixed. Full-bleed hides the rails, never the alarm summary.
- The left rail is why `grammar/Dot.tsx` cannot lean on colour alone: the attention queue and the
  lifecycle list are siblings with different grammars and must stay distinguishable by glyph.
- A page outside the product bar is not built and fetches nothing at page load; its folder code and
  layout behavior stay tested through an injected initial view.
- `EffectsToggle` is the only UI writer of `html[data-effects]`.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. The design authority is the requirement packet `MIK-R79@v1` (rules 1, 13 and 16); it
lives outside the code and memory repositories, so it is named here and not cited as a row.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The product bar and its order are one list. [32]

- The shell opens on Chats and renders the retained layers. [33]

- Knowledge is a full-bleed, hidden-not-unmounted layer. [34]

- Full-bleed is derived for the product and retained machine-map views. [35]

- A page outside the bar mounts only through an injected view. [36]

- The layer wrapper that hides without unmounting. [37]
- The mode-bar primitive that renders the product entries. [38]
- The Knowledge reader the retained layer mounts. [39]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

## MIK-R95 Document Rail

The Chat side of the right rail now mounts `DocumentChat` on the canonical viewed task plus the shared task series; the `RailChat` module, its `viewedLeafKey` plumbing and the leaf-chat context it consumed were removed (rule 8). `RightRail` receives `series` and `active={!fullBleed}` instead of engine/context values, so the retained rail keeps one frame while a full-bleed page hides it. The highlight composer no longer receives a direct leaf-chat target.
