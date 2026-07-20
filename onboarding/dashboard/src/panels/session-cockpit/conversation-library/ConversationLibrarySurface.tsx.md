# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The in-stage prior-conversation browser (design §4.4). It is NOT a route, tab, or second Chats
destination — it opens in the stage *over* the live conversation (whose store keeps updating behind
it) and lays out a native list column beside a read-only preview column with the sole resume action.
It is the composition seam for `ConversationLibraryList`, `ConversationHistoryPreview`, and
`OpenConversationAction`, and it owns the surface-level focus, return, and height-containment
discipline that the review's F8/F16/F22/F23 findings and register entry L4.R5 made load-bearing.

## Code Commentary

### Logic

- **Data reads** (L87-L89): pulls `list`/`preview`/`selectedKey` from `useConversationLibrary`; the
  loaders (`loadLibraryList`, `loadLibraryPreview`) are stable module functions from the library store.
- **Heading focus on open** (L92-L97, §14.1): the mount effect focuses the surface's own heading
  (`tabIndex={-1}`), NEVER a result row, then loads the list once for this harness/scope; async
  list/preview updates therefore never steal focus.
- **§4.4 return paths** (L101-L115, F16): `Escape` (when the target is not an input/textarea/
  contenteditable) calls `onBack`, which consumes the same focus-return token as the `← back to
  current chat` button (L128) and the palette `conversation.backToChat` command in `SessionsView`.
- **Selection → preview only** (L141): selecting a row loads its preview; it never opens/activates.
- **`OpenConversationAction`** is mounted only for the selected row (L153-L162), so the sole resume
  affordance appears once a row is chosen.

### Invariants And Boundaries

- **Height containment is the whole point of the CSS here (F23 / register L4.R5).** The `columns`
  flex box is `nowrap` (L61-L67): a *wrapping* flex container is multi-line, so each line's cross-size
  is sized to content — the columns would then grow to full content height inside this
  `overflow:hidden` clip and the interior `overflow-y:auto` scrollers would never engage, pushing
  `Open as new chat`/`Load more` past the fold and out of pointer reach. `nowrap` keeps one flex line
  whose cross-size is the definite container height, so each column (`minHeight:0`) hands its own
  overflow to its interior scroller. Stacking at the ~80-col floor is owned entirely by the
  `@container (max-width: 640px)` query, which only matches because this surface sets
  `containerType: "inline-size"` (L30-L32, F22). This is the reliable in-stage-overlay idiom the
  register records; do not reintroduce `flexWrap`.
- The live conversation surface stays mounted (its store keeps updating) but is rendered inert behind
  the library by `ChatsStageBody`; the diagnostics drawer is not rendered while the library is up, so
  the two surfaces can never overlay (F8 — enforced in `ChatsStageBody`, relied on here).
- This surface reads the library store and never writes a durable index; the list is server-native
  cursor-paged, never locally accumulated as a database.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The library store the surface reads and drives (list/preview/open loaders). | L12-L17 | [../../../data/conversation-library/store.ts](../../../data/conversation-library/store.ts) |
| The native list column. | L133-L146 | [ConversationLibraryList.tsx](ConversationLibraryList.tsx) |
| The read-only preview column in the same block grammar. | L147-L152 | [ConversationHistoryPreview.tsx](ConversationHistoryPreview.tsx) |
| The sole resume action mounted for the selected row. | L153-L162 | [OpenConversationAction.tsx](OpenConversationAction.tsx) |
| The harness label used for the heading. | L10 | [../../../data/conversation/format.ts](../../../data/conversation/format.ts) |
| The stage body that renders this surface, keeps the live surface inert behind it, and suppresses the drawer while it is up. | — | [../ChatsStageBody.tsx](../ChatsStageBody.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the in-stage
  prior-conversation browser surface — heading-focus-on-open, the three §4.4 return paths on one
  focus-return token, and the F23/L4.R5 `nowrap` + `min-height:0` + interior-scroll + `@container`
  height-containment idiom that keeps the resume action and pager pointer-reachable. Verification is
  pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
