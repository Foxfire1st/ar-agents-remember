# mcp/tests/test_attention_quiescence.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins rule 9 on the delta side: quiet minutes emit nothing, and the threshold crossing emits exactly one
membership change.

## Code Commentary

One case builds in-memory native facts around a single interval start, advances the pass clock by a minute and
then by seven with the facts unchanged, and runs the real `diff_projection`: neither quiet step emits a delta, and
the step where the stall entry appears emits exactly one. Holding the interval start fixed is the point (v2 rule
7): an age-only pass moves `waitSeconds` under a row whose id does not move, so newest-first ordering does not
re-order either. That is the projection-side counterpart of the reader-side rule that an age-only pass parses no
native store, and together they are what keeps a quiet queue quiet.

The module proves the delta side only. A store reread on every pass is counted by
`mcp/tests/test_attention_native_inputs.py`, not here.

## Evidence boundary

One source-level pytest case at the reviewed freeze over in-memory facts and the real `diff_projection`, not a
live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7 unrun.
