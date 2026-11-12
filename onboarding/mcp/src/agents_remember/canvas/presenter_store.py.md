# mcp/src/agents_remember/canvas/presenter_store.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The durable presenter attempt store: record identities, ledger and retention. It owns how an attempt record is named, guarded, read, written and reclaimed, which is the one thing the capability must not re-implement.

## Code Commentary

- Every record is one JSON file sized before it is read, under the page's presenter directory; `read_bounded` refuses a huge file unread.
- `AttemptStore.locked` and `mutate` hold one lock across a whole read-modify-write, so a delayed host receipt cannot overwrite a cancellation.
- `prune` keeps the newest retained attempts and never removes a live one; `_bounded_record` settles the oldest turns to keep a record inside its byte ceiling.
- `by_request` and `by_session` reconcile one identity across every retained record rather than the displayed window, so a retried request finds its own attempt.

The one `PresenterRefused` class now lives in the import-light `presenter_refusals` module and is imported back here unchanged. The store and `StartOutcomeUnknown` keep the same exception identity while declaration modules can catch it without importing the store’s heavy implementation graph.

## Evidence

- An attempt record is sized before it is read. [1]
- One locked transaction covers a whole record mutation. [2]
- A receipt that arrives after a cancellation does not revive the attempt. [3]

- The current implementation moves the refusal class into an import-light owner without changing store transitions or exception identity. [4]
