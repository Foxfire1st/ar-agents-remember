# dashboard/src/cockpit/roleChatTarget.test.ts

## Governing Overview

[overview](overview.md)

## Purpose

Pins the seat-to-chat seam in isolation: what a row asks for, which selection reaches it, which frame target
answers, and when the named chat stops being the one on screen.

## Code Commentary

`carries the exact agent with its role and its own document, and invents no task` pins that a bound seat keeps
its document reference and a taskless seat carries none. `is the launcher selection of the seat, or none for a
role the launcher does not have` pins the null case and the `system-specialist` → `investigator` mapping.
`asks for the named agent over the seat another receipt of the same scope names` pins the named agent winning
over another receipt and returning nothing for a rejected execution. `scopes the frame to the seat the row
named, whose document the launcher cannot hold` pins the seat's own JSON scope. `keeps the named chat while the
launcher repairs the seat, and drops it on a real pick` pins that a role-only repair keeps the chat and a
document pick or another role ends it.

## Evidence boundary

Source-level tests at the reviewed freeze, in the dashboard suite. No test was run for this leaf, so they are
not an executed witness, and they are not a live-page witness either:
evidence item 6 is unrun and carried to L36, and item 7 is unrun.
