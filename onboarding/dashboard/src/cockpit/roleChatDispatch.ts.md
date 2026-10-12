# dashboard/src/cockpit/roleChatDispatch.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Build, submit, adopt and recover a role start or exact-request Revive.

## Code Commentary

Dispatch retains the selected retry UUID and full task scope, carries sticky refusals, and validates accepted execution identity before polling. A foreign acceptance stops polling. An offline task-bound recovery read is not pinned to the unavailable host; a usable accepted host notifies the current callback, not the callback captured when the request began.

## Boundaries

Start/Revive transport is separate from automatic Result and rendering. Revive does not invent a per-request operator override. Options refresh still runs in the dispatch finally path.

## Evidence

- dispatchRoleAction is a current owner of the behavior described above. [1]
- applyDispatchReceipt is a current owner of the behavior described above. [2]
- failDispatchOffline is a current owner of the behavior described above. [3]
