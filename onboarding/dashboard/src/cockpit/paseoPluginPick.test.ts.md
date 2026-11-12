# dashboard/src/cockpit/paseoPluginPick.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify the tray-pick portion of the pinned Paseo plugin bridge against representative chat DOM and row records.

## Code Commentary

### Logic

The fixtures model the pinned Paseo 0.11.1 chat root, message/tool row ids, React DOM row props and host-recorded timestamps; they also draw Paseo's sidebar and a terminal pane beside the chat, each with its own rectangle, and a message box carrying its own left. The installed bridge runs against a fake trusted page with fake timers and a fake resize observer; the class/style watch is the environment's own MutationObserver, reached through the page rather than replaced by a fake.

Cases assert an explicit add offer preserves selection/focus, supplies each user/assistant/tool/older message’s own time, and never pages the host timeline. An unrecorded message stays unadded until its row has a recorded time. Unsupported/missing DOM or time yields the named notice/refusal, and split/no-agent or outside-row highlights supply no pick.

Copy-on-highlight requires the dashboard capability and preference. Composer cases report geometry on hello/growth/resize, reserve and release one tray-height style, allow a grace period during switching, then report a missing message box once and recover when it appears. Three cases cover the horizontal extent and the reservation's own boundary: a split layout posts the box's own left and width and posts again when only they change, a container resize and a class change that resizes nothing each post the box's new left, and a split layout pads the chat's scroll root alone while the sidebar, the terminal pane and the page body stay unpadded.

### Invariants And Boundaries

The DOM and row-prop values are explicitly modeled pinned inputs; this file does not establish current live Paseo DOM compatibility or execute a browser against a host.

## Evidence

- Selection-preserving add and no timeline read [1]
- Unrecorded time, unreadable DOM, copy preference and no-agent boundaries [2]
- Composer measurement, reservation and grace/recovery cases [3]
