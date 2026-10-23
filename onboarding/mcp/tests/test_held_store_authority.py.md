# mcp/tests/test_held_store_authority.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins that the held store, not the delivery queue, holds the authority: a store the queue never names still
reaches the view, and a queue that is torn, expired or empty changes nothing about what the stores say.

## Code Commentary

The cases walk real stores, real receipts and a real queue under a coordination root. They pin the two-line
rule the module exists for — the queue is a hint and never the census, and each store contributes its own rows
— across a cold reader with no queue at all, a cold reader over a torn queue, an entry expired by age or evicted
by the queue bound, and a store beside a named one reached only by bounded enumeration.

The retention cases are the other half: a torn observation is incomplete rather than empty, a store that goes
unreadable keeps the row already read, a row stamped long ago is never dropped for its age, a removed working
folder is a complete emptiness, and a receipt naming no existing store invents nothing. Bounds are shown to shed
only what they must — a pass over more receipts than one observation resumes bounded, rows beyond the row bound
are shed with the view saying incomplete, and retention trims the retained view even on an incomplete pass.
Sixty-five holders are reached by rotation in one complete pass, and a row cleared between passes does not
survive it.

## Evidence boundary

Source-level pytest cases at the reviewed freeze — real stores, receipts and queue JSON, up to sixty-five
holders — not a live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36,
item 7 unrun.
