# Silent turn-end notification decision

## Governing Overview

[Plugin overview](../overview.md)

## Purpose

Own the pure, host-free decision about what a role agent's ended turn owes: its parent's wake-up line, or — for a Worker, Reviewer or Curator that stopped without handing off — a message back to the seat itself. The plugin entry feeds host events and supplies the sender; role facts come from the role-start-published record.

## Contract

One recogniser decides which AR tool a `tool_call` row names and reads its answer: the bare name, `<server>.<tool>`, and each Hermes title with or without a preview, with non-AR ACP kinds never matching; the answer comes from Codex's `output` or from Hermes's text in either wrapper after one unescape, and a cut answer is read as far as it shows. The recipient is read from Codex's `input` or from a Hermes answer that names it. A row that shows no recipient still counts as a hand-off where it is one, but never as a return to its parent.

A turn hands off when its own rows hold a `role_message` whose finished answer is not `refused`, `ok: false` or `recipient-busy` (delivered, held and the waiting outcomes all count), or a `task_doc` write that is not `ok: false`. A leaf seat may start no role, so a `role_start` is no hand-off of theirs.

An end is silent only when the turn completed, holds no hand-off, and nothing holds it: the seat is not archived, waits for no permission, has no child agent in a turn, and is not answering a waiting sender. The turn's rows are, when the host tags them with the event's turn id, the rows carrying that id; otherwise those after the seat's previous end as this build saw it — its remembered row count and the identity of its last row — falling back to the last `user_message` on the first end seen or when a replaced timeline no longer holds that row. A child is an agent whose `paseo.parent-agent-id` label names the seat, read from the host's agent list; only a listing that ran to exhaustion supplies authoritative host facts, and an incomplete listing leaves the seat alone.

Every silent end waits 60 seconds before anything is sent, the counted parent line included. A turn of the seat that starts inside the wait cancels the send and the end is not counted. At the end of the wait the host state is read again: only a seat out of a turn, unarchived and owing no permission is acted on; otherwise nothing is sent, a row is written, and the end is not counted.

The first two silent ends in a row send the seat one message: a fixed first line of the plugin's own, its role and task, the ended turn's own last line of text shortened to 300 characters, that the turn ended with no hand-off, and an instruction to go on with its stage in this turn or to send what blocks it to its parent with `role_message`; when the turn's rows hold a `delegate_task` call the message adds that a helper's result does not come back as a message here. From the third on, every silent end sends the seat nothing and gives its parent MIK-R172's line marked with the count. The count is per seat agent id and returns to zero on a hand-off or on a turn begun by a message the plugin did not send. Only Workers, Reviewers and Curators are sent back; a parent that is in a turn is still told when its turn ends rather than steered into it, unless the product knows its provider keeps its turn under a steer.

A leaf agent whose recorded parent is archived or missing gives its line to the current Manager of its master; an agent the product's agent list does not hold gives no line and is named in the host log once. The tracker records active turns, permissions, parent links, the provider each agent runs on, the per-seat timeline mark and silent-end run, and the pending wait of each seat. Its historical maps — parent links, the started order, provider history, departed agents, silent runs, seats' epochs and timeline marks — keep capped windows; the active turn and permission sets are live state with no historical cap, and the pending waits are capped fleet-wide at `TURN_ENDED_WAIT_LIMIT`, one wait per seat, an end past the cap shedding its own wake with a skipped row. A delivery in flight is not a separate registry: its wait leaves the map before the host await, and a later epoch makes the continuation void. A subject with a direct child in a turn is held, and a line whose parent awaits permission waits; a batch that has just started a turn in the parent leaves the rest owed. Flushes do not overlap, and delivery order is the order the turns ended even across requeues and a Manager rebind.

Every decision row the current generation emits is offered to the plugin's own files through `turn_log.ts`: one JSON row per line in `turn-ends.jsonl` for each message sent, marked line, cancelled wait, skipped send and left-alone end, with the file turned over at 2 MiB to one retained archive, and a failed write named once in `turn-ends.error.json`. An obsolete intake outcome and a send that spans a generation boundary emit no row, an unmarked ordinary parent line is not a rule row, a sink without `PASEO_HOME` writes nothing, and a failed write is best-effort. `host-activity.json` keeps its bytes.

## Boundaries

The implementation caps a line at `TURN_ENDED_LINE_LIMIT`, the carried last line at `TURN_ENDED_LAST_TEXT_LIMIT`, the self-wake run at `TURN_ENDED_SENT_BACK_LIMIT`, the wait at `TURN_ENDED_WAIT_MS` and the log at `TURN_END_LOG_LIMIT_BYTES`; the decision does not read roleMessageLimit dynamically. The historical stores keep bounded recent windows and hold no owed line, and an evicted or absent provider reads as unknown, so a lost entry can delay a wake but cannot send into a running turn. The log records the plugin's own decisions and writes; it is not a census of messages the host delivered. These are in-memory event decisions and host-free composition, not durable message filing, cross-process deduplication, live SDK delivery proof, or a promise about repeated host events. Host wiring is `turn_events.ts`.

## Evidence

- Timeline tool-call recipients, not sibling traffic, decide which call is a return and which is only a hand-off. [1]
- Descendant restart removes held lines and invalidates claimed ancestor lines. [2]
- Synchronous claim ownership and send-point rechecks prevent overlapping flushes owning one deferred line. [3]
- Role/parent facts, return and permission state decide whether a silent end produces, holds or drops the parent's line. [4]
