# mcp/src/agents_remember/canvas/explainer_service.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The order of a seat's life — build at the first request, Update, Retire, cancel — and the state the review page reads between those acts.

## Code Commentary

- `build_seat` refuses a Send that carries neither a message nor a reference, records the request in the leaf's ledger, and answers a repeated request with the seat it already made instead of building a second one.
- The first message is sent after the leaf lock is released, so the message store's own lock never nests under the leaf lock.
- `_checked_facts` refuses `task-archived` when the master is retired or archived, so an archived leaf never gets a working environment back.
- `update_seat` refuses `explainer-in-turn` while the seat is answering, `explainer-retired` when a marker stands, and `explainer-missing` when there is no binding to replace; it never waits for the lock.
- `retire_seat` waits for the leaf lock, finishes a pending receipt it finds, and answers an already-finished receipt as retired rather than retiring the same seat twice.
- `cancel_seat` names the seat and the request from the ledger, reports a request the ledger does not name as uncertain, and leaves the last ready page revision in place.

## Evidence

- A Send that carries nothing, or names an unknown history mode, is refused before any build [1]
- The seat and the ledger row are prepared under the leaf lock, and a repeated request answers the existing seat [2]
- A retired or archived master is refused by name, so no environment is rebuilt [3]
- An Update refuses when the seat is in a turn, already retired, or has no environment, and takes no lock deadline
- A Retire waits for the lock, finishes a pending receipt and answers a finished one without repeating it
- A cancel names the seat and the request, and reports an unnaming ledger as uncertain rather than cancelled

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_service.py:1043-1095 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/canvas/explainer_service.py:1098-1166 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/canvas/explainer_service.py:1250-1284 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.
