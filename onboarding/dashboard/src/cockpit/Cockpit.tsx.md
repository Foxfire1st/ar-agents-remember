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

## 260921-ICR-L33 The Change-Set Takeover Re-Targets Itself

`ChangeSetTakeover` gained one prop and the shell supplies it: `onOpenChangeSet`, wired to the same
`actions.openChangeSet` the shell already owns. It is passed through to `ChangeSetViewer` as
`onOpenLeaf`, which composes a leaf target (`{ repo, master, leaf, mode }`) from a row of the master
net's `by leaf (N)` rail. **The point is reachability without a second screen:** a landed leaf is
offered from the master's own net listing, its committed change-set opens in the takeover the reader is
already in, and the back link still clears the takeover as before. Nothing else in the dispatch chain
changed — `target.review` still routes to `ReviewSurface` and the change-set viewer is still never
mounted for a review, so a leaf opened this way is an ordinary change-set target with `master` as its
qualifier.

## 260831-CCR-L23 Requirement-Artifact Takeover Kind

The L17 Notes takeover was widened into a generic task-artifact reader takeover:
the notes-only `NotesReaderTarget` shape became the discriminated
`TaskArtifactReaderTarget` (`dashboard/src/data/taskArtifacts.ts`) with a
`kind` member, and that shared target type is now imported from the data module
rather than from the notes reader. `NotesTakeover` spreads the whole target onto
`NotesReaderViewer` (`{...target}`) and keys the view marker on the kind:
`data-view` is `notes-reader` for a notes target and
`requirements-reader` for a requirements target. The shell, the shared takeover
flag, hidden-not-unmounted retention, and the `onOpenNotes` wiring are
unchanged.

## 260915-KS-L22 Intent-Review Takeover Kind

The change-set takeover now carries a second kind. `ChangeSetTarget` gained an optional
`review: { selectorKind, selectorId }` member, and `ChangeSetTakeover` reads it: `data-view` is
`intent-review` when the target carries a review and `changeset` when it does not, and the review
variant mounts `ReviewSurface` (`dashboard/src/panels/review/ReviewSurface`) in place of
`ChangeSetViewer`, passing `repo`, `master`, `leaf`, the two selector fields and `onBack`. The review
surface therefore sits beside `NotesTakeover` and the requirements variant of the task-artifact
reader as one more takeover the shell dispatches on the target's own shape, and nothing in the
shell's routing, rails or change-set plumbing changed with it: the target chooses the pane.

## Code Commentary

### Logic

- **Shared streams.** Cockpit wires connectState and one connectEvents raw-line consumer into the Event River/store, with a ready marker used for hydration. There is no seat-event reconciler, catalog poll driver or eager/cross-tab hosted-seat reconciler. Native Chats remains the retained host-chat surface. `CockpitShell` starts the screen wake lock once on mount through `useEffect(() => startScreenWakeLock(), [])`, using the returned stop function on unmount. The browser releases the lock while hidden, and `startScreenWakeLock` reacquires on visibility return; unsupported or denied requests do not add a banner.

### 260928-MIK-L114 Ready Last-Feed Handoff

Native tasks come from the shared `s.tasks` map and a memoized `Object.values` array. The stable empty-array fallback belongs to `analytics?.engineProcesses`, not to a second analytics task collection.

The event-stream ready handler receives the parsed `ready` marker and passes
`ready?.lastEventTs` into `markEventsHydrated`, so the store — and the panel head — name
the last feed even when the replay window holds nothing.

### Conventions

Panda `css`/`cva`/`cx`; `shell__body` carries `data-fullbleed` for the rails-hide assertions. The
marker classes (`cockpit--shell`, `rail`, `viewport`) are kept for tests. `useShouldAnimate` is the
shared honest-motion gate.

### Invariants And Boundaries

- The shell treats projected server evidence as read-only; selection and view state are local
  and lifted. A proven bundle mismatch is a tooltip cue, with no reload-client action in the
  shell. Any browser reload remains operator-owned outside that cue.
- The shell pins to `100vh` with `overflow:hidden`, so rails and viewport scroll internally and the
  bars stay fixed. Full-bleed hides the rails, never the alarm summary.
- The left rail is why `grammar/Dot.tsx` cannot lean on colour alone: the attention layer and the task
  tree carry different grammars in the same column and must stay distinguishable by glyph.
- A page outside the product bar is not built and fetches nothing at page load; its folder code and
  layout behavior stay tested through an injected initial view.
- `EffectsToggle` is the only UI writer of `html[data-effects]`.

### Todos

No additional work is asserted by this card.

### FEUI-L9R account — current source correction

`ServingBuildStamp` now compares the executing bundle fingerprint with
`servingBuild.dashboardBuild`. It exposes unknown, matching, or mismatching diagnostic evidence;
only a definite mismatch appends “reload to update” to the stamp’s tooltip. The current owner
renders a span, not the formerly described `reload client` button; reload remains an operator
browser action, not a shell control. An older server without the optional fingerprint remains
neutral rather than falsely stale.

### Logic

MainLayers keeps RoleChatsPane in its existing keep-alive ViewLayer, passing the single served TaskEntry array. active reflects Chats visibility and takeover coverage; hiding the view preserves pane identity. Native host-chat and rail discovery retain their own request and transport authorities.



The raw event stream calls the store Event River consumer and marks hydration on the ready event. It has no per-connection seatEvents backlog applier or onInterrupt callback; a reconnect does not restore those deleted consumers. Current ordering/hydration and the independent native host-chat mounting remain distinct source-owned behavior.

The body is the `bodyGrid` cva: the railed 3-column shell when `!fullBleed`, a single full-width column
when `fullBleed`. The two `<aside>` rails (`rail--left` = task list with its header attention bell/layer;
`rail--right` = event river) remain mounted and are hidden while full-bleed, retaining rail state;
their transitions use a `motion.aside` gated by `useShouldAnimate()` (instant under
`data-effects=off` / reduced-motion, keeping snapshots stable). `ViewBody` switches the centre by
`view`; the mode bar is the `<ModeBar>` primitive. `open(id)` selects a node AND jumps to Operations.

**Operations-integration L4** adds a `changeSet` TAKEOVER: `CockpitShell` holds a `changeSet:
ChangeSetTarget | null` state; when set, a full-bleed `<ChangeSetViewer>` shows (its back link clears it,
restoring the rails), and `open(id)` plus a mode-bar switch (`changeView`) also clear it — the takeover is
transient (a task-scoped screen), not a standing view. `onOpenChangeSet` passes from `RailedBody` through `MainLayers`
into its retained `DetailPanel`; `ViewBody` accepts only `view` and `onOpen`. **L4a** changes the takeover from *replacing* the railed body to **overlaying** it:
the railed body is now kept mounted but `display:none`/`aria-hidden` while the takeover shows (the same
hidden-not-unmounted pattern as the File Viewer + Chats layers), so the `DetailPanel`'s drill state (which
leaf you were reading) survives — the viewer's back link returns you to exactly where you opened it from
(a drilled leaf), instead of `DetailPanel` remounting fresh at the master overview.

`TopBar` shows the master-caution (`⚠ N waiting`, severity-keyed from `selectQueue`). **260718-CHATS-L5P
(RV-4/R4):** the waiting chip renders ONLY when `queue.length > 0` — a reassurance zero wearing an alarm
glyph is a lie, so an empty queue shows nothing (absence = clear); a real alarm is still never hidden in
a full-bleed view. **Top-bar humanization + honesty (V15/V6/R7):** `ServingBuildStamp`'s `up` label is a
HUMANIZED uptime (`humanizeDuration(Date.now() - bootedAt)`, one time format in the bar; the absolute
start stamp stays in the tooltip — was a second 12h clock, V15); the brand `title` + each fact-chip
(`dim`, `caution`, `connBadge`) are `whiteSpace:nowrap` and the `statusRow` is `flex-wrap:wrap` so the
bar wraps BETWEEN chips, never mid-phrase (`1 running · 0/blocked`, V6); and the task metrics use the server's taskCounts: planned, started, completed, aborted, works, paused and unknown, labeled by the shared status grammar. The unknown bucket is omitted when its count is zero; a nonempty bucket retains the shared started/host-state-unknown wording. The other buckets keep their served counts. The browser does not count raw lifecycle states. **5g G6** adds an `EffectsToggle` to the `TopBar`
(`effects-toggle`): a ✦ Effects / ❄ Calm button that flips `html[data-effects]` (which `useShouldAnimate`
reads live, so the engine-room backdrop + all gated motion respond at once) and persists the choice to the
`calm-cockpit` localStorage flag `main.tsx` reads on the next load.

The existing onOpenLifecycle callback name is retained as a navigation seam: it carries the opaque taskdoc-prefixed entry selection to open(id), which selects Operations and clears a takeover. It does not identify a session lifecycle.

**Historical FEUI-L1/FEUI-L8 seam.** FEUI-L1 briefly registered a separate "sessions" route
and mounted SessionsView there. FEUI-L8 retired that route and the legacy Chats component, then
used one SessionsView inside chatsLayer. That historical mount is now replaced by RoleChatsPane;
the existing display/aria-hidden keep-alive layer remains. The retained session-cockpit modules
and their WebTUI/keyboard markers still describe their own legacy consumers. ChatContextBar owns
those modules' launch/attach/move controls, not the current full-page Role chats launcher.

selectedId is the shared Operations selection. open(id) preserves the opaque entry selection exactly; taskdoc: carries a served entry key. Task state, activity, membership and workspace counts come from server entries and taskCounts, not raw-id normalization or lifecycle/series resolution.

**One comment, and it records a shape the dispatch already supported.** The `ChangeSetTakeover` component's review branch gained a comment stating that a review target may carry a subject's selector **or none at all** — the task-context entry opens the review on the task, and `ReviewSurface` asks the server for exactly what it was handed. The dispatch itself was not changed: it already forwarded an optional selector, which is why the task-context target reaches the surface without a code change here. Nothing else in the cockpit moved, and the two lines are the whole of this file's diff.

**The shell provides the entry's re-validation context (`260921-ICR-L47`, ruling 2026-09-28T16:27:28+02:00
on L47-R1-F2).** `CockpitShell` wraps its tree in
`<IntentEntryRevalidation shown={state.view === "operations" && !state.takeover}>`. The Operations
`DetailPanel` is never unmounted (only hidden during view switches and takeovers), so remounting could not
re-read the entry; instead the generation increments when `shown` turns true — a view switch back to
Operations or any takeover closing (the reviewer, a change set, notes) — and the entry's summary re-reads
once. This is 3 lines of wiring (1156 → 1159, already in the 900–1200 soft band; the diff is mostly
re-indentation); review R2 judged it wiring, not feature logic (O-R2-2).

### Conventions

Panda `css`/`cva`/`cx`. The marker classes (`cockpit--shell`/`shell__body`/`rail`/`viewport`) are kept
via `cx` for tests/structure; `shell__body` carries `data-fullbleed` for the rails-hide assertion. The dashboard no longer mounts a `crt-overlay` element; the scanline/vignette overlay and its sole flicker keyframe were removed, while the global effects cascade slot and determinism freeze remain. `useShouldAnimate` is imported from
`panels/engine-room/` (the shared honest-motion gate).

### Invariants And Boundaries

The shell treats projected server evidence as read-only; selection state is local + lifted. A proven
bundle mismatch contributes a tooltip cue, not a shell reload action; the operator may reload through
the browser. The shell pins to `100vh` + `overflow:hidden` so the
rails/viewport scroll internally and the bars stay fixed. The master-caution lives in the always-visible
top bar; full-bleed only hides the rails, never the alarm summary (§4.1). The `EffectsToggle` is the only
writer of `html[data-effects]` from the UI (vs the `?effects=off` URL param / `calm-cockpit` flag
`main.tsx` applies at boot); default is effects-on.
**The left column keeps attention severity and task status distinct.** The bell opens the queue layer over the task tree; the old sibling-panel account no longer holds. Severity glyphs and shared task marks have separate meanings; neither creates the other fact.
`selectedId` is an opaque entry selection, not a raw lifecycle id; consumers resolve it in the shared tasks map.
Missing serving-build evidence stays neutral; it is not evidence of staleness.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## 260921-ICR-L12 The Takeover Hands The Record To The Review Surface

`260921-ICR-L12` (`ICR-R12@v1`) adds one prop at the takeover: when the change-set target's review
carries `historical`, `ChangeSetTakeover` mounts `ReviewSurface` with `history="recorded"`, and
otherwise with `undefined` — the live candidate, which is what every ordinary entry asks for. The
target's own comment records why the record travels this way: a closed leaf's entry carries it, so the
surface asks for that leaf's recorded comparison rather than for a live candidate there is none of.

Nothing else in the takeover changed: the review target's subject still travels as it did, the
`onBack` contract is the same, and the cockpit adds no resolution of its own — the browser names a
record and the server owns which comparison that record is.

## Document Rail — native entry binding and keepalive

The right rail passes the viewed canonical `taskDocumentRef` and shared `TaskEntry[]` to `DocumentChat`, not a separate series or lifecycle collection. Its unkeyed wrapper stays mounted and hides behind `display:none` and `aria-hidden` when the River is shown; the River itself mounts conditionally. `active` requires both the chat toggle and a non-full-bleed shell. This shell-level keepalive preserves the chat component, not every native iframe generation: fallback, retry and host-return behavior belong to `DocumentChat` and its native host owner. The former `RailChat`, `viewedLeafKey` prop and leaf-chat context are historical, not current rail inputs.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. The design authority is the requirement packet `MIK-R79@v1` (rules 1, 13 and 16); it
lives outside the code and memory repositories, so it is named here and not cited as a row.

No relevant domain documentation was found for this file.

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

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


- The provider around the shell, shown only for Operations with no takeover. [64]


- The body grid bleed variant switches between three railed columns and a single full-width column. [65]


- Files, Engine Room, Topology, Knowledge, and Chats request the full-bleed layout. [66]


- Rail fade properties are selected by the animation permission. [67]


- The `chatsLayer` keep-alive class used by the Chats layer. [68]


- `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. [69]

- The boot-time effects flag it persists to. [70]
- The honest-motion gate the rail transition + the toggle drive. [71]

- Cockpit wires connectState and one connectEvents raw Event River consumer, plus the ready hydration marker; no seat-event reconciler. [72]


- A `#knowledge?…` reader URL selects the Knowledge view as the shell's initial view. [73]

- The reader's hash parser. [75]


- The frontend `Analytics` projection includes the `engineProcesses` process-map collection. [79]






- The reviewed UI contract owner `MainLayers`. [88]


- The reviewed UI contract owner `RoleChatsPane`. [89]


- The reviewed UI contract owner `ViewLayer`. [90]


- The sole Chats destination mounts RoleChatsPane directly, has no Chats-mode selector or SessionsView child, and keeps the pane identity while hiding/showing the existing layer. [91]

- Native task selection and memoization are separate from the Engine Room stable-empty fallback. [95]
- The right rail keeps the chat side mounted in an unkeyed stable wrapper and hides it when the River shows; the River still mounts conditionally. [92]
- The hidden chat side stays mounted but out of reach behind display:none and aria-hidden. [93]

- The header labels served taskCounts through the shared status table and hides only an empty unknown bucket. [94]

- The shell starts the screen wake lock once on mount; the wake-lock helper follows document visibility and releases its held sentinel on stop. [96]


### Cross-Repo References

No cross-repo boundary is crossed by this file.

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
