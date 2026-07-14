# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Fake-adapter conformance suite for the protocol-neutral harness control contract and bridge.

## Code Commentary

Tests cover exact identity and capability handshakes, normalized state/events, immediate and queued
acceptance, blocked/settling/completion states, disconnect before/after possible send, reconciliation
without resend, malformed/additive events, private IPC, bounded transcript/subscriber/receipt
retention, terminal/durable ordering, R11 draft custody, and graceful/forced shutdown including
misbehaving-adapter and stop-race paths.

## Invariants And Boundaries

- The fake adapter proves contract behavior without registering a production vendor driver.
- Tests assert bounded-time loud failure rather than allowing stranded awaits.
- Draft-preservation tests pin surface ownership and whole-message ordering.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Contract models. | [harness_control_models.py](../src/agents_remember/serving/harness_control_models.py) |
| Bridge under test. | [harness_control_bridge.py](../src/agents_remember/serving/harness_control_bridge.py) |
| Queue and IPC seams. | [harness_control_queue.py](../src/agents_remember/serving/harness_control_queue.py), [harness_control_ipc.py](../src/agents_remember/serving/harness_control_ipc.py) |

## Update History

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for fake-adapter
  conformance, R11 draft preservation, ambiguous-send recovery, bounds, and shutdown coverage.
