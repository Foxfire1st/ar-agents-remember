# Native held-message store and delivery

[MCP package overview](../../../overview.md)

## Contract

Hold only still-waiting native role messages in `.ar-product/held-messages/<recipient>.json` under the recipient’s own workspace, with the store's schema strings, file names and bounds taken from the read-side layout owner `controlplane/held_store_layout.py` so the delivery machinery and the attention reader cannot disagree about them. Admission is locked, uses atomic replacement and fsync, admits at most twenty messages and never drops an existing message to make room. Text is limited by the message input boundary, not summarized by this module. The store is independent of hosted-seat/control-plane messaging.

## Delivery and recovery

A drain claims one immutable FIFO batch under a durable message ID. Later admissions remain behind that batch. One recipient has one claim owner; a live claim prevents withdrawal and a stale claim resumes its original members and ID, not an expanded batch. The first addressed work for an unopened held seat is prefixed by its compiled handover exactly once on the normal successful path. Receipt-bound role identity is published before an unopened held seat is launched; closed-seat drain/send resumes use `role_activity.resume_role_agent`, which publishes before native resume. This ordering does not make host acceptance and durable queue settlement one transaction.

Attempt the whole remainder before using any learned byte budget. A successful size is only a lower bound; after a whole refusal, find the largest admitted FIFO prefix. This yields the fewest deliveries under a stable monotone size limit without a word-count splitter. A single unadmitted message stays held. Part IDs survive recovery. Exactly-once recovery across a host-accepted/disk-not-committed boundary additionally depends on host deduplication by the supplied message ID; these tests establish it with a deduping fake host, not a real-host witness.

Stage compact terminal metadata before removing waiting text, then flush it into the launch receipt. Terminal receipt failure keeps that metadata for a later sweep, never the ended text. Archive/gone and sender withdrawal are terminal ends; elapsed time is not. Clearing an ended queue also removes an empty delivery claim.

## Bounded actor

The serving loop calls `sweep_held_messages`. Its queued slice and receipt walks share a limit of thirty-two receipt reads and thirty-two drains per tick. Delivery synchronously enumerates all receipt roots with `receipt_roots`, then retains one resumable `ReceiptWalk` per root; this root enumeration and walk population have no sixty-four-folder cap. Each directory is read through a live `os.scandir` iterator in filesystem order, without materializing or sorting its names or all receipt paths. Each delivery walk uses the default 256-entry traversal allowance, while the attention reader supplies its remaining entry allowance explicitly; the sixty-four open/cached folder limit belongs to attention's `HeldFolderDiscovery`. History and message-binding subtrees are not descended into. `_receipt_needs_drain` checks the store even when a receipt counter is absent or zero. Product shutdown may pause delivery; durable text resumes with serving, without a sender/model turn.

## Turn-end delivery and the held-receipt queue

The serving tick delivers what waits for a recipient the host's own activity record reports as having just ended a turn: `deliver_ended_turns` drains only the receipts a holder named in the queue, sends nothing to the recipient, and stops at thirty-two receipts. `note_held_receipt` names a receipt in the queue on every hold; the queue is a working surface of at most 512 entries and 24 hours, and losing it costs one later sweep visit, never a message.

`sweep_held_messages` drains the queued receipts before it walks any path, in a slice that starts where the previous tick stopped, so a receipt beyond the first thirty-two is reached within a bounded number of ticks while the receipts ahead of it stay held. The walk remains the fallback for receipts no holder named, under the same per-tick read and drain budget.

Before a resend, a message attempted under a host id goes alone and under that id: the drain asks the recipient's timeline through the bridge's `agent-has-message` command and, when the copy is already there, records the delivery with no send. A drain that pauses — the host unreachable, the resume unconfirmed, the store unclaimed or unreadable — writes one warning line naming the recipient and the reason and recounts the receipt's waiting count from the store it holds.

## Current Contract — Scoped Launch And Settings Changes

_open_held_seat now invokes the receipt owner’s _restore_launch_handover with the saved launch call before adding waiting messages to the frozen opening prompt. The common path validates frozen detail identity/revision as well as restoring/verifying the primary handover and any takeover material.

A ValueError releases the claim and returns cannot-open with the specific recovery detail; no host opening occurs and waiting messages remain. Existing successful opening stages terminal metadata before removal, and existing FIFO, batching, store limits, permission guards and bounded sweep contracts remain unchanged.

## Evidence



- Admission appends under the store lock and refuses overflow without dropping text. [1]



- A drain delegates claim/readiness checks and whole-first FIFO delivery. [2]



- Terminal lines are published separately from ended text and retain failure state. [3]


- Yielded receipt paths, reads and drains are capped; each directory stays open as a live filesystem-order scan. Delivery root discovery is synchronous and retains one walk per discovered root, without the attention reader's sixty-four-folder cap. [4]

- Validation precedes prompt construction and host launch; failures retain waiting work. [5]


- Common restoration also validates instruction details and takeover references. [6]


- Test source checks cannot-open, zero second host calls and retained/reclaimable work. [7]

**L184 — INV-1ZKP4R.** The held store is where a waiting row's fields are written and read, so the reset survives here or not at all. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
