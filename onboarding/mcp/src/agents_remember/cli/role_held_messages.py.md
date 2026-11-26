# Native held-message store and delivery

[MCP package overview](../../../overview.md)

## Contract

Hold only still-waiting native role messages in `.ar-product/held-messages/<recipient>.json` under the recipient's own workspace, with the store's schema strings, file names and bounds taken from the read-side layout owner `controlplane/held_store_layout.py` so the delivery machinery and the attention reader cannot disagree about them. Store admission, claims, and settlement run under the recipient's launch-receipt lock (`cli/role_held_store.py::open_held_store`, using atomic replacement and fsync), refuse closed seats or missing workspaces without creating a store or folder, admit at most twenty messages and never drop an existing message to make room. Hold-time admission stores texts accepted at the message input boundary without summarizing; at held-seat open time, `_open_held_seat` enforces `settings.role_message_limit` across the rendered FIFO batch via `role_opening_offload.prepare_held_opening_batch`, offloading over-limit batches to content-addressed `.held-batch-<sha256>.md`. The store is independent of hosted-seat/control-plane messaging.

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

## Held-seat opening and batch offload

`_open_held_seat` invokes the receipt owner's `_restore_launch_handover` with the saved launch call (verifying and restoring `.handover.txt`, `.handover.json`, `.step-up.json`, `.opening-message.md`, and frozen details, or validating frozen details directly when no artifact references exist). After restoration succeeds, `_open_held_seat` calls `role_opening_offload.prepare_held_opening_batch(batch.config, batch.receipt, combined_text(messages))` to enforce `settings.role_message_limit` (offloading over-limit batches to `<report_stem>.held-batch-<sha256>.md`), and joins the restored `opening` (which ends with its suffix `artifact_line`), any applicable `product_start_message` for a held leaf Reviewer or Curator, and `bounded_batch` with `"\n\n"`.

A `ValueError` from `_restore_launch_handover` releases the claim and returns `cannot-open` with the recovery detail; an `(AgenticSettingsError, OSError, ValueError)` from `prepare_held_opening_batch` releases the claim, preserves all waiting messages without calling `run_launch_call`, and returns `open-failed`. Successful opening stages terminal metadata before removal, and FIFO, batching, store limits, permission guards, and bounded sweep contracts remain intact.

## Evidence


- Admission appends under the store lock and refuses overflow without dropping text. [1]
- A drain delegates claim/readiness checks and whole-first FIFO delivery. [2]
- Terminal lines are published separately from ended text and retain failure state. [3]



- Test source checks cannot-open, zero second host calls and retained/reclaimable work. [7]

- Yielded receipt paths, reads and drains are capped; each directory stays open as a live filesystem-order scan. Delivery root discovery is synchronous and retains one walk per discovered root, without the attention reader's sixty-four-folder cap. [4]
- `_open_held_seat` runs handover restoration (`cannot-open` on `ValueError`) and `prepare_held_opening_batch` (`open-failed` on `AgenticSettingsError`/`OSError`/`ValueError`) before host launch, releasing the claim and preserving waiting messages on failure. [5]
- Held-seat opening checks frozen details and restores or verifies recorded handover/opening artifact files before composing its message. [6]
- The held opening inserts its product notice between the restored prompt (ending with its suffix `artifact_line`) and the bounded FIFO batch. [9]
