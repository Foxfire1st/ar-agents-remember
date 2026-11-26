# Native held-message store and delivery

[MCP package overview](../../../overview.md)

## Contract

Hold only still-waiting native role messages in `.ar-product/held-messages/<recipient>.json` under the recipient’s own workspace, with the store's schema strings, file names and bounds taken from the read-side layout owner `controlplane/held_store_layout.py` so the delivery machinery and the attention reader cannot disagree about them. Store admission, claims, and settlement run under the recipient's launch-receipt lock (`cli/role_held_store.py::open_held_store`, using atomic replacement and fsync), refuse closed seats or missing workspaces without creating a store or folder, admit at most twenty messages and never drop an existing message to make room. Text is limited by the message input boundary, not summarized by this module. The store is independent of hosted-seat/control-plane messaging.

## Delivery and recovery

A drain claims one immutable FIFO batch under a durable message ID. Later admissions remain behind that batch. One recipient has one claim owner; a live claim prevents withdrawal and a stale claim resumes its original members and ID, not an expanded batch. The first addressed work for an unopened held seat is prefixed by its compiled handover exactly once on the normal successful path. Receipt-bound role identity is published before an unopened held seat is launched; closed-seat drain/send resumes use `role_activity.resume_role_agent`, which publishes before native resume. This ordering does not make host acceptance and durable queue settlement one transaction.

Attempt the whole remainder before using any learned byte budget. A successful size is only a lower bound; after a whole refusal, find the largest admitted FIFO prefix. This yields the fewest deliveries under a stable monotone size limit without a word-count splitter. A single unadmitted message stays held. Part IDs survive recovery. Exactly-once recovery across a host-accepted/disk-not-committed boundary additionally depends on host deduplication by the supplied message ID; these tests establish it with a deduping fake host, not a real-host witness.

Delivered batches stage compact terminal metadata before removing waiting text and flush it into the launch receipt (keeping only that metadata for a later sweep on receipt-write failure). When a recipient is closed, archived, gone, or seat-lost, `_end_batch` settles the store through `settle_held_store`, recording every still-waiting message with its text in `heldStoreClosures` on the launch receipt before unlinking the store file; sender withdrawal remains a terminal end, and elapsed time is not. Clearing an ended queue also removes an empty delivery claim.

## Bounded actor

The serving loop calls `sweep_held_messages`. Its queued slice and receipt walks share a limit of thirty-two receipt reads and thirty-two drains per tick. Delivery synchronously enumerates all receipt roots with `receipt_roots`, then retains one resumable `ReceiptWalk` per root; this root enumeration and walk population have no sixty-four-folder cap. Each directory is read through a live `os.scandir` iterator in filesystem order, without materializing or sorting its names or all receipt paths. Each delivery walk uses the default 256-entry traversal allowance, while the attention reader supplies its remaining entry allowance explicitly; the sixty-four open/cached folder limit belongs to attention's `HeldFolderDiscovery`. History and message-binding subtrees are not descended into. `_receipt_needs_drain` checks the store even when a receipt counter is absent or zero. Product shutdown may pause delivery; durable text resumes with serving, without a sender/model turn.

## Turn-end delivery and the held-receipt queue

The serving tick delivers what waits for a recipient the host's own activity record reports as having just ended a turn: `deliver_ended_turns` drains only the receipts a holder named in the queue, sends nothing to the recipient, and stops at thirty-two receipts. `note_held_receipt` names a receipt in the queue on every hold; the queue is a working surface of at most 512 entries and 24 hours, and losing it costs one later sweep visit, never a message.

`sweep_held_messages` drains the queued receipts before it walks any path, in a slice that starts where the previous tick stopped, so a receipt beyond the first thirty-two is reached within a bounded number of ticks while the receipts ahead of it stay held. The walk remains the fallback for receipts no holder named, under the same per-tick read and drain budget.

Before a resend, a message attempted under a host id goes alone and under that id: the drain asks the recipient's timeline through the bridge's `agent-has-message` command and, when the copy is already there, records the delivery with no send. A drain that pauses — the host unreachable, the resume unconfirmed, the store unclaimed or unreadable — writes one warning line naming the recipient and the reason and recounts the receipt's waiting count from the store it holds.

## Current Contract — Scoped Launch And Settings Changes

`_open_held_seat` invokes the receipt owner’s `_restore_launch_handover` with the saved launch call and runs `run_launch_call` with `LaunchExecutionPolicy(mode="open-held", on_retry_agent=...)` so eager-harness held seats re-confirm exclusive `agents-remember-task` binding before receiving their first message (re-publishing `role-agents.json` on retry). The artifact-backed path validates frozen details and verifies the primary handover and any takeover material. With neither artifact reference, the helper validates the frozen details directly. A held leaf Reviewer or Curator receives its applicable product notice between the frozen handover and the claimed waiting messages. When binding confirmation fails twice or the seat is lost (`is_held_seat_lost`), `_open_held_seat` settles waiting messages through `held_seat_lost_settlement` and `settle_held_store`, and `apply_drain_to_receipt` applies `apply_held_open_confirmation` for `bindingConfirmation` and retried `agentId`/`replayRequest` updates.

A ValueError releases the claim and returns cannot-open with the specific recovery detail; no host opening occurs and waiting messages remain. Existing successful opening stages terminal metadata before removal, and existing FIFO, batching, store limits, permission guards and bounded sweep contracts remain unchanged.

## Evidence






- Admission appends under the store lock and refuses overflow without dropping text. Anchor: `hold_message` [1]









- A drain delegates claim/readiness checks and whole-first FIFO delivery. Anchor: `drain_held` `_deliver_waiting` [2]









- Terminal lines are published separately from ended text and retain failure state. Anchor: `apply_drain_to_receipt` [3]





- Yielded receipt paths, reads and drains are capped; each directory stays open as a live filesystem-order scan. Delivery root discovery is synchronous and retains one walk per discovered root, without the attention reader's sixty-four-folder cap.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/controlplane/held_store_discovery.py:70-95 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08; mcp/src/agents_remember/controlplane/held_store_discovery.py:158-191 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted




- Handover validation precedes prompt construction and host launch. Invalid handover details release the claim while preserving the waiting batch. [5]









- Held-seat opening checks frozen details before composing its message. If artifact references are present, the helper also restores or verifies their files. [6]







- Test source checks cannot-open, zero second host calls and retained/reclaimable work. [7]


**L184 — INV-1ZKP4R.** The held store is where a waiting row's fields are written and read, so the reset survives here or not at all. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/controlplane/held_store_discovery.py:70-95 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08; mcp/src/agents_remember/controlplane/held_store_discovery.py:158-191 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted.




- The held opening inserts its product notice between the restored prompt and the FIFO batch. [9]




- Yielded receipt paths, reads and drains are capped; each directory stays open as a live filesystem-order scan. Delivery root discovery is synchronous and retains one walk per discovered root, without the attention reader's sixty-four-folder cap. [4]
