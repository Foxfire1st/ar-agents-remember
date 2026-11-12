# mcp/tests/test_held_store_partial_rows.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins the narrow case that a partly malformed store never replaces the complete reading the reader already had.

## Code Commentary

One case builds a real store, receipt and queue, takes a complete reading, then splices an impossible row into
the store and reads again: the two rows of the earlier reading are kept and the observation is reported
incomplete rather than being replaced by the rows the malformed file happens to parse.

That is the difference between "this store says less now" and "this store cannot be read whole", and it is what
stops a partly written file from clearing a held row that is still held.

## Evidence boundary

One source-level pytest case at the reviewed freeze, not a live-page witness and no measurement: MIK-R200
evidence item 6 is unrun and carried to L36, item 7 unrun.
