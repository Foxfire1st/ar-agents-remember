# dashboard/src/cockpit/layout.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Own cockpit shell recipes, shared sidebar/column styling and rail resizing separately from view and task routing.

## Code Commentary

Above 40rem the shell is a 100vh hidden-overflow flex column. At 40rem and narrower it permits vertical scrolling, constrains width and wraps title/status content. The three stacked body rows, 24rem rails and 28rem minimum viewport apply only to a non-fullbleed body outside the review page. Review is expressly excluded from those stack heights. Cockpit chooses its actual column tracks. [1] [2] [5]

`RailResizeHandle` clamps rounded width to 220–560 pixels. Opposite left/right drag directions and 24px arrow-key nudges use the same bounded width. Pointer listeners end on pointerup; the memoized handle is omitted at the narrow breakpoint. Optional label/test IDs distinguish review handles from retained Operations handles. Saved-width persistence remains in the caller. [3]

The shared left/right rail IDs are the targets of sidebar `aria-controls`; the review chat column reuses the right ID. `sidebarStrip` aligns Operations' toggles at the document edges. `reviewChatColumn` supplies a bordered surface and `reviewChatClose` its own toggle line; placement and width calculations remain with the review layout owners.

`useMediaQuery` owns the initial match and one change subscription with cleanup for the supplied query. `useNarrowCockpit` delegates the 40rem query. `takeoverBody` supplies fixed/inset/z-index styling at that width; the ordinary change-set takeover consumes it, while review is in the railed body. [4] [5]

## Invariants And Boundaries

The viewport and rails hide their own overflow and leave internal scrolling to their panels. The narrow shell is the outer vertical scroller. The Chats layer supplies layout, while actual retained mounting and active visibility belong to Cockpit. Desktop never-wrap styling has an explicit narrow override. Styles and comments alone do not establish measured browser overflow.

## Evidence


- Grid base keeps desktop variants; the caller selects responsive columns. [2]

- Narrow shell scrolling and stack heights exclude the review page. [1]
- Resizing remains bounded and directional, with distinct optional names for review handles. [3]
- Media-query changes have listener cleanup; narrow takeover styling remains a separate recipe. [4]
- Cockpit selects its Operations/review tracks and narrow one-column grid. [5]
- Sidebar IDs and strip styling connect the shared Operations controls to retained rails. [6]
- The review chat surface and close-toggle line have their own styling without owning placement geometry. [7]
