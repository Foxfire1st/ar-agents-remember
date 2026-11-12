# mcp/tests/test_canvas_presenter_store.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The attempt store: records are durable on disk, listing is chronological while lookups ignore the shown window, retention reclaims to its ceiling, and concurrent chat, activity and cancellation lose no state.

## Code Commentary

- Reconciliation by request identity finds an attempt outside the displayed window.
- A cancelled attempt is not revived by a late receipt.

- The concurrent chat/activity/cancellation case joins its workers under `HANG_GUARD_SECONDS`; its no-lost-state assertions remain the condition being tested.

## Evidence

- The case `test_attempt_listing_is_chronological_and_lookups_ignore_the_shown_window` protects this behaviour. [1]

- The case `test_concurrent_chat_activity_and_cancellation_lose_no_state` protects this behaviour. [2]
