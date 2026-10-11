# Native held-message store and delivery

[MCP package overview](../../../overview.md)

## Contract

Hold only still-waiting native role messages in `.ar-product/held-messages/<recipient>.json` under the recipient’s own workspace. Admission is locked, uses atomic replacement and fsync, admits at most twenty messages and never drops an existing message to make room. Text is limited by the message input boundary, not summarized by this module. The store is independent of hosted-seat/control-plane messaging.

## Delivery and recovery

A drain claims one immutable FIFO batch under a durable message ID. Later admissions remain behind that batch. One recipient has one claim owner; a live claim prevents withdrawal and a stale claim resumes its original members and ID, not an expanded batch. The first addressed work for an unopened held seat is prefixed by its compiled handover exactly once on the normal successful path.

Attempt the whole remainder before using any learned byte budget. A successful size is only a lower bound; after a whole refusal, find the largest admitted FIFO prefix. This yields the fewest deliveries under a stable monotone size limit without a word-count splitter. A single unadmitted message stays held. Part IDs survive recovery. Exactly-once recovery across a host-accepted/disk-not-committed boundary additionally depends on host deduplication by the supplied message ID; these tests establish it with a deduping fake host, not a real-host witness.

Stage compact terminal metadata before removing waiting text, then flush it into the launch receipt. Terminal receipt failure keeps that metadata for a later sweep, never the ended text. Archive/gone and sender withdrawal are terminal ends; elapsed time is not. Clearing an ended queue also removes an empty delivery claim.

## Bounded actor

The serving loop calls `sweep_held_messages`. Resumable per-root walks yield at most thirty-two candidate paths and read at most thirty-two receipts per tick; drains have the same cap. Each visited directory’s names are materialized and sorted once per pass before yielding paths: that directory-listing cost is not a constant-time or elapsed-time bound. The accepted owner ruling permits this stable per-directory order, while forbidding a materialized set of all receipt paths. Root discovery is a separate glob over execution roots. History and message-binding subtrees are not descended into. `_receipt_needs_drain` checks the store even when a receipt counter is absent or zero. Product shutdown may pause delivery; durable text resumes with serving, without a sender/model turn.

## Evidence

- Admission appends under the store lock and refuses overflow without dropping text. [1]

- A drain delegates claim/readiness checks and whole-first FIFO delivery. [2]

- Terminal lines are published separately from ended text and retain failure state. [3]

- Yielded receipt paths, reads and drains are capped; one directory’s names are materialized in stable order per pass. [4]
