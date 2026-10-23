# mcp/tests/test_attention_notice_publication.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins the abandonment notice at its native boundary: one notice on success, none on failure, and the outcome
stated beside the archive — on both the master and the leaf shape.

## Code Commentary

A fake guard publishes, rolls back or raises over a real pre-success archive. The cases show one successful
master abandonment publishing one notice under the master's key, a successful leaf abandonment naming that
leaf's keys, a failed publication leaving no notice and no intent in either shape, a committed abandonment
stating its outcome beside the archive with the digest recorded, and a refused abandonment stating no outcome.

The landing counterpart lives in `mcp/tests/test_record_landing.py`, which owns that route's fixture; this file
covers the abandonment boundary.

## Evidence boundary

Source-level pytest cases at the reviewed freeze, not a live-page witness and no measurement: MIK-R200 evidence
item 6 is unrun and carried to L36, item 7 unrun.
