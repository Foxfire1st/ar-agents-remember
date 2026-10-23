# mcp/src/agents_remember/controlplane/held_store_layout.py

## Governing Overview

[overview](overview.md)

## Purpose

The held-message store on disk: its names, schemas and bounds, the atomic writer, the receipt lines, and the
authority reader that decides which store rows are really held. It sends and drains nothing; holding, withdrawal
and ending a waiting reply are its own writes.

## Code Commentary

Discovery primitives come from the adjacent `controlplane/held_store_discovery.py`; delivery and native attention read this same lower store owner.

The queue is a visit order and never a census; the authority is the store file. That distinction is the point
of the module: the delivery queue names receipts to look at, the reader then reads those stores, and a store the
queue does not mention is still found through bounded discovery.

Store and queue: `ar-held-messages/v1` with `MAX_HELD_PER_RECIPIENT = 20` per recipient at
`<workspace>/.ar-product/held-messages/<agent id>.json`, and the queue `ar-held-message-queue/v1` at
`<coordination_root>/temp/held-message-queue.json` with `HELD_QUEUE_MAX_ENTRIES = 512` and a 24-hour age bound.
`store_path_for` refuses a name that is not a canonical UUID, so a directory entry is never read as a store.

Authority reading is bounded end to end: `MAX_HELD_AUTHORITY_RECEIPTS = 512`, `MAX_HELD_AUTHORITY_STORES = 64`,
`MAX_HELD_AUTHORITY_RETAINED = 1024` receipts and `MAX_HELD_AUTHORITY_ROWS = 256`, with the enumeration share
taken from the discovery budget. `HeldAuthorityReader.reset` lets one reader serve repeated passes, and
`read_held_authority` answers rows plus completeness, so an unreadable or shed branch is incomplete rather than
empty. `MAX_HELD_RECORD_LINES = 30` and `STALE_CLAIM_SECONDS = 120.0` bound the record text and claim freshness.

## Evidence boundary

Current source interpretation at the reviewed freeze; the hint-not-census rule, torn readings, bounds and the
UUID refusal are pinned by `mcp/tests/test_held_store_authority.py`,
`test_held_store_partial_rows.py` and `test_attention_native_inputs.py`. No live-page witness and no CPU or
resource measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
