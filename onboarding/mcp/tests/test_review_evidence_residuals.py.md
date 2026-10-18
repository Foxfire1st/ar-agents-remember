# mcp/tests/test_review_evidence_residuals.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The residual contract cases the earlier review rounds left open: a filename is only a locator, corrupt store metadata stops at its byte bound, an over-cap descriptor authorizes no asset opens, and the comparison owner's real partial index and failed cache build survive into the packet.

## Code Commentary

Each case measures the defect it guards: the native-identifier mismatch is unreadable rather than falsely resolving a foreign revision, the corrupt manifest reads exactly one byte past its admitted cap before refusing, and the partial-index case builds a real bound Git tree with an omitted malformed record so the emitted packet carries a measured partial state and an absence-unknown limitation.

## Evidence

- A filename match alone cannot supply a record's revision or origin. [1]
- Corrupt stored metadata stops at the admitted byte bound. [2]
- A real partial index and a cold rebuild keep the owner's measured state in the packet. [3]
