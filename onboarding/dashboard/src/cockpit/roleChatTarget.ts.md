# dashboard/src/cockpit/roleChatTarget.ts

## Governing Overview

[overview](overview.md)

## Purpose

The seam between a bell row's served seat and the Chats pane: the chat it names, the launcher selection that
reaches it, the frame target, and the scope the frame must show.

## Code Commentary

A row names an exact agent and, when the seat has one, its role and task document. `seatChatTarget` turns that
into the chat request; `seatChatSelection` turns it into the launcher's selection, mapping
`system-specialist` to the launcher's `investigator` and returning nothing for a role the launcher does not
hold; `chatFrameTarget` resolves the agent the embedded application is asked to show, preferring the named agent
over another receipt of the same scope and treating a `rejected` execution as no target; `chatFrameScope` and
`selectionEndsNamedChat` keep the shown chat attached to the seat the row named until a real document pick or a
different role ends it.

It never writes the observed-chat channel (`frameTrayChannel.setFrameChat`): that records the chat a frame
reports showing, and only the frame's own answer may say it. A row that names an agent therefore asks for that
agent and then waits for the frame, rather than asserting what is on screen.

## Evidence boundary

Current source interpretation at the reviewed freeze; the seat-to-chat mapping, the taskless case, the
`system-specialist` mapping and the observed-chat rule are pinned by `dashboard/src/cockpit/roleChatTarget.test.ts`
and `dashboard/src/panels/lifecycle-list/bellSubjects.test.tsx`. No live-page witness and no CPU or resource
measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
