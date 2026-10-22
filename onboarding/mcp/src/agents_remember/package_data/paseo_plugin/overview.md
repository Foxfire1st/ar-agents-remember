# Native Paseo plugin

## Governing Overview

[MCP repository overview](../../../../overview.md)

## Purpose

The product-owned plugin bridges provisioned embed data and role-agent lifecycle events into the native host. It neither edits the host's implementation nor asks it at intervals.

## Hot Path Summary

`index.server.ts` retains the embed RPC, contributes the host-activity snapshot RPC and installs two separate event owners. `server/host_activity.ts` publishes recorded agents' activity; `server/turn_events.ts` wires parent wakes through the shared tracker in `server/turn_ended.ts`, reads the host's agent state and sinks every decision row to `server/turn_log.ts`, the plugin's own bounded file. `server/role_agents.ts` supplies published role/task/report facts through one replaceable stat-generation cache, not a fresh JSON parse on each event. `server/fixtures/evidence-rows.json` holds the five captured host rows verbatim, and `server/turn_events.test.ts` drives the contributed adapter against incomplete and complete listings.

## Structure And Boundaries

The client bridge steers the one native frame through exact parent-window/origin admission and an agent-only open. Ready and pong advertise abilities; hello gates newer navigated/on-chat/load-failed replies. Selected-screen identity releases input, drawing completes the dashboard wait, and the application own failed-load pane ends it without invented dashboard failure prose. This does not add another frame, host polling, server lifecycle writer or semantic task acceptance. An older plugin stays message-capable where it supports open and its earlier-answer limitation is disclosed by the dashboard.



The provisioned embed list is read at plugin load, retaining visible malformed-data failure. Role facts have a different lifetime: role start publishes them, and readers stat their path and reuse the parsed value only for the same device/inode/size/mtime/ctime generation. A changed registration replaces that single cached value; absence clears it and returns no records, while malformed content fails visibly. Pure decision tests establish selected event schedules without proving live-host installation or event delivery. Asynchronous turn-end/permission handlers catch and log failures instead of throwing into the host loop. Missing role facts yield no line; they are not reconstructed from source or titles.

Host activity is a separate replaceable publication, bounded by the existing role-agent records. It starts incomplete, becomes usable only after a complete paginated host reconciliation, and returns to incomplete on unload. Events arriving during the whole read win over its older snapshot. Permission waits remain activity, and an idle snapshot invents no event timestamp. The snapshot RPC returns the plugin boot identity after reconciliation; the dashboard input qualifies that boot at its startup and on a newly observed plugin boot, not by periodic status polling. Parent-wake sends separately retain their turn/permission gates: a line goes to a parent that is mid-turn only where the product knows that provider keeps its turn under a steer, and otherwise waits for the turn to end.

A line carries the ended turn's own last line of agent text, shortened to 300 characters, and no document; a turn with no text says so, and a refused return still gives the line. A return to the parent suppresses it wherever the row shows the recipient — Codex's input or a Hermes answer that names it — while a row that shows no recipient is only a hand-off. A parent awaiting permission holds the line, and so does one that is in a turn unless the product knows its provider keeps that turn under a steer — the build names no such provider, so in practice a running parent is told when its turn ends, never steered into it and never replaced; the same gate is asked again before each send, so a batch cannot steer into a turn it has just started. Child activity holds the line, while descendant restarts drop the older owed one, including an already claimed deferred one. Each line is sent once, in the order the turns ended, across requeues and a Manager rebind. A leaf agent whose recorded parent is archived or missing gives its line to the current Manager of its master, and an agent outside the product's list is named once in the host log. The tracker is process-local and the source cap is distinct from the settings-reloaded role_message limit.

A Worker, Reviewer or Curator that stops without handing off is sent back to its work instead: after every silent end the plugin waits 60 seconds, then — if the seat is out of a turn, unarchived and owing no permission — sends the seat one message naming its role and task, quoting the ended turn's own last line and asking it to go on, or sends its parent the counted line from the third silent end in a row. A turn start inside the wait cancels the send and the end is not counted; a hand-off or a turn begun by another agent's message resets the run. Other roles are unchanged. Every message, marked line, cancelled wait, skipped send and left-alone end the current generation emits is offered to the plugin's own `turn-ends.jsonl`, turned over at 2 MiB to one archive, with a failed write named once in `turn-ends.error.json`; an obsolete intake outcome and a generation-boundary send add no row, a sink without `PASEO_HOME` writes nothing, and `host-activity.json` keeps its bytes. The plugin's cleanup drops pending and in-flight waits and clears the runs, so a reload starts afresh.

The client also carries the tray channel. `index.client.tsx` keeps supported theme/screen/RPC wiring separate from the pinned DOM adapters under `client/`. The bridge negotiates `pick` and `showing` with the trusted parent: `showing` reports the chat actually displayed, independently of a pending navigation request, and names no agent for missing/load-failed or ambiguous chat identity. Tray chat highlights can copy through the host copy handler and offer a non-modal Add control; only clicking Add posts a pick. Each pick carries the displayed agent, message ID and time from that row's own recorded timeline data. A row without recorded time is refused in place, and unreadable adapter structure produces a named notice rather than invented provenance. The same channel observes the message-box rectangle for an external tray dock — the box's own left and width beside its vertical edge, the pair optional as a unit — and reserves finite tray-height padding in the chat scroll root; missing composer measurement is named, and teardown disconnects every observer, including the class/style watch over the box and its ancestors that re-measures a layout move resizing nothing, and releases the reservation. These pinned DOM/React-property adapters are explicit unsupported host seams; source declarations and local tests do not establish live-host acceptance.

## Load-Bearing Files

- `index.client.tsx`: supported contribution wiring and the explicit boundary to unsupported client adapters.
- `client/bridge.ts`: trusted parent control, displayed-chat reporting and negotiated tray channel lifetime.
- `client/pick.ts`: chat highlight offers and exact row provenance, message-box measurements and reserved tray space.

- `index.server.ts`: embed and host-activity RPCs, independent event owners and unload publication.
- `server/host_activity.ts`: bound, boot-qualified host activity and atomic publication.
- `server/role_agents.ts`: typed, stat-generation-cached per-agent fact reader.
- `server/turn_events.ts`: contributed parent-wake handlers, host-state reads, log sink and steering sends.
- `server/turn_ended.ts`: stateful pure notification decision, including the leaf self-wake.
- `server/turn_log.ts`: the plugin's own bounded turn-end log and write-error file.
- `server/turn_ended.test.ts`: host-free schedules and preservation controls.
- `server/turn_events.test.ts`: the contributed adapter under incomplete and complete host listings.
- `server/fixtures/evidence-rows.json`: the five captured host rows, verbatim, for the row-shape tests.



**L184.** The plugin subscribes once per boot to provider subagent updates, publishes the running counts, reads the limit file at the send-back and the parent gate, and states its host requirement at 0.12.0.

## Evidence

- The client bridge negotiates display replies while keeping native navigation, selected-screen admission and drawing/failure distinct. [3]
- Keep embed RPC while wiring turn, permission and archive events to product-owned decisions; asynchronous handler failures are logged. [1]
- Read current role/task/report registrations through one replaceable stat-generation cache; absence clears it and malformed content remains visible. [2]
- Host activity is boot-qualified, record-bounded and event-driven; concurrent events win over the whole host read and no idle event time is invented. [4]
- Parent-wake handlers retain the existing gates: any admitted send asks the host for a steer, a free parent takes the line at once, and only a parent that is already in a turn is withheld unless the product knows its provider keeps that turn. [5]

- Supported client contributions remain separate from explicitly pinned DOM adapters. [6]
- The displayed chat is observed independently and published only to a dashboard that negotiates showing. [7]
- Trusted parent messages negotiate and control the tray channel, with complete teardown. [8]
- Message time comes from the exact row record; offer activation preserves the highlight and focus. [9]
- Only explicit Add posts a timed pick; unrecorded time and unreadable structure remain named. [10]
- Composer measurement carries the box's own left and width beside its vertical edge, names absence and owns the lifetime of its resize and class/style observers. [11]
- Negotiated tray space is bounded by the frame and released at teardown. [12]
