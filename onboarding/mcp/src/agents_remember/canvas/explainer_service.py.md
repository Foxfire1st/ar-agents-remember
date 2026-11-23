# mcp/src/agents_remember/canvas/explainer_service.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The order of a seat's life — build at the first request, Update, Retire, cancel — and the state the review page reads between those acts.

## Code Commentary

- `build_seat` selects the planned request for blank composed content when the caller passes the planned history option and otherwise uses the end-to-end request, refuses an unknown history mode, records the request in the leaf's ledger, and answers a repeated request with the existing seat.
- The first message is sent after the leaf lock is released, so the message store's own lock never nests under the leaf lock.
- `_checked_facts` refuses `task-archived` when the master is retired or archived, so an archived leaf never gets a working environment back.
- `update_seat` refuses an in-turn seat. It reports a missing workspace, or a workspace with neither a binding nor trees, as `explainer-missing`. It acquires the leaf lock immediately or refuses.
- `retire_seat` waits for the leaf lock, finishes a pending receipt it finds, and answers an already-finished receipt as retired rather than retiring the same seat twice.
- `cancel_seat` names the seat and the request from the ledger, reports a request the ledger does not name as uncertain, and leaves the last ready page revision in place.
- `PLANNED_REQUEST` supplies the plan's empty Send, covering the requirement, effects, bound code and memory, the essay before visuals, and page assembly.

The dashboard’s Build route passes its parsed history to `build_seat`, whose optional history accepts None. Blank composed content with planned history selects the planned request. Other blank requests use the end-to-end words.

## Evidence

- An unknown history mode is refused before a build. For blank composed content both requests put the essay before visuals and the page last. The explicit planned history option selects the planned words.


- A Retire waits for the lock, finishes a pending receipt and answers a finished one without repeating it
- A cancel names the seat and the request, and reports an unnaming ledger as uncertain rather than cancelled


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_service.py:1043-1095 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/canvas/explainer_service.py:1098-1166 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/canvas/explainer_service.py:1250-1284 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Build refuses unknown history modes, records a request and returns the existing seat on replay. [1]


- The seat and ledger row are prepared under the lock. Repeated requests reuse the recorded seat. [2]
- A retired or archived master is refused before rebuilding the environment. [3]
- Update refuses an in-turn seat or an absent environment and acquires its lock immediately. [6]

- With blank composed content and explicit planned history, the service delivers a request to explain the requirement and planned effects, then write the essay, make visuals and assemble the page. [4]
- With blank composed content and recorded or omitted history, the service uses the end-to-end essay-first request. [5]

- The dashboard submits selected history. The HTTP handler forwards that validated value, and the builder chooses the planned first turn for blank composed text with planned history. [7]
