# Silent turn-end notification decision

## Governing Overview

[Plugin overview](../overview.md)

## Purpose

Own the pure, host-free decision about when a role agent's ended turn owes its parent a wake-up line. The plugin entry feeds host events and supplies the sender; role facts come from the role-start-published record.

## Contract

An eligible silent end composes one line naming the role/agent, task, ended turn and newest report. A recognized `role_message` return to the parent by id or role/task suppresses the line; a sibling handover does not. Missing role/parent records, no parent, or a permission-waiting subject produce none.

The tracker records active turns, permissions and parent links. A subject with a direct child in a turn is held, as is a line whose parent is busy or awaiting permission. A descendant restart invalidates held and claimed ancestor lines. Flush removes and claims ready lines synchronously before awaiting, groups them by parent, then rechecks claim ownership and readiness at each send point. Invalidated claims drop permanently; failed sends and currently unavailable valid claims are requeued. Dropped own lines yield `none` rather than `sent`.

## Boundaries

The implementation caps a line and a parent batch at `TURN_ENDED_LINE_LIMIT`; the decision does not read roleMessageLimit dynamically. It recognizes return calls from timeline metadata, not arbitrary transcript prose. These are in-memory event decisions, not durable message filing, cross-process deduplication, or a promise about repeated host events. Host wiring and actual event delivery are separate from the pure decision tests.

## Evidence

- Timeline tool-call recipients, not sibling traffic, determine whether the turn returned to its parent. [1]
- Descendant restart removes held lines and invalidates claimed ancestor lines. [2]
- Synchronous claim ownership and send-point rechecks prevent overlapping flushes owning one deferred line. [3]
- Role/parent facts, return and permission state decide whether a silent end produces, holds or drops its line. [4]
