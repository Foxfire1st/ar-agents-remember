# mcp/src/agents_remember/observer/reducer_impl/_attention_native.py

## Governing Overview

[overview](../overview.md)

## Purpose

The four deterministic row builders that turn native facts into attention rows — one per file-backed kind, with
the two notice kinds sharing the last: identity, severity, lane,
action-or-notice class and the subject each row opens.

## Code Commentary

`native_attention_items(facts, tasks, now)` concatenates the four builders and lets the queue's one total sort
rank them. Row identities are stable and occurrence-scoped: `permission-wait:{agent_id}:{prompt_id}`,
`held-message:{recipient}:{message_id}`, `task-stalled:{task.key}`, and the store's own `occurrenceId` for a
notice.

The three live kinds are `warn`, `itemClass="action"` and `dismissible=False`; they clear only when their native
cause ends and the backend refuses a dismissal of one. The two notices are `info`, `itemClass="notice"` and
dismissible, acknowledged once per occurrence.

Nothing here infers a cause from lifecycle prose or invents a task for a taskless seat: a stall requires stage
`started`, activity `paused` and an idle interval at or past `STALL_SECONDS`, its detail is the fixed sentence
*"no bound agent has held a turn for the settled interval"*, and a taskless agent's row carries no task. The
builders apply `MAX_PERMISSION_ITEMS`, `MAX_HELD_ITEMS` and `MAX_TERMINAL_ITEMS`.

## Evidence boundary

Current source interpretation at the reviewed freeze; identity, class, dismissal, the deadline and the fixed
detail are pinned by `mcp/tests/test_attention_native_kinds.py`. No live-page witness and no CPU or resource
measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
