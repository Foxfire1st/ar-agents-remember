# Silent turn-end notification decision

## Governing Overview

[Plugin overview](../overview.md)

## Purpose

Own the pure, host-free decision about when a role agent's ended turn owes its parent a wake-up line. The plugin entry feeds host events and supplies the sender; role facts come from the role-start-published record.

## Contract

An eligible silent end composes one line naming the role/agent, task, the ended turn's last line of the agent's own text shortened to 300 characters, and the newest report; a turn with no such text says `no text` and a timeline the module cannot read says `unreadable`, and the line still goes out. A delivered `role_message` return to the agent that waits — by agent id, or by role plus the task reference as a `repository`/`path` pair, `repo:path`, `repo/path` or bare path — suppresses the line; a refused call, a sibling handover and an earlier turn's return do not. The turn read is the ended turn's own: rows carrying the event's `turnId` when they do, else the rows from the last `user_message`. A leaf agent whose recorded parent is archived or missing gives its line to the current Manager of its master; an agent the product's agent list does not hold gives no line and is named in the host log once, with the reason.

The tracker records active turns, permissions, parent links, the provider each agent runs on and the departed-agent window. A subject with a direct child in a turn is held, and so is a line whose parent is awaiting permission; a parent that is in a turn takes the line only when the product knows its provider keeps a running turn under a steer — `TURN_ENDED_STEERING_PROVIDERS` names no provider in this build, so absent named evidence every in-turn parent is told when its turn ends rather than having the host's steer-or-replace cut that turn off — and the gate is asked again at each actual send, so a batch that has just started a turn in the parent leaves the rest of the batch owed. A held line carries its subject's task, its turn-end sequence number and the alternate Manager known when it was owed, so an archived parent's line moves to that alternate and, with no successor recorded yet, stays owed for a flush to re-resolve. A descendant restart invalidates held and claimed ancestor lines. Flushes do not overlap — a later one waits for the one in flight — and, because the sequence number is taken when the event arrives, delivery order is the order the turns ended even across requeues and a Manager rebind. Flush removes and claims ready lines synchronously before awaiting, groups them by parent, re-resolves a departed parent at each send point, partitions whole lines into messages that each fit the cap, and rechecks claim ownership and readiness. Invalidated claims drop permanently; failed sends and currently unavailable valid claims are requeued. Dropped own lines yield `none` rather than `sent`.

## Boundaries

The implementation caps a line at `TURN_ENDED_LINE_LIMIT` and the carried last line at `TURN_ENDED_LAST_TEXT_LIMIT`; the decision does not read roleMessageLimit dynamically. It recognizes return calls from timeline metadata, not arbitrary transcript prose. The provider history is capped at `TURN_ENDED_PROVIDER_LIMIT`, re-inserted as the most recent on each event and reclaimed when its agent is archived; an absent or evicted provider reads as unknown, and unknown holds the line, so a lost entry can delay a wake but cannot send into a running turn. The historical stores (`started`, `archived`, `notedMissing`, `parentOf`) keep bounded recent windows and hold no owed line; `held` is bounded by who is waiting. These are in-memory event decisions, not durable message filing, cross-process deduplication, or a promise about repeated host events. Host wiring and actual event delivery are separate from the pure decision tests.

## Evidence

- Timeline tool-call recipients, not sibling traffic, determine whether the turn returned to its parent. [1]
- Descendant restart removes held lines and invalidates claimed ancestor lines. [2]
- Synchronous claim ownership and send-point rechecks prevent overlapping flushes owning one deferred line. [3]
- Role/parent facts, return and permission state decide whether a silent end produces, holds or drops its line. [4]
