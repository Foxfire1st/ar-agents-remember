# dashboard/src/cockpit/paseoPluginBridge.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Owns the real plugin control-channel fixture cases extracted from the client-part suite, including native display confirmation and capability-gated early/failure reports.

## Code Commentary

The cases retain exact parent/origin admission, current-generation navigation, route/store/visible-chat confirmation, compact-layout fail-closed checks, teardown and SDK identity controls. Negotiated on-chat and load-failed cases distinguish being on the selected native screen from drawing its messages or reporting the application's failure pane. A dashboard without the advertised ability receives no new answer kind. Page/SDK/DOM fixtures do not certify actual native host timing, installation framing or post-release message delivery.

The `showing` cases observe the chat chosen through Paseo’s own navigation. No report or observation timer is started for a dashboard that has not advertised `showing`. After hello, the compact fixture reports the routed workspace’s stored focused chat even when its native `selection` is empty; a later focus change reports the new chat once, and not-found or terminal focus reports null. The wide/split fixture follows the focused one of the visible chats. None of these observations calls `openScreen`.

The compact fixture models display signs attributed to the pinned @getpaseo/server 0.16.2 web build. Its DOM and timer cases exercise the control bridge against fixtures.

## Evidence

- The extracted suite retains channel/native-display safety and checks capability-gated on-chat and native failure completion. [1]
- Showing is opt-in, follows compact native focus, suppresses duplicate reports, reports null for non-chat screens and navigates nothing. [2]
- The wide and split-pane showing fixture follows the stored focus among visible chats. [3]

- The compact DOM fixture names the pinned @getpaseo/server 0.16.2 release. [4]
