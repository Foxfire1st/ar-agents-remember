# mcp/tests/test_review_evidence_residuals.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The residual contract cases the earlier review rounds left open: a filename is only a locator, corrupt store metadata stops at its byte bound, an over-cap descriptor authorizes no asset opens, and the comparison owner's real partial index and failed cache build survive into the packet.

## Code Commentary

Each case measures the defect it guards: the native-identifier mismatch is unreadable rather than falsely resolving a foreign revision, the corrupt manifest reads exactly one byte past its admitted cap before refusing, and the partial-index case builds a real bound Git tree with an omitted malformed record so the emitted packet carries a measured partial state and an absence-unknown limitation.

## Evidence

- A filename match alone cannot supply a record's revision or origin. [1]
- Corrupt stored metadata stops at the admitted byte bound. 
- A real partial index and a cold rebuild keep the owner's measured state in the packet. [3]

- Retired at the fifth freeze d59c3493: mcp/tests/test_review_evidence_residuals.py::test_f10_corrupt_store_reads_stop_at_the_admitted_byte_bound - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 6df6b68c1b9714d360296e4cdeb978f5c22f7eea. Retired means the anchor no longer stands, not that the cited subject was deleted.
