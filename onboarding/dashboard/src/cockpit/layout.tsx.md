# dashboard/src/cockpit/layout.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Own the cockpit's Panda shell recipes and rail-resize interaction separately from view/task routing. This extraction keeps shell marker classes usable by Cockpit while adding a narrow layout; importing these styles does not itself mount a page or choose its columns.

## Code Commentary

Above 40rem the shell remains a 100vh hidden-overflow flex column. At 40rem and narrower it permits vertical shell scrolling, constrains width, wraps title/status content and gives a non-fullbleed body three rows, 24rem rails and a viewport with a 28rem minimum height. Cockpit's RailedBody—not bodyGrid's desktop recipe—actually selects a single column at that width. `takeoverBody` is a separate fixed/inset/z-index style consumed by the review/change-set takeover. Do not infer that Notes uses it.

`RailResizeHandle` clamps rounded widths to 220–560 pixels. Left and right drag directions are opposite; ArrowLeft/ArrowRight nudge by 24 pixels with the corresponding side orientation. Pointer listeners are removed on pointerup. `useNarrowCockpit` reads matchMedia initially, subscribes to changes and cleans up its listener; the handle returns null when narrow. Width persistence belongs to Cockpit's persisted-number hooks, so temporarily omitting the handle or using one column does not erase saved widths.

`viewport` and `rail` still hide their own overflow and delegate internal scrolling; the narrow shell is the outer vertical scroller. `chatsLayer` supplies only layout for retained children: actual keep-alive mounting/visibility belongs to Cockpit. The top-bar brand comment's never-wrap wording describes the desktop base only; its explicit media override permits narrow wrapping. No source style proves a measured browser overflow result.

## Evidence

- Narrow shell scroll/width/row/rail rules are explicit media overrides. [1]
- Grid base keeps desktop variants; the caller selects responsive columns. [2]
- Resizing is bounded, directional and keyboard reachable only above the narrow breakpoint. [3]
- Narrow takeover is fixed; matchMedia state has listener cleanup. [4]
- Cockpit actually chooses the narrow one-column grid. [5]
