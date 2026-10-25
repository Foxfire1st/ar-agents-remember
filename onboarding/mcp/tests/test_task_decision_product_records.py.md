# mcp/tests/test_task_decision_product_records.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One retained server predicate case marks legacy product-written decision strings (including `Finalize task lifecycle.`) while named authored controls and near-misses remain unmarked. The former finalizer-append/shape case was removed; this module no longer exercises a finalizer writer.

## Code Commentary

The retained `test_writer_constants_are_marked_and_authored_text_is_not` case checks exact finalize text and remove/skip prefixes against named nonmatching controls. It preserves marking for existing legacy records; the finalizer no longer writes a decision. The removed `test_finalizer_entry_keeps_its_shape_and_is_marked` is historical append-proof evidence, not a current case. Exact/prefix matching still cannot prove arbitrary authored text never collides with product strings. No DOM page, wire sample or predicate-only call establishes native finalization behavior.

## Separate Native No-Append Witnesses

Current native finalization assertions live in the lifecycle/series suites: they preserve existing decision arrays while recording completion time on the completed document. These distinct witnesses do not inherit or silently rebind the retired finalizer-append proof.

- Leaf/native finalization preserves authored and legacy decisions and stable retry bytes. [3]
- Master completion preserves its decisions and the sprint decisions while only the completed master receives time. [4]

## Evidence

- Exact legacy finalize constant and remove/skip prefixes mark records; the named authored controls/near-misses do not match, with no impossibility guarantee for arbitrary text. [1]

The removed `test_finalizer_entry_keeps_its_shape_and_is_marked` was an append/shape witness anchored in original source blob `b20b96423d9336c163334edc709616cec4ddcc75`. Its active proof `PRF-3GSFRB` is removed, with the original anchor retained in knowledge history; it is not rebound to the distinct current no-append cases above. The former reference to that absent symbol is retired rather than made to claim a current test.
