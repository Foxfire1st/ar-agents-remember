# mcp/tests/test_attention_native_inputs.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins the facts one projection pass reads — permissions, held rows, the stall interval and the notice store — and
the two retention rules that keep an incomplete read from clearing anything.

## Code Commentary

Permissions: two published prompts arrive and keep their identity through an unreadable publication, and an
observation with no identity retains the known prompt until a complete read ends it. Held rows: a row comes from
its store row without the message text and leaves only when the store does, an expired queue entry is inert, and
a delivered row does not return because another store is torn.

The stall interval is the subtlest: only an explicit pause suppresses a stall, the clock starts at the first
complete eligible observation, and an unknown observation, a new native boot, bound work, a paused master's
listed child and a reacquisition each break or restart the interval rather than letting it accrue.

The store-read cases pin that a pass reads only the stores its domains name: an age-only pass parses no native
store, a controlplane refresh reads its own stores and not the held queue, and the parse budget covers the
admitted pause population. The notice cases pin an unproven intent publishing nothing while it waits, and an
acknowledgement keeping one occurrence and not the next.

## Evidence boundary

Source-level pytest cases at the reviewed freeze over a real host publication, held store and receipt, queue,
activation record and notice store, not a live-page witness and no measurement: MIK-R200 evidence item 6 is
unrun and carried to L36, item 7 unrun.
