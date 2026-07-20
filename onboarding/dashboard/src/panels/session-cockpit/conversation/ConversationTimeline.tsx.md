# dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The one navigable `role="feed"` (design §14.2/§14.3): a `@tanstack/react-virtual` timeline virtualized
by stable conversation ITEM (never by rendered line), so DOM pruning is independent of the
store/history authority. Each row is an `<article>` carrying `aria-posinset` from the server
`globalOrdinal` and `aria-setsize` only when the total is honestly known. It owns the accessible feed
mechanics — roving tabindex + focus pinning, bottom-follow, older paging, widget-scoped keyboard
navigation, and unknown-vendor run collapse — and no data/cursor logic.

## Code Commentary

### Logic

- **ARIA honesty** (L337-L355, R5): `aria-posinset` is the item's server `globalOrdinal` (or the run's
  first ordinal), NOT the array index; `aria-setsize` is emitted ONLY when `totalItems` is a known
  number (`knownTotal`), else omitted and the older-paging button reads `Load older (total unknown)`
  (L321). Every article is `aria-live="off"` (the surface owns announcements).
- **Focus pinning** (L184-L194, F18): `rangeExtractor` pins the focused row AND unconditionally the
  last row (`rows.length - 1`), so a tabbable article always stays mounted even when both scroll out of
  the virtual window — incoming data can never relocate focus to the container. `tabbable` (L342-L343)
  gives the focused row, or the last row when nothing is focused, `tabIndex=0`.
- **Bottom-follow** (L205-L232): `handleScroll` tracks `nearBottom` (within `BOTTOM_FOLLOW_PX=120`); a
  new last row while near-bottom scrolls to end, otherwise increments `pendingUpdates` and shows the
  NON-animated `N new updates` button (L369-L382). Older prepend restores the captured top stable row +
  pixel offset (L234-L242, anchor-preserving paging).
- **Widget-scoped keyboard nav** (L259-L289, §14.4/F14 accepted deviation): `onKeyDown` on the `feed`
  element (the ARIA feed pattern), NOT a global document handler. `]`/`[` move next/prev; `Home`/`End`
  jump ends. The exclusion list is complete — `isEditableTarget` (L97-L105) skips
  `INPUT/TEXTAREA/SELECT/contentEditable` and any `closest('button,a,[contenteditable],.cm-editor')`;
  `inOverflowRegion` (L107-L110) plus an active text selection make Home/End YIELD to labeled overflow
  regions (`[role="group"], pre`) and to selections instead of hijacking them.
- **Unknown-vendor run collapse** (L112-L148, L177): `groupUnknownVendorRuns` folds a run of ≥3
  identical-summary unknown-vendor items into one de-emphasized expandable `unknown-run` row; members
  stay addressable (`#ordinal · evidenceRef`), identity is never mutated.

### Invariants And Boundaries

- Virtualization keys on the stable item, never rendered lines; the store/history authority is
  independent of what is mounted.
- `aria-posinset` is the server ordinal; `aria-setsize` is present ONLY when the total is honestly
  known — never a fabricated total.
- A tabbable article is always mounted (focused or default-last), so keyboard users never skip the feed.
- Keyboard navigation is widget-scoped; printable `[`/`]` cannot live in the document registry without
  fighting the printable-suppression contract, and Home/End defer to labeled overflow regions/selections.

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
| Feed ARIA, focus pinning, bottom-follow, older paging, widget keyboard nav, run collapse. | L160-L385 | [ConversationTimeline.tsx](ConversationTimeline.tsx) |
| The pure unknown-vendor run grouping this feed renders. | — | [collapse.ts](collapse.ts) |
| The kind dispatcher + stable accessible-name helper per article. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |
| The item wire type (`globalOrdinal`/`kind`/`phase`) the feed reads. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface that mounts this feed and owns announcements + paging callbacks. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The feed ARIA + default-closed diagnostics render suite. | — | [renderer.test.tsx](renderer.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the one `role="feed"`
  timeline — item-virtualized with server-ordinal `aria-posinset`, honest `aria-setsize`/`total
  unknown`, focus pinning of both the focused and default-last rows (F18), non-animated bottom-follow,
  anchor-preserving older paging, the widget-scoped keyboard nav with the completed exclusion list
  (F14), and unknown-vendor run collapse (F10). Verification is pinned to the leaf base (`0be0099`)
  because the new source file is uncommitted; closeout owns its first source stamp.
