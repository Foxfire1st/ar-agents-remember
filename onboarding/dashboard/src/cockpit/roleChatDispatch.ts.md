# dashboard/src/cockpit/roleChatDispatch.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Build, submit, adopt and recover a role start or exact-request Revive.

## Code Commentary

Dispatch retains the selected retry UUID and full task scope, carries sticky refusals, and validates accepted execution identity before polling. A foreign acceptance stops polling. An offline task-bound recovery read is not pinned to the unavailable host; a usable accepted host notifies the current callback, not the callback captured when the request began.

## Boundaries

Start/Revive transport is separate from automatic Result and rendering. Revive does not invent a per-request operator override. Options refresh still runs in the dispatch finally path.

## Current Contract

Start requests now copy a truthy selection.stepUp into both the saved retry selection and HTTP body. Revive never carries that field, and per-request Revive still omits operator overrides. Step-up asks may pass true as the browser canStart operand while ordinary starts use execution.canStart; runnable, request-identity and unresolved-retry guards still apply and the backend still owns retirement, liveness, choices and permission admission. Only fresh per-request starts (`perRequest && action === "start" && !replayRequestId`), including request-scoped Architect/Investigator selections, publish their UUID, pending flag and retry selection through `updateActiveRequest` before POST. Other dispatches construct a local saved selection without taking that pre-POST persistence branch; ordinary task-seat offline recovery is separate. The per-request retry selection retains the same UUID/reason/overrides. This transport neither counts tries nor selects a stronger model.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]
- Reason admission, threshold and differing-harness/model inheritance boundary. [5]

- Saved taskless UUID/pending plus trimmed reason/override restoration keeps the legacy Investigator storage slot. [6]

- The same start-only reason enters saved retry payload and POST body. [7]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [8]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [9]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [10]

- dispatchRoleAction is a current owner of the behavior described above. [1]
- applyDispatchReceipt is a current owner of the behavior described above. [2]
- failDispatchOffline is a current owner of the behavior described above. [3]
