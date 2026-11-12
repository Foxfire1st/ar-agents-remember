# mcp/src/agents_remember/observer/reducer_impl/_attention_native.py

## Governing Overview

[overview](../overview.md)

## Purpose

The four deterministic row builders that turn native facts into attention rows — one per file-backed kind, with
the two notice kinds sharing the last: identity, severity, lane,
action-or-notice class, dismissibility and the subject each row opens.

## Code Commentary

`native_attention_items(facts, tasks, now)` concatenates the four builders and lets the queue's one total sort
rank them. Row identities are stable and occurrence-scoped: `permission-wait:{agent_id}:{prompt_id}`,
`held-message:{recipient}:{message_id}`, `task-stalled:{task.key}:{interval start}` — the task's last published
bound turn end, read from `facts.turn_ends` — and the store's own `occurrenceId` for a notice. `stall_occurrences`
(:121-134) publishes the same identities for every started task that is idle now, before the settled deadline has
passed, so the interval that is reclaimed and the row that is published can never be two different things.

Each builder states its class: the three live kinds are `warn` and `itemClass="action"`, the two notices are
`info` and `itemClass="notice"`. Every row the module builds is `dismissible=True` (:74, :110, :199, :232): the developer's acknowledgement hides one occurrence of any kind, and the class says only how
that occurrence also ends — a live cause when its native fact ends, a notice when the bounded store drops it — and
how its identity is named. Dismissing changes nothing at the cause.

Nothing here infers a cause from lifecycle prose or invents a task for a taskless seat: a stall requires stage
`started`, activity `paused` (a task whose seat waits on a declared wait still to be checked is `waiting`, so it is no candidate) and an idle interval at or past `STALL_SECONDS`, its detail is the fixed sentence
*"no bound agent has held a turn for the settled interval"*, and a taskless agent's row carries no task. The
builders apply `MAX_PERMISSION_ITEMS`, `MAX_HELD_ITEMS` and `MAX_TERMINAL_ITEMS`.

### 20261023-L190-v2 The Interval Start Joins The Stall Identity

A stall's occurrence is named by the task *and the start of that idle interval*, so the row id carries the
interval's stamp (:189) and `_interval_start` (:251-279) resolves it: the latest published turn-end of the task's
bound agents, then the task's own `eventAt`, then the reader's watch (`stall_clocks`). A reader that restarted
after the developer read the entry derives the same stamp from the same publication and the acknowledgement keeps
hiding the interval it acknowledged.

`_stall_candidates` (:137-156) is the one owner of stall eligibility, read by both `_stall_items` (:159-204)
and `stall_occurrences` (:121-134), so the settled deadline, the pause suppression and the identity cannot drift
apart. The deadline counts on the reader's own watch and the detail words do not move with age; only
the identity is named by the publication. A resumed bound turn ends the interval, so the acknowledgement leaves and
the next interval is published as a new entry.

## Evidence boundary

Current source interpretation; identity, class, dismissal, the deadline and the fixed
detail are pinned by `mcp/tests/test_attention_native_kinds.py`. No live-page witness and no CPU or resource
measurement.
