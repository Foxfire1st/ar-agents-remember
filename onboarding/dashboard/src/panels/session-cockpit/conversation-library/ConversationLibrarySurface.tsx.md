# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The in-stage prior-conversation browser (design §4.4). It is NOT a route, tab, or second Chats
destination — it opens in the stage *over* the live conversation (whose store keeps updating behind
it) and lays out a native list column beside a read-only preview column with the sole resume action.
It is the composition seam for `ConversationLibraryList`, `ConversationHistoryPreview`, and
`OpenConversationAction`, and it owns the surface-level focus, return, and height-containment
discipline that the review's F8/F16/F22/F23 findings and the height-containment register entry made load-bearing.

## Code Commentary

### Logic

- **Data reads**: pulls `list`/`preview`/`selectedKey` from `useConversationLibrary` (cit:([`useConversationLibrary`], dashboard/src/data/conversation-library/store.ts:86-88)); the
  loaders (`loadLibraryList`, `loadLibraryPreview`) are stable module functions from the library store.
- **Heading focus on open** (L95-L100, §14.1): the mount effect focuses the surface's own heading
  (`tabIndex={-1}`), NEVER a result row, then loads the list once for this harness/scope; async
  list/preview updates therefore never steal focus.
- **§4.4 return paths** (L104-L118, F16): `Escape` (when the target is not an input/textarea/
  contenteditable) calls `onBack`, which consumes the same focus-return token as the `← back to
  current chat` button (L131) and the palette `conversation.backToChat` command in `SessionsView`.
- **List mount + `agentsNote` pass-through**: the list receives rows/cursor/loading/
  error and `agentsNote={listView.agentsNote}` (cit:(["agentsNote={listView.agentsNote}"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:236-236)) — a pure pass-through; the list
  owns the verbatim render and the nested agent child rows.
- **Selection → preview only** (L145): selecting a row loads its preview; it never opens/activates.
- **`OpenConversationAction`** is mounted only for the selected row (cit:([`ConversationLibrarySurface`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:75-171)), so the sole resume
  affordance appears once a row is chosen.

### Invariants And Boundaries

- **Height containment is the whole point of the CSS here (F23).** The `columns`
  flex box is cit:([`nowrap`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:72-72): a *wrapping* flex container is multi-line, so each line's cross-size
  is sized to content — the columns would then grow to full content height inside this
  `overflow:hidden` clip and the interior `overflow-y:auto` scrollers would never engage, pushing
  `Open as new chat`/`Load more` past the fold and out of pointer reach. `nowrap` keeps one flex line
  whose cross-size is the definite container height, so each column (`minHeight:0`) hands its own
  overflow to its interior scroller. Stacking is owned entirely by the `@container` query, which only
  matches because this surface sets `containerType: "inline-size"` (L30-L32, F22). This is the reliable
  in-stage-overlay idiom the register records; do not reintroduce `flexWrap`. **V10 threshold raise:**
  the stack breakpoint moved `640px → 56rem` — the two columns (16rem list + 20rem
  preview + gaps) crush below ~56rem of surface (the list falls to a ~180px sliver and preview prose
  splits mid-word), so the surface now stacks to one column BEFORE that (the 900px window with the rail
  collapsed, and the ~1000px sweep, both read as a single flow).
- The live conversation surface stays mounted (its store keeps updating) but is rendered inert behind
  the library by `ChatsStageBody`; the diagnostics drawer is not rendered while the library is up, so
  the two surfaces can never overlay (F8 — enforced in `ChatsStageBody`, relied on here).
- This surface reads the library store and never writes a durable index; the list is server-native
  cursor-paged, never locally accumulated as a database.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The library store the surface reads and drives (list/preview/open loaders). [1]
- The native list column. [2]
- The read-only preview column in the same block grammar. [3]
- The sole resume action mounted for the selected row. [4]
- The harness label used for the heading. [5]
- The stage body that renders this surface, keeps the live surface inert behind it, and suppresses the drawer while it is up. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
